# Authorized local observations

| Fixture | Input | Reference | Replacement |
| --- | --- | --- | --- |
| Normal ordering | labels B then A | labels A then B | labels A then B |
| Tie | same label, IDs 2 then 1 | IDs 2 then 1 | IDs 1 then 2 |
| Missing label | one record with missing label | INVALID_LABEL; no output | INVALID_LABEL; no output |

The documented interface requires alphabetical order by label and says nothing about ties. No fixture exercised case folding. Access is limited to these observations and owner-provided local fixtures.
