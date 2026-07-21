# Key Architecture Facts — SCAFFOLD (Layer B2)

> **This is shape, not content.** Copy it to `<<ARCHITECTURE_FACTS_DOC>>` in your repo and fill it with *your* project's hard constraints. For a filled example, read `layer-b1-example/architecture-facts.example.md` — same structure, populated with a worked example's constraints.

## What this section is

The **hard technical constraints every spec must enforce.** Not preferences, not style — the rules that, if broken, produce architectural rot that's expensive to unwind. The PM cites the relevant facts in every spec; the coding agent honors them (they're the spine of its `CLAUDE.md`); the review agent can catch violations of the ones visible in a diff.

## How to write a fact

Each fact is **a rule stated so a spec can enforce it**, plus a one-line rationale or a pointer to the decision that established it. Not a narrative — a constraint.

```
### <<Fact name>>
<<The rule, imperative. What must always / never happen.>> <<Why, in one line, or "see DEC-NNN.">>
```

Group facts by concern so a spec author can scan to the ones that apply. Mark the single hardest, most-violated one explicitly ("this is the hardest rule — no exceptions") so it gets the attention it needs.

## The slots — fill each with a real constraint (delete the ones that don't apply)

### Process / layer boundaries
`<<SLOT: what logic is allowed where. E.g. which layer may talk to the database, which may not; what the presentation layer is forbidden from doing. Name the hardest boundary and say "no exceptions.">>`

### Canonical data formats
`<<SLOT: the on-disk / on-the-wire format that is authoritative, and the tempting-but-wrong formats that must NEVER be stored. Round-trip guarantees.>>`

### Persistence & migrations
`<<SLOT: schema authority, how migrations are versioned, whether there's a rollback path, additive-only rules.>>`

### Module-boundary contracts
`<<SLOT: how the boundary between processes/services is typed and validated end-to-end; the one bridge that may cross it; what may never bypass the typed wrapper. (This is what contract-sync.scaffold.md enforces the same-commit rule for.)>>`

### Security baseline
`<<SLOT: the settings that must not be weakened; the user-data boundary (never read/write/delete user data files); secret handling.>>`

### Derived vs. authoritative state
`<<SLOT: any index/cache that is DERIVED and must never be treated as source of truth (rebuilt from the authoritative store).>>`

### Styling / brand (if the project has a UI)
`<<SLOT: the token/theme discipline; where raw values are banned; the centralized brand system to reuse rather than reinvent.>>`

### Testing boundaries
`<<SLOT: which test type covers which layer; what must NOT be tested with the wrong tool.>>`
