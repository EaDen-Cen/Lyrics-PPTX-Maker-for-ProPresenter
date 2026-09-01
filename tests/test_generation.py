import os
import tempfile
import unittest

from pptx import Presentation

from main import generate


class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.lyric_path = os.path.join(self.directory.name, "song.txt")

        with open(self.lyric_path, "w", encoding="utf-8") as lyric_file:
            lyric_file.write(
                "#测试歌曲\n"
                "#Test Song\n\n"
                "第一句歌词\n"
                "First lyric\n"
            )

    def test_generates_pptx_with_automatic_name(self):
        output_path = generate(
            self.lyric_path,
            self.directory.name,
            "",
        )

        self.assertEqual(
            os.path.basename(output_path),
            "测试歌曲.pptx",
        )
        self.assertTrue(os.path.isfile(output_path))

        presentation = Presentation(output_path)
        self.assertEqual(len(presentation.slides), 2)

    def test_requires_confirmation_before_overwrite(self):
        output_path = generate(
            self.lyric_path,
            self.directory.name,
            "Manual Name",
        )

        with self.assertRaises(FileExistsError):
            generate(
                self.lyric_path,
                self.directory.name,
                "Manual Name",
            )

        overwritten_path = generate(
            self.lyric_path,
            self.directory.name,
            "Manual Name",
            overwrite=True,
        )
        self.assertEqual(overwritten_path, output_path)


if __name__ == "__main__":
    unittest.main()
