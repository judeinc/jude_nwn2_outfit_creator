# Jude NWN2 Outfit Creator Project

## Current Baseline
- Version: 1.3.0
- Blender target: 5.1+
- Main add-on file: `__init__.py`
- Starter asset blend: `judes_ai_outfit_creator_skels.blend`
- Current release changelog: `CHANGELOG_1.3.0A.txt`
- Latest packaged zip: `C:\Users\Raymond Arellano\AppData\Roaming\Blender Foundation\Blender\5.1\scripts\addons\Jude_NWN2_Outfit_Creator_v1.3.0A.zip`

## Supported Profiles
- HHM: Human Male
- HHF: Human Female
- OOM: Half-Orc Male
- OOF: Half-Orc Female

## Key Systems
- Modular body profile registry via `NWN2_BODY_PROFILES`
- Profile shaping presets via `NWN2_PROFILE_SHAPE_PRESETS`
- Hidden profile mannequins for safer weight-transfer fallback
- Step-based workflow from AI mesh import through rigging, baking, Repository storage, and MDB export
- Substance Painter handoff export
- Repository workflow for storing multiple finished outfits in one Blender session
- Batch Export Repository with preflight checks and one-folder-per-outfit output
- Robe/dress donor weighting for HHM and HHF profiles
- v1.3.0A robe mode uses only the robe donor mesh, not boots/gloves donors
- v1.3.0A reduced Ai_Rig excludes palm bones and cleans palm vertex groups from
  fitted donors
- MDB texture flag controls and post-export flag patching
- Main-step and sub-step workflow highlighting for guided user progress

## Important Stability Notes
- Repository meshes must never be normalized into starter asset names.
- Starter duplicate cleanup should only target true Blender suffix duplicates such as `.001`.
- Step 1 ignores meshes in `NWN2_Repository` and `NWN2_Export`.
- MDB export requires object name, mesh data name, and material name to match exactly.
- COLS should stay hidden except during export.
- Batch export stops on the first export error and restores the Export slot afterward.

## Recommended Codex Project Root
Use this folder as the project root:

`C:\Users\Raymond Arellano\AppData\Roaming\Blender Foundation\Blender\5.1\scripts\addons\jude_nwn2_outfit_creator`

This is the live add-on folder Blender loads, so edits here are immediately testable after restarting or reloading the add-on.
