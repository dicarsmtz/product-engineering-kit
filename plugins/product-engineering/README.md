# Product Engineering Plugin

Private Codex and Claude Code plugin bundle for Dicodeit product engineering workflows.

This repository is meant to be installed as a Codex marketplace or Claude Code marketplace directly from GitHub. It includes portable skills and sanitized MCP configuration, but intentionally excludes auth tokens, agent state, logs, sessions, caches, and local history.

## Included

- Dicodeit workflow skills copied from the current `~/.codex/skills` install, excluding system skills.
- Selected OpenAI skills repo downloads or OpenAI-derived skills, with their license/notice files preserved where present.
- `.mcp.json` with the active remote MCP server definitions for Notion, GitHub, and Atlassian.
- `templates/codex-config.template.toml` with the enabled official plugin and MCP wiring from the current Codex config.
- `.agents/plugins/marketplace.json` and `templates/marketplace.example.json` for GitHub marketplace installation.
- `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` for Claude Code marketplace installation.
- `docs/setup-inventory.md` with the captured setup inventory and portability notes.
- `docs/skill-sources.md` with the source ledger for bundled skills.

## Intended Workflow

The bundle is organized around product engineering delivery:

- Turn mixed product resources into Notion PRDs.
- Turn PRDs, prompts, architecture notes, and code context into Notion technical designs.
- Turn product and technical decisions into Jira implementation stories.
- Review UI/UX quality, accessibility, and design-system consistency.
- Perform security best-practice reviews and repository-grounded threat models.
- Verify implementation behavior with Playwright, screenshots, and browser interaction.

## Not Included

- `~/.codex/auth.json`
- Codex logs, SQLite state, shell snapshots, session history, model cache, and ambient suggestions
- OpenAI bundled/primary-runtime plugin cache contents
- Any private access token values

## Install In Codex

The GitHub repository should publish this layout:

```text
.agents/plugins/marketplace.json
.claude-plugin/marketplace.json
plugins/product-engineering/.codex-plugin/plugin.json
plugins/product-engineering/.claude-plugin/plugin.json
plugins/product-engineering/...
```

Do not publish unrelated local workspace folders, Codex state, auth files, caches, logs, or sessions into the marketplace repository.

Install the private marketplace from GitHub:

```bash
codex plugin marketplace add dicarsmtz/product-engineering-kit --ref main
```

Then enable the `product-engineering` plugin in Codex. For private repositories, authenticate with GitHub in the environment Codex uses before running the command.

The marketplace file uses a relative `source.path` of `./plugins/product-engineering`. That path is resolved inside Codex's fetched GitHub marketplace checkout; it is not a requirement to keep a local clone under `~/plugins`.

For GitHub MCP access, set `GITHUB_PAT_TOKEN` in the environment used by Codex. Notion and Atlassian should authenticate through their normal Codex/MCP auth flows when prompted.

## Install In Claude Code

Install the same repository as a Claude Code marketplace:

```bash
claude plugin marketplace add dicarsmtz/product-engineering-kit
claude plugin install product-engineering@product-engineering-kit
```

Claude Code reads `.claude-plugin/marketplace.json` at the repository root and installs `plugins/product-engineering` through the relative `source` path. The plugin-level Claude manifest exposes the existing `skills/` directory and `.mcp.json`.

For private repository auto-updates, set `GITHUB_TOKEN` or `GH_TOKEN` in the environment used by Claude Code. For GitHub MCP access through the bundled remote MCP server, keep `GITHUB_PAT_TOKEN` available where Claude Code runs.

## Track Updates

Track the repository's `main` branch by installing with `--ref main`. Pull marketplace updates with:

```bash
codex plugin marketplace upgrade product-engineering-kit
```

For stable rollouts, publish tags such as `v0.1.0` and install with `codex plugin marketplace add dicarsmtz/product-engineering-kit --ref v0.1.0`.

Enable the plugin as:

```toml
[plugins."product-engineering@product-engineering-kit"]
enabled = true
```

## Refresh This Repo

When the live setup changes, refresh the bundled skills from `~/.codex/skills` and update `docs/setup-inventory.md`. Do not copy `~/.codex/auth.json`, `history.jsonl`, `logs_*.sqlite*`, `state_*.sqlite*`, cache directories, or session files into this repo.

When importing updates from the OpenAI skills repo, preserve upstream license and notice files and update `docs/skill-sources.md` with the source commit or tag when known.

Run validation after edits:

```bash
python3 -m json.tool .agents/plugins/marketplace.json
python3 -m json.tool .claude-plugin/marketplace.json
python3 -m json.tool plugins/product-engineering/.codex-plugin/plugin.json
python3 -m json.tool plugins/product-engineering/.claude-plugin/plugin.json
python3 -m json.tool plugins/product-engineering/.mcp.json
python3 -m json.tool plugins/product-engineering/templates/marketplace.example.json
claude plugin validate .
claude plugin validate plugins/product-engineering
```
