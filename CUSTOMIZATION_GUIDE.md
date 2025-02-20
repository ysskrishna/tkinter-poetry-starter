# Customizing the Tkinter Poetry Starter Template

This guide will help you customize this template for your own project. Follow these steps in order to properly rename and set up your project.

## Prerequisites

- Python 3.9 or higher installed
- Poetry installed (`pip install poetry`)
- Git installed
- A GitHub account (optional, if you plan to host on GitHub)

## Step-by-Step Guide

### 1. Clone and Setup the Template

```bash
# Clone the template
git clone https://github.com/ysskrishna/tkinter-poetry-starter.git

# Rename the directory to your project name
mv tkinter-poetry-starter your-project-name

# Enter the project directory
cd your-project-name
```

### 2. Initialize Version Control

You have two options:

#### Option A: Keep the template's history
```bash
# Update the origin remote with your own repository
git remote set-url origin https://github.com/yourusername/your-project-name.git
```

#### Option B: Start with a clean history
```bash
# Remove the existing git history
rm -rf .git

# Initialize a new git repository
git init

# Add your remote repository (if using GitHub)
git remote add origin https://github.com/yourusername/your-project-name.git
```

### 3. Update Project Configuration

#### 3.1. Update pyproject.toml

Edit the `pyproject.toml` file and modify these fields:

```toml
[tool.poetry]
name = "your-project-name"
version = "1.0.0"  # Start with your desired version
description = "Your project description"
authors = ["Your Name <your.email@example.com>"]
repository = "https://github.com/yourusername/your-project-name"
readme = "README.md"
packages = [{include = "src"}]

[tool.poetry.scripts]
your_project_name = "src.gui.app:main"  # Change from tkinter_poetry_starter
```

### 4. Update Source Files

1. Rename the PyInstaller spec file:
```bash
# Rename the spec file
mv tkinter_poetry_starter.spec your_project_name.spec
```

2. Edit the spec file (`your_project_name.spec`):
```python
# Update these fields in your_project_name.spec
name='your-project-name',
```

3. Update GitHub Workflow (if using GitHub Actions):
Edit `.github/workflows/release.yml` and update:
```yaml
# Find and replace APP_NAME
echo "APP_NAME=your-project-name" >> $GITHUB_ENV
```

4. Update Application Title (Optional):
- Check `src/gui/app.py` for any references to "Tkinter Poetry Starter"
- Update any branding images in `src/assets/`
- Update any documentation references

### 5. Set Up the Development Environment

```bash
# Install dependencies
poetry install

# Install pre-commit hooks (recommended)
poetry run pre-commit install

# Verify the installation
poetry run python -c "from src.gui.app import main; print('Setup successful!')"
```

### 6. Test Your Setup

```bash
# Run the application
poetry run python -m src.gui.app

# Build the executable (optional)
poetry run pyinstaller your_project_name.spec
```

### 7. Update Documentation

1. Update README.md with:
   - Your project name
   - Description
   - Setup instructions
   - Usage guidelines
   - License information

2. Remove template-specific files:
   - CUSTOMIZE_TEMPLATE.md (this file)
   - Any other template-specific documentation

### 8. Commit Your Changes

```bash
# Add all files to git
git add .

# Create initial commit
git commit -m "Initial commit: Project setup from tkinter-poetry-starter template"

# Push to your repository (if using GitHub)
git branch -M main
git push -u origin main
```

## Verification Checklist

Before starting development, verify that:

- [ ] Project directory is renamed
- [ ] Project name and metadata are updated in pyproject.toml
- [ ] Poetry script name is updated
- [ ] Spec file is renamed and updated
- [ ] GitHub workflow is updated (if using)
- [ ] Dependencies are installed correctly
- [ ] Application runs without errors
- [ ] Build process works
- [ ] Documentation is updated
- [ ] Git repository is properly initialized
- [ ] All template-specific files are removed or updated

## Troubleshooting

If you encounter any issues:

1. Ensure all prerequisites are properly installed
2. Check that Poetry environment is properly activated
3. Verify that all paths in spec and configuration files match your project name
4. Make sure all dependencies are installed with `poetry install`

For build issues:
- Run `poetry run pyinstaller your_project_name.spec --clean` to clean and rebuild
- Check the `dist` directory for the built executable
