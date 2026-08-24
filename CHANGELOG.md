# Changelog

All notable changes to LyricsMaker will be documented in this file.

The format is based on Semantic Versioning.

---

## [0.0.1] - 2026-08-24

### Added

- Added TXT lyric file parsing.
- Added Chinese-English bilingual lyric support.
- Added song title parsing using `#`.
- Added lyric group parsing using `[Group]`.
- Added automatic title slide generation.
- Added bilingual lyric slide generation.
- Added independent Chinese and English font settings.
- Added independent Chinese and English font size settings.
- Added automatic vertical text offset calculation.
- Added 16:9 PPTX generation.
- Added automatic output filename generation based on the song title.
- Added centralized configuration through `config.py`.

### Notes

This version establishes the basic TXT → PPTX workflow.

The project is currently intended as an early development
prototype rather than a finished end-user application.

### Known Limitations

- Requires Python and the required Python packages.
- Requires compatible fonts to be installed on the system.
- Lyric line wrapping is not yet automated.
- Long lyrics may require manual adjustment.
- Automatic short-line merging is not yet implemented.
- PPTX generation is currently the primary output method.
- ProPresenter-specific group integration is not yet implemented.
- GUI is not yet available.
- JSON-based lyric storage is not yet implemented.
- Standalone Windows/macOS builds are not yet available.
