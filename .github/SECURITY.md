# Security Policy

## Supported Versions

We release patches for security vulnerabilities.  Which versions are
eligible for patches depends on the severity and CVSS score.

| Version | Supported          |
|---------|--------------------|
| ≥ 1.0   | Full support       |
| < 1.0   | Best-effort only   |

## Reporting a Vulnerability

If you discover a security vulnerability, please do **not** open a public
issue.  Instead, report it privately via email:

**security@spamlyser.dev**

We will acknowledge receipt within 48 hours and send a more detailed
response within 5 business days describing the next steps.

### What to include

- Type of issue (e.g. XSS, CSRF, dependency vulnerability)
- Steps to reproduce
- Affected versions
- Any proof-of-concept or exploit code (if available)

## Disclosure Policy

When we receive a security bug report, we will:

1.  Confirm the problem and determine the affected versions.
2.  Audit the code to find any similar issues.
3.  Prepare fixes and release them as soon as possible (typically within
    7–14 days, depending on severity).
4.  Credit the reporter in the release notes (unless anonymity is
    requested).

## Security-related Configuration

See `.env.example` and `.streamlit/secrets.toml.example` for recommended
production settings.
