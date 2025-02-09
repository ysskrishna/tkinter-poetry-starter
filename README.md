# Tkinter Poetry Starter

This is a starter template for creating a Python GUI application using Tkinter and Poetry.

## Installation from Source

This project uses Poetry for dependency management. To install from source:

1. Make sure you have Poetry installed:
   ```bash
   pip install poetry
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/ysskrishna/tkinter-poetry-starter.git
   cd tkinter-poetry-starter
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

## Usage for Developers

To run the application:

```bash
poetry run tkinter_poetry_starter
```

To build the application:

```bash
poetry run pyinstaller tkinter_poetry_starter.spec
```


### Creating Releases

This project uses GitHub Actions to automatically build and publish binaries when a new version tag is pushed. To create a new release:

1. Update the version in `pyproject.toml`:
   ```toml
   [tool.poetry]
   version = "x.y.z"  # Update this version
   ```

2. Create and push a new tag:
   ```bash
   # Create a new tag
   git tag v1.1.0  # Replace with your version

   # Push the tag to GitHub
   git push origin v1.1.0
   ```

3. GitHub Actions will automatically:
   - Build binaries for Windows, Linux, and macOS
   - Create a new release on GitHub
   - Attach the binaries to the release

To delete a tag if needed:
```bash
# Delete local tag
git tag -d v1.1.0

# Delete remote tag
git push --delete origin v1.1.0
```

## MIT License

Copyright (c) 2025 [Y. Siva Sai Krishna](https://github.com/ysskrishna)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.