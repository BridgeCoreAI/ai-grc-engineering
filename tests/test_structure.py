import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FRAMEWORKS = {"eu-ai-act": 9, "iso-42001": 9, "nist-ai-rmf": 8}
REFERENCES = ["ai-lifecycle-stages.md", "human-oversight-levels.md",
              "risk-types.md", "trustworthy-ai-properties.md"]
PLACEHOLDERS = ["TODO", "TBD", "FIXME", "coming soon", "under construction"]


def module_files(fw):
    return sorted((ROOT / "frameworks" / fw / "modules").glob("module-*.md"))


class TestCompleteness(unittest.TestCase):
    def test_expected_top_level_files(self):
        for name in ["README.md", "AIGRC_Executive_Summary.md"]:
            self.assertTrue((ROOT / name).is_file(), f"missing {name}")

    def test_module_counts_match_claims(self):
        total = 0
        for fw, expected in FRAMEWORKS.items():
            files = module_files(fw)
            self.assertEqual(len(files), expected,
                             f"{fw}: expected {expected}, found {len(files)}")
            total += len(files)
        self.assertEqual(total, 26)

    def test_module_numbering_has_no_gaps(self):
        for fw in FRAMEWORKS:
            nums = [int(f.stem.split("-")[1]) for f in module_files(fw)]
            self.assertEqual(nums, list(range(1, len(nums) + 1)),
                             f"{fw}: gap in module numbering")

    def test_reference_cards_exist(self):
        ref_dir = ROOT / "frameworks" / "nist-ai-rmf" / "references"
        for name in REFERENCES:
            self.assertTrue((ref_dir / name).is_file(),
                            f"missing reference card {name}")


class TestModuleIntegrity(unittest.TestCase):
    def all_modules(self):
        for fw in FRAMEWORKS:
            yield from module_files(fw)

    def test_each_module_has_h1(self):
        for f in self.all_modules():
            self.assertRegex(f.read_text(encoding="utf-8"), r"^# .+",
                             f"{f.name}: missing H1 title")

    def test_each_module_is_substantive(self):
        for f in self.all_modules():
            words = len(f.read_text(encoding="utf-8").split())
            self.assertGreaterEqual(words, 150,
                                    f"{f.name}: too short ({words} words)")

    def test_no_placeholders(self):
        for f in self.all_modules():
            text = f.read_text(encoding="utf-8").lower()
            for marker in PLACEHOLDERS:
                self.assertNotIn(marker.lower(), text,
                                 f"{f.name}: placeholder '{marker}'")


class TestLinks(unittest.TestCase):
    LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

    def test_internal_links_resolve(self):
        for md in ROOT.rglob("*.md"):
            for raw in self.LINK_RE.findall(md.read_text(encoding="utf-8")):
                if "://" in raw or raw.startswith(("#", "mailto:")):
                    continue
                target = raw.split("#")[0].strip()
                if target:
                    self.assertTrue((md.parent / target).resolve().exists(),
                                    f"{md.name}: broken link -> {raw}")
