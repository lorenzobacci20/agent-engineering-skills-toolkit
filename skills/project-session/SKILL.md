---
name: project-session
description: Start, resume, or hand off substantive work in a software repository. Use when inheriting a branch or prior session, changing an existing project, or closing work with reproducible evidence.
---

# Project Session

1. Confirm the intended outcome and the working repository. Read the applicable local instructions. Record the branch, commit, working-tree state, and the relevant existing tests or CI. Treat another contributor's local edits as input to preserve.
2. Read only the handoff, decision, or task history needed to understand the change. Recheck assumptions about current code and availability at the live source. If an inherited failing baseline matters, capture it before editing.
3. Follow the normal entry point through the affected code and data. Reuse the repository's conventions and validation. Keep operational writes, external publication, and release actions within the user's authorization.
4. Exercise the changed behavior and consequential regression paths. Record what ran, the revision or dirty-tree state it ran against, and the result. Reconcile pre-existing failures separately. Inspect the final diff for unrelated edits, generated files, and sensitive content.
5. Close with a reproducible handoff. Include the outcome, touched surfaces, source anchors, checks and results, unresolved work, and the exact next action if incomplete. Put durable project facts in project documentation or its tracker when authorized.

For interrupted work or conflicting validation evidence, use the [handoff worksheet](references/handoff.md).
