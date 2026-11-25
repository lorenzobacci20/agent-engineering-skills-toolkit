# Contract and equivalence table

Agree on the reference version, replacement version, permissible differences, and input partitions. Reuse input fixtures when the formats permit it.

| Case | Setup and input | Expected observation | Source | Comparison |
| --- | --- | --- | --- | --- |
| Tied labels | two records with the same label, distinct IDs | IDs remain in input order | fixture run of the reference version | exact output order |
| Omitted label | a record without a label | validation error with no saved output | reference test at the candidate commit | error category and unchanged output |
| Non-ASCII folding | mixed scripts | unknown | no observation | exclude from equivalence claims |

Record inferred rules with their competing explanation. Record the result for each comparison and any difference the owner explicitly accepted. For nondeterministic fields, document a precise invariant and preserve the raw observation locally when permitted.
