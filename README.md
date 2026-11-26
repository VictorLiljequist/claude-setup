# Claude Code Setup

Reusable Claude Code configuration only — no application source, customer data, or secrets.

Includes focused agents, reusable skills, baseline rules, portable settings, Playwright MCP, and GitHub CI. Superpowers and Anthropic-maintained plugins are installed separately; see `docs/PLUGIN-SETUP.md`.

## Use in an application repository

Copy `.claude/`, `.github/`, `.mcp.json`, and `CLAUDE.md` into your app repo. Review/merge existing files instead of overwriting them blindly. Then run `claude` from the app root.

This is a starter: update `CLAUDE.md` with the app's verified stack, commands, architecture, and deployment rules. Never commit secrets or grant unattended production/destructive permissions.
=======
# claude-setup

