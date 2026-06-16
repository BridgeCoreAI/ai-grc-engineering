"""
risk_tier_classifier.py

Classifies an AI system intake submission into a risk tier (1-4) based on
decision autonomy, affected population, population size, and data sensitivity.

This encodes the same logic demonstrated in the interactive intake workflow
widget from Module 4 — now as a reusable function that can plug into an
actual intake system (web form, ServiceNow, Jira automation).

BridgeCore AI LLC — AI GRC Engineering
"""


def classify_risk_tier(decision_autonomy, affected_population,
                        population_size, contains_sensitive_data):
    """
    Classifies an AI system into a risk tier based on intake responses.

    Args:
        decision_autonomy (str): 'in_the_loop', 'on_the_loop', or 'out_of_loop'
        affected_population (str): 'internal_staff', 'customers_public',
            'patients', 'job_applicants', 'government_beneficiaries', 'other'
        population_size (str): 'under_100', '100_to_1000', '1000_to_10000',
            '10000_to_100000', 'over_100000'
        contains_sensitive_data (bool): Whether the system processes
            sensitive personal data

    Returns:
        dict: tier (int), label (str), score (int), review_track (str)
    """
    score = 0

    # Decision autonomy scoring — less human oversight = higher risk
    autonomy_scores = {
        'out_of_loop': 3,
        'on_the_loop': 2,
        'in_the_loop': 1
    }
    score += autonomy_scores.get(decision_autonomy, 0)

    # Affected population scoring
    high_impact_populations = [
        'customers_public', 'patients',
        'job_applicants', 'government_beneficiaries'
    ]
    if affected_population in high_impact_populations:
        score += 2

    # Population size scoring
    size_scores = {
        'over_100000': 2,
        '10000_to_100000': 2,
        '1000_to_10000': 1,
        '100_to_1000': 0,
        'under_100': 0
    }
    score += size_scores.get(population_size, 0)

    # Sensitive data scoring
    if contains_sensitive_data:
        score += 2

    # Determine tier and review track
    if score >= 7:
        return {
            'tier': 1,
            'label': 'Critical',
            'score': score,
            'review_track': (
                'Full AI Review Board approval required. All five specialist '
                'reviews mandatory. No deployment until all Critical risks '
                'have approved treatment plans.'
            )
        }
    elif score >= 5:
        return {
            'tier': 2,
            'label': 'High',
            'score': score,
            'review_track': (
                'Full AI Review Board approval required. All specialist '
                'reviews mandatory. Enhanced post-deployment monitoring.'
            )
        }
    elif score >= 3:
        return {
            'tier': 3,
            'label': 'Medium',
            'score': score,
            'review_track': (
                'GRC lead approval sufficient. Legal, privacy, and security '
                'reviews required. Standard monitoring.'
            )
        }
    else:
        return {
            'tier': 4,
            'label': 'Low',
            'score': score,
            'review_track': (
                'Expedited review. GRC engineer sign-off sufficient. '
                'Basic monitoring required.'
            )
        }


if __name__ == "__main__":
    # Example: federal benefits eligibility AI system
    example_result = classify_risk_tier(
        decision_autonomy='out_of_loop',
        affected_population='government_beneficiaries',
        population_size='over_100000',
        contains_sensitive_data=True
    )

    print("=" * 50)
    print("AI System Risk Tier Classification")
    print("=" * 50)
    print(f"Tier: {example_result['tier']} ({example_result['label']})")
    print(f"Score: {example_result['score']}")
    print(f"Review track: {example_result['review_track']}")
