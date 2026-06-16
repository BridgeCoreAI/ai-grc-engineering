"""
check_evidence_staleness.py

Reads an evidence inventory and flags any control evidence that is overdue
based on its required refresh frequency. This is the single highest-value
script for a GRC engineer — it catches evidence gaps before an auditor does.

Usage:
    python check_evidence_staleness.py evidence_inventory.csv status_report.xlsx

Expected CSV columns:
    control_id, control_name, evidence_type, last_updated,
    frequency_days, owner

BridgeCore AI LLC — AI GRC Engineering
"""

import sys
import pandas as pd
from datetime import datetime


def check_evidence_staleness(evidence_inventory_path, output_path):
    """
    Reads an evidence inventory and flags overdue evidence.

    Args:
        evidence_inventory_path (str): Path to evidence inventory CSV
        output_path (str): Path where the status report Excel file is saved

    Returns:
        tuple: (full DataFrame with status, DataFrame of items needing attention)
    """
    df = pd.read_csv(evidence_inventory_path, parse_dates=['last_updated'])

    required_columns = ['control_id', 'control_name', 'evidence_type',
                         'last_updated', 'frequency_days', 'owner']
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Input CSV is missing required columns: {missing}")

    today = datetime.now()
    df['days_since_update'] = (today - df['last_updated']).dt.days

    def get_status(row):
        days_overdue = row['days_since_update'] - row['frequency_days']
        if days_overdue > 30:
            return 'CRITICAL - Severely Overdue'
        elif days_overdue > 0:
            return 'OVERDUE'
        elif row['frequency_days'] - row['days_since_update'] <= 7:
            return 'DUE SOON'
        else:
            return 'CURRENT'

    df['status'] = df.apply(get_status, axis=1)

    needs_attention = df[df['status'] != 'CURRENT'].sort_values(
        'days_since_update', ascending=False
    )

    print("=" * 60)
    print("Evidence Staleness Report — BridgeCore AI LLC")
    print("=" * 60)
    print(f"Total controls tracked: {len(df)}")
    print(f"Controls needing attention: {len(needs_attention)}")

    if len(needs_attention) > 0:
        print("\nControls requiring immediate action:")
        print(needs_attention[['control_id', 'control_name', 'owner', 'status']]
              .to_string(index=False))
    else:
        print("\nAll evidence is current. No action required.")
    print("=" * 60)

    df.to_excel(output_path, index=False, sheet_name='Evidence Status')
    print(f"\nFull report saved to: {output_path}")

    return df, needs_attention


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_evidence_staleness.py <input.csv> <output.xlsx>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    check_evidence_staleness(input_path, output_path)
