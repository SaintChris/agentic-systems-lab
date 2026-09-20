# AGENTS.md

## Scope

This repository is a learning/portfolio engineering lab. Preserve the distinction between demonstrated behavior, simulated/demo behavior, design intent, and production-grade capability.

## Change discipline

- Make focused changes with a clear reason.
- Do not inflate project claims, test counts, reliability, scale, or production status.
- Update tests when behavior changes.
- Keep setup and verification commands reproducible.
- Preserve local-first operation unless a change explicitly introduces and documents an external dependency.
- Never commit credentials, private user data, tokens, or environment-specific secrets.

## Required verification

Before claiming a change works, run the relevant test/lint/build commands documented by this repository. If verification cannot be run, state that explicitly in the PR or commit documentation.

## Documentation

Update the README or architecture documentation when a change alters:

- setup,
- runtime dependencies,
- architecture,
- security/privacy boundaries,
- user-visible behavior,
- verification procedures.

AI-generated changes require the same evidence and review standard as human-authored changes.
