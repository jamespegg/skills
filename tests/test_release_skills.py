import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from scripts.release_skills import stage_release


class ReleaseSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name, version in (("skill-one", "0.0.1"), ("skill-two", "1.5.0")):
            path = self.root / "skills" / name
            (path / "agents").mkdir(parents=True)
            (path / "SKILL.md").write_text(
                f'---\nname: {name}\nmetadata:\n  version: "{version}"\n---\n\n# {name}\n'
            )
            (path / "agents" / "openai.yaml").write_text("name: example\n")

    def test_versions_all_skills_and_packages_contents_at_archive_root(self):
        archives = stage_release(self.root, "2.0.0", self.root / "dist")
        self.assertEqual([p.name for p in archives], ["skill-one-v2.0.0.zip", "skill-two-v2.0.0.zip"])
        for archive in archives:
            with ZipFile(archive) as zipped:
                self.assertEqual(zipped.namelist(), ["SKILL.md", "agents/openai.yaml"])
                self.assertIn(b'version: "2.0.0"', zipped.read("SKILL.md"))
            self.assertIn('version: "2.0.0"', (self.root / "skills" / archive.name.removesuffix("-v2.0.0.zip") / "SKILL.md").read_text())

    def test_invalid_metadata_fails_before_modifying_any_skill(self):
        second = self.root / "skills" / "skill-two" / "SKILL.md"
        second.write_text(second.read_text().replace("  version:", "  revision:"))
        first = self.root / "skills" / "skill-one" / "SKILL.md"
        original = first.read_text()
        with self.assertRaisesRegex(ValueError, "metadata.version"):
            stage_release(self.root, "2.0.0", self.root / "dist")
        self.assertEqual(first.read_text(), original)

    def test_invalid_semver_rejected(self):
        with self.assertRaisesRegex(ValueError, "Invalid release version"):
            stage_release(self.root, "2.0.0-rc.1", self.root / "dist")

    def test_symlink_rejected(self):
        (self.root / "skills" / "skill-one" / "other").symlink_to(self.root / "skills" / "skill-two")
        with self.assertRaisesRegex(ValueError, "Symlinks"):
            stage_release(self.root, "2.0.0", self.root / "dist")


if __name__ == "__main__":
    unittest.main()
