# Changelog

All notable changes to LyricsMaker will be documented in this file.

The format is based on Semantic Versioning.

---

## [0.1.1] - 2026-09-01

### Added

- Added validation for TXT file type, UTF-8 encoding, bilingual titles, and paired lyric lines.
- Added output directory validation and overwrite confirmation.
- Added automated parser and PPTX generation tests.

### Fixed

- Fixed a PPTX export failure caused by saving the output file before presentation generation was complete.
- Fixed output path handling that incorrectly treated the `.pptx` file path as a directory.
- Ensured the output directory is created only when necessary and the completed presentation is saved once.
- Fixed automatic output naming so an empty PPT name now uses the Chinese song title.
- Fixed manual output names containing characters that are invalid on Windows or macOS.
- Fixed duplicate `.pptx` extensions when a user includes the extension manually.

### Changed

- Separated TXT parsing from PPTX generation by passing the parsed lyric model to the presentation generator.
- Deferred GUI imports until application startup so the core generation logic can be tested independently.
- Updated success and error messages to show clearer export results.

### Notes

- This is a patch release and does not change the lyric input format or slide layout behavior.

---

## [0.1.0] - 2026-08-24

### Added

- Added TXT lyric file parsing.
- Added Chinese-English bilingual lyric support.
- Added song title parsing using `#`. 
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
- The GUI is limited to file selection, output location, and PPT naming.
- JSON-based lyric storage is not yet implemented.
- Standalone Windows/macOS builds are not yet available.
