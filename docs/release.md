# Release preparation

The 0.1.0 candidate is prepared in an independent private repository. Export the reviewed tree, verify its file paths, modes, and bytes, and record the candidate changes in a private comparison. Create a new root commit with the approved noreply identity for both author and committer. Keep the source history and review evidence in their existing private locations.

## Candidate scope

| Evaluated area | Decision |
| --- | --- |
| Context retrieval, memory checkpoint, project session, deployment verification | Publishable after abstraction and original English authoring. Shared retrieval, maintenance, recency, and ownership ideas are integrated where they affect the same decision. |
| Behavior reconstruction | Publishable after original authoring for authorized local software contracts. Examples and evaluation evidence are synthetic. |
| Final Audit | Deferred pending rights review. Prefer a separately designed method using public references and synthetic cases if a future release needs a software readiness gate. |
| Audit Orchestrator | Deferred pending dependency and rights review. A future proposal would need an independently specified static workflow, isolation evidence, and actual provider tests. |
| Specialized .NET procedures | Deferred pending rights review. A future generic skill can start from public framework documentation and original examples. |
| Internal registries, scripts, runbooks, state, and history | Private. Generalizable candidate triage and context drift are handled by two released procedures where applicable. |
| Independent tools | Third-party. Links only. The MIT proposal pertains to original distribution material. |

## Publication checklist

- [ ] Freeze the candidate SHA and build the distribution from the reviewed path inventory.
- [ ] Confirm rights and license with the maintainer, including the copyright notice, tools, references, and any required attributions.
- [ ] Inspect the complete tree and reachable Git objects (commit messages and identities, all refs, tags, trees, and blobs). Check remotes, workflows, links, fixtures, attachments, binary files, and any stored release artifacts.
- [ ] Run a redacted secret scan over the tree and reachable history. Apply private-reference checks and manually review results without exporting the private rule list.
- [ ] Record results for the exact SHA, CI jobs, client checks, and unresolved limitations. Keep raw review artifacts and the private provenance record outside the distribution.
- [ ] Obtain an independent review, resolve demonstrated issues, and repeat affected checks on the final candidate.
- [ ] Verify CI on a push to `main` for the exact candidate SHA. Inventory pull requests, Projects, workflows, logs, artifacts, and repository settings on the destination. Check that the destination cannot resolve the excluded source revisions using authenticated access and record any permission limits.
- [ ] Obtain explicit approval for public visibility, the proposed MIT license, and the release. Recheck branch, tag, and release settings before changing visibility.

## Maintenance

For 0.1.0, keep the private source canonical for its own workflows. Review and port generalizable changes manually into the distribution. Periodically evaluate making the public skill packages the canonical source for generic procedures while retaining overlays for private tools, paths, and policies. Adopt that ownership change by explicit approval and decide how private overlays pin reviewed upstream versions. Keep distribution approvals, provenance, and private exceptions separately.

The [Agent Context Kit roadmap](agent-context-kit.md) describes a separate, unimplemented framework proposal.
