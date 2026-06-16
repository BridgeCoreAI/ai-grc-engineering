"""
package_evidence.py

Packages all evidence for a specific AI system into an audit-ready ZIP
archive with a manifest mapping every document to its control. Turns a
48-hour audit document request into a same-day response.

Usage:
    python package_evidence.py <system_name> <evidence_root> <control_mapping.json> <output_dir>

BridgeCore AI LLC — AI GRC Engineering
"""

import os
import sys
import shutil
import zipfile
import json
from datetime import datetime


def package_evidence_for_audit(system_name, evidence_root_path,
                                  control_mapping_path, output_dir):
    """
    Packages all evidence for an AI system into an audit-ready ZIP archive.

    Args:
        system_name (str): Name of the AI system (matches folder name
            under evidence_root_path)
        evidence_root_path (str): Root path containing per-system evidence folders
        control_mapping_path (str): Path to a JSON file mapping evidence
            category names to control IDs
        output_dir (str): Directory where the final ZIP package is saved

    Returns:
        tuple: (path to the ZIP file, manifest dict)
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    package_name = f"{system_name}_evidence_package_{timestamp}"
    package_path = os.path.join(output_dir, package_name)

    os.makedirs(package_path, exist_ok=True)

    with open(control_mapping_path, 'r') as f:
        control_mapping = json.load(f)

    manifest = {
        'system_name': system_name,
        'package_generated': timestamp,
        'generated_by': 'BridgeCore AI LLC — AI GRC Engineering',
        'documents': []
    }

    system_evidence_path = os.path.join(evidence_root_path, system_name)

    if not os.path.exists(system_evidence_path):
        raise FileNotFoundError(
            f"No evidence folder found for system '{system_name}' at "
            f"{system_evidence_path}"
        )

    for category in os.listdir(system_evidence_path):
        category_path = os.path.join(system_evidence_path, category)
        if os.path.isdir(category_path):
            dest_category_path = os.path.join(package_path, category)
            shutil.copytree(category_path, dest_category_path)

            for file in os.listdir(category_path):
                manifest['documents'].append({
                    'filename': file,
                    'category': category,
                    'mapped_control': control_mapping.get(category, 'Unmapped')
                })

    manifest_path = os.path.join(package_path, 'MANIFEST.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)

    zip_path = f"{package_path}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, package_path)
                zipf.write(file_path, arcname)

    print("=" * 60)
    print("Evidence Package — BridgeCore AI LLC")
    print("=" * 60)
    print(f"System: {system_name}")
    print(f"Total documents included: {len(manifest['documents'])}")
    print(f"Package saved to: {zip_path}")
    print("=" * 60)

    return zip_path, manifest


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python package_evidence.py <system_name> "
            "<evidence_root> <control_mapping.json> <output_dir>"
        )
        sys.exit(1)

    package_evidence_for_audit(
        system_name=sys.argv[1],
        evidence_root_path=sys.argv[2],
        control_mapping_path=sys.argv[3],
        output_dir=sys.argv[4]
    )
