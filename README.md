# Jude NWN2 Outfit Creator

Jude NWN2 Outfit Creator is a Blender 5.1+ add-on for converting AI-generated or high-poly outfit meshes into Neverwinter Nights 2-ready outfit assets.

It provides a guided, step-by-step workflow for importing meshes, creating low-poly versions, fitting and weighting them to NWN2 body profiles, baking texture maps, organizing finished outfits in a local Repository collection, and exporting `.mdb` files for use with NWN2 modding tools.

## Video Demonstration

[![Jude NWN2 Outfit Creator video demonstration](https://img.youtube.com/vi/ij2G52nT5i0/maxresdefault.jpg)](https://youtu.be/ij2G52nT5i0)

Watch the public demonstration: [Jude NWN2 Outfit Creator on YouTube](https://youtu.be/ij2G52nT5i0)

## First Official Release

Version 1.2.4 is the first official public release of the add-on.

Earlier 1.2.x builds were pre-release and beta-tested during active development. Those builds helped validate the profile system, repeated-session Repository workflow, batch export behavior, half-orc support, and the final Blender 5.1 workflow polish included here.

## Current Version

- Release: 1.2.4
- Blender target: 5.1+
- Status: First official public release
- Main add-on file: `__init__.py`

## What It Does

- Imports high-poly AI outfit meshes into Blender.
- Creates a low-poly working mesh through bundled/assisted decimation workflows.
- UV unwraps the low-poly mesh with the bundled Ministry of Flat command-line tool.
- Fits the outfit to NWN2 profile skeletons.
- Transfers and repairs weights for NWN2-compatible rigging.
- Supports final pose, sculpt, and fitting adjustments.
- Bakes diffuse, normal, specular/roughness, metallic, and AO texture maps.
- Exports Substance Painter handoff files.
- Stores finished outfits in an in-scene Repository collection.
- Exports NWN2 `.mdb` files with the matching skeleton, COLS hierarchy, and optional textures.
- Batch exports Repository outfits into one folder per outfit.

## Supported Body Profiles

- `HHM` - Human Male
- `HHF` - Human Female
- `OOM` - Half-Orc Male
- `OOF` - Half-Orc Female

The add-on uses a modular profile registry so additional NWN2 body profiles can be added later without rewriting the whole workflow.

## Major 1.2.4 Features

- Added workflow progress tracking with a `Next:` status line.
- Added red next-button highlighting so users know which step to click next.
- Fixed Substance Painter handoff orientation so exported OBJ files import upright.
- Added a `Show Vanilla Gloves/Boots` toggle for final fitting.
- Kept `Show Vanilla Body` independent from gloves/boots visibility.
- Preserved Repository safety and batch export behavior from v1.2.3.

## Installation

1. Download the release zip:
   `Jude_NWN2_Outfit_Creator_v1.2.4.zip`
2. Open Blender 5.1 or newer.
3. Go to `Edit > Preferences > Add-ons`.
4. Click `Install from Disk`.
5. Select the zip file.
6. Enable `Jude's AI to NwN2 Outfit Creator`.
7. Open the 3D View sidebar and use the `NWN2 Outfit` tab.

The zip should be installed as a Blender add-on package. Do not unzip it manually unless you are developing or debugging the add-on.

## Basic Workflow

1. Load the starter scene.
2. Import the high-poly AI mesh.
3. Decimate or duplicate a low-poly working mesh.
4. UV unwrap the low-poly mesh.
5. Lock the low-poly bake reference.
6. Identify the AI mesh.
7. Prepare the rig.
8. Fit and auto-weight the rig.
9. Restore to NWN2 scale.
10. Perform final fitting and sculpt cleanup.
11. Build the material name and setup shader nodes.
12. Bake texture maps.
13. Optionally export a Substance Painter handoff.
14. Clean up and send the outfit to the Repository.
15. Send an outfit to the Export slot.
16. Export the final `.mdb`.

The add-on now tracks the expected next action and highlights the next button in red.

## Bundled Files

This repository includes the files needed by the add-on:

- `judes_ai_outfit_creator_skels.blend` - starter skeleton/reference asset library
- `UnWrapConsole3.exe` - Ministry of Flat UV unwrap helper
- `texconv.exe` - DDS texture conversion helper
- `CHANGELOG_1.2.4.txt` - current release notes

## Notes For Modders

- Repository meshes are protected from starter asset normalization.
- Starter duplicate cleanup only targets true Blender suffix duplicates such as `.001`.
- Step 1 ignores meshes inside `NWN2_Repository` and `NWN2_Export`.
- MDB export enforces matching object, mesh data, and material names.
- COLS remains hidden except during export.
- Batch export stops on the first export error and restores the Export slot afterward.

## Development Notes

This add-on is currently maintained as a single Blender add-on module:

- `__init__.py`

Recommended local checks:

```powershell
python -m py_compile __init__.py
& 'C:\Program Files\Blender Foundation\Blender 5.1\blender.exe' --background --factory-startup --python-expr "import sys, bpy; sys.path.insert(0, r'C:\Users\Raymond Arellano\AppData\Roaming\Blender Foundation\Blender\5.1\scripts\addons'); import jude_nwn2_outfit_creator as a; a.register(); a.unregister(); print('OK')"
```

## Credits

Created by Jude / Raymond Arellano for Neverwinter Nights 2 outfit modding workflows.

This project is intended to make AI-assisted outfit creation more approachable for NWN2 modders while preserving the naming, skeleton, weighting, texture, and export rules the game expects.
