# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Features

- HTTPS enforcement in production
- Content Security Policy headers
- Rate limiting (10 requests/minute per IP)
- Input validation and sanitization
- Request size limits (16KB max)
- CSRF protection via Flask secret key
- Secure session cookies

## Reporting a Vulnerability

If you discover a security vulnerability, please email security@example.com.

Do not open public issues for security vulnerabilities.

## Best Practices

1. Always use HTTPS in production
2. Set a strong SECRET_KEY environment variable
3. Keep dependencies updated
4. Monitor logs for suspicious activity
5. Use environment variables for sensitive data
