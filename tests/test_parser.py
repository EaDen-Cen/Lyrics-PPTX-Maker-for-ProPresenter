import os
import tempfile
import unittest

from parser import (
    LyricsFormatError,
    clean_filename,
    get_output_filename,
    read_lyrics,
)


class ParserTests(unittest.TestCase):
    def create_lyric_file(self, content):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = os.path.join(directory.name, "song.txt")
        with open(path, "w", encoding="utf-8") as lyric_file:
            lyric_file.write(content)
        return path

    def test_reads_valid_bilingual_lyrics(self):
        path = self.create_lyric_file(
            "#中文歌名\n#English Title\n\n中文歌词\nEnglish lyric\n"
        )

        lyrics = read_lyrics(path)

        self.assertEqual(lyrics["title_cn"], "中文歌名")
        self.assertEqual(lyrics["title_en"], "English Title")
        self.assertEqual(
            lyrics["slides"],
            [{"chinese": "中文歌词", "english": "English lyric"}],
        )

    def test_rejects_unpaired_lyric_line(self):
        path = self.create_lyric_file(
            "#中文歌名\n#English Title\n中文歌词\nEnglish lyric\n落单歌词\n"
        )

        with self.assertRaises(LyricsFormatError):
            read_lyrics(path)

    def test_rejects_missing_titles(self):
        path = self.create_lyric_file(
            "中文歌名\nEnglish Title\n中文歌词\nEnglish lyric\n"
        )

        with self.assertRaises(LyricsFormatError):
            read_lyrics(path)

    def test_uses_chinese_title_as_default_output_name(self):
        lyrics = {
            "title_cn": "中文歌名",
            "filename": "song.txt",
        }

        self.assertEqual(get_output_filename(lyrics), "中文歌名.pptx")

    def test_cleans_manual_output_name(self):
        lyrics = {"title_cn": "中文歌名", "filename": "song.txt"}

        self.assertEqual(
            get_output_filename(lyrics, 'My:Song?.pptx'),
            "MySong.pptx",
        )
        self.assertEqual(clean_filename(" Song. "), "Song")


if __name__ == "__main__":
    unittest.main()
