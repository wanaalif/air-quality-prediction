# Contributing to Air Quality Prediction Project

First off, thank you for considering contributing to this project! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Style Guidelines](#style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating a welcoming and inclusive environment. By participating, you are expected to uphold these values:

- **Be respectful**: Treat everyone with respect and kindness
- **Be collaborative**: Work together and help others
- **Be professional**: Keep discussions focused and constructive
- **Be open-minded**: Welcome different perspectives and ideas

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Run command '....'
3. See error

**Expected behavior**
What you expected to happen.

**Environment:**
 - OS: [e.g., Windows 10, Ubuntu 20.04]
 - Python version: [e.g., 3.8.10]
 - TensorFlow version: [e.g., 2.8.0]

**Additional context**
Add any other context about the problem here.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title**: Descriptive title for the suggestion
- **Detailed description**: Explain the enhancement and its benefits
- **Use cases**: Provide examples of how it would be used
- **Alternatives**: Any alternative solutions you've considered

### Code Contributions

We welcome code contributions! Here are areas where you can help:

1. **Feature Development**
   - Implementing new prediction models (LSTM, GRU, etc.)
   - Adding data visualization features
   - Creating API endpoints for predictions

2. **Improvements**
   - Optimizing model performance
   - Improving data preprocessing
   - Enhancing documentation

3. **Bug Fixes**
   - Fixing reported issues
   - Improving error handling
   - Adding input validation

4. **Testing**
   - Writing unit tests
   - Adding integration tests
   - Improving test coverage

5. **Documentation**
   - Improving README
   - Adding code comments
   - Creating tutorials

## Getting Started

### Setting Up Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork**:
```bash
git clone https://github.com/your-username/air-quality-prediction.git
cd air-quality-prediction
```

3. **Add upstream remote**:
```bash
git remote add upstream https://github.com/original-owner/air-quality-prediction.git
```

4. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

5. **Install dependencies**:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development dependencies
```

6. **Create a new branch**:
```bash
git checkout -b feature/your-feature-name
```

## Development Process

### 1. Keep Your Fork Updated

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### 2. Make Your Changes

- Write clean, readable code
- Follow the style guidelines (see below)
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Run unit tests
pytest tests/

# Run specific test file
pytest tests/test_preprocessing.py

# Check code coverage
pytest --cov=src tests/
```

### 4. Commit Your Changes

Follow the commit guidelines (see below)

### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

Go to GitHub and create a pull request from your fork to the main repository.

## Style Guidelines

### Python Code Style

We follow **PEP 8** style guidelines with some modifications:

```python
# Good example
def preprocess_data(df: pd.DataFrame, 
                   remove_outliers: bool = True) -> pd.DataFrame:
    """
    Preprocess the air quality dataset.
    
    Args:
        df: Input DataFrame with raw sensor data
        remove_outliers: Whether to remove outliers (default: True)
        
    Returns:
        Preprocessed DataFrame
        
    Raises:
        ValueError: If DataFrame is empty
    """
    if df.empty:
        raise ValueError("Input DataFrame cannot be empty")
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle outliers if requested
    if remove_outliers:
        df = handle_outliers(df)
    
    return df
```

**Key Points:**

- **Line length**: Maximum 100 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Naming conventions**:
  - Functions/variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_CASE`
- **Docstrings**: Use Google style docstrings
- **Type hints**: Use type hints for function arguments and returns
- **Imports**: 
  ```python
  # Standard library
  import os
  import sys
  
  # Third-party
  import numpy as np
  import pandas as pd
  
  # Local
  from src.utils import helper_function
  ```

### Code Formatting Tools

We recommend using:

- **Black**: Code formatter
  ```bash
  black src/ tests/
  ```

- **Flake8**: Linter
  ```bash
  flake8 src/ tests/
  ```

- **mypy**: Type checker
  ```bash
  mypy src/
  ```

### Documentation Style

- **README files**: Use Markdown with clear headers and examples
- **Code comments**: Explain *why*, not *what*
- **Docstrings**: Required for all public functions and classes
- **Inline comments**: Use sparingly, when logic is complex

### Notebook Style

For Jupyter notebooks:

- **Clear sections**: Use markdown headers to organize
- **Cell outputs**: Clear outputs before committing (optional)
- **Explanations**: Add markdown cells to explain the analysis
- **Code quality**: Same standards as .py files

## Commit Guidelines

We follow the **Conventional Commits** specification:

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (formatting, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding or updating tests
- **chore**: Changes to build process or auxiliary tools

### Examples

```bash
# Good commit messages
feat(model): add LSTM architecture for time series prediction

fix(preprocessing): handle missing values in temperature column

docs(readme): update installation instructions for Windows

refactor(utils): simplify feature scaling function

test(model): add unit tests for ANN architecture
```

```bash
# Bad commit messages
update code
fix bug
changes
WIP
```

### Commit Message Best Practices

- **Use present tense**: "add feature" not "added feature"
- **Use imperative mood**: "change" not "changes" or "changed"
- **Be specific**: Describe *what* and *why*, not *how*
- **Reference issues**: Use `Fixes #123` or `Closes #456`
- **Keep subject line short**: Under 50 characters
- **Separate subject from body**: With a blank line
- **Wrap body at 72 characters**

## Pull Request Process

### Before Submitting

1. **Update documentation**: Ensure README, docstrings are updated
2. **Add/update tests**: Maintain or improve test coverage
3. **Run tests locally**: All tests must pass
4. **Format code**: Run Black and Flake8
5. **Update CHANGELOG**: Add entry for your changes (if applicable)

### PR Template

When you create a pull request, please include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing unit tests pass locally
- [ ] Any dependent changes have been merged and published

## Screenshots (if applicable)

## Additional Notes
```

### Review Process

1. **Automated checks**: CI/CD pipeline will run tests
2. **Code review**: Maintainers will review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Once approved, your PR will be merged

### After Your PR is Merged

1. **Delete your branch**: Both locally and on GitHub
2. **Update your fork**: Pull the latest changes
3. **Close related issues**: If your PR fixes issues

## Development Dependencies

For development, install additional packages:

```bash
pip install pytest pytest-cov black flake8 mypy
```

Or use:

```bash
pip install -r requirements-dev.txt
```

## Questions?

If you have questions:

1. **Check documentation**: README, docs folder
2. **Search issues**: Someone may have asked before
3. **Open a discussion**: GitHub Discussions
4. **Contact maintainers**: See README for contact info

## Recognition

Contributors will be recognized in:

- **README.md**: Contributors section
- **CHANGELOG.md**: For significant contributions
- **GitHub**: Automatic contributor recognition

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to making air quality prediction better! 🌍💚
