# Contributing to Nadesiko Python

Thank you for your interest in contributing to Nadesiko Python! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Bugs

- Use [GitHub Issues](https://github.com/nadesiko3-python/nadesiko3-python/issues) to report bugs
- Provide detailed information about the bug including:
  - Operating system and Python version
  - Steps to reproduce the issue
  - Expected vs actual behavior
  - Error messages (if any)

### Suggesting Features

- Use [GitHub Discussions](https://github.com/nadesiko3-python/nadesiko3-python/discussions) for feature suggestions
- Describe the feature and its use case clearly
- Explain why the feature would be beneficial

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 🛠️ Development Setup

### Prerequisites

- Python 3.7 or higher
- Git
- Recommended: virtual environment

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/your-username/nadesiko3-python.git
cd nadesiko3-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## 📝 Code Style

We use the following tools to maintain code quality:

- **Black**: Code formatting
- **Flake8**: Linting
- **MyPy**: Type checking

```bash
# Format code
black src/ tests/

# Run linting
flake8 src/ tests/

# Run type checking
mypy src/
```

### Code Guidelines

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Add type hints where appropriate

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_parser.py
```

### Writing Tests

- Write tests for new functionality
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies when necessary

## 📚 Documentation

### Updating Documentation

- Update README.md for user-facing changes
- Update docstrings for API changes
- Add examples for new features
- Update English documentation when needed

### Documentation Style

- Use clear, simple language
- Provide code examples
- Include both Japanese and English when relevant
- Use consistent formatting

## 🌍 Language Support

This project supports both Japanese and English:

### Adding New Keywords

When adding new language keywords:

1. Add to both Japanese and English parsers
2. Update documentation in both languages
3. Add tests for both language variants
4. Update keyword lists

### Translation Guidelines

- Maintain consistency with existing terminology
- Consider educational context for language choices
- Ensure natural phrasing in both languages

## 🏗️ Project Structure

```
nadesiko3-python/
├── src/                    # Source code
├── tests/                  # Test files
├── docs/                   # Documentation
├── examples/               # Example programs
├── README.md              # Main documentation
├── README_EN.md           # English documentation
├── CONTRIBUTING.md        # This file
├── LICENSE                # MIT license
└── pyproject.toml         # Project configuration
```

## 🔄 Release Process

### Version Numbers

We follow [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps

1. Update version number in `pyproject.toml` and `setup.py`
2. Update CHANGELOG.md
3. Create Git tag (`git tag v6.0.1`)
4. Push tag (`git push origin v6.0.1`)
5. GitHub Actions will automatically create release

## 📋 Getting Help

- **Documentation**: Check the `docs/` directory
- **Issues**: Search existing issues before creating new ones
- **Discussions**: Use GitHub Discussions for questions
- **Email**: nadesiko-python@googlegroups.com

## 🎯 Priority Areas

We particularly welcome contributions in:

1. **Educational Examples**: Simple examples for beginners
2. **Documentation**: Improving existing documentation
3. **Bug Fixes**: Especially in core parsing functionality
4. **Test Coverage**: Increasing test coverage
5. **Internationalization**: Better language support

## 📜 Code of Conduct

### Our Pledge

We are committed to making participation in this project a harassment-free experience for everyone, regardless of:

- Age, body size, disability, ethnicity, gender identity and expression
- Level of experience, education, socioeconomic status, nationality, personal appearance
- Race, religion, or sexual identity

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Enforcement

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned with this Code of Conduct.

## 🙏 Acknowledgments

Thank you to all contributors who help make Nadesiko Python better! Special thanks to:

- The original Nadesiko project for inspiration
- All beta testers and early adopters
- The open-source community for tools and libraries

---

**Happy coding! 皆さん、頑張りましょう！**
