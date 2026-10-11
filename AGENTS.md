# Repository Guidance

## Purpose and boundaries
- Maintain a reusable typed REST client baseline, independent of any one API provider.
- Keep authentication, transport, and response behavior replaceable after cloning.

## Development
- Put client implementation in `src/` and contract tests in `tests/`.
- Preserve clear exception and public method behavior when changing the template surface.

## Validation
- Run `uv sync --frozen --group dev`, `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy`, `uv run pytest`, and `uv run pre-commit run --all-files`.
- Run `uv build` for package and release metadata changes.

## Architecture constraints
- Keep provider URLs and credentials out of defaults; use injectable configuration.
- Keep the package rename path and README examples aligned.

## Safety
- Tests and examples must use fake responses or non-sensitive public fixtures.

## Branching strategy

- This repository uses **trunk-based development**. Create short-lived change branches from current `main` and target PRs to `main`.
- Follow the [canonical branching and delivery policy](https://github.com/SpencerRWood/codex-config/blob/main/docs/branching-policy.md), available through the installed codex-config source path. Verify the strategy, release association, fetched base and PR target before implementation and record them in Story evidence. Story completion does not authorize publication or deployment; retain existing review, CI, security and rollback requirements.
- This classification applies to maintenance of the template repository. Replace it with the new repository's classification during project creation; applications must use release-branch integration before Story development begins.
