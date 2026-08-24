# LyricsMaker

LyricsMaker is a Python-based tool for generating bilingual lyric slides
from structured text files.

It is designed primarily for creating Chinese-English worship lyric
presentations for ProPresenter and PowerPoint.

## Current Version

v0.1.0

## Features

- Parse bilingual Chinese-English lyrics from TXT files
- Automatically generate PPTX lyric slides
- Generate a title slide
- Support lyric groups such as `[Verse]`, `[Chorus]`, `[Bridge]`
- Customize Chinese and English fonts
- Customize Chinese and English font sizes
- Automatically calculate vertical text offset
- Automatically generate output filenames from song titles
- 16:9 presentation support
- Centralized configuration through `config.py`

## Input Format

```text
#Chinese Title
#English Title

[Verse]

中文歌词
English lyrics

中文歌词
English lyrics

[Chorus]

中文歌词
English lyrics
