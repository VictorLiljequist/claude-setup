# Plugin setup

Plugins are intentionally not vendored here. Install them in Claude Code using their current official instructions.

## Superpowers
Repository and current setup instructions: https://github.com/obra/superpowers

## Anthropic-maintained plugins
Official marketplace: https://github.com/anthropics/claude-plugins-official
Install only the plugins you need and review requested permissions.

## Playwright MCP
`.mcp.json` configures `npx -y @playwright/mcp@latest`. Requires Node.js/npm. Start Claude Code from the project root and approve/connect the server when prompted. Follow the package's current browser installation instructions. Avoid authenticated production sessions in automated tests.

## GitHub
Use least-privilege GitHub access. Prefer pull requests. Never commit a personal access token.
