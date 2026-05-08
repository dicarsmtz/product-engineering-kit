# Startup Codex Plugin

Private Codex plugin bundle for Dicodeit/Roampler startup workflows.

This repository is meant to be installed as a Codex marketplace directly from GitHub. It includes portable skills and sanitized MCP configuration, but intentionally excludes auth tokens, Codex state, logs, sessions, caches, and local history.

## Included

- Dicodeit workflow skills copied from the current `~/.codex/skills` install, excluding system skills.
- Selected OpenAI skills repo downloads or OpenAI-derived skills, with their license/notice files preserved where present.
- `.mcp.json` with the active remote MCP server definitions for Notion, GitHub, and Atlassian.
- `templates/codex-config.template.toml` with the enabled official plugin and MCP wiring from the current Codex config.
- `.agents/plugins/marketplace.json` and `templates/marketplace.example.json` for GitHub marketplace installation.
- `docs/setup-inventory.md` with the captured setup inventory and portability notes.
- `docs/skill-sources.md` with the source ledger for bundled skills.

## Not Included

- `~/.codex/auth.json`
- Codex logs, SQLite state, shell snapshots, session history, model cache, and ambient suggestions
- OpenAI bundled/primary-runtime plugin cache contents
- Any private access token values

## Install From GitHub

The GitHub repository should publish this layout:

```text
.agents/plugins/marketplace.json
plugins/startup/.codex-plugin/plugin.json
plugins/startup/...
```

Do not publish unrelated local workspace folders, Codex state, auth files, caches, logs, or sessions into the marketplace repository.

Install the private marketplace from GitHub:

```bash
codex plugin marketplace add dicarsmtz/codex-plugins --ref main
```

Then enable the `startup` plugin in Codex. For private repositories, authenticate with GitHub in the environment Codex uses before running the command.

The marketplace file uses a relative `source.path` of `./plugins/startup`. That path is resolved inside Codex's fetched GitHub marketplace checkout; it is not a requirement to keep a local clone under `~/plugins`.

For GitHub MCP access, set `GITHUB_PAT_TOKEN` in the environment used by Codex. Notion and Atlassian should authenticate through their normal Codex/MCP auth flows when prompted.

## Track Updates

Track the repository's `main` branch by installing with `--ref main`. Pull marketplace updates with:

```bash
codex plugin marketplace upgrade codex-plugins
```

For stable rollouts, publish tags such as `v0.1.0` and install with `codex plugin marketplace add dicarsmtz/codex-plugins --ref v0.1.0`.

Enable the plugin as:

```toml
[plugins."startup@codex-plugins"]
enabled = true
```

## Refresh This Repo

When the live setup changes, refresh the bundled skills from `~/.codex/skills` and update `docs/setup-inventory.md`. Do not copy `~/.codex/auth.json`, `history.jsonl`, `logs_*.sqlite*`, `state_*.sqlite*`, cache directories, or session files into this repo.

When importing updates from the OpenAI skills repo, preserve upstream license and notice files and update `docs/skill-sources.md` with the source commit or tag when known.

Run validation after edits:

```bash
python3 -m json.tool .agents/plugins/marketplace.json
python3 -m json.tool plugins/startup/.codex-plugin/plugin.json
python3 -m json.tool plugins/startup/.mcp.json
python3 -m json.tool plugins/startup/templates/marketplace.example.json
```
