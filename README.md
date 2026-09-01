# LyricsMaker

LyricsMaker is a Python-based tool that converts structured bilingual lyrics into PowerPoint (PPTX) lyric slides.

It is designed primarily for Chinese-English worship lyrics and is intended for use with ProPresenter and Microsoft PowerPoint.

## Current Version

**v0.1.1**

## Features

- Parse bilingual Chinese-English lyrics from TXT files
- Automatically generate PPTX lyric slides
- Generate a title slide
- Support Chinese and English lyrics on the same slide
- Customize Chinese and English fonts
- Customize Chinese and English font sizes
- Automatically calculate vertical text offset
- Automatically generate output filenames from the Chinese song title
- Validate lyric titles, bilingual line pairs, file format, and output paths
- Ask for confirmation before overwriting an existing presentation
- Support 16:9 presentations
- Store user-specific settings locally through `settings.json`

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

LyricsMaker validates this structure before export. The file must use UTF-8
encoding, contain two non-empty titles, and contain a complete English line for
every Chinese lyric line.

## Installation

### Requirements

- Python 3.10 or newer
- python-pptx
- PySide6

Install the required packages with:

```bash
pip install python-pptx PySide6
```

### Usage

Run the application with:

```bash
python main.py
```

Select a TXT lyric file and an output directory through the application. You
may enter a custom PPT name or leave it empty to use the Chinese song title.
If the target file already exists, LyricsMaker asks before replacing it.

### Configuration

LyricsMaker uses a local settings.json file for user-specific settings.

A default configuration template is provided as:

```text
settings.example.json
```

If `settings.json` does not exist, LyricsMaker automatically copies the default
configuration from `settings.example.json` when it starts.

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
├── tests/                  # Parser and PPTX generation tests
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

> Structured lyrics → validated lyric model → formatted PPTX

The project currently includes a basic PySide6 interface for file selection,
output naming, export, overwrite confirmation, and error reporting. Automatic
layout, in-app lyric editing, previews, and standalone builds are still planned.

## Testing

Run the automated test suite with:

```bash
python -m unittest discover -s tests -v
```

Future versions may expand the lyric data structure, presentation controls, and ProPresenter workflow.

## License

This project is currently not licensed for redistribution.
