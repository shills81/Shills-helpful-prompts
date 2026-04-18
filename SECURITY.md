# Security Policy

## Repository scope

This is a read-only reference library of prompts and security documentation.

- No server-side code is deployed from this repository
- No user data is collected
- No credentials, API keys, or secrets should ever appear in this repo

## Reporting a vulnerability

If you discover a security issue with this repository (for example, a file that accidentally contains sensitive information), please report it privately rather than opening a public issue.

**Contact:** Open a private vulnerability report via GitHub's [Security Advisories](../../security/advisories/new) feature.

Please include:
- A description of what you found
- The file path(s) involved
- Why you believe it is sensitive

We will respond within 7 days and take corrective action (removal + history scrub) if needed.

## What is NOT in scope

- Requests to add new prompts
- Pull requests of any kind
- Bug reports unrelated to sensitive data exposure

## Secret scanning

This repository uses:

1. **GitHub native secret scanning** — enabled automatically for public repos. GitHub will alert the owner if any known secret pattern is pushed.
2. **`.gitleaks.toml`** — a local config for running [gitleaks](https://github.com/gitleaks/gitleaks) scans before committing.
3. **`.gitignore`** — blocks common credential file patterns from ever being staged.

## Security audits

Third-party tool audits are published in the [`security-audits/`](security-audits/) folder for transparency.
