# Installation

Use a clone or a source archive you are allowed to access. For reproducibility, select the reviewed commit and keep its SHA in your notes. A private GitHub repository requires authenticated access. Open the target project in the client only after reviewing the copied files.

| Client | Project directory (preferred) | User directory (optional) | Explicit invocation |
| --- | --- | --- | --- |
| Codex | .agents/skills/ | ~/.agents/skills/ | Use the skill picker or enter $deployment-verification in the request |
| Claude Code | .claude/skills/ | ~/.claude/skills/ | Enter /deployment-verification followed by the task and fixture path |

Use the project root for project installation. Inspect other applicable discovery paths for the same skill name before adding it. Project trust and organization policies may affect discovery. See the [Codex guide](https://learn.chatgpt.com/docs/build-skills) and [Claude Code guide](https://code.claude.com/docs/en/skills).

## Manual installation

Start in the target project. Replace the example source path with the path to the reviewed checkout. Select the appropriate client directory from the table. Copy the full skill directory so that references and scripts remain available.

POSIX shell example for Codex:

~~~sh
source_repo=../agent-engineering-skills
skill=deployment-verification
destination=.agents/skills
test -f "$source_repo/skills/$skill/SKILL.md" &&
  test -f "$source_repo/LICENSE" &&
  mkdir -p "$destination" &&
  mkdir "$destination/$skill" &&
  cp -R "$source_repo/skills/$skill/." "$destination/$skill/" &&
  cp "$source_repo/LICENSE" "$destination/$skill/LICENSE"
~~~

PowerShell example for Claude Code:

~~~powershell
$sourceRepo = '../agent-engineering-skills'
$skill = 'deployment-verification'
$source = Join-Path $sourceRepo "skills/$skill"
$license = Join-Path $sourceRepo 'LICENSE'
if (-not (Test-Path -LiteralPath $license -PathType Leaf)) { throw 'The distribution license is missing.' }
$destination = '.claude/skills'
if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) {
    throw 'The reviewed source skill is missing.'
}
$null = New-Item -ItemType Directory -Path $destination -Force -ErrorAction Stop
$slot = Join-Path $destination $skill
if (Test-Path -LiteralPath $slot) { throw "The skill already exists at $slot." }
$null = New-Item -ItemType Directory -Path $slot -ErrorAction Stop
Get-ChildItem -LiteralPath $source -Force |
    Copy-Item -Destination $slot -Recurse -ErrorAction Stop
Copy-Item -LiteralPath $license -Destination $slot -ErrorAction Stop
~~~

Repeat for each selected skill. The new destination must be absent. If the copy fails, inspect the incomplete directory before retrying. These commands require no downloads, configuration edits, or hooks.

## Optional Skills CLI

The independent [Skills CLI](https://github.com/vercel-labs/skills) supports local source directories and agent selection. Review the specific CLI version before using it. Use an already installed version and a fresh scratch project without an existing target skill. The CLI may manage installation metadata and links, so evaluate that behavior in the scratch project first.

~~~sh
skills add ../agent-engineering-skills --skill deployment-verification --agent codex
skills list --agent codex
~~~

For Claude Code, select the claude-code agent instead. Keep the command interactive and review the proposed destination before accepting. Use the manual approach if you require an ordinary directory copy. Check that standalone copies include the distribution LICENSE with its copyright and permission notice. If the installer omits it, copy LICENSE from the reviewed source before sharing the installed files. The optional CLI is outside the package tests.

## Verify and invoke

Start a fresh client session in the target project. Confirm the skill name in the client's picker or skill commands. Copy only the [synthetic receipt](../examples/synthetic-project/release-wrong-rollout.json) into that workspace and run the following request with the applicable prefix.

~~~text
$deployment-verification Assess release-wrong-rollout.json. Distinguish CI, deployment, and runtime status using only this fixture.
/deployment-verification Assess release-wrong-rollout.json. Distinguish CI, deployment, and runtime status using only this fixture.
~~~

The expected result identifies a CI mismatch, a consistent deployment receipt, and a runtime rollout mismatch. Optionally run the checker directly from the reviewed checkout. Its exit status should be 1 for this fixture.

## Update or remove

Review the old-to-new diff and pin the new SHA. For manual updates, move the existing installed directory outside all discovery paths before copying the new version. Keep it as a backup until a fresh session discovers and exercises the update. For removal, inspect the selected project or user path, then remove only your installed copy or link and restart the client. Preserve any local edits elsewhere. If the Skills CLI manages the copy, review its documented update and remove behavior in the scratch project and select the exact skill and destination before applying it.
