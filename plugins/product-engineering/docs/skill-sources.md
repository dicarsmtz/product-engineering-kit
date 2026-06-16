# Skill Sources

Track the source of every bundled skill here so GitHub installs stay reviewable and upstream updates can be refreshed deliberately.

| Skill | Source | Tracking Notes |
| --- | --- | --- |
| `resources-to-jira` | Dicodeit/Roampler custom skill | Keep aligned with `resources-to-notion-prd` and `resources-to-notion-technical-design`. |
| `resources-to-notion-prd` | Dicodeit/Roampler custom skill | Product-only Notion PRD workflow. |
| `resources-to-notion-technical-design` | Dicodeit/Roampler custom skill | Codebase-validated Notion technical design workflow. |
| `playwright` | Downloaded or derived from the OpenAI skills repo; includes material derived from `microsoft/playwright-cli` | Preserve `LICENSE.txt` and `NOTICE.txt`; refresh deliberately from upstream. |
| `screenshot` | Downloaded from the OpenAI skills repo | Preserve `LICENSE.txt`; record upstream commit/tag when refreshing. |
| `security-best-practices` | Downloaded from the OpenAI skills repo | Preserve `LICENSE.txt`; record upstream commit/tag when refreshing. |
| `security-threat-model` | Downloaded from the OpenAI skills repo | Preserve `LICENSE.txt`; record upstream commit/tag when refreshing. |
| `playwright-interactive` | Local Dicodeit adaptation | Reuses Playwright assets and notices; keep `NOTICE.txt` aligned with asset provenance. |

## Refresh Policy

When importing upstream skill updates:

1. Record the upstream repository, commit, tag, or release used.
2. Preserve license and notice files from the imported skill.
3. Review local modifications before replacing files.
4. Validate the plugin manifest and marketplace JSON after refresh.
