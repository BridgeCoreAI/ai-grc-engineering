"""
risk_rating.py

Encodes the NIST AI RMF likelihood-severity heat map as a reusable function.
This is the foundational scoring logic used by generate_risk_register.py.

BridgeCore AI LLC — AI GRC Engineering
"""


def calculate_risk_rating(likelihood, severity):
    """
    Calculates a composite risk rating from likelihood and severity scores.

    Args:
        likelihood (str): 'Low', 'Medium', or 'High'
        severity (str): 'Low', 'Medium', 'High', or 'Critical'

    Returns:
        str: The composite rating per the NIST AI RMF heat map
             ('Accept', 'Low', 'Medium', 'High', or 'Critical')

    Raises:
        ValueError: If likelihood or severity values are not recognized
    """
    matrix = {
        ('Low', 'Low'): 'Accept',
        ('Low', 'Medium'): 'Accept',
        ('Low', 'High'): 'Low',
        ('Low', 'Critical'): 'Medium',
        ('Medium', 'Low'): 'Low',
        ('Medium', 'Medium'): 'Low',
        ('Medium', 'High'): 'Medium',
        ('Medium', 'Critical'): 'High',
        ('High', 'Low'): 'Low',
        ('High', 'Medium'): 'Medium',
        ('High', 'High'): 'High',
        ('High', 'Critical'): 'Critical',
    }

    rating = matrix.get((likelihood, severity))
    if rating is None:
        raise ValueError(
            f"Invalid combination: likelihood='{likelihood}', severity='{severity}'. "
            f"Likelihood must be one of: Low, Medium, High. "
            f"Severity must be one of: Low, Medium, High, Critical."
        )

    return rating


if __name__ == "__main__":
    # Demonstration of all 12 possible combinations
    likelihoods = ['Low', 'Medium', 'High']
    severities = ['Low', 'Medium', 'High', 'Critical']

    print("NIST AI RMF Risk Rating Matrix")
    print("=" * 50)
    for likelihood in likelihoods:
        for severity in severities:
            rating = calculate_risk_rating(likelihood, severity)
            print(f"Likelihood: {likelihood:8} | Severity: {severity:8} -> {rating}")
