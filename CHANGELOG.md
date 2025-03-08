# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-03-08
### Breaking Changes
- Converted project to a Copier template
- All project files are now templated using Jinja2 syntax
- Project name and other variables are now dynamically generated

### Added
- Copier configuration file for template customization
- Template variables for project customization
- Automated release workflow using GitHub Actions based on Git Tags
- `release.sh` script for creating version branches and tags

### Changed
- All static file references converted to template variables
- Documentation structure improved for template usage
- Installation and setup process now uses Copier
- Development guide updated to reflect template-based workflow

## [1.1.0] - 2025-02-20
### Added
- Added `CUSTOMIZATION_GUIDE.md` file to guide users on customizing the current template

### Changed
- Updated `README.md` file to include links to `CUSTOMIZATION_GUIDE.md` and `DEVELOPMENT.md` files

## [1.0.0] - 2025-02-19
### Added
- Initial project setup with Poetry
- Basic Tkinter GUI structure
- Project documentation
- GitHub Actions for automated builds and releases
- Pre-commit hooks for code quality checks
- PyInstaller configuration for building standalone executables



[1.1.0]: https://github.com/ysskrishna/tkinter-poetry-starter/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ysskrishna/tkinter-poetry-starter/releases/tag/v1.0.0