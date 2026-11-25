# Compatibility

The packages follow the [Agent Skills specification](https://agentskills.io/specification). They use two fields, name and description, in plain YAML frontmatter. Their Markdown resources resolve from the skill directory. The optional Python receipt checker requires Python 3.10 or newer. No client-specific metadata, hooks, or connectors are required.

## Format and discovery

| Surface | Documented discovery and invocation | Candidate check |
| --- | --- | --- |
| Codex CLI | Project-local .agents/skills and explicit skill invocation | CLI 0.164.0 app-server discovered all five project-local skill copies on Windows |
| Claude Code CLI | Project-local .claude/skills and slash invocation | CLI 2.1.323 listed all five project-local skills in its initialization event on Windows |
| Other Agent Skills consumers | Implementation-specific discovery | Unverified |
| Optional Skills CLI | Local source and agent selection | Documentation reviewed, installation untested |

The official skills-ref validator accepted all five packages at validator source revision 83021e2be457a9b6679148719c1f6074f0ad975e. Both manual install examples copied the complete selected skill and refused to overwrite an existing installation in scratch projects on Windows. POSIX commands were exercised through Git Bash.

## Deterministic checks

The repository validator checks package structure, Markdown destinations, and the ten synthetic scenarios. The Python suite and 24 independent CLI cases exercised the offline receipt checker. The checker tests consistency within the supplied receipt. Authenticity, freshness, and live state require separate evidence from the systems involved.

## Observed model behavior

The independent trials used synthetic fixtures and project-local skills on Windows. The principal trials ran Codex CLI 0.164.0 and Claude Code 2.1.323 against Ollama 0.40.18 with `gpt-oss:20b` and a 16,384-token context. The two clients used different evidence paths.

| Trial | Observed outcome |
| --- | --- |
| Codex CLI, Deployment Verification | Failed the case. During manual review it found the runtime rollout mismatch and incorrectly accepted the CI commit. The turn did not execute the checker. |
| Claude Code, Deployment Verification | Partial. The trace shows the installed checker ran and returned exit 1. The response reported all six stage states correctly and incorrectly attributed a timestamp comparison to the script. The checker has no timestamp check. |
| Codex CLI, Memory Checkpoint | Failed deduplication in an earlier trial on the same skill content. It proposed duplicating an existing ADR and assumed knowledge of the project ledger. |
| Claude Code, additional trials with `qwen2.5-coder:14b` | Failed the observed tasks. The output resembled tool calls, with no corresponding execution event. |

Cloud backends remain unverified. The isolated Codex cloud request returned HTTP 401, and Claude Code required login. Discovery establishes which skills the client listed. Effectiveness requires scored task outcomes. The [paired A/B study](evaluation.md) has yet to run.

Discovery can be affected by organization settings, duplicate names, project trust, and client version. Skill selection behavior, tool permissions, and skill use are separate from package compatibility. See the [installation guide](installation.md), [Codex documentation](https://learn.chatgpt.com/docs/build-skills), [Claude Code documentation](https://code.claude.com/docs/en/skills), and [Skills CLI documentation](https://github.com/vercel-labs/skills).
