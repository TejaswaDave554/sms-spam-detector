# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2024

### Added
- Security headers (CSP, HSTS, X-Frame-Options)
- Rate limiting (10 requests/minute per IP)
- Input validation and sanitization
- Request size limits (16KB max)
- Health check endpoint at `/health`
- Environment variable configuration
- Thread-safe model loading
- LRU caching for text preprocessing
- Comprehensive logging
- Docker support
- Docker Compose configuration
- CI/CD with GitHub Actions
- Automated testing with pytest
- Security scanning in CI pipeline
- Multiple deployment options
- CSRF protection
- Error handlers for common HTTP errors

### Changed
- Updated Flask from 2.3.3 to 3.0.3
- Updated numpy from 1.24.3 to 1.26.4
- Updated pandas from 2.0.3 to 2.2.2
- Updated scikit-learn from 1.3.0 to 1.5.1
- Updated nltk from 3.8.1 to 3.9.1
- Updated gunicorn from 21.2.0 to 22.0.0
- Refactored app.py for better code quality
- Improved error handling
- NLTK data downloads only once on startup
- Debug mode disabled in production

### Fixed
- Global state management issues
- Model loading race conditions
- Missing CSRF protection
- Security vulnerabilities in dependencies
- Missing input validation
- Poor error messages

### Security
- Added Content Security Policy
- Added rate limiting
- Added input length validation
- Removed debug mode in production
- Added secure session configuration
- Added security documentation
