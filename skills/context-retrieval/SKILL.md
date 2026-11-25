---
name: context-retrieval
description: Retrieve the minimum decision-relevant context for a coding task when project documentation, saved memory, and live evidence may disagree. Use for resuming work, routing a project lookup, or resolving a stale claim.
---

# Context Retrieval

1. Write the decision or claim to establish and its subject, scope, and required freshness. Skip memory retrieval when the answer is independent of project or user context.
2. Start with the nearest relevant project index or a short context pack. Use it to locate sources. Read the live artifact that can establish the specific claim, such as a test at the current commit or a runtime observation for a live-state question.
3. Set a first-pass budget. A usable default is one index and up to three targeted reads. Prefer exact paths, matched lines, and narrow queries. Expand only to resolve a gap that could change the decision. State the gap before expanding and stop once the evidence supports the decision.
4. Compare sources on the same subject, scope, and effective period. Use the most recent reliable observation from a source competent to establish the claim. A newer summary of an older observation keeps the older evidence date. Current user instructions govern the action.
5. If the primary route fails, try one distinct permitted route such as a local index or direct file read. When live evidence is unavailable, qualify the conclusion as historical, provisional, or unknown. Surface any conflict that still changes the outcome.

Return the decision, the smallest useful set of source anchors, and the residual uncertainty. Record observation dates for volatile claims. Avoid reading unrelated domains or broad indexes of sensitive material.

Use the [source comparison worksheet](references/source-comparison.md) for conflicting snapshots or multiple environments.
