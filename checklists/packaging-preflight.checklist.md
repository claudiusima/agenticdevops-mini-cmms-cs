# Checklist — Packaging Pre-Flight

**When:** before tagging a release / running the packaging pipeline. This is the **Class-B** companion to `npm run <<PREFLIGHT>>`: the local pre-flight catches logic/lint/test/doc failures (the things a developer machine *can* reproduce), but packaging failures live on the CI runners and in cross-platform native builds, which a local machine **cannot** reproduce. Those don't get "pre-flighted" by running them — they get caught by *reading this list before the tag*.

**Why it exists:** the source project's beta launch cost five human round-trips because each packaging failure only surfaced on the runner and revealed the next. All five are now known. The unknown sixth will be new — but the known five must never recur, and that's what a read-before-tag checklist buys.

## Read before you tag

- [ ] **Runtime version matches the developer's known-working local toolchain — not another pipeline's choice.** The packaging build compiles native code; it must use the version that compiles cleanly on the maintainer's actual machines. If the human says "we use version X," that is ground truth (Rule 19) — use X. `<<SLOT: your packaging runtime + why (e.g. "Node 22 — native addon fails to compile on 24/Windows"). Note if the test-CI runtime deliberately differs.>>`
- [ ] **Lock-file / package-manager version pinned to match the lock file.** A runner whose default package-manager version differs from the one that *wrote* the lock file will reject the install. Pin the writer's version. `<<SLOT: your pin, e.g. "npm 11 to match the lock file.">>`
- [ ] **Publish/upload side-effects are disabled unless intended.** A packaging tool that sees a version tag may try to publish a release and fail on a missing token — or worse, succeed. `<<SLOT: your "don't auto-publish" flag, e.g. "--publish never on all dist scripts.">>`
- [ ] **Runner OS image pinned where a toolchain version matters.** A `*-latest` image can silently roll to a compiler/SDK the build's toolchain can't detect yet. Pin the known-good image for the platform that's sensitive to it. `<<SLOT: e.g. "windows-2022 — windows-latest ships a VS the bundled node-gyp can't find.">>`
- [ ] **Per-target arch is controlled in exactly one place.** If both the build config *and* the CLI invocation set architecture, the config can silently override the flag — producing a package with the wrong native binary inside (builds green, crashes on load). Set arch in one layer only; split per-arch into separate jobs if needed. `<<SLOT: your arch-control decision.>>`
- [ ] **Every platform's installer built from one commit, and the maintainer launched the primary one.** Green build ≠ launches. The human runtime-tests the real installer on the real target before it's called done (Rule 14 for packaging).

## The general shape

Local pre-flight handles what a dev machine can reproduce. This list handles what only the runner and cross-platform native builds reveal. When a *new* packaging gotcha surfaces, add a line here and a comment at its point-of-use in the CI config — so it's read before the next tag, not rediscovered on the next runner.
