# Changelog

## Unreleased

- Added a uv-based `edit-master` harness CLI for build, bridge, validate, eval, answer, feedback, and full-loop execution.
- Added `edit-master.toml`, `pyproject.toml`, and `uv.lock` so users no longer need to run individual Python scripts directly.
- Updated README usage examples to prefer `uv run edit-master ...`.

## 0.1

Initial Learnable Agent wiki/runtime baseline.

- Scene-first recommendation graph and matcher
- Graphify-generated wiki and source graph outputs
- Source-to-recommender bridge validation
- Natural photo-coach answer renderer
- Client-provided image observation contract
- Local personalization learning loop
- Hourly collection and legacy evaluation artifacts removed
