# Contributing

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment
3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
4. Install pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

## Running Tests

```bash
pytest tests/ -v --cov=app
```

## Code Style

- Follow PEP 8
- Use Black for formatting
- Maximum line length: 120 characters
- Add docstrings to functions

## Pull Request Process

1. Create a feature branch
2. Make your changes
3. Add tests for new features
4. Ensure all tests pass
5. Update documentation
6. Submit pull request

## Reporting Issues

- Use GitHub Issues
- Include reproduction steps
- Provide error messages and logs
- Specify Python version and OS
