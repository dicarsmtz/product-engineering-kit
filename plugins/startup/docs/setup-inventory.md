# Setup Inventory

Captured on 2026-05-08 from `/Users/dicodeit/.codex` and `/Users/dicodeit/astreal/code/roampler`.

## GitHub Marketplace Install

This bundle is intended to be installed from GitHub as a Codex marketplace:

```bash
codex plugin marketplace add dicodeit/codex-startup --ref main
```

Update tracking is handled by Codex marketplace upgrades:

```bash
codex plugin marketplace upgrade startup
```

The active marketplace file is `.agents/plugins/marketplace.json` at the repository root. Its plugin entry points to `./plugins/startup`, resolved inside Codex's fetched marketplace checkout.

The GitHub repository should publish only the marketplace files needed for this bundle, not unrelated local Roampler workspace folders.

## Bundled Skills

Custom Dicodeit/Roampler workflow skills:

- `jira-from-design`
- `resources-to-notion-prd`
- `resources-to-notion-technical-design`

OpenAI skills repo downloads or OpenAI-derived skills:

- `playwright`
- `screenshot`
- `security-best-practices`
- `security-threat-model`

Local adaptation using Playwright assets:

- `playwright-interactive`

See `docs/skill-sources.md` for source tracking notes.

## Excluded System Skills

System skills were not copied because they are supplied by Codex itself:

- `imagegen`
- `openai-docs`
- `plugin-creator`
- `skill-creator`
- `skill-installer`

## Enabled Official Plugins

These were detected in `~/.codex/config.toml` and are recorded in `templates/codex-config.template.toml`. They are not vendored into this private plugin because they are supplied by Codex runtime marketplaces.

- `browser-use@openai-bundled`
- `documents@openai-primary-runtime`
- `spreadsheets@openai-primary-runtime`
- `presentations@openai-primary-runtime`

## App Connectors

The current session exposed Codex Apps tools for Figma and Notion. No local `.app.json` manifest was found during capture, so those connectors are treated as account/runtime-managed integrations rather than files to vendor into this plugin.

## MCP Servers

Bundled in `.mcp.json`:

- `notion`: `https://mcp.notion.com/mcp`
- `github`: `https://api.githubcopilot.com/mcp/`, using `GITHUB_PAT_TOKEN`
- `atlassian`: `https://mcp.atlassian.com/v1/mcp/authv2`

## Excluded For Safety

- `auth.json`
- `history.jsonl`
- `logs_2.sqlite*`
- `state_5.sqlite*`
- `.codex-global-state.json*`
- `sessions/`
- `shell_snapshots/`
- `cache/`
- `vendor_imports/`
- `models_cache.json`
- `ambient-suggestions/`

Keep this plugin private because the bundled skills encode internal workflow assumptions and repository-specific planning behavior.
