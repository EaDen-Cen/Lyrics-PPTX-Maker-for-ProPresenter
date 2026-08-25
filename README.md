# LyricsMaker

LyricsMaker is a Python-based tool that converts structured bilingual lyrics into PowerPoint (PPTX) lyric slides.

It is designed primarily for Chinese-English worship lyrics and is intended for use with ProPresenter and Microsoft PowerPoint.

## Current Version

**v0.1.0**

## Features

- Parse bilingual Chinese-English lyrics from TXT files
- Automatically generate PPTX lyric slides
- Generate a title slide
- Support Chinese and English lyrics on the same slide
- Customize Chinese and English fonts
- Customize Chinese and English font sizes
- Automatically calculate vertical text offset
- Automatically generate output filenames
- Support 16:9 presentations
- Default Local configuration through `settings.example.json`

## How It Works

```text
TXT Lyrics File
      │
      ▼
  LyricsMaker
      │
      ▼
   PPTX File
      │
      ├── PowerPoint
      │
      └── ProPresenter
```

LyricsMaker reads a structured TXT file containing Chinese and English lyrics and converts it into a formatted PPTX presentation.

## Input Format

Lyrics should be written in the following format:

```text
#中文歌名
#English Title

中文歌词
English lyrics

中文歌词
English lyrics

中文歌词
English lyrics

```

The first # line is used as the Chinese title, while the second # line is used as the English title.

Each Chinese lyric line should be followed by its corresponding English lyric line.

## Installation

### Requirements

·Python 3.10 or newer
·python-pptx
·PySide6

Install the required packages with:

```text
pip install python-pptx PySide6
```

### Usage

Run the application with:

```text
python main.py
```

Select a TXT lyric file through the application and generate the corresponding PPTX presentation.

### Configuration

LyricsMaker uses a local settings.json file for user-specific settings.

A default configuration template is provided as:

```text
settings.example.json
```

Copy the example configuration to settings.json before running the application for the first time.

settings.json is intended to remain local and is not synchronized through Git.

## Project Structure

```text
Lyrics-PPTX-Maker-for-ProPresenter/
│
├── main.py                 # Application entry point
├── ui.py                   # Graphical user interface
├── parser.py               # Lyrics file parser
├── ppt_creator.py          # PPTX generation
├── config.py               # Configuration handling
├── settings.example.json   # Default configuration template
│
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
└── .gitignore
```

## Roadmap

See ROADMAP.md for planned features and future development.

## Changelog

See CHANGELOG.md for version history.

## Project Status

LyricsMaker is currently in early development.

Version 0.1 focuses on the core workflow:

|  Structured lyrics → formatted PPTX

Future versions may expand the lyric data structure, presentation controls, and ProPresenter workflow.

## License

This project is currently not licensed for redistribution.