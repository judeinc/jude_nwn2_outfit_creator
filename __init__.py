bl_info = {
    "name": "Jude's AI to NwN2 Outfit Creator",
    "author": "Jude / Raymond Arellano",
    "version": (1, 2, 4),
    "blender": (5, 1, 0),
    "location": "View3D > Sidebar > NWN2 Outfit, Pie: Ctrl+Alt+N",
    "description": "Step-by-step modular body workflow for converting AI meshes to Neverwinter Nights 2 outfits with rigging, baking, MDB export, and Substance Painter handoff tools.",
    "category": "Import-Export",
    "support": "COMMUNITY",
}

import bpy


NWN2_BODY_PROFILES = {
    "HHM": {
        "label": "Human Male (HHM)",
        "model_token": "HHM",
        "skeleton": "P_HHM_skel",
        "body": "P_HHM_CL_Body01",
        "boots": "P_HHM_CL_Boots01",
        "gloves": "P_HHM_CL_Gloves01",
        "head": "P_HHM_Head01",
        "mannequin": "NWN2_WeightMannequin_HHM",
    },
    "HHF": {
        "label": "Human Female (HHF)",
        "model_token": "HHF",
        "skeleton": "P_HHF_skel",
        "body": "P_HHF_CL_Body01",
        "boots": "P_HHF_CL_Boots01",
        "gloves": "P_HHF_CL_Gloves01",
        "head": "P_HHF_Head01",
        "mannequin": "NWN2_WeightMannequin_HHF",
    },
    "OOM": {
        "label": "Half-Orc Male (OOM)",
        "model_token": "OOM",
        "skeleton": "P_OOM_skel",
        "body": "P_OOM_CL_Body01",
        "boots": "P_OOM_CL_Boots01",
        "gloves": "P_OOM_CL_Gloves01",
        "head": "P_OOM_Head01",
        "mannequin": "NWN2_WeightMannequin_OOM",
    },
    "OOF": {
        "label": "Half-Orc Female (OOF)",
        "model_token": "OOF",
        "skeleton": "P_OOF_skel",
        "body": "P_OOF_CL_Body01",
        "boots": "P_OOF_CL_Boots01",
        "gloves": "P_OOF_CL_Gloves01",
        "head": "P_OOF_Head01",
        "mannequin": "NWN2_WeightMannequin_OOF",
    },
}


NWN2_PROFILE_SHAPE_PRESETS = {
    "OOM": {
        "label": "Half-Orc Male (OOM)",
        "forward_shift": 0.03,
        "pose_bones": {
            "Spine": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (1.45000005, 1.0, 1.44999993),
            },
            "Ribcage": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.99877512, -0.04673043, 0.0, 0.0),
                "scale": (0.99999994, 1.29697502, 1.0),
            },
            "LArm0CollarBone": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (0.99435467, 0.75856066, 0.95631617),
            },
            "RArm1CollarBone": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (0.99435478, 0.75856066, 0.95631623),
            },
            "LArm010": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.97236991, 0.00102492, 0.00292757, 0.23342475),
                "scale": (1.0, 1.0, 1.0),
            },
            "RArm110": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.97236991, 0.00102493, -0.0029276, -0.2334248),
                "scale": (1.0, 1.0, 1.0),
            },
            "LLeg1": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.99965733, 0.00022588, 0.00263573, 0.02604292),
                "scale": (1.18, 1.0, 1.18),
            },
            "RLeg1": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.99965733, 0.00022588, -0.00263573, -0.02604292),
                "scale": (1.18, 1.0, 1.18),
            },
            "LLeg2": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (1.12, 1.0, 1.12),
            },
            "RLeg2": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (1.12, 1.0, 1.12),
            },
            "Neck": {
                "location": (0.0, 0.0, -0.04203466),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (1.0, 1.0, 1.0),
            },
        },
    },
    "OOF": {
        "label": "Half-Orc Female (OOF)",
        "forward_shift": 0.01,
        "tilt_degrees": -0.5,
        "pose_bones": {
            "Spine": {
                "location": (0.0, -0.00007833, -0.00149459),
                "rotation_quaternion": (0.99965733, -0.02617695, 0.0, 0.0),
                "scale": (1.30000007, 1.0, 1.30000019),
            },
            "Ribcage": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.9994185, 0.02733646, 0.0, 0.0),
                "scale": (1.17000008, 1.28565001, 0.93600005),
            },
            "LArm0CollarBone": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (0.99672639, 0.83804935, 0.96948504),
            },
            "RArm1CollarBone": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (0.99672645, 0.83804923, 0.96948504),
            },
            "LArm010": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.96592593, 0.0010159, 0.0032587, 0.25879654),
                "scale": (0.97627008, 0.84939826, 0.99999988),
            },
            "RArm110": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.96592593, 0.00101606, -0.0032587, -0.25879657),
                "scale": (0.97627014, 0.84939831, 1.00000012),
            },
            "LLeg1": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.99965721, 0.00018985, 0.0026357, 0.02604322),
                "scale": (1.22, 1.0, 1.22),
            },
            "RLeg1": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (0.99965721, 0.00018985, -0.00263571, -0.02604321),
                "scale": (1.22, 1.0, 1.22),
            },
            "LLeg2": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (1.14, 1.0, 1.14),
            },
            "RLeg2": {
                "location": (0.0, 0.0, 0.0),
                "rotation_quaternion": (1.0, 0.0, 0.0, 0.0),
                "scale": (1.14, 1.0, 1.14),
            },
        },
    },
}


def nwn2_profile_items(self, context):
    return [(key, profile["label"], "") for key, profile in NWN2_BODY_PROFILES.items()]


NWN2_BODY_PROFILE_ITEMS = tuple(
    (key, profile["label"], "")
    for key, profile in NWN2_BODY_PROFILES.items()
)


def nwn2_profile_key(context=None, obj=None):
    if obj:
        stored = obj.get("nwn2_body_profile")
        if stored in NWN2_BODY_PROFILES:
            return stored

        names = [obj.name]
        if obj.type == 'MESH':
            names.append(obj.data.name)
            names.extend(mat.name for mat in obj.data.materials if mat)
        for name in names:
            for key, profile in NWN2_BODY_PROFILES.items():
                token = profile["model_token"]
                if f"_{token}_" in name or name.startswith(f"P_{token}_"):
                    return key

    scene = getattr(context, "scene", None)
    if scene:
        selected = getattr(scene, "nwn2_body_profile", "HHM")
        if selected in NWN2_BODY_PROFILES:
            return selected
    return "HHM"


def nwn2_profile(context=None, obj=None):
    return NWN2_BODY_PROFILES[nwn2_profile_key(context, obj)]


def nwn2_profile_object(context, role, obj=None):
    return bpy.data.objects.get(nwn2_profile(context, obj).get(role, ""))


def nwn2_profile_asset_names():
    names = set()
    for profile in NWN2_BODY_PROFILES.values():
        for role in ("skeleton", "body", "boots", "gloves", "head", "mannequin"):
            names.add(profile[role])
    return names


def nwn2_temp_profile_asset_names():
    names = set()
    for profile in NWN2_BODY_PROFILES.values():
        for role in ("body", "boots", "gloves", "head", "mannequin"):
            names.add(profile[role])
    return names


def nwn2_canonical_profile_asset_name(name):
    base = nwn2_strip_blender_suffix(name)
    profile_assets = nwn2_profile_asset_names()
    if base in profile_assets:
        return base

    return None


def nwn2_is_profile_asset_name(name):
    if nwn2_canonical_profile_asset_name(name):
        return True
    base = nwn2_strip_blender_suffix(name)
    if "WeightMannequin" in base:
        return True

    return False


def nwn2_object_in_collection_names(obj, collection_names):
    return any(col.name in collection_names for col in obj.users_collection)


def nwn2_strip_blender_suffix(name):
    base = name
    while len(base) > 4 and base[-4] == '.' and base[-3:].isdigit():
        base = base[:-4]
    return base


def nwn2_safe_hide_set(context, obj, hidden):
    try:
        if obj.name in context.view_layer.objects.keys():
            obj.hide_set(hidden)
    except RuntimeError:
        pass


def nwn2_stamp_profile(obj, context=None, profile_key=None):
    if obj:
        obj["nwn2_body_profile"] = profile_key or nwn2_profile_key(context)


def nwn2_set_vanilla_body_visible(context, visible, obj=None):
    scene = getattr(context, "scene", None)
    profile_key = nwn2_profile_key(context, obj)

    for key, profile in NWN2_BODY_PROFILES.items():
        body = bpy.data.objects.get(profile["body"])
        if not body:
            continue
        show = bool(visible and key == profile_key)
        body.hide_viewport = not show
        nwn2_safe_hide_set(context, body, not show)
        body.hide_render = True
        body.show_in_front = False

    if scene and hasattr(scene, "nwn2_show_vanilla_body"):
        scene.nwn2_show_vanilla_body = bool(visible)


def nwn2_set_vanilla_accessories_visible(context, visible, obj=None):
    scene = getattr(context, "scene", None)
    profile_key = nwn2_profile_key(context, obj)

    for key, profile in NWN2_BODY_PROFILES.items():
        show = bool(visible and key == profile_key)
        for role in ("boots", "gloves"):
            part = bpy.data.objects.get(profile[role])
            if not part:
                continue
            part.hide_viewport = not show
            nwn2_safe_hide_set(context, part, not show)
            part.hide_render = True
            part.show_in_front = False

    if scene and hasattr(scene, "nwn2_show_vanilla_accessories"):
        scene.nwn2_show_vanilla_accessories = bool(visible)


NWN2_WORKFLOW_STEP_LABELS = {
    "load_starter": "Load Starter Scene",
    "presetup_import_highpoly": "Import High Poly",
    "presetup_decimate": "Decimate & Create Low Poly",
    "presetup_uv": "UV Unwrap",
    "presetup_lock": "Lock Bake Reference",
    "step1": "Step 1 - Identify AI Mesh",
    "step2": "Step 2 - Prepare to Rig",
    "step3": "Step 3 - Fit Rig to Mesh",
    "step3_done": "Step 3 Done - Auto Weight Mesh",
    "step4": "Step 4 - Restore to NWN2 Scale",
    "step5": "Step 5 - Final Fitting",
    "step5_done": "Step 5 Done - Attach to Game Skeleton",
    "step6_build": "Step 6 - Build Material Name",
    "step6_setup": "Step 6 - Setup Material",
    "step7_bake": "Step 7 - Bake Maps",
    "substance_handoff": "Export Substance Handoff",
    "step8_cleanup": "Step 8 - Clean Up & Send to Repository",
    "step8_send_export": "Send Repository Outfit to Export",
    "step8_export": "Export .mdb",
    "done": "Workflow Complete",
}


def nwn2_set_workflow_next_step(context, step_id):
    scene = getattr(context, "scene", None)
    if not scene:
        return
    if hasattr(scene, "nwn2_workflow_next_step"):
        scene.nwn2_workflow_next_step = step_id
    else:
        scene["nwn2_workflow_next_step"] = step_id


def nwn2_infer_workflow_next_step(context):
    scene = getattr(context, "scene", None)

    if not nwn2_profile_object(context, "skeleton"):
        return "load_starter"

    if scene and getattr(scene, "nwn2_step3_active", False):
        return "step3_done"
    if scene and getattr(scene, "nwn2_step5_active", False):
        return "step5_done"

    export_col = bpy.data.collections.get("NWN2_Export")
    if export_col and any(obj.type == 'MESH' for obj in export_col.objects):
        return "step8_export"

    repo_col = bpy.data.collections.get("NWN2_Repository")
    if repo_col and any(obj.type == 'MESH' for obj in repo_col.objects):
        return "step8_send_export"

    mesh_obj = bpy.data.objects.get("newModel_Mesh")
    if not mesh_obj:
        return "step1"

    ai_rig = bpy.data.objects.get("Ai_Rig")
    if not ai_rig:
        return "step2"

    if not mesh_obj.vertex_groups:
        return "step3"

    return "step4"


def nwn2_workflow_next_step(context):
    scene = getattr(context, "scene", None)
    if scene:
        stored = getattr(scene, "nwn2_workflow_next_step", "")
        if not stored and hasattr(scene, "get"):
            stored = scene.get("nwn2_workflow_next_step", "")
        if stored:
            return stored
    return nwn2_infer_workflow_next_step(context)


def nwn2_is_workflow_next(context, *step_ids):
    return nwn2_workflow_next_step(context) in step_ids


# ---------------------------------------------------------------------------
# STEP 1 — Identify AI Mesh
# ---------------------------------------------------------------------------

class NWN2_OT_Step1_IdentifyMesh(bpy.types.Operator):
    """Scan the scene for the AI outfit mesh outside of NWN2 starter assets"""
    bl_idname = "nwn2.step1_identify_mesh"
    bl_label = "Step 1: Identify AI Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def get_cols_hierarchy(self):
        cols_names = set()
        cols_root = bpy.data.objects.get("COLS")
        if cols_root:
            cols_names.add(cols_root.name)
            changed = True
            while changed:
                changed = False
                for obj in bpy.data.objects:
                    if obj.name not in cols_names and obj.parent and obj.parent.name in cols_names:
                        cols_names.add(obj.name)
                        changed = True
        return cols_names

    def get_profile_skel_hierarchy(self):
        skel_names = set()
        roots = [
            bpy.data.objects.get(profile["skeleton"])
            for profile in NWN2_BODY_PROFILES.values()
        ]
        for root in [obj for obj in roots if obj]:
            skel_names.add(root.name)
            changed = True
            while changed:
                changed = False
                for obj in bpy.data.objects:
                    if obj.name not in skel_names and obj.parent and obj.parent.name in skel_names:
                        skel_names.add(obj.name)
                        changed = True
        return skel_names

    def align_mesh_to_rig(self, mesh_obj):
        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        bpy.context.view_layer.objects.active = mesh_obj
        mesh_obj.rotation_euler.z = 0.0
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    def execute(self, context):
        cols_hierarchy = self.get_cols_hierarchy()
        profile_hierarchy = self.get_profile_skel_hierarchy()

        outside_meshes = [
            obj for obj in bpy.data.objects
            if obj.type == 'MESH'
            and obj.name not in cols_hierarchy
            and obj.name not in profile_hierarchy
            and not nwn2_object_in_collection_names(obj, {"NWN2_Repository", "NWN2_Export"})
            and not nwn2_is_profile_asset_name(obj.name)
            and obj.name != "HighPoly_Mesh"
            and obj.name != "LowPoly_Mesh"
        ]

        if len(outside_meshes) == 0:
            self.report({'ERROR'}, "No AI mesh found outside starter skeletons and COLS.")
            return {'CANCELLED'}

        if len(outside_meshes) > 1:
            names = ", ".join([o.name for o in outside_meshes])
            self.report({'ERROR'}, f"More than one mesh detected: {names}")
            return {'CANCELLED'}

        ai_mesh = outside_meshes[0]
        old_name = ai_mesh.name

        if ai_mesh.name != "newModel_Mesh":
            ai_mesh.name = "newModel_Mesh"
        nwn2_stamp_profile(ai_mesh, context)

        hp_obj = bpy.data.objects.get("HighPoly_Mesh")
        if hp_obj:
            hp_obj.hide_viewport = True
            hp_obj.hide_render = False

        self.align_mesh_to_rig(ai_mesh)

        context.scene.nwn2_mesh_rotation_steps = 0
        context.scene.nwn2_mesh_front_direction = "+Y"

        nwn2_set_workflow_next_step(context, "step2")
        hp_msg = " HighPoly_Mesh hidden." if hp_obj else ""
        self.report({'INFO'}, f"✓ '{old_name}' verified as newModel_Mesh, aligned to +Y.{hp_msg}")
        return {'FINISHED'}


class NWN2_OT_RotateMeshAround(bpy.types.Operator):
    """Rotate newModel_Mesh 90° on Z. Also rotates HighPoly_Mesh and LowPoly_Mesh in sync."""
    bl_idname = "nwn2.rotate_mesh_around"
    bl_label = "Rotate Mesh Around"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import math
        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found. Run Step 1 first.")
            return {'CANCELLED'}

        # Rotate newModel_Mesh
        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        bpy.context.view_layer.objects.active = mesh_obj
        mesh_obj.rotation_euler.z += math.radians(90)
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        # Rotate HighPoly_Mesh and LowPoly_Mesh in sync
        for ref_name in ["HighPoly_Mesh", "LowPoly_Mesh"]:
            ref_obj = bpy.data.objects.get(ref_name)
            if ref_obj:
                was_hidden = ref_obj.hide_viewport
                ref_obj.hide_viewport = False
                bpy.ops.object.select_all(action='DESELECT')
                ref_obj.select_set(True)
                bpy.context.view_layer.objects.active = ref_obj
                ref_obj.rotation_euler.z += math.radians(90)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                ref_obj.hide_viewport = was_hidden

        # Restore newModel_Mesh selection
        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        bpy.context.view_layer.objects.active = mesh_obj

        scene = context.scene
        scene.nwn2_mesh_rotation_steps = (scene.nwn2_mesh_rotation_steps + 1) % 4
        directions = ["+Y", "-X", "-Y", "+X"]
        scene.nwn2_mesh_front_direction = directions[scene.nwn2_mesh_rotation_steps]

        self.report({'INFO'}, f"Rotated 90° — MeshFrontDirection: {scene.nwn2_mesh_front_direction}")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 2 — Prepare to Rig
# ---------------------------------------------------------------------------

class NWN2_OT_Step2_PrepareToRig(bpy.types.Operator):
    """Set viewport to Back Orthographic, duplicate active profile skeleton to Ai_Rig"""
    bl_idname = "nwn2.step2_prepare_to_rig"
    bl_label = "Prepare to Rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.mode != 'OBJECT':
            try:
                bpy.ops.object.mode_set(mode='OBJECT')
            except Exception:
                pass

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        space = area.spaces.active
                        with context.temp_override(area=area, region=region, space_data=space):
                            bpy.ops.view3d.view_axis(type='BACK', align_active=False)
                            space.region_3d.view_perspective = 'ORTHO'
                            bpy.ops.object.select_all(action='SELECT')
                            bpy.ops.view3d.view_selected(use_all_regions=False)
                            bpy.ops.object.select_all(action='DESELECT')

        profile_key = nwn2_profile_key(context)
        profile = nwn2_profile(context)
        source_skel = nwn2_profile_object(context, "skeleton")
        if not source_skel:
            self.report({'ERROR'}, f"{profile['skeleton']} not found in scene.")
            return {'CANCELLED'}

        existing_rig = bpy.data.objects.get("Ai_Rig")
        if existing_rig and existing_rig.get("nwn2_body_profile") != profile_key:
            bpy.data.objects.remove(existing_rig, do_unlink=True)
            existing_rig = None

        if existing_rig:
            ai_rig = existing_rig
        else:
            bpy.ops.object.select_all(action='DESELECT')
            source_skel.hide_viewport = False
            source_skel.hide_set(False)
            source_skel.select_set(True)
            context.view_layer.objects.active = source_skel
            bpy.ops.object.duplicate(linked=False)

            ai_rig = context.active_object
            ai_rig.name = "Ai_Rig"
            ai_rig.data.name = "Ai_Rig_data"
            nwn2_stamp_profile(ai_rig, context, profile_key)
            ai_rig["nwn2_source_skeleton"] = profile["skeleton"]

            BONES_TO_KEEP = {
                profile["skeleton"],
                "LLeg1", "LLeg2", "RLeg1", "RLeg2", "Spine", "Ribcage",
                "LArm0CollarBone", "LArm010", "LArm011", "LArm02", "LArm0Palm",
                "RArm1CollarBone", "RArm110", "RArm111", "RArm12", "RArm1Palm",
                "Neck", "RLegAnkle", "LLegAnkle", "RLegAnkleDigit011", "LLegAnkleDigit011",
            }

            bpy.ops.object.select_all(action='DESELECT')
            ai_rig.select_set(True)
            context.view_layer.objects.active = ai_rig
            bpy.ops.object.mode_set(mode='EDIT')

            for bone in [b for b in ai_rig.data.edit_bones if b.name not in BONES_TO_KEEP]:
                ai_rig.data.edit_bones.remove(bone)

            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.mode_set(mode='EDIT')

            larm02 = ai_rig.data.edit_bones.get("LArm02")
            rarm12 = ai_rig.data.edit_bones.get("RArm12")
            if larm02 and rarm12:
                direction = (larm02.tail - larm02.head).normalized()
                larm02.tail = larm02.head + direction * rarm12.length

            bpy.ops.object.mode_set(mode='OBJECT')

        ARM_BONES  = {"RArm110", "LArm010"}
        LEG_BONES  = {"RLeg1", "LLeg1"}
        FOOT_BONES = {"RLegAnkle", "LLegAnkle"}

        for pbone in ai_rig.pose.bones:
            if pbone.name in ARM_BONES:
                pbone.color.palette = 'CUSTOM'
                pbone.color.custom.normal = (1.0, 0.1, 0.1)
                pbone.color.custom.select = (1.0, 0.5, 0.5)
                pbone.color.custom.active = (1.0, 0.8, 0.8)
            elif pbone.name in LEG_BONES:
                pbone.color.palette = 'CUSTOM'
                pbone.color.custom.normal = (1.0, 0.9, 0.0)
                pbone.color.custom.select = (1.0, 1.0, 0.5)
                pbone.color.custom.active = (1.0, 1.0, 0.8)
            elif pbone.name in FOOT_BONES:
                pbone.color.palette = 'CUSTOM'
                pbone.color.custom.normal = (0.1, 0.4, 1.0)
                pbone.color.custom.select = (0.5, 0.7, 1.0)
                pbone.color.custom.active = (0.8, 0.9, 1.0)

        bpy.ops.object.select_all(action='DESELECT')
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig
        bpy.ops.object.mode_set(mode='POSE')

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.overlay.show_bones = True
                area.tag_redraw()

        source_skel_name = profile["skeleton"]

        def return_to_object_mode():
            obj = bpy.context.view_layer.objects.active
            if obj and obj.mode == 'POSE':
                bpy.ops.object.mode_set(mode='OBJECT')
            source = bpy.data.objects.get(source_skel_name)
            if source:
                source.hide_viewport = True
            return None

        bpy.app.timers.register(return_to_object_mode, first_interval=2.0)

        import json
        snapshot = {
            "scale": list(ai_rig.scale),
            "location": list(ai_rig.location),
            "bones": {}
        }
        for bone in ai_rig.data.bones:
            snapshot["bones"][bone.name] = {
                "head": list(bone.head_local),
                "tail": list(bone.tail_local),
                "length": bone.length,
            }

        context.scene.nwn2_ai_rig_snapshot = json.dumps(snapshot)
        nwn2_set_workflow_next_step(context, "step3")
        self.report({'INFO'}, f"Ai_Rig created from {profile['label']}, bones colored, snapshot saved.")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 3 — Fit Rig to Mesh
# ---------------------------------------------------------------------------

class NWN2_OT_Step3_FitRigInstructions(bpy.types.Operator):
    """Scale Ai_Rig to mesh then show fitting instructions"""
    bl_idname = "nwn2.step3_fit_rig_instructions"
    bl_label = "Step 3: Fit Rig to Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import mathutils

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig   = bpy.data.objects.get("Ai_Rig")

        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Force OBJECT mode regardless of what mode the user left Blender in
        if context.mode != 'OBJECT':
            win = context.window
            scr = win.screen
            area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
            region = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None
            if area_3d and region:
                with context.temp_override(window=win, screen=scr, area=area_3d, region=region):
                    bpy.ops.object.mode_set(mode='OBJECT')

        def get_bbox_z(obj):
            corners = [obj.matrix_world @ mathutils.Vector(c) for c in obj.bound_box]
            return min(c.z for c in corners), max(c.z for c in corners)

        mesh_z_min, mesh_z_max = get_bbox_z(mesh_obj)
        rig_z_min,  rig_z_max  = get_bbox_z(ai_rig)
        mesh_height = mesh_z_max - mesh_z_min
        rig_height  = rig_z_max  - rig_z_min

        scale_factor = 1.0
        if rig_height > 0.001:
            scale_factor = mesh_height / rig_height

            for obj in context.view_layer.objects:
                obj.select_set(False)
            ai_rig.select_set(True)
            context.view_layer.objects.active = ai_rig
            ai_rig.scale = (scale_factor, scale_factor, scale_factor)

            def get_bbox_info(obj):
                corners = [obj.matrix_world @ mathutils.Vector(c) for c in obj.bound_box]
                return {
                    "x_min": min(c.x for c in corners), "x_max": max(c.x for c in corners),
                    "y_min": min(c.y for c in corners), "y_max": max(c.y for c in corners),
                    "z_min": min(c.z for c in corners), "z_max": max(c.z for c in corners),
                }

            mesh_bb = get_bbox_info(mesh_obj)
            rig_bb  = get_bbox_info(ai_rig)

            mesh_cx = (mesh_bb["x_min"] + mesh_bb["x_max"]) / 2
            rig_cx  = (rig_bb["x_min"]  + rig_bb["x_max"])  / 2
            mesh_cy = (mesh_bb["y_min"] + mesh_bb["y_max"]) / 2
            rig_cy  = (rig_bb["y_min"]  + rig_bb["y_max"])  / 2

            ai_rig.location.x += mesh_cx - rig_cx
            ai_rig.location.y += mesh_cy - rig_cy
            ai_rig.location.z += mesh_bb["z_min"] - rig_bb["z_min"]

            context.view_layer.update()

            mat = ai_rig.matrix_world
            lowest_z = None
            for bname in ["LLegAnkleDigit011", "RLegAnkleDigit011"]:
                bone = ai_rig.data.bones.get(bname)
                if bone:
                    bone_min = min((mat @ bone.head_local).z, (mat @ bone.tail_local).z)
                    if lowest_z is None or bone_min < lowest_z:
                        lowest_z = bone_min
            if lowest_z is not None and abs(lowest_z) > 0.0001:
                ai_rig.location.z -= lowest_z

        context.scene.tool_settings.transform_pivot_point = 'INDIVIDUAL_ORIGINS'
        ai_rig.show_in_front = True
        context.scene.nwn2_step3_active = True
        nwn2_set_workflow_next_step(context, "step3_done")

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'UI':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.wm.context_set_boolean(
                                data_path="space_data.show_region_ui", value=True
                            )
                        break

        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None
        if area_3d and region:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region):
                bpy.ops.object.mode_set(mode='POSE')
        else:
            bpy.ops.object.mode_set(mode='POSE')

        self.report({'INFO'}, f"Ai_Rig scaled by {scale_factor:.4f}. Adjust bones then click Done.")
        return {'FINISHED'}


class NWN2_OT_Step3_Done(bpy.types.Operator):
    """Auto-weight newModel_Mesh to Ai_Rig"""
    bl_idname = "nwn2.step3_done"
    bl_label = "Done — Auto Weight Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def clear_vertex_groups(self, mesh_obj):
        for vg in list(mesh_obj.vertex_groups):
            mesh_obj.vertex_groups.remove(vg)

    def get_weight_stats(self, mesh_obj):
        unweighted = []
        nonzero_groups = set()

        for vert in mesh_obj.data.vertices:
            total = 0.0
            for g in vert.groups:
                if g.weight > 0.000001:
                    total += g.weight
                    nonzero_groups.add(g.group)
            if total <= 0.000001:
                unweighted.append(vert.index)

        total_vertices = len(mesh_obj.data.vertices)
        return {
            "total_vertices": total_vertices,
            "weighted_count": total_vertices - len(unweighted),
            "unweighted_count": len(unweighted),
            "unweighted_indices": unweighted,
            "nonzero_group_count": len(nonzero_groups),
        }

    def ensure_armature_binding(self, mesh_obj, arm_obj):
        world = mesh_obj.matrix_world.copy()
        mesh_obj.parent = arm_obj
        mesh_obj.matrix_world = world

        arm_mod = None
        for mod in list(mesh_obj.modifiers):
            if mod.type == 'ARMATURE':
                if mod.object == arm_obj:
                    arm_mod = mod
                else:
                    mesh_obj.modifiers.remove(mod)

        if not arm_mod:
            arm_mod = mesh_obj.modifiers.new(name="Armature", type='ARMATURE')
            arm_mod.object = arm_obj
            arm_mod.use_vertex_groups = True

    def normalize_vertex_weights(self, mesh_obj):
        for vert in mesh_obj.data.vertices:
            active = []
            for g in vert.groups:
                if g.weight > 0.000001 and g.group < len(mesh_obj.vertex_groups):
                    active.append((mesh_obj.vertex_groups[g.group], g.weight))

            total = sum(weight for _, weight in active)
            if total <= 0.000001:
                continue

            for group, weight in active:
                group.add([vert.index], weight / total, 'REPLACE')

    def get_weight_donor_sources(self, context, arm_obj=None):
        profile = nwn2_profile(context, arm_obj)
        custom_names = [
            profile["mannequin"],
            "WeightTransfer_Mannequin",
            "Fallback_Mannequin",
            "NWN2_Fallback_Mannequin",
        ]
        for name in custom_names:
            obj = bpy.data.objects.get(name)
            if obj and obj.type == 'MESH' and obj.vertex_groups:
                return [obj]

        donor_names = [profile["body"], profile["boots"], profile["gloves"]]
        return [
            obj for obj in (bpy.data.objects.get(name) for name in donor_names)
            if obj and obj.type == 'MESH' and obj.vertex_groups
        ]

    def build_fitted_weight_donor(self, context, arm_obj):
        sources = self.get_weight_donor_sources(context, arm_obj)
        if not sources:
            return None

        bone_names = {bone.name for bone in arm_obj.data.bones}
        pieces = []

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        for src in sources:
            donor_obj = src.copy()
            donor_obj.data = src.data.copy()
            donor_obj.name = "__nwn2_weight_donor_" + src.name
            donor_obj.data.name = "__nwn2_weight_donor_data_" + src.name
            donor_obj.animation_data_clear()
            context.scene.collection.objects.link(donor_obj)

            donor_obj.hide_viewport = False
            donor_obj.hide_set(False)
            donor_obj.hide_render = True
            donor_obj.parent = None
            donor_obj.matrix_world = arm_obj.matrix_world.copy()

            for mod in list(donor_obj.modifiers):
                donor_obj.modifiers.remove(mod)

            for vg in list(donor_obj.vertex_groups):
                if vg.name not in bone_names:
                    donor_obj.vertex_groups.remove(vg)

            if not donor_obj.vertex_groups:
                bpy.data.objects.remove(donor_obj, do_unlink=True)
                continue

            arm_mod = donor_obj.modifiers.new(name="__nwn2_fit_to_ai_rig__", type='ARMATURE')
            arm_mod.object = arm_obj
            arm_mod.use_vertex_groups = True

            bpy.ops.object.select_all(action='DESELECT')
            donor_obj.select_set(True)
            context.view_layer.objects.active = donor_obj
            bpy.ops.object.modifier_apply(modifier=arm_mod.name)
            pieces.append(donor_obj)

        if not pieces:
            return None

        bpy.ops.object.select_all(action='DESELECT')
        for piece in pieces:
            piece.select_set(True)
        context.view_layer.objects.active = pieces[0]
        if len(pieces) > 1:
            bpy.ops.object.join()

        donor = context.view_layer.objects.active
        donor.name = "__nwn2_weight_transfer_donor__"
        donor.data.name = "__nwn2_weight_transfer_donor_data__"
        donor.hide_viewport = True
        donor.hide_render = True
        return donor

    def transfer_weights_from_donor(self, mesh_obj, donor_obj, arm_obj):
        if not donor_obj:
            return False

        bone_names = {bone.name for bone in arm_obj.data.bones}
        self.clear_vertex_groups(mesh_obj)
        for bone in arm_obj.data.bones:
            mesh_obj.vertex_groups.new(name=bone.name)

        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.hide_viewport = False
        mesh_obj.hide_set(False)
        donor_obj.hide_viewport = False
        donor_obj.hide_set(False)
        mesh_obj.select_set(True)
        context = bpy.context
        context.view_layer.objects.active = mesh_obj

        mod = mesh_obj.modifiers.new(name="__nwn2_weight_transfer__", type='DATA_TRANSFER')
        mod.object = donor_obj
        mod.use_vert_data = True
        mod.data_types_verts = {'VGROUP_WEIGHTS'}
        mod.vert_mapping = 'POLYINTERP_NEAREST'
        mod.layers_vgroup_select_src = 'ALL'
        mod.layers_vgroup_select_dst = 'NAME'
        mod.mix_mode = 'REPLACE'
        mod.mix_factor = 1.0

        try:
            bpy.ops.object.modifier_apply(modifier=mod.name)
        except Exception:
            if mod.name in mesh_obj.modifiers:
                mesh_obj.modifiers.remove(mod)
            return False

        for vg in list(mesh_obj.vertex_groups):
            if vg.name not in bone_names:
                mesh_obj.vertex_groups.remove(vg)

        return True

    def copy_donor_weights_to_vertices(self, mesh_obj, donor_obj, arm_obj, vertex_indices):
        if not donor_obj or not vertex_indices:
            return False

        bone_names = {bone.name for bone in arm_obj.data.bones}
        target_groups = {}
        for bone_name in bone_names:
            target_groups[bone_name] = (
                mesh_obj.vertex_groups.get(bone_name) or
                mesh_obj.vertex_groups.new(name=bone_name)
            )

        donor_group_names = {vg.index: vg.name for vg in donor_obj.vertex_groups}
        donor_rows = []
        for vert in donor_obj.data.vertices:
            weights = []
            for g in vert.groups:
                name = donor_group_names.get(g.group)
                if name in target_groups and g.weight > 0.000001:
                    weights.append((name, g.weight))
            if weights:
                donor_rows.append((donor_obj.matrix_world @ vert.co, weights))

        if not donor_rows:
            return False

        for vi in vertex_indices:
            world_co = mesh_obj.matrix_world @ mesh_obj.data.vertices[vi].co
            best_weights = None
            best_dist_sq = None
            for donor_co, weights in donor_rows:
                dist_sq = (world_co - donor_co).length_squared
                if best_dist_sq is None or dist_sq < best_dist_sq:
                    best_dist_sq = dist_sq
                    best_weights = weights

            if not best_weights:
                continue

            total = sum(weight for _, weight in best_weights)
            if total <= 0.000001:
                continue

            for name, weight in best_weights:
                target_groups[name].add([vi], weight / total, 'REPLACE')

        return True

    def remove_temp_weight_donor(self, donor_obj):
        if donor_obj and donor_obj.name in bpy.data.objects:
            bpy.data.objects.remove(donor_obj, do_unlink=True)

    def execute(self, context):
        import json
        context.scene.nwn2_step3_active = False

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig   = bpy.data.objects.get("Ai_Rig")

        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}
        nwn2_stamp_profile(mesh_obj, context, ai_rig.get("nwn2_body_profile") or nwn2_profile_key(context))

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        pose_snapshot = {}
        for pbone in ai_rig.pose.bones:
            pose_snapshot[pbone.name] = {
                "location":            list(pbone.location),
                "rotation_quaternion": list(pbone.rotation_quaternion),
                "rotation_euler":      list(pbone.rotation_euler),
                "scale":               list(pbone.scale),
                "rotation_mode":       pbone.rotation_mode,
            }
        context.scene.nwn2_pose_snapshot = json.dumps(pose_snapshot)

        fitted_donor = self.build_fitted_weight_donor(context, ai_rig)

        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.pose.armature_apply(selected=False)
        bpy.ops.object.mode_set(mode='OBJECT')

        self.clear_vertex_groups(mesh_obj)

        for obj in context.view_layer.objects:
            obj.select_set(False)
        mesh_obj.select_set(True)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')
        self.ensure_armature_binding(mesh_obj, ai_rig)

        weight_method = "Blender heat weights"
        stats = self.get_weight_stats(mesh_obj)

        # Blender may return FINISHED after a bone-heat failure while leaving the
        # mesh with empty vertex groups. Detect that and fall back to a fitted
        # weighted mannequin/reference donor so Step 4/5 never continue unskinned.
        if (
            stats["total_vertices"] > 0 and
            (
                stats["nonzero_group_count"] == 0 or
                stats["unweighted_count"] > stats["total_vertices"] * 0.25
            )
        ):
            if fitted_donor and self.transfer_weights_from_donor(mesh_obj, fitted_donor, ai_rig):
                self.ensure_armature_binding(mesh_obj, ai_rig)
                weight_method = "weighted mannequin transfer fallback"
                stats = self.get_weight_stats(mesh_obj)
            else:
                self.remove_temp_weight_donor(fitted_donor)
                self.report(
                    {'ERROR'},
                    "Blender heat weights failed and no weighted mannequin/reference donor was available."
                )
                return {'CANCELLED'}
        elif stats["unweighted_count"] > 0:
            if fitted_donor and self.copy_donor_weights_to_vertices(
                mesh_obj, fitted_donor, ai_rig, stats["unweighted_indices"]
            ):
                weight_method = "Blender heat weights + mannequin fill"
            stats = self.get_weight_stats(mesh_obj)

        # --- Post-weight cleanup: remove cross-contamination ---
        # LArm02 and LLeg1 should never share influence on the same vertex
        # RArm12 and RLeg1 should never share influence on the same vertex
        CONFLICT_PAIRS = [
            ("LArm02", "LLeg1"),
            ("RArm12", "RLeg1"),
        ]

        for arm_name, leg_name in CONFLICT_PAIRS:
            arm_vg = mesh_obj.vertex_groups.get(arm_name)
            leg_vg = mesh_obj.vertex_groups.get(leg_name)
            if not arm_vg or not leg_vg:
                continue

            # Build sets of vertices with non-zero weight in each group
            arm_verts = set()
            leg_verts = set()

            for vert in mesh_obj.data.vertices:
                for g in vert.groups:
                    if g.group == arm_vg.index and g.weight > 0:
                        arm_verts.add(vert.index)
                    if g.group == leg_vg.index and g.weight > 0:
                        leg_verts.add(vert.index)

            # Vertices shared by both — remove the lighter influence
            shared = arm_verts & leg_verts
            for vi in shared:
                vert = mesh_obj.data.vertices[vi]
                arm_w = next((g.weight for g in vert.groups if g.group == arm_vg.index), 0)
                leg_w = next((g.weight for g in vert.groups if g.group == leg_vg.index), 0)
                # Remove whichever bone has less influence on this vertex
                if arm_w <= leg_w:
                    try:
                        arm_vg.remove([vi])
                    except:
                        pass
                else:
                    try:
                        leg_vg.remove([vi])
                    except:
                        pass

        self.normalize_vertex_weights(mesh_obj)
        stats = self.get_weight_stats(mesh_obj)
        if stats["unweighted_count"] > 0:
            if fitted_donor:
                self.copy_donor_weights_to_vertices(
                    mesh_obj, fitted_donor, ai_rig, stats["unweighted_indices"]
                )
            self.normalize_vertex_weights(mesh_obj)
            stats = self.get_weight_stats(mesh_obj)

        mesh_obj.data.update()
        self.remove_temp_weight_donor(fitted_donor)

        if stats["unweighted_count"] > 0 or stats["nonzero_group_count"] == 0:
            self.report(
                {'ERROR'},
                f"Auto-weight failed: {stats['unweighted_count']} vertices remain unweighted."
            )
            return {'CANCELLED'}

        self.report(
            {'INFO'},
            f"Mesh weighted using {weight_method}: {stats['weighted_count']}/{stats['total_vertices']} vertices, "
            f"{stats['nonzero_group_count']} active groups."
        )
        nwn2_set_workflow_next_step(context, "step4")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 4
# ---------------------------------------------------------------------------

class NWN2_OT_Step4_Finalize(bpy.types.Operator):
    """Scale Ai_Rig back to NWN2 size"""
    bl_idname = "nwn2.step4_finalize"
    bl_label = "Step 4: Restore to NWN2 Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import json, mathutils

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig   = bpy.data.objects.get("Ai_Rig")

        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}
        if not mesh_obj.vertex_groups:
            self.report({'ERROR'}, "No vertex groups. Run Step 3 Done first.")
            return {'CANCELLED'}

        snapshot_str = context.scene.nwn2_ai_rig_snapshot
        if not snapshot_str:
            self.report({'ERROR'}, "No snapshot found.")
            return {'CANCELLED'}

        snapshot = json.loads(snapshot_str)
        orig_location = snapshot["location"]

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        if mesh_obj.parent != ai_rig:
            bpy.ops.object.select_all(action='DESELECT')
            mesh_obj.select_set(True)
            ai_rig.select_set(True)
            context.view_layer.objects.active = ai_rig
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        has_mod = any(m.type == 'ARMATURE' and m.object == ai_rig for m in mesh_obj.modifiers)
        if not has_mod:
            for mod in list(mesh_obj.modifiers):
                if mod.type == 'ARMATURE':
                    mesh_obj.modifiers.remove(mod)
            arm_mod = mesh_obj.modifiers.new(name="Armature", type='ARMATURE')
            arm_mod.object = ai_rig
            arm_mod.use_vertex_groups = True

        bpy.ops.object.select_all(action='DESELECT')
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig
        ai_rig.scale = (1.0, 1.0, 1.0)
        ai_rig.location = mathutils.Vector(orig_location)

        context.view_layer.update()
        mat = ai_rig.matrix_world
        lowest_z = None
        for bname in ["LLegAnkleDigit011", "RLegAnkleDigit011"]:
            bone = ai_rig.data.bones.get(bname)
            if bone:
                bone_min = min((mat @ bone.head_local).z, (mat @ bone.tail_local).z)
                if lowest_z is None or bone_min < lowest_z:
                    lowest_z = bone_min
        if lowest_z is not None and abs(lowest_z) > 0.0001:
            ai_rig.location.z -= lowest_z

        pose_snapshot_str = context.scene.nwn2_pose_snapshot
        if pose_snapshot_str:
            pose_snapshot = json.loads(pose_snapshot_str)
            ADJUSTMENT_BONES = {
                "RArm110", "LArm010", "RArm111", "LArm011",
                "RArm12", "LArm02", "RArm1Palm", "LArm0Palm",
                "RLeg1", "LLeg1", "RLeg2", "LLeg2", "RLegAnkle", "LLegAnkle",
            }

            bpy.ops.object.select_all(action='DESELECT')
            ai_rig.select_set(True)
            context.view_layer.objects.active = ai_rig
            bpy.ops.object.mode_set(mode='POSE')

            for pbone in ai_rig.pose.bones:
                if pbone.name not in ADJUSTMENT_BONES or pbone.name not in pose_snapshot:
                    continue
                snap = pose_snapshot[pbone.name]
                pbone.rotation_mode = snap["rotation_mode"]
                loc = snap["location"]
                pbone.location = (-loc[0], -loc[1], -loc[2])
                if snap["rotation_mode"] == 'QUATERNION':
                    import mathutils as mu
                    q = snap["rotation_quaternion"]
                    pbone.rotation_quaternion = mu.Quaternion((q[0], q[1], q[2], q[3])).inverted()
                else:
                    r = snap["rotation_euler"]
                    pbone.rotation_euler = (-r[0], -r[1], -r[2])
                s = snap["scale"]
                pbone.scale = (
                    1.0 / s[0] if s[0] != 0 else 1.0,
                    1.0 / s[1] if s[1] != 0 else 1.0,
                    1.0 / s[2] if s[2] != 0 else 1.0,
                )

            bpy.ops.object.mode_set(mode='OBJECT')

        for profile in NWN2_BODY_PROFILES.values():
            skel = bpy.data.objects.get(profile["skeleton"])
            if skel:
                skel.hide_viewport = True
                skel.hide_set(True)
            ref = bpy.data.objects.get(profile["body"])
            if ref:
                ref.hide_viewport = True
                ref.hide_set(True)

        target_skel = nwn2_profile_object(context, "skeleton", mesh_obj)
        if target_skel:
            target_skel.hide_viewport = False
            target_skel.hide_set(False)

        # Show reference body so user has a live scale comparison
        ref_body = nwn2_profile_object(context, "body", mesh_obj)
        if ref_body:
            ref_body.hide_viewport = False
            ref_body.hide_set(False)

        context.scene.nwn2_scale_adjustment = 1.0
        context.scene.nwn2_shift_adjustment = 0.0
        context.scene.nwn2_vertical_shift_adjustment = 0.0
        mesh_obj["nwn2_scale_adjust_base"] = tuple(mesh_obj.scale)
        ai_rig["nwn2_scale_adjust_base"] = tuple(ai_rig.scale)

        nwn2_set_workflow_next_step(context, "step5")
        self.report({'INFO'}, f"Ai_Rig restored to {nwn2_profile(context, mesh_obj)['label']} scale. Reference body visible for comparison.")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 4B — Scale Adjustment
# ---------------------------------------------------------------------------

class NWN2_OT_Step4_TiltAdjust(bpy.types.Operator):
    """Tilt mesh forward or backward in 0.5 degree increments"""
    bl_idname = "nwn2.step4_tilt_adjust"
    bl_label = "Tilt Adjust"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.IntProperty(default=1)

    def execute(self, context):
        import math
        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}
        angle = math.radians(0.25 * self.direction)
        mesh_obj.rotation_euler.x += angle
        if ai_rig:
            ai_rig.rotation_euler.x += angle
        context.scene.nwn2_tilt_adjustment = round(
            context.scene.nwn2_tilt_adjustment + (0.25 * self.direction), 2
        )
        self.report({'INFO'}, f"Tilt: {context.scene.nwn2_tilt_adjustment:.1f}°")
        return {'FINISHED'}


class NWN2_OT_Step4_ScaleAdjust(bpy.types.Operator):
    """Increase or decrease rig display scale in small increments"""
    bl_idname = "nwn2.step4_scale_adjust"
    bl_label = "Scale Adjust"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.IntProperty(default=1)  # +1 or -1

    def execute(self, context):
        import mathutils

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig = bpy.data.objects.get("Ai_Rig")

        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        if "nwn2_scale_adjust_base" not in mesh_obj:
            mesh_obj["nwn2_scale_adjust_base"] = tuple(mesh_obj.scale)
        if "nwn2_scale_adjust_base" not in ai_rig:
            ai_rig["nwn2_scale_adjust_base"] = tuple(ai_rig.scale)

        context.scene.nwn2_scale_adjustment = round(
            context.scene.nwn2_scale_adjustment + (0.005 * self.direction), 3
        )
        scale_factor = context.scene.nwn2_scale_adjustment

        mesh_base = mathutils.Vector(mesh_obj["nwn2_scale_adjust_base"])
        rig_base = mathutils.Vector(ai_rig["nwn2_scale_adjust_base"])

        # newModel_Mesh is parented to Ai_Rig after Step 4. Scaling both creates
        # double transforms, so keep the child mesh at its base scale and let the
        # rig carry this fine adjustment.
        mesh_obj.scale = tuple(mesh_base)
        ai_rig.scale = tuple(component * scale_factor for component in rig_base)

        self.report({'INFO'}, f"Scale: {scale_factor:.3f}")
        return {'FINISHED'}


class NWN2_OT_Step4_ShiftAdjust(bpy.types.Operator):
    """Shift the fitted rig forward/backward in small increments"""
    bl_idname = "nwn2.step4_shift_adjust"
    bl_label = "Shift Adjust"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.IntProperty(default=1)  # +1 forward, -1 backward

    def execute(self, context):
        import mathutils

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig = bpy.data.objects.get("Ai_Rig")

        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        step = 0.01 * self.direction
        offset = mathutils.Vector((0.0, step, 0.0))
        ai_rig.location += offset
        if mesh_obj and mesh_obj.parent != ai_rig:
            mesh_obj.location += offset

        context.scene.nwn2_shift_adjustment = round(
            context.scene.nwn2_shift_adjustment + step, 3
        )
        self.report({'INFO'}, f"Forward shift: {context.scene.nwn2_shift_adjustment:.3f}")
        return {'FINISHED'}


class NWN2_OT_Step4_VerticalShiftAdjust(bpy.types.Operator):
    """Shift the fitted rig up/down in small increments"""
    bl_idname = "nwn2.step4_vertical_shift_adjust"
    bl_label = "Vertical Shift Adjust"
    bl_options = {'REGISTER', 'UNDO'}

    direction: bpy.props.IntProperty(default=1)  # +1 up, -1 down

    def execute(self, context):
        import mathutils

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig = bpy.data.objects.get("Ai_Rig")

        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        step = 0.01 * self.direction
        offset = mathutils.Vector((0.0, 0.0, step))
        ai_rig.location += offset
        if mesh_obj and mesh_obj.parent != ai_rig:
            mesh_obj.location += offset

        context.scene.nwn2_vertical_shift_adjustment = round(
            context.scene.nwn2_vertical_shift_adjustment + step, 3
        )
        self.report({'INFO'}, f"Vertical shift: {context.scene.nwn2_vertical_shift_adjustment:.3f}")
        return {'FINISHED'}


class NWN2_OT_Step4_ProfileShape(bpy.types.Operator):
    """Apply the selected body's race/profile shaping preset"""
    bl_idname = "nwn2.step4_profile_shape"
    bl_label = "Shape to Selected Profile"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import math
        import mathutils

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig = bpy.data.objects.get("Ai_Rig")

        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        profile_key = nwn2_profile_key(context, mesh_obj or ai_rig)
        preset = NWN2_PROFILE_SHAPE_PRESETS.get(profile_key)
        if not preset:
            self.report({'INFO'}, f"No profile-shape preset is defined for {profile_key}.")
            return {'CANCELLED'}

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        target_tilt = preset.get("tilt_degrees")
        if target_tilt is not None:
            target_angle = math.radians(target_tilt)
            delta = target_angle - ai_rig.rotation_euler.x
            if abs(delta) > 0.000001:
                ai_rig.rotation_euler.x += delta
                if mesh_obj:
                    mesh_obj.rotation_euler.x += delta
                context.scene.nwn2_tilt_adjustment = round(target_tilt, 2)

        target_shift = preset.get("forward_shift")
        if target_shift is not None:
            current_shift = getattr(context.scene, "nwn2_shift_adjustment", 0.0)
            delta = target_shift - current_shift
            if abs(delta) > 0.000001:
                offset = mathutils.Vector((0.0, delta, 0.0))
                ai_rig.location += offset
                if mesh_obj and mesh_obj.parent != ai_rig:
                    mesh_obj.location += offset
                context.scene.nwn2_shift_adjustment = round(target_shift, 3)

        bpy.ops.object.select_all(action='DESELECT')
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig
        bpy.ops.object.mode_set(mode='POSE')

        missing_bones = []
        for bone_name, transform in preset.get("pose_bones", {}).items():
            pbone = ai_rig.pose.bones.get(bone_name)
            if not pbone:
                missing_bones.append(bone_name)
                continue

            pbone.rotation_mode = 'QUATERNION'
            pbone.location = transform.get("location", (0.0, 0.0, 0.0))
            pbone.rotation_quaternion = mathutils.Quaternion(
                transform.get("rotation_quaternion", (1.0, 0.0, 0.0, 0.0))
            )
            pbone.scale = transform.get("scale", (1.0, 1.0, 1.0))

        bpy.ops.object.mode_set(mode='OBJECT')
        context.view_layer.update()

        if missing_bones:
            self.report({'WARNING'}, f"Profile shape applied, but missing bones: {', '.join(missing_bones)}")
        else:
            self.report({'INFO'}, f"Applied {preset['label']} shape preset.")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 5 — Final Fitting
# ---------------------------------------------------------------------------

class NWN2_OT_Step5_FinalFitting(bpy.types.Operator):
    """Enter Pose Mode, select arm bones for final fitting"""
    bl_idname = "nwn2.step5_final_fitting"
    bl_label = "Step 5: Final Fitting"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import json

        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        # Take snapshot of current pose before any edits
        step5_snapshot = {}
        for pbone in ai_rig.pose.bones:
            step5_snapshot[pbone.name] = {
                "location":            list(pbone.location),
                "rotation_quaternion": list(pbone.rotation_quaternion),
                "rotation_euler":      list(pbone.rotation_euler),
                "scale":               list(pbone.scale),
                "rotation_mode":       pbone.rotation_mode,
            }
        context.scene.nwn2_step5_snapshot = json.dumps(step5_snapshot)

        bpy.ops.pose.select_all(action='DESELECT')
        ARM_BONES = {"RArm110", "RArm111", "RArm12", "RArm1Palm", "LArm010", "LArm011", "LArm02", "LArm0Palm"}
        for pbone in ai_rig.pose.bones:
            if pbone.name in ARM_BONES:
                pbone.select = True

        context.scene.transform_orientation_slots[0].type = 'NORMAL'
        context.scene.nwn2_step5_active = True

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'UI':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.wm.context_set_boolean(data_path="space_data.show_region_ui", value=True)
                        break

        # Hide reference body — no longer needed after scale adjustment
        nwn2_set_vanilla_body_visible(context, False, ai_rig)
        nwn2_set_vanilla_accessories_visible(context, False, ai_rig)

        nwn2_set_workflow_next_step(context, "step5_done")
        self.report({'INFO'}, "Pose snapshot saved. Arm bones selected.")
        return {'FINISHED'}


class NWN2_OT_Step5_ToggleVanillaBody(bpy.types.Operator):
    """Toggle the active profile vanilla body reference for final sculpt fitting"""
    bl_idname = "nwn2.step5_toggle_vanilla_body"
    bl_label = "Show Vanilla Body"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ref_obj = ai_rig or mesh_obj
        profile = nwn2_profile(context, ref_obj)
        body = bpy.data.objects.get(profile["body"])
        if not body:
            self.report({'ERROR'}, f"{profile['body']} not found.")
            return {'CANCELLED'}

        visible = body.hide_get() or body.hide_viewport
        nwn2_set_vanilla_body_visible(context, visible, ref_obj)
        state = "shown" if visible else "hidden"
        self.report({'INFO'}, f"{profile['label']} vanilla body {state}.")
        return {'FINISHED'}


class NWN2_OT_Step5_ToggleVanillaAccessories(bpy.types.Operator):
    """Toggle the active profile vanilla boots and gloves for final sculpt fitting"""
    bl_idname = "nwn2.step5_toggle_vanilla_accessories"
    bl_label = "Show Vanilla Gloves/Boots"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ref_obj = ai_rig or mesh_obj
        profile = nwn2_profile(context, ref_obj)

        parts = [
            bpy.data.objects.get(profile["boots"]),
            bpy.data.objects.get(profile["gloves"]),
        ]
        available_parts = [part for part in parts if part]
        missing = [
            profile[role]
            for role, part in (("boots", parts[0]), ("gloves", parts[1]))
            if not part
        ]

        if not available_parts:
            self.report({'ERROR'}, f"{profile['gloves']} and {profile['boots']} not found.")
            return {'CANCELLED'}

        visible = any(part.hide_get() or part.hide_viewport for part in available_parts)
        nwn2_set_vanilla_accessories_visible(context, visible, ref_obj)
        state = "shown" if visible else "hidden"

        if missing:
            self.report({'WARNING'}, f"{profile['label']} vanilla gloves/boots {state}; missing: {', '.join(missing)}.")
        else:
            self.report({'INFO'}, f"{profile['label']} vanilla gloves/boots {state}.")
        return {'FINISHED'}


class NWN2_OT_Step5_ResetPose(bpy.types.Operator):
    """Reset pose back to the state it was in when Step 5 was first clicked"""
    bl_idname = "nwn2.step5_reset_pose"
    bl_label = "Reset Pose"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        import json

        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        snapshot_str = context.scene.nwn2_step5_snapshot
        if not snapshot_str:
            self.report({'ERROR'}, "No Step 5 snapshot found. Click Step 5 first.")
            return {'CANCELLED'}

        snapshot = json.loads(snapshot_str)

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        for pbone in ai_rig.pose.bones:
            if pbone.name not in snapshot:
                continue
            stored = snapshot[pbone.name]
            pbone.rotation_mode = stored["rotation_mode"]
            pbone.location = stored["location"]
            if stored["rotation_mode"] == 'QUATERNION':
                pbone.rotation_quaternion = stored["rotation_quaternion"]
            else:
                pbone.rotation_euler = stored["rotation_euler"]
            pbone.scale = stored["scale"]

        self.report({'INFO'}, "Pose reset to Step 5 start state.")
        return {'FINISHED'}


class NWN2_OT_Step5_ActionA(bpy.types.Operator):
    """Select arm bones, set Normal orientation, Back view"""
    bl_idname = "nwn2.step5_action_a"
    bl_label = "A: Select Arms — Press S then Y to Scale"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.pose.reveal(select=False)
                        break

        bpy.ops.pose.select_all(action='DESELECT')
        ARM_BONES = {"RArm110", "RArm111", "RArm12", "RArm1Palm", "LArm010", "LArm011", "LArm02", "LArm0Palm"}
        for pbone in ai_rig.pose.bones:
            if pbone.name in ARM_BONES:
                pbone.select = True

        context.scene.transform_orientation_slots[0].type = 'NORMAL'

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        space = area.spaces.active
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type='BACK', align_active=False)
                            space.region_3d.view_perspective = 'ORTHO'
                        break

        self.report({'INFO'}, "Arm bones selected. Press S then Y to scale.")
        return {'FINISHED'}


class NWN2_OT_Step5_ActionB(bpy.types.Operator):
    """Left view, hide non-arm bones"""
    bl_idname = "nwn2.step5_action_b"
    bl_label = "B: Right View — Press R to Rotate Arms"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        ARM_BONES = {"RArm110", "RArm111", "RArm12", "RArm1Palm", "LArm010", "LArm011", "LArm02", "LArm0Palm"}

        bpy.ops.pose.select_all(action='SELECT')
        for pbone in ai_rig.pose.bones:
            if pbone.name in ARM_BONES:
                pbone.select = False

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.pose.hide(unselected=False)
                        break

        bpy.ops.pose.select_all(action='DESELECT')
        for pbone in ai_rig.pose.bones:
            if pbone.name in ARM_BONES:
                pbone.select = True

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        space = area.spaces.active
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type='LEFT', align_active=False)
                            space.region_3d.view_perspective = 'ORTHO'
                        break

        self.report({'INFO'}, "Non-arm bones hidden. Press R to rotate.")
        return {'FINISHED'}


class NWN2_OT_Step5_ActionC_Left(bpy.types.Operator):
    """Select LEFT arm bones only"""
    bl_idname = "nwn2.step5_action_c_left"
    bl_label = "Left Arm"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        LEFT_ARM = {"LArm010", "LArm011", "LArm02", "LArm0Palm"}

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.pose.reveal(select=False)
                        break

        bpy.ops.pose.select_all(action='SELECT')
        for pbone in ai_rig.pose.bones:
            if pbone.name in LEFT_ARM:
                pbone.select = False

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.pose.hide(unselected=False)
                        break

        bpy.ops.pose.select_all(action='DESELECT')
        for pbone in ai_rig.pose.bones:
            if pbone.name in LEFT_ARM:
                pbone.select = True

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        space = area.spaces.active
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type='BACK', align_active=False)
                            space.region_3d.view_perspective = 'ORTHO'
                        break

        self.report({'INFO'}, "Left arm bones selected.")
        return {'FINISHED'}


class NWN2_OT_Step5_ActionC_Right(bpy.types.Operator):
    """Select RIGHT arm bones only"""
    bl_idname = "nwn2.step5_action_c_right"
    bl_label = "Right Arm"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        RIGHT_ARM = {"RArm110", "RArm111", "RArm12", "RArm1Palm"}

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.pose.reveal(select=False)
                        break

        bpy.ops.pose.select_all(action='SELECT')
        for pbone in ai_rig.pose.bones:
            if pbone.name in RIGHT_ARM:
                pbone.select = False

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            bpy.ops.pose.hide(unselected=False)
                        break

        bpy.ops.pose.select_all(action='DESELECT')
        for pbone in ai_rig.pose.bones:
            if pbone.name in RIGHT_ARM:
                pbone.select = True

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        space = area.spaces.active
                        with context.temp_override(area=area, region=region):
                            bpy.ops.view3d.view_axis(type='BACK', align_active=False)
                            space.region_3d.view_perspective = 'ORTHO'
                        break

        self.report({'INFO'}, "Right arm bones selected.")
        return {'FINISHED'}


class NWN2_OT_Step5_ActionD(bpy.types.Operator):
    """Enter Sculpt Mode with Elastic Deform brush"""
    bl_idname = "nwn2.step5_action_d"
    bl_label = "D: Enter Sculpt Mode — Elastic Deform"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ai_rig = bpy.data.objects.get("Ai_Rig")
        mesh_obj = bpy.data.objects.get("newModel_Mesh")

        if not ai_rig or not mesh_obj:
            self.report({'ERROR'}, "Ai_Rig or newModel_Mesh not found.")
            return {'CANCELLED'}

        if context.mode == 'POSE':
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            with context.temp_override(area=area, region=region):
                                bpy.ops.pose.reveal(select=False)
                            break
            bpy.ops.object.mode_set(mode='OBJECT')

        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj
        bpy.ops.object.mode_set(mode='SCULPT')
        mesh_obj.use_mesh_mirror_x = True

        for area in context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        with context.temp_override(area=area, region=region):
                            try:
                                bpy.ops.brush.asset_activate(
                                    asset_library_type='ESSENTIALS',
                                    relative_asset_identifier="brushes/essentials_brushes-mesh_sculpt.blend/Brush/Elastic Grab"
                                )
                                if context.tool_settings.sculpt and context.tool_settings.sculpt.brush:
                                    context.tool_settings.sculpt.brush.size = 200
                            except Exception as e:
                                self.report({'WARNING'}, f"Could not set brush: {e}")
                        break

        self.report({'INFO'}, "Sculpt Mode — Elastic Deform active with X symmetry.")
        return {'FINISHED'}


class NWN2_OT_Step5_FootRotate(bpy.types.Operator):
    """Rotate a single ankle bone 5° on Z axis in global space"""
    bl_idname = "nwn2.step5_foot_rotate"
    bl_label = "Rotate Foot"
    bl_options = {'REGISTER', 'UNDO'}

    bone_name: bpy.props.StringProperty()
    direction: bpy.props.IntProperty()  # +1 or -1

    def execute(self, context):
        import math
        ai_rig = bpy.data.objects.get("Ai_Rig")
        if not ai_rig:
            self.report({'ERROR'}, "Ai_Rig not found.")
            return {'CANCELLED'}

        # Ensure Ai_Rig is visible and active regardless of current mode
        ai_rig.hide_viewport = False
        for obj in context.view_layer.objects:
            obj.select_set(False)
        ai_rig.select_set(True)
        context.view_layer.objects.active = ai_rig

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'POSE' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='POSE')

        # Set transform to Global
        context.scene.transform_orientation_slots[0].type = 'GLOBAL'

        pbone = ai_rig.pose.bones.get(self.bone_name)
        if not pbone:
            self.report({'ERROR'}, f"{self.bone_name} not found.")
            return {'CANCELLED'}

        # Select only this bone
        bpy.ops.pose.select_all(action='DESELECT')
        pbone.select = True
        ai_rig.data.bones.active = ai_rig.data.bones[self.bone_name]

        # Rotate 5° on global Z
        angle = math.radians(5 * self.direction)
        import mathutils
        rot = mathutils.Matrix.Rotation(angle, 4, 'Z')
        pbone.matrix = rot @ pbone.matrix

        self.report({'INFO'}, f"{self.bone_name} rotated {5 * self.direction}° on Z.")
        return {'FINISHED'}


class NWN2_OT_Step5_Done(bpy.types.Operator):
    """Attach mesh to the active profile skeleton"""
    bl_idname = "nwn2.step5_done"
    bl_label = "Done - Attach to Game Skeleton"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.nwn2_step5_active = False

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        ai_rig   = bpy.data.objects.get("Ai_Rig")
        nwn2_set_vanilla_body_visible(context, False, ai_rig or mesh_obj)
        nwn2_set_vanilla_accessories_visible(context, False, ai_rig or mesh_obj)
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}
        profile_key = ai_rig.get("nwn2_body_profile") if ai_rig else nwn2_profile_key(context, mesh_obj)
        if profile_key not in NWN2_BODY_PROFILES:
            profile_key = nwn2_profile_key(context, mesh_obj)
        nwn2_stamp_profile(mesh_obj, context, profile_key)
        target_skel = nwn2_profile_object(context, "skeleton", mesh_obj)
        if not target_skel:
            self.report({'ERROR'}, f"{nwn2_profile(context, mesh_obj)['skeleton']} not found.")
            return {'CANCELLED'}

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        region_3d = next((r for r in area_3d.regions if r.type == 'WINDOW'), None) if area_3d else None

        if context.mode != 'OBJECT' and area_3d and region_3d:
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                if context.mode == 'POSE':
                    bpy.ops.pose.reveal(select=False)
                bpy.ops.object.mode_set(mode='OBJECT')

        context.view_layer.objects.active = mesh_obj
        mesh_obj.select_set(True)

        ai_rig_mod = None
        for mod in mesh_obj.modifiers:
            if mod.type == 'ARMATURE' and mod.object == ai_rig:
                ai_rig_mod = mod
                break

        if ai_rig_mod:
            ai_rig_mod.show_viewport = True
            ai_rig_mod.show_render = True
            with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
                while mesh_obj.modifiers[0].name != ai_rig_mod.name:
                    bpy.ops.object.modifier_move_up(modifier=ai_rig_mod.name)
                bpy.ops.object.modifier_apply(modifier=ai_rig_mod.name)

        for mod in list(mesh_obj.modifiers):
            if mod.type == 'ARMATURE':
                mesh_obj.modifiers.remove(mod)

        with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

        arm_mod = mesh_obj.modifiers.new(name="Armature", type='ARMATURE')
        arm_mod.object = target_skel
        arm_mod.use_vertex_groups = True

        mesh_obj.select_set(True)
        target_skel.select_set(True)
        context.view_layer.objects.active = target_skel
        with context.temp_override(window=win, screen=scr, area=area_3d, region=region_3d):
            bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)

        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj

        if ai_rig:
            ai_rig.select_set(True)
            context.view_layer.objects.active = ai_rig
            bpy.ops.object.mode_set(mode='POSE')
            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.pose.armature_apply(selected=False)
            bpy.ops.object.mode_set(mode='OBJECT')
            ai_rig.hide_viewport = True

        nwn2_set_workflow_next_step(context, "step6_build")
        self.report({'INFO'}, f"newModel_Mesh attached to {target_skel.name}.")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 6 — Material / Shader Setup
# ---------------------------------------------------------------------------

class NWN2_OT_Step6_SetupMaterial(bpy.types.Operator):
    """Create NWN2 material with Principled BSDF, D and N image nodes"""
    bl_idname = "nwn2.step6_setup_material"
    bl_label = "Step 6: Setup Material & Shader"
    bl_options = {'UNDO'}

    def execute(self, context):
        nwn2_set_vanilla_body_visible(context, False)
        nwn2_set_vanilla_accessories_visible(context, False)
        mat_name = context.scene.nwn2_material_name.strip()

        if not mat_name:
            self.report({'ERROR'}, "Please build a material name first.")
            return {'CANCELLED'}

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}

        try:
            if hasattr(mesh_obj, 'nwn2mdk'):
                mesh_obj.nwn2mdk.object_type = 'MESH'

            mat_names = [m.name for m in mesh_obj.data.materials if m]
            mesh_obj.data.materials.clear()
            for n in mat_names:
                if n in bpy.data.materials:
                    bpy.data.materials.remove(bpy.data.materials[n])
            if mat_name in bpy.data.materials:
                bpy.data.materials.remove(bpy.data.materials[mat_name], do_unlink=True)

            mat = bpy.data.materials.new(name=mat_name)
            mat.use_nodes = True
            mesh_obj.data.materials.append(mat)

            # Also assign to LowPoly_Mesh so bake target stays in sync
            lp_obj = bpy.data.objects.get("LowPoly_Mesh")
            if lp_obj:
                lp_obj.data.materials.clear()
                lp_obj.data.materials.append(mat)

            nodes = mat.node_tree.nodes
            links = mat.node_tree.links
            nodes.clear()

            output = nodes.new('ShaderNodeOutputMaterial')
            output.location = (600, 0)
            bsdf = nodes.new('ShaderNodeBsdfPrincipled')
            bsdf.location = (300, 0)
            links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

            d_node = nodes.new('ShaderNodeTexImage')
            d_node.location = (-300, 150)
            d_node.label = f"{mat_name}_D"
            d_node.image = bpy.data.images.get(f"{mat_name}_D.png") or \
                           bpy.data.images.new(name=f"{mat_name}_D.png", width=1024, height=1024)
            links.new(d_node.outputs['Color'], bsdf.inputs['Base Color'])

            n_node = nodes.new('ShaderNodeTexImage')
            n_node.location = (-300, -150)
            n_node.label = f"{mat_name}_N"
            n_node.image = bpy.data.images.get(f"{mat_name}_N.png") or \
                           bpy.data.images.new(name=f"{mat_name}_N.png", width=1024, height=1024)
            n_node.image.colorspace_settings.name = 'Non-Color'

            # DirectX normal map — plug straight in, no inversion
            # The bake outputs DirectX format, so Material Preview = what NWN2 renders
            normal_map = nodes.new('ShaderNodeNormalMap')
            normal_map.location = (50, -150)
            normal_map.space = 'TANGENT'
            links.new(n_node.outputs['Color'], normal_map.inputs['Color'])
            links.new(normal_map.outputs['Normal'], bsdf.inputs['Normal'])

            for area in context.screen.areas:
                area.tag_redraw()

            nwn2_set_workflow_next_step(context, "step7_bake")
            self.report({'INFO'}, f"Material '{mat_name}' created with _D and _N nodes.")

        except Exception as e:
            self.report({'ERROR'}, f"Failed: {str(e)}")
            return {'CANCELLED'}

        return {'FINISHED'}


class NWN2_OT_Step6_BuildName(bpy.types.Operator):
    """Build the NWN2 material name from the selected options"""
    bl_idname = "nwn2.step6_build_name"
    bl_label = "Build Material Name"
    bl_options = {'REGISTER'}

    def execute(self, context):
        nwn2_set_vanilla_body_visible(context, False)
        nwn2_set_vanilla_accessories_visible(context, False)
        scene = context.scene
        profile = nwn2_profile(context)
        token = profile["model_token"]
        scene.nwn2_sex = token[-1]

        number = scene.nwn2_part_number.strip()
        if not number:
            self.report({'ERROR'}, "Please enter a part number.")
            return {'CANCELLED'}

        scene.nwn2_material_name = f"P_{token}_{scene.nwn2_armor_code}_{scene.nwn2_part_type}{number}"
        nwn2_set_workflow_next_step(context, "step6_setup")
        self.report({'INFO'}, f"Material name: {scene.nwn2_material_name}")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# STEP 7 — Bake Maps
# ---------------------------------------------------------------------------

class NWN2_OT_Step7_Bake(bpy.types.Operator):
    """Bake maps from HighPoly_Mesh onto LowPoly_Mesh using Selected to Active"""
    bl_idname = "nwn2.step7_bake"
    bl_label = "Bake Maps"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return (
            bpy.data.objects.get("HighPoly_Mesh") is not None and
            bpy.data.objects.get("LowPoly_Mesh") is not None
        )

    def fix_normals_for_bake(self, obj):
        """Recalculate outside, average by face area, apply weighted normals"""
        was_hidden = obj.hide_viewport
        obj.hide_viewport = False
        bpy.context.view_layer.update()
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

        if bpy.context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.normals_make_consistent(inside=False)
        bpy.ops.mesh.average_normals(average_type='FACE_AREA')
        bpy.ops.object.mode_set(mode='OBJECT')

        for mod in list(obj.modifiers):
            if mod.type == 'WEIGHTED_NORMAL':
                obj.modifiers.remove(mod)

        wn_mod = obj.modifiers.new(name="WeightedNormal", type='WEIGHTED_NORMAL')
        wn_mod.mode = 'FACE_AREA_WITH_ANGLE'
        wn_mod.weight = 50
        wn_mod.keep_sharp = True

        while obj.modifiers[0].name != wn_mod.name:
            bpy.ops.object.modifier_move_up(modifier=wn_mod.name)
        bpy.ops.object.modifier_apply(modifier=wn_mod.name)

        obj.hide_viewport = was_hidden

    def ensure_image(self, name, size):
        """Get or create a bake target image"""
        img = bpy.data.images.get(name)
        if img:
            if img.size[0] != size:
                bpy.data.images.remove(img)
                img = None
        if not img:
            img = bpy.data.images.new(name=name, width=size, height=size, alpha=False)
        return img

    def ensure_image_node(self, mat, img, label):
        """Get or create an image texture node with given label, set as active"""
        nodes = mat.node_tree.nodes
        node = next((n for n in nodes if n.type == 'TEX_IMAGE' and n.label == label), None)
        if not node:
            node = nodes.new('ShaderNodeTexImage')
            node.label = label
            node.name = label
        # Always explicitly set image
        node.image = img
        if img:
            img.update()
        # Blender bake requires node to be both selected AND active
        for n in nodes:
            n.select = False
        node.select = True
        nodes.active = node
        return node

    def execute(self, context):
        scene = context.scene
        nwn2_set_vanilla_body_visible(context, False)
        nwn2_set_vanilla_accessories_visible(context, False)
        hp_obj = bpy.data.objects.get("HighPoly_Mesh")
        lp_obj = bpy.data.objects.get("LowPoly_Mesh")

        if not hp_obj or not lp_obj:
            self.report({'ERROR'}, "HighPoly_Mesh or LowPoly_Mesh not found.")
            return {'CANCELLED'}

        mat_name = scene.nwn2_material_name.strip()
        if not mat_name:
            self.report({'ERROR'}, "Please build a material name in Step 6 first.")
            return {'CANCELLED'}

        nwn2_mat = bpy.data.materials.get(mat_name)
        if not nwn2_mat:
            self.report({'ERROR'}, f"Material '{mat_name}' not found. Run Step 6 Setup first.")
            return {'CANCELLED'}

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        # Temporarily unhide both meshes
        hp_was_hidden = hp_obj.hide_viewport
        lp_was_hidden = lp_obj.hide_viewport
        hp_was_render_hidden = hp_obj.hide_render
        lp_was_render_hidden = lp_obj.hide_render
        working_obj = bpy.data.objects.get("newModel_Mesh")
        working_was_hidden = working_obj.hide_viewport if working_obj else None
        working_was_select_hidden = working_obj.hide_get() if working_obj else None
        working_was_render_hidden = working_obj.hide_render if working_obj else None
        hp_obj.hide_viewport = False
        lp_obj.hide_viewport = False
        hp_obj.hide_render = False
        lp_obj.hide_render = False
        if working_obj and working_obj not in {hp_obj, lp_obj}:
            # Keep the rigged working mesh out of Cycles bake rays. It can
            # self-occlude AO and stamp hard dark intersections into _D.
            working_obj.hide_viewport = True
            working_obj.hide_set(True)
            working_obj.hide_render = True

        # HighPoly keeps its own original material (source of color/detail)
        # LowPoly gets a clean temp bake-target material — no circular dependency
        bake_mat_name = "__nwn2_bake_temp__"
        bake_mat = bpy.data.materials.get(bake_mat_name)
        if bake_mat:
            bpy.data.materials.remove(bake_mat)
        bake_mat = bpy.data.materials.new(name=bake_mat_name)
        bake_mat.use_nodes = True
        bake_mat.node_tree.nodes.clear()

        lp_orig_mats = list(lp_obj.data.materials)
        lp_obj.data.materials.clear()
        lp_obj.data.materials.append(bake_mat)

        size = int(scene.nwn2_bake_resolution)

        # Save and set render settings
        # Fix normals before baking
        bpy.ops.object.select_all(action='DESELECT')
        for fix_name in ["LowPoly_Mesh"]:
            fix_obj = bpy.data.objects.get(fix_name)
            if fix_obj:
                self.fix_normals_for_bake(fix_obj)

        prev_engine  = scene.render.engine
        prev_device  = scene.cycles.device
        prev_samples = scene.cycles.samples
        prev_denoise = scene.cycles.use_denoising
        prev_denoiser = scene.cycles.denoiser

        scene.render.engine = 'CYCLES'
        has_gpu_device = False
        try:
            cycles_prefs = bpy.context.preferences.addons['cycles'].preferences
            cycles_prefs.get_devices()
            has_gpu_device = any(device.type != 'CPU' for device in cycles_prefs.devices)
        except Exception:
            has_gpu_device = False
        scene.cycles.device = 'GPU' if has_gpu_device else 'CPU'
        scene.cycles.samples = scene.nwn2_bake_samples
        scene.cycles.use_denoising = True
        for denoiser in ('OPENIMAGEDENOISE', 'OPTIX', 'NLM'):
            try:
                scene.cycles.denoiser = denoiser
                break
            except TypeError:
                continue

        scene.render.bake.use_selected_to_active = True
        scene.render.bake.cage_extrusion = scene.nwn2_bake_ray_distance
        scene.render.bake.max_ray_distance = scene.nwn2_bake_max_ray_distance
        scene.render.bake.use_pass_direct = False
        scene.render.bake.use_pass_indirect = False
        scene.render.bake.use_pass_color = True
        scene.render.bake.margin = 512
        scene.render.bake.margin_type = 'EXTEND'

        maps_baked = []
        errors = []

        def clean_ao_diffuse_multiply():
            if not nwn2_mat or not nwn2_mat.use_nodes or not nwn2_mat.node_tree:
                return
            nodes = nwn2_mat.node_tree.nodes
            links = nwn2_mat.node_tree.links
            ao_mix = nodes.get('__ao_multiply__')
            d_node = next(
                (n for n in nodes if n.type == 'TEX_IMAGE' and (
                    (n.label or '').endswith('_D') or
                    n.name.endswith('_D') or
                    (n.image and n.image.name.replace('.png', '').endswith('_D'))
                )),
                None
            )
            bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
            if bsdf:
                base_color = bsdf.inputs.get('Base Color')
                if base_color:
                    uses_ao_mix = ao_mix and any(lnk.from_node == ao_mix for lnk in base_color.links)
                    if d_node and (uses_ao_mix or not base_color.links):
                        for lnk in list(base_color.links):
                            links.remove(lnk)
                        links.new(d_node.outputs['Color'], base_color)
            if ao_mix:
                nodes.remove(ao_mix)

        def wire_ao_diffuse_multiply():
            if not nwn2_mat or not nwn2_mat.use_nodes or not nwn2_mat.node_tree:
                return
            clean_ao_diffuse_multiply()
            nodes = nwn2_mat.node_tree.nodes
            links = nwn2_mat.node_tree.links
            d_node = next(
                (n for n in nodes if n.type == 'TEX_IMAGE' and (
                    (n.label or '').endswith('_D') or
                    n.name.endswith('_D') or
                    (n.image and n.image.name.replace('.png', '').endswith('_D'))
                )),
                None
            )
            ao_node = next(
                (n for n in nodes if n.type == 'TEX_IMAGE' and (
                    (n.label or '').endswith('_AO') or
                    n.name.endswith('_AO') or
                    (n.image and n.image.name.replace('.png', '').endswith('_AO'))
                )),
                None
            )
            bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
            if not d_node or not ao_node or not bsdf:
                return

            ao_mix = nodes.new('ShaderNodeMixRGB')
            ao_mix.name = '__ao_multiply__'
            ao_mix.label = 'Diffuse x AO'
            ao_mix.blend_type = 'MULTIPLY'
            factor_input = ao_mix.inputs.get('Fac') or ao_mix.inputs.get('Factor')
            if factor_input:
                factor_input.default_value = 1.0
            ao_mix.location = (-430, 80)

            base_color = bsdf.inputs.get('Base Color')
            if not base_color:
                return
            for lnk in list(base_color.links):
                links.remove(lnk)
            links.new(d_node.outputs['Color'], ao_mix.inputs['Color1'])
            links.new(ao_node.outputs['Color'], ao_mix.inputs['Color2'])
            links.new(ao_mix.outputs['Color'], base_color)

        def do_bake(bake_type, img_name, colorspace='sRGB', selected_to_active=True):
            try:
                # Create fresh bake image
                img = bpy.data.images.get(img_name)
                if img:
                    bpy.data.images.remove(img)
                img = bpy.data.images.new(name=img_name, width=size, height=size, alpha=False)
                img.colorspace_settings.name = colorspace

                # Add clean image node to temp bake material
                nodes = bake_mat.node_tree.nodes
                for n in list(nodes):
                    if n.type == 'TEX_IMAGE':
                        nodes.remove(n)

                img_node = nodes.new('ShaderNodeTexImage')
                img_node.image = img
                img_node.location = (0, 0)

                # Both select AND active required by Blender bake
                for n in nodes:
                    n.select = False
                img_node.select = True
                nodes.active = img_node

                # HP = source, LP = active target. AO can be baked target-only.
                bpy.ops.object.select_all(action='DESELECT')
                if selected_to_active:
                    hp_obj.select_set(True)
                lp_obj.select_set(True)
                context.view_layer.objects.active = lp_obj

                ret = bpy.ops.object.bake('EXEC_DEFAULT', type=bake_type, use_clear=True)

                if 'FINISHED' in ret:
                    # Copy baked image into the NWN2 material node
                    if nwn2_mat.node_tree:
                        base_name = img_name.replace('.png', '')
                        target = next(
                            (n for n in nwn2_mat.node_tree.nodes
                             if n.type == 'TEX_IMAGE' and (
                                 n.label == base_name or
                                 n.label == img_name or
                                 base_name in (n.label or '')
                             )),
                            None
                        )
                        if target:
                            target.image = img
                        else:
                            new_node = nwn2_mat.node_tree.nodes.new('ShaderNodeTexImage')
                            new_node.label = base_name
                            new_node.name = base_name
                            new_node.image = img
                    img.pack()
                    maps_baked.append(img_name)
                else:
                    errors.append(f"{img_name}: bake returned {ret}")

            except Exception as e:
                errors.append(f"{img_name}: {e}")

        def do_projected_highpoly_ao_bake(img_name):
            old_selected_to_active = scene.render.bake.use_selected_to_active
            hp_orig_mats = list(hp_obj.data.materials)
            hidden_render = {}
            hidden_viewport = {}
            lp_cycles_visibility = {}
            ao_mat = None

            def stash_cycles_visibility(obj):
                values = {}
                cycles_vis = getattr(obj, "cycles_visibility", None)
                if not cycles_vis:
                    return values
                for attr in ("camera", "diffuse", "glossy", "transmission", "shadow", "scatter"):
                    if hasattr(cycles_vis, attr):
                        values[attr] = getattr(cycles_vis, attr)
                return values

            def restore_cycles_visibility(obj, values):
                cycles_vis = getattr(obj, "cycles_visibility", None)
                if not cycles_vis:
                    return
                for attr, value in values.items():
                    try:
                        setattr(cycles_vis, attr, value)
                    except Exception:
                        pass

            try:
                scene.render.bake.use_selected_to_active = True

                # Isolate the source/target pair so the AO shader reads the
                # high-poly surface instead of nearby rig helpers or leftovers.
                for obj in context.scene.objects:
                    if obj.type != 'MESH' or obj in {hp_obj, lp_obj}:
                        continue
                    hidden_render[obj] = obj.hide_render
                    hidden_viewport[obj] = obj.hide_viewport
                    obj.hide_render = True
                    obj.hide_viewport = True

                hp_obj.hide_render = False
                hp_obj.hide_viewport = False
                hp_obj.hide_set(False)
                lp_obj.hide_render = False
                lp_obj.hide_viewport = False
                lp_obj.hide_set(False)

                lp_cycles_visibility = stash_cycles_visibility(lp_obj)
                cycles_vis = getattr(lp_obj, "cycles_visibility", None)
                if cycles_vis:
                    for attr in ("diffuse", "glossy", "transmission", "shadow", "scatter"):
                        if hasattr(cycles_vis, attr):
                            setattr(cycles_vis, attr, False)

                ao_mat = bpy.data.materials.new(name="__nwn2_projected_ao_source__")
                ao_mat.use_nodes = True
                nodes = ao_mat.node_tree.nodes
                links = ao_mat.node_tree.links
                nodes.clear()
                out_node = nodes.new('ShaderNodeOutputMaterial')
                emission = nodes.new('ShaderNodeEmission')
                ao_node = nodes.new('ShaderNodeAmbientOcclusion')
                if 'Distance' in ao_node.inputs:
                    ao_distance = max(0.02, min(0.25, float(scene.nwn2_bake_ray_distance) * 4.0))
                    ao_node.inputs['Distance'].default_value = ao_distance
                ao_output = ao_node.outputs.get('AO') or ao_node.outputs.get('Color')
                links.new(ao_output, emission.inputs['Color'])
                emission.inputs['Strength'].default_value = 1.0
                links.new(emission.outputs['Emission'], out_node.inputs['Surface'])

                hp_obj.data.materials.clear()
                hp_obj.data.materials.append(ao_mat)
                do_bake('EMIT', img_name, 'Non-Color', selected_to_active=True)
            finally:
                hp_obj.data.materials.clear()
                for mat in hp_orig_mats:
                    hp_obj.data.materials.append(mat)
                restore_cycles_visibility(lp_obj, lp_cycles_visibility)
                for obj, value in hidden_render.items():
                    obj.hide_render = value
                for obj, value in hidden_viewport.items():
                    obj.hide_viewport = value
                if ao_mat and ao_mat.name in bpy.data.materials:
                    bpy.data.materials.remove(ao_mat)
                scene.render.bake.use_selected_to_active = old_selected_to_active

        clean_ao_diffuse_multiply()

        if scene.nwn2_bake_diffuse:
            do_bake('DIFFUSE', f"{mat_name}_D.png", 'sRGB')
            clean_ao_diffuse_multiply()

        if scene.nwn2_bake_normal:
            # DirectX normal map — invert green, no cage, disconnect HP normals
            scene.render.bake.normal_space = 'TANGENT'
            scene.render.bake.normal_r = 'POS_X'
            scene.render.bake.normal_g = 'NEG_Y'
            scene.render.bake.normal_b = 'POS_Z'
            scene.render.bake.use_cage = False

            # Temporarily disconnect Normal/Roughness/Metallic from HP BSDF
            hp_mat = hp_obj.data.materials[0] if hp_obj.data.materials else None
            disconnected_links = []
            if hp_mat and hp_mat.node_tree:
                bsdf = next((n for n in hp_mat.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'), None)
                if bsdf:
                    for input_name in ['Normal', 'Roughness', 'Metallic']:
                        socket = bsdf.inputs.get(input_name)
                        if socket and socket.links:
                            for link in list(socket.links):
                                disconnected_links.append((link.from_socket, link.to_socket))
                                hp_mat.node_tree.links.remove(link)

            do_bake('NORMAL', f"{mat_name}_N.png", 'Non-Color')

            # Reconnect HP material
            if hp_mat and hp_mat.node_tree and disconnected_links:
                for from_sock, to_sock in disconnected_links:
                    hp_mat.node_tree.links.new(from_sock, to_sock)

        if scene.nwn2_bake_metallic:
            # Wire roughness into emission on high poly for correct EMIT bake
            hp_mat = hp_obj.data.materials[0] if hp_obj.data.materials else None
            emit_link_added = None
            if hp_mat and hp_mat.use_nodes:
                hp_nodes = hp_mat.node_tree.nodes
                hp_links = hp_mat.node_tree.links
                hp_bsdf = next((n for n in hp_nodes if n.type == 'BSDF_PRINCIPLED'), None)
                hp_out = next((n for n in hp_nodes if n.type == 'OUTPUT_MATERIAL'), None)
                roughness_socket = hp_bsdf.inputs.get('Roughness') if hp_bsdf else None
                if roughness_socket and roughness_socket.links and hp_out:
                    roughness_source = roughness_socket.links[0].from_socket
                    emit_node = hp_nodes.new('ShaderNodeEmission')
                    emit_node.name = '__tmp_emit__'
                    emit_node.location = (hp_bsdf.location.x, hp_bsdf.location.y - 300)
                    hp_links.new(roughness_source, emit_node.inputs['Color'])
                    # Save original surface link and replace with emission
                    orig_surface = hp_out.inputs['Surface'].links[0].from_socket if hp_out.inputs['Surface'].links else None
                    hp_links.new(emit_node.outputs['Emission'], hp_out.inputs['Surface'])
                    emit_link_added = (emit_node, orig_surface, hp_out, hp_mat)
            do_bake('EMIT', f"{mat_name}_S_raw.png", 'Non-Color')
            # Restore high poly material
            if emit_link_added:
                emit_node, orig_surface, hp_out, hp_mat = emit_link_added
                hp_mat.node_tree.nodes.remove(emit_node)
                if orig_surface:
                    hp_mat.node_tree.links.new(orig_surface, hp_out.inputs['Surface'])
            # Invert roughness to get NWN2 specular map
            raw_img = bpy.data.images.get(f"{mat_name}_S_raw.png")
            if raw_img:
                pixels = list(raw_img.pixels)
                arr = [1.0 - v if (i % 4 != 3) else v for i, v in enumerate(pixels)]
                s_img = bpy.data.images.get(f"{mat_name}_S.png")
                if s_img:
                    bpy.data.images.remove(s_img)
                s_img = bpy.data.images.new(f"{mat_name}_S.png", raw_img.size[0], raw_img.size[1], alpha=False)
                s_img.colorspace_settings.name = 'Non-Color'
                s_img.pixels = arr
                s_img.pack()
                bpy.data.images.remove(raw_img)
                # Add _S node to material — clean up any leftover raw node first
                if nwn2_mat.node_tree:
                    nodes = nwn2_mat.node_tree.nodes
                    # Remove any raw bake node that snuck in
                    raw_node = nodes.get(f"{mat_name}_S_raw")
                    if raw_node:
                        nodes.remove(raw_node)
                    # Find or create proper _S node
                    s_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_S')), None)
                    if not s_node:
                        s_node = nodes.new('ShaderNodeTexImage')
                    s_node.label = f"{mat_name}_S"
                    s_node.name = f"{mat_name}_S"
                    s_node.location = (-300, -450)
                    s_node.image = s_img
                    # Connect _S to Specular IOR Level on Principled BSDF
                    bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
                    if bsdf:
                        specular_input = bsdf.inputs.get('Specular IOR Level') or bsdf.inputs.get('Specular')
                        if specular_input:
                            # Remove existing links on specular input
                            for lnk in list(specular_input.links):
                                nwn2_mat.node_tree.links.remove(lnk)
                            nwn2_mat.node_tree.links.new(s_node.outputs['Color'], specular_input)
                    # Make it the active node so it shows in UV editor
                    for n in nodes:
                        n.select = False
                    s_node.select = True
                    nodes.active = s_node
                maps_baked.append(f"{mat_name}_S.png")

        if scene.nwn2_bake_metallic_map:
            # Wire metallic into emission on high poly for correct EMIT bake
            hp_mat = hp_obj.data.materials[0] if hp_obj.data.materials else None
            emit_link_added_m = None
            if hp_mat and hp_mat.use_nodes:
                hp_nodes = hp_mat.node_tree.nodes
                hp_links = hp_mat.node_tree.links
                hp_bsdf = next((n for n in hp_nodes if n.type == 'BSDF_PRINCIPLED'), None)
                hp_out = next((n for n in hp_nodes if n.type == 'OUTPUT_MATERIAL'), None)
                metallic_socket = hp_bsdf.inputs.get('Metallic') if hp_bsdf else None
                if metallic_socket and metallic_socket.links and hp_out:
                    metallic_source = metallic_socket.links[0].from_socket
                    emit_node = hp_nodes.new('ShaderNodeEmission')
                    emit_node.name = '__tmp_emit_m__'
                    emit_node.location = (hp_bsdf.location.x, hp_bsdf.location.y - 400)
                    hp_links.new(metallic_source, emit_node.inputs['Color'])
                    orig_surface = hp_out.inputs['Surface'].links[0].from_socket if hp_out.inputs['Surface'].links else None
                    hp_links.new(emit_node.outputs['Emission'], hp_out.inputs['Surface'])
                    emit_link_added_m = (emit_node, orig_surface, hp_out, hp_mat)
            do_bake('EMIT', f"{mat_name}_M.png", 'Non-Color')
            # Restore high poly material
            if emit_link_added_m:
                emit_node, orig_surface, hp_out, hp_mat = emit_link_added_m
                hp_mat.node_tree.nodes.remove(emit_node)
                if orig_surface:
                    hp_mat.node_tree.links.new(orig_surface, hp_out.inputs['Surface'])
            # Keep _M as source data for the _S/specular build only.
            # Do not wire it into Principled Metallic; that distorts PBR preview.
            m_img = bpy.data.images.get(f"{mat_name}_M.png")
            if m_img and nwn2_mat.node_tree:
                nodes = nwn2_mat.node_tree.nodes
                m_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_M')), None)
                if not m_node:
                    m_node = nodes.new('ShaderNodeTexImage')
                m_node.label = f"{mat_name}_M"
                m_node.name = f"{mat_name}_M"
                m_node.location = (-300, -650)
                m_node.image = m_img
                bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
                if bsdf:
                    metallic_input = bsdf.inputs.get('Metallic')
                    if metallic_input:
                        for lnk in list(metallic_input.links):
                            from_node = lnk.from_node
                            from_image = getattr(from_node, 'image', None)
                            from_is_metallic_map = (
                                from_node == m_node or
                                (from_node.label or '').endswith('_M') or
                                from_node.name.endswith('_M') or
                                (from_image and from_image.name.replace('.png', '').endswith('_M'))
                            )
                            if from_is_metallic_map:
                                nwn2_mat.node_tree.links.remove(lnk)

        if scene.nwn2_bake_ao:
            do_projected_highpoly_ao_bake(f"{mat_name}_AO.png")
            ao_img = bpy.data.images.get(f"{mat_name}_AO.png")

            # Keep _D clean. Some robe/skirt meshes self-occlude during AO and
            # multiplying that into diffuse can stamp hard black blotches onto
            # otherwise good color bakes. Preserve _AO as its own optional map.
            if ao_img and nwn2_mat and nwn2_mat.use_nodes:
                nodes = nwn2_mat.node_tree.nodes
                ao_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_AO')), None)
                if not ao_node:
                    ao_node = nodes.new('ShaderNodeTexImage')
                    ao_node.label = f"{mat_name}_AO"
                ao_node.name = f"{mat_name}_AO"
                ao_node.image = ao_img
                ao_node.location = (-800, -100)
            wire_ao_diffuse_multiply()

        # Restore LowPoly_Mesh original materials
        lp_obj.data.materials.clear()
        for m in lp_orig_mats:
            lp_obj.data.materials.append(m)

        # --- OVERLAY COMPOSITE: blend _M over _S if both were baked ---
        s_img = bpy.data.images.get(f"{mat_name}_S.png")
        m_img = bpy.data.images.get(f"{mat_name}_M.png")
        if s_img and m_img:
            try:
                s_px = list(s_img.pixels)
                m_px = list(m_img.pixels)
                composited = []
                for i in range(0, len(s_px), 4):
                    for c in range(3):
                        s = s_px[i + c]
                        m = m_px[i + c]
                        # Mix: lerp between S (non-metal) and S*1.5 (metal) using M as factor
                        boosted = min(1.0, s * 1.5)
                        blended = s * (1.0 - m) + boosted * m
                        composited.append(min(1.0, max(0.0, blended)))
                    composited.append(s_px[i + 3])

                # Remove old _S and create fresh to force Blender to update display
                img_w, img_h = s_img.size[0], s_img.size[1]
                bpy.data.images.remove(s_img)
                new_s = bpy.data.images.new(f"{mat_name}_S.png", img_w, img_h, alpha=False)
                new_s.colorspace_settings.name = 'Non-Color'
                new_s.pixels = composited
                new_s.pack()

                # Rewire nodes: _S → MixRGB(Overlay) ← _M → Specular IOR Level
                if nwn2_mat and nwn2_mat.use_nodes:
                    nodes = nwn2_mat.node_tree.nodes
                    links = nwn2_mat.node_tree.links

                    # Remove any existing overlay mix node
                    old_mix = nodes.get('__spec_metallic_overlay__')
                    if old_mix:
                        nodes.remove(old_mix)

                    # Get or create _S node
                    s_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_S')), None)
                    if not s_node:
                        s_node = nodes.new('ShaderNodeTexImage')
                        s_node.label = f"{mat_name}_S"
                        s_node.name = f"{mat_name}_S"
                    s_node.image = new_s
                    s_node.location = (-600, -450)

                    # Get _M node
                    m_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_M')), None)

                    bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
                    spec_input = bsdf.inputs.get('Specular IOR Level') or bsdf.inputs.get('Specular') if bsdf else None

                    if m_node and bsdf and spec_input:
                        # Remove any existing overlay/mix nodes
                        for n_name in ['__spec_metallic_overlay__', '__spec_boost__']:
                            old_n = nodes.get(n_name)
                            if old_n:
                                nodes.remove(old_n)

                        # Boost node: _S * 1.5 (brightened specular for metal areas)
                        boost_node = nodes.new('ShaderNodeMath')
                        boost_node.name = '__spec_boost__'
                        boost_node.label = 'Spec Boost (Metal)'
                        boost_node.operation = 'MULTIPLY'
                        boost_node.inputs[1].default_value = 1.5
                        boost_node.use_clamp = True
                        boost_node.location = (-400, -550)

                        # Mix node: _M as factor between _S (non-metal) and boosted _S (metal)
                        mix_node = nodes.new('ShaderNodeMixRGB')
                        mix_node.name = '__spec_metallic_overlay__'
                        mix_node.label = 'Spec + Metallic Mix'
                        mix_node.blend_type = 'MIX'
                        mix_node.location = (-200, -450)
                        m_node.location = (-600, -650)
                        s_node.location = (-600, -450)

                        # Disconnect any existing specular links
                        for lnk in list(spec_input.links):
                            links.remove(lnk)

                        # Wire: _S → boost → Color2, _S → Color1, _M → Fac, out → Specular
                        links.new(s_node.outputs['Color'], boost_node.inputs[0])
                        links.new(s_node.outputs['Color'], mix_node.inputs['Color1'])
                        links.new(boost_node.outputs['Value'], mix_node.inputs['Color2'])
                        links.new(m_node.outputs['Color'], mix_node.inputs['Fac'])
                        links.new(mix_node.outputs['Color'], spec_input)
                    else:
                        # No _M node — just wire _S directly
                        if spec_input:
                            for lnk in list(spec_input.links):
                                links.remove(lnk)
                            links.new(s_node.outputs['Color'], spec_input)

                for window in bpy.context.window_manager.windows:
                    for area in window.screen.areas:
                        area.tag_redraw()

                maps_baked.append(f"{mat_name}_S.png (+ metallic overlay)")
            except Exception as e:
                errors.append(f"Overlay composite failed: {e}")

        # Remove temp bake material
        bpy.data.materials.remove(bake_mat)

        # Restore render settings
        scene.render.engine  = prev_engine
        scene.cycles.device  = prev_device
        scene.cycles.samples = prev_samples
        scene.cycles.use_denoising = prev_denoise
        try:
            scene.cycles.denoiser = prev_denoiser
        except TypeError:
            pass

        # Restore visibility
        hp_obj.hide_viewport = hp_was_hidden
        lp_obj.hide_viewport = lp_was_hidden
        hp_obj.hide_render = hp_was_render_hidden
        lp_obj.hide_render = lp_was_render_hidden
        if working_obj and working_obj not in {hp_obj, lp_obj}:
            working_obj.hide_viewport = working_was_hidden
            working_obj.hide_render = working_was_render_hidden
            if working_was_select_hidden is not None:
                working_obj.hide_set(working_was_select_hidden)

        # Force image reload and viewport refresh
        for img in bpy.data.images:
            if mat_name in img.name:
                img.update()

        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        if errors:
            self.report({'WARNING'}, f"Baked: {maps_baked}. Errors: {errors}")
        else:
            self.report({'INFO'}, f"Baked successfully: {', '.join(maps_baked)}")

        nwn2_set_workflow_next_step(context, "substance_handoff")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# PRE-SETUP — Decimation
# ---------------------------------------------------------------------------

class NWN2_OT_PreSetup_Decimate(bpy.types.Operator):
    """Decimate HighPoly_Mesh using PyMeshLab Quadric Edge Collapse"""
    bl_idname = "nwn2.presetup_decimate"
    bl_label = "Decimate & Create Low Poly"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.data.objects.get("HighPoly_Mesh") is not None

    def execute(self, context):
        import site, sys, os, tempfile

        user_site = site.getusersitepackages()
        if user_site not in sys.path:
            sys.path.append(user_site)

        # Ensure user site-packages is in sys.path (needed for Blender's embedded Python)
        import site, importlib
        user_site = site.getusersitepackages()
        if user_site not in sys.path:
            sys.path.append(user_site)
        importlib.invalidate_caches()

        try:
            import pymeshlab
        except ImportError:
            self.report({'INFO'}, "PyMeshLab not found — attempting auto-install...")
            import subprocess
            try:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "pymeshlab"],
                    capture_output=True, check=True
                )
                importlib.invalidate_caches()
                import pymeshlab
                self.report({'INFO'}, "PyMeshLab installed successfully.")
            except Exception as e:
                self.report({'ERROR'}, f"Auto-install failed. Please restart Blender and try again.")
                return {'CANCELLED'}

        hp_obj = bpy.data.objects.get("HighPoly_Mesh")
        if not hp_obj:
            self.report({'ERROR'}, "HighPoly_Mesh not found.")
            return {'CANCELLED'}

        target_faces = context.scene.nwn2_decimate_face_count
        was_hidden = hp_obj.hide_viewport
        hp_obj.hide_viewport = False

        bpy.ops.object.select_all(action='DESELECT')
        hp_obj.select_set(True)
        context.view_layer.objects.active = hp_obj

        tmp_dir = tempfile.gettempdir()
        hp_path = os.path.join(tmp_dir, "nwn2_highpoly_temp.obj")
        lp_path = os.path.join(tmp_dir, "nwn2_lowpoly_temp.obj")

        self.report({'INFO'}, "Decimation in progress — Blender may freeze, this is normal...")

        bpy.ops.wm.obj_export(filepath=hp_path, export_selected_objects=True, export_materials=False)
        hp_obj.hide_viewport = was_hidden

        ms = pymeshlab.MeshSet()
        ms.load_new_mesh(hp_path)
        ms.meshing_decimation_quadric_edge_collapse(
            targetfacenum=target_faces, targetperc=0, qualitythr=0.3,
            preserveboundary=True, boundaryweight=1.0, preservenormal=True,
            preservetopology=True, optimalplacement=True, planarquadric=False,
            planarweight=0.001, qualityweight=False, autoclean=True, selected=False
        )
        ms.save_current_mesh(lp_path)

        existing = bpy.data.objects.get("newModel_Mesh")
        if existing:
            bpy.data.objects.remove(existing, do_unlink=True)

        before = set(bpy.data.objects.keys())
        bpy.ops.wm.obj_import(filepath=lp_path)
        after = set(bpy.data.objects.keys())

        new_objs = [bpy.data.objects[n] for n in (after - before)]
        if not new_objs:
            self.report({'ERROR'}, "Failed to import decimated mesh.")
            return {'CANCELLED'}

        lp_obj = new_objs[0]
        lp_obj.name = "newModel_Mesh"
        lp_obj.data.name = "newModel_Mesh_data"

        for p in [hp_path, lp_path]:
            try:
                os.remove(p)
            except:
                pass

        nwn2_set_workflow_next_step(context, "presetup_uv")
        self.report({'INFO'}, f"Decimated to {len(lp_obj.data.polygons)} faces.")
        return {'FINISHED'}


class NWN2_OT_PreSetup_ResetLowPoly(bpy.types.Operator):
    """Delete newModel_Mesh so decimation can be run again"""
    bl_idname = "nwn2.presetup_reset_lowpoly"
    bl_label = "Reset — Delete Low Poly & Re-Decimate"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        removed = []
        for name in ["newModel_Mesh", "LowPoly_Mesh"]:
            obj = bpy.data.objects.get(name)
            if obj:
                bpy.data.objects.remove(obj, do_unlink=True)
                removed.append(name)
        if removed:
            self.report({'INFO'}, f"Reset: removed {', '.join(removed)}.")
        else:
            self.report({'WARNING'}, "Nothing to reset.")
        nwn2_set_workflow_next_step(context, "presetup_decimate")
        return {'FINISHED'}


class NWN2_OT_LockBakeRef(bpy.types.Operator):
    """Duplicate newModel_Mesh as LowPoly_Mesh and hide it — static bake reference"""
    bl_idname = "nwn2.lock_bake_reference"
    bl_label = "Lock Reference — Duplicate as LowPoly_Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.data.objects.get("newModel_Mesh") is not None

    def execute(self, context):
        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}

        if not mesh_obj.data.uv_layers:
            self.report({'ERROR'}, "newModel_Mesh has no UV map. Run UV unwrap first.")
            return {'CANCELLED'}

        existing = bpy.data.objects.get("LowPoly_Mesh")
        if existing:
            bpy.data.objects.remove(existing, do_unlink=True)

        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj
        bpy.ops.object.duplicate()
        lp_ref = context.active_object
        lp_ref.name = "LowPoly_Mesh"
        lp_ref.data.name = "LowPoly_Mesh_data"
        lp_ref.hide_viewport = True
        lp_ref.hide_render = False

        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj

        nwn2_set_workflow_next_step(context, "step1")
        self.report({'INFO'}, "LowPoly_Mesh created and hidden.")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# PRE-SETUP — Load Starter Scene
# ---------------------------------------------------------------------------

class NWN2_OT_FirstTimeSetupPopup(bpy.types.Operator):
    """First time setup complete popup"""
    bl_idname = "nwn2.first_time_popup"
    bl_label = "Jude's NWN2 Outfit Creator"
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=420)

    def draw(self, context):
        layout = self.layout
        layout.separator()
        col = layout.column()
        col.scale_y = 1.2
        col.label(text="🎉 First-time setup complete!", icon='CHECKMARK')
        col.separator()
        col.label(text="All the thingamaggies and cool stuff have been")
        col.label(text="installed for the first time using this plugin.")
        col.label(text="(PyMeshLab + bundled DDS tools)")
        col.separator()
        col.label(text="⚠  Please restart Blender to activate", icon='ERROR')
        col.label(text="    the decimation tools.")
        layout.separator()


def install_dependencies():
    """Silently install PyMeshLab and download texconv.exe if not already available."""
    import subprocess, sys, site, importlib, os

    # Add user site to path
    user_site = site.getusersitepackages()
    if user_site not in sys.path:
        sys.path.append(user_site)
    importlib.invalidate_caches()

    needs_restart = False

    # Install PyMeshLab if missing
    try:
        import pymeshlab
    except ImportError:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "pymeshlab"],
                capture_output=True, check=True
            )
            needs_restart = True
        except Exception:
            pass

    return needs_restart


class NWN2_OT_PreSetup_LoadStarter(bpy.types.Operator):
    """Append NWN2 starter profile objects from bundled .blend file"""
    bl_idname = "nwn2.presetup_load_starter"
    bl_label = "Load Starter Scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        import os

        addon_dir = os.path.dirname(os.path.abspath(__file__))
        blend_file = os.path.join(addon_dir, "judes_ai_outfit_creator_skels.blend")

        if not os.path.isfile(blend_file):
            self.report({'ERROR'}, f"Starter .blend not found: {blend_file}")
            return {'CANCELLED'}

        # First-time dependency check — install PyMeshLab if missing
        needs_restart = install_dependencies()
        if needs_restart:
            def show_popup():
                bpy.ops.nwn2.first_time_popup('INVOKE_DEFAULT')
                return None
            bpy.app.timers.register(show_popup, first_interval=0.5)

        # Clean up default Blender scene objects (cube, camera, light)
        DEFAULT_OBJECTS = ["Cube", "Camera", "Light"]
        for name in DEFAULT_OBJECTS:
            obj = bpy.data.objects.get(name)
            if obj:
                bpy.data.objects.remove(obj, do_unlink=True)

        # Remove the default "Collection" if empty or only had defaults
        default_col = bpy.data.collections.get("Collection")
        if default_col and len(default_col.objects) == 0:
            bpy.data.collections.remove(default_col)

        # Collections must exist before visibility is restored. On repeated
        # sessions Blender may keep starter objects outside the active view layer.
        def get_or_create_collection(name):
            col = bpy.data.collections.get(name)
            if not col:
                col = bpy.data.collections.new(name)
            if name not in [c.name for c in context.scene.collection.children]:
                context.scene.collection.children.link(col)
            return col

        working_col = get_or_create_collection("NWN2_Working")
        get_or_create_collection("NWN2_Repository")
        get_or_create_collection("NWN2_Export")

        def ensure_in_working_collection(obj):
            if obj.name not in working_col.objects.keys():
                working_col.objects.link(obj)

        def retarget_object_references(old_obj, new_obj):
            for other in bpy.data.objects:
                if other == old_obj:
                    continue

                if other.parent == old_obj:
                    world_matrix = other.matrix_world.copy()
                    parent_type = other.parent_type
                    parent_bone = other.parent_bone
                    other.parent = new_obj
                    other.parent_type = parent_type
                    if parent_type == 'BONE':
                        other.parent_bone = parent_bone
                    other.matrix_world = world_matrix

                for modifier in other.modifiers:
                    if hasattr(modifier, "object") and modifier.object == old_obj:
                        modifier.object = new_obj

                for constraint in other.constraints:
                    if hasattr(constraint, "target") and constraint.target == old_obj:
                        constraint.target = new_obj

        def repair_profile_asset_parenting():
            for profile in NWN2_BODY_PROFILES.values():
                skel = bpy.data.objects.get(profile["skeleton"])
                if not skel:
                    continue

                for role in ("body", "boots", "gloves", "head", "mannequin"):
                    obj = bpy.data.objects.get(profile[role])
                    if not obj:
                        continue

                    if obj.parent is None:
                        world_matrix = obj.matrix_world.copy()
                        obj.parent = skel
                        obj.matrix_world = world_matrix

                    for modifier in obj.modifiers:
                        if modifier.type == 'ARMATURE' and modifier.object is None:
                            modifier.object = skel

        def normalize_starter_duplicates():
            for obj in list(bpy.data.objects):
                if nwn2_object_in_collection_names(obj, {"NWN2_Repository", "NWN2_Export"}):
                    continue

                base_name = nwn2_canonical_profile_asset_name(obj.name)
                if not base_name or obj.name == base_name:
                    continue

                existing = bpy.data.objects.get(base_name)
                if existing and existing != obj:
                    retarget_object_references(obj, existing)
                    bpy.data.objects.remove(obj, do_unlink=True)
                else:
                    obj.name = base_name

            repair_profile_asset_parenting()

        def apply_starter_visibility():
            normalize_starter_duplicates()
            active = nwn2_profile(context)
            active_visible = {
                active["skeleton"],
                active["boots"],
                active["gloves"],
                active["head"],
            }
            always_hidden = {
                profile["body"]
                for profile in NWN2_BODY_PROFILES.values()
            } | {
                profile["mannequin"]
                for profile in NWN2_BODY_PROFILES.values()
            }
            profile_assets = nwn2_profile_asset_names()
            for obj in bpy.data.objects:
                base_name = nwn2_strip_blender_suffix(obj.name)

                if base_name in profile_assets or base_name.startswith("COLS"):
                    ensure_in_working_collection(obj)
                    context.view_layer.update()
                    should_hide = (
                        base_name not in active_visible or
                        base_name in always_hidden or
                        "WeightMannequin" in base_name or
                        base_name.startswith("COLS")
                    )
                    obj.hide_viewport = should_hide
                    obj.hide_render = should_hide
                    nwn2_safe_hide_set(context, obj, should_hide)

            context.view_layer.update()

        # Append only objects that are missing from the scene
        normalize_starter_duplicates()
        with bpy.data.libraries.load(blend_file, link=False) as (data_from, data_to):
            existing_names = {o.name for o in bpy.data.objects}
            data_to.objects = [name for name in data_from.objects if name not in existing_names]

        if not data_to.objects:
            apply_starter_visibility()
            nwn2_set_workflow_next_step(context, "step1")
            self.report({'INFO'}, "All starter objects already in scene.")
            return {'FINISHED'}

        # Link appended objects into NWN2_Working collection
        added = []
        for obj in data_to.objects:
            if obj is not None:
                ensure_in_working_collection(obj)
                added.append(obj.name)

        apply_starter_visibility()
        nwn2_set_workflow_next_step(context, "step1")
        self.report({'INFO'}, f"Starter objects loaded/restored: {len(added)} objects.")
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# PRE-SETUP — Import High Poly
# ---------------------------------------------------------------------------

class NWN2_OT_PreSetup_ImportHighPoly(bpy.types.Operator):
    """Import high poly mesh and rename to HighPoly_Mesh"""
    bl_idname = "nwn2.presetup_import_highpoly"
    bl_label = "Import High Poly Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype='FILE_PATH')
    filter_glob: bpy.props.StringProperty(
        default="*.fbx;*.obj;*.glb;*.gltf;*.dae;*.stl;*.ply;*.abc",
        options={'HIDDEN'}
    )

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        import os
        filepath = self.filepath
        ext = os.path.splitext(filepath)[1].lower()
        before = set(bpy.data.objects.keys())

        try:
            if ext == '.fbx':
                bpy.ops.import_scene.fbx(filepath=filepath)
            elif ext == '.obj':
                bpy.ops.wm.obj_import(filepath=filepath)
            elif ext in ('.glb', '.gltf'):
                bpy.ops.import_scene.gltf(filepath=filepath)
            elif ext == '.dae':
                bpy.ops.wm.collada_import(filepath=filepath)
            elif ext == '.stl':
                bpy.ops.wm.stl_import(filepath=filepath)
            elif ext == '.ply':
                bpy.ops.wm.ply_import(filepath=filepath)
            elif ext == '.abc':
                bpy.ops.wm.alembic_import(filepath=filepath)
            else:
                self.report({'ERROR'}, f"Unsupported format: {ext}")
                return {'CANCELLED'}
        except Exception as e:
            self.report({'ERROR'}, f"Import failed: {e}")
            return {'CANCELLED'}

        after = set(bpy.data.objects.keys())
        new_objs = [bpy.data.objects[n] for n in (after - before) if bpy.data.objects[n].type == 'MESH']

        if not new_objs:
            self.report({'ERROR'}, "No mesh found in imported file.")
            return {'CANCELLED'}

        hp_obj = max(new_objs, key=lambda o: len(o.data.vertices))
        for obj in new_objs:
            if obj != hp_obj:
                bpy.data.objects.remove(obj, do_unlink=True)

        hp_obj.name = "HighPoly_Mesh"
        hp_obj.data.name = "HighPoly_Mesh_data"
        context.scene.nwn2_highpoly_name = "HighPoly_Mesh"

        nwn2_set_workflow_next_step(context, "presetup_decimate")
        self.report({'INFO'}, f"HighPoly_Mesh imported — {len(hp_obj.data.vertices)} verts.")
        return {'FINISHED'}


class NWN2_OT_PreSetup_CreateLowPoly(bpy.types.Operator):
    """Duplicate HighPoly_Mesh as newModel_Mesh"""
    bl_idname = "nwn2.presetup_create_lowpoly"
    bl_label = "Duplicate & Create Low Poly"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        hp_obj = bpy.data.objects.get("HighPoly_Mesh")
        if not hp_obj:
            self.report({'ERROR'}, "HighPoly_Mesh not found.")
            return {'CANCELLED'}

        bpy.ops.object.select_all(action='DESELECT')
        hp_obj.select_set(True)
        context.view_layer.objects.active = hp_obj
        bpy.ops.object.duplicate()
        lp_obj = context.active_object
        lp_obj.name = "newModel_Mesh"
        lp_obj.data.name = "newModel_Mesh_data"
        hp_obj.hide_viewport = True
        hp_obj.hide_render = False

        nwn2_set_workflow_next_step(context, "presetup_uv")
        self.report({'INFO'}, "newModel_Mesh created. HighPoly_Mesh hidden.")
        return {'FINISHED'}


class NWN2_OT_PreSetup_UVUnwrap(bpy.types.Operator):
    """UV Unwrap newModel_Mesh using MinistryOfFlat (UnWrapConsole3.exe)"""
    bl_idname = "nwn2.presetup_uv_unwrap"
    bl_label = "UV Unwrap with MinistryOfFlat"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return bpy.data.objects.get("newModel_Mesh") is not None

    def get_mof_exe(self, context):
        import os
        addon_dir = os.path.dirname(os.path.abspath(__file__))
        bundled = os.path.join(addon_dir, "UnWrapConsole3.exe")
        if os.path.isfile(bundled):
            return bundled
        scene_path = context.scene.nwn2_mof_exe_path.strip()
        if scene_path and os.path.isfile(scene_path):
            return scene_path
        return None

    def execute(self, context):
        import subprocess, os, tempfile, time

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found.")
            return {'CANCELLED'}

        exe = self.get_mof_exe(context)
        if not exe:
            self.report({'ERROR'}, "UnWrapConsole3.exe not found. Set path in panel.")
            return {'CANCELLED'}

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        if not mesh_obj.data.uv_layers:
            mesh_obj.data.uv_layers.new(name="UVMap")

        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj

        tmp_dir = tempfile.gettempdir()
        ts = int(time.time())
        in_path  = os.path.join(tmp_dir, f"nwn2_mof_in_{ts}.obj")
        out_path = os.path.join(tmp_dir, f"nwn2_mof_out_{ts}.obj")

        bpy.ops.wm.obj_export(
            filepath=in_path, export_selected_objects=True,
            export_materials=False, forward_axis='Y', up_axis='Z'
        )

        cmd = [
            exe, in_path, out_path,
            "-RESOLUTION", context.scene.nwn2_mof_resolution,
            "-SEPARATE",   "TRUE" if context.scene.nwn2_mof_separate_hard else "FALSE",
            "-NORMALS",    "TRUE", "-ASPECT", "1.0",
            "-OVERLAP",    "TRUE" if context.scene.nwn2_mof_overlap_identical else "FALSE",
            "-MIRROR",     "TRUE" if context.scene.nwn2_mof_overlap_mirrored else "FALSE",
        ]

        try:
            ret = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
            if ret.returncode != 0 and not (os.path.exists(out_path) and os.path.getsize(out_path) > 0):
                self.report({'ERROR'}, f"MOF failed: {ret.stderr[:300]}")
                return {'CANCELLED'}
        except subprocess.TimeoutExpired:
            self.report({'ERROR'}, "MOF timed out.")
            return {'CANCELLED'}
        except Exception as e:
            self.report({'ERROR'}, f"MOF error: {e}")
            return {'CANCELLED'}

        if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
            self.report({'ERROR'}, "MOF did not produce output.")
            return {'CANCELLED'}

        before = set(bpy.data.objects.keys())
        bpy.ops.wm.obj_import(filepath=out_path, forward_axis='Y', up_axis='Z')
        after  = set(bpy.data.objects.keys())

        new_objs = [bpy.data.objects[n] for n in (after - before) if bpy.data.objects[n].type == 'MESH']
        if not new_objs:
            self.report({'ERROR'}, "Failed to import MOF result.")
            return {'CANCELLED'}

        imported = new_objs[0]

        if imported.data.uv_layers:
            src_uv = imported.data.uv_layers[0]
            while mesh_obj.data.uv_layers:
                mesh_obj.data.uv_layers.remove(mesh_obj.data.uv_layers[0])
            new_uv = mesh_obj.data.uv_layers.new(name="UVMap")
            for i in range(len(mesh_obj.data.loops)):
                if i < len(src_uv.data):
                    new_uv.data[i].uv = src_uv.data[i].uv

        bpy.data.objects.remove(imported, do_unlink=True)

        bpy.ops.object.select_all(action='DESELECT')
        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.pack_islands(margin=0.002)
        bpy.ops.object.mode_set(mode='OBJECT')

        for p in [in_path, out_path]:
            try:
                os.remove(p)
            except:
                pass

        nwn2_set_workflow_next_step(context, "presetup_lock")
        self.report({'INFO'}, "UV unwrap complete. UVMap applied to newModel_Mesh.")
        return {'FINISHED'}




# ---------------------------------------------------------------------------
# STEP 8 — Clean Up, Repository & Export
# ---------------------------------------------------------------------------

class NWN2_OT_ExportSubstanceHandoff(bpy.types.Operator):
    """Export low/high OBJ files and PBR source maps for Substance Painter"""
    bl_idname = "nwn2.export_substance_handoff"
    bl_label = "Export Substance Handoff"
    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(subtype='DIR_PATH')

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def clean_filename(self, name):
        invalid = '<>:"/\\|?*'
        cleaned = ''.join('_' if ch in invalid else ch for ch in name.strip())
        return cleaned or "NWN2_Substance_Handoff"

    def find_image(self, *names):
        for name in names:
            img = bpy.data.images.get(name)
            if img:
                return img
        return None

    def save_image_copy(self, src_img, filepath, colorspace='sRGB', invert_rgb=False, default_rgb=None, size=1024):
        if src_img:
            width, height = src_img.size[0], src_img.size[1]
            pixels = list(src_img.pixels)
        else:
            width = height = size
            rgb = default_rgb if default_rgb else (0.0, 0.0, 0.0)
            pixels = []
            for _ in range(width * height):
                pixels.extend([rgb[0], rgb[1], rgb[2], 1.0])

        if invert_rgb:
            for i in range(0, len(pixels), 4):
                pixels[i] = 1.0 - pixels[i]
                pixels[i + 1] = 1.0 - pixels[i + 1]
                pixels[i + 2] = 1.0 - pixels[i + 2]

        tmp = bpy.data.images.new(
            name="__nwn2_substance_tmp__",
            width=width,
            height=height,
            alpha=True
        )
        tmp.colorspace_settings.name = colorspace
        tmp.pixels = pixels
        tmp.filepath_raw = filepath
        tmp.file_format = 'PNG'
        tmp.save()
        bpy.data.images.remove(tmp)

    def make_export_duplicate(self, src_obj, obj_name, mat_name=None):
        dup = src_obj.copy()
        dup.data = src_obj.data.copy()
        dup.name = obj_name
        dup.data.name = obj_name
        dup.animation_data_clear()
        bpy.context.scene.collection.objects.link(dup)
        dup.hide_viewport = False
        dup.hide_set(False)
        dup.hide_render = False
        dup.parent = None
        dup.matrix_world = src_obj.matrix_world.copy()

        for mod in list(dup.modifiers):
            dup.modifiers.remove(mod)

        if mat_name:
            mat = bpy.data.materials.get(mat_name)
            if not mat:
                mat = bpy.data.materials.new(name=mat_name)
            dup.data.materials.clear()
            dup.data.materials.append(mat)

        return dup

    def export_obj(self, obj, filepath):
        bpy.ops.object.select_all(action='DESELECT')
        obj.hide_viewport = False
        obj.hide_set(False)
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.wm.obj_export(
            filepath=filepath,
            export_selected_objects=True,
            export_materials=True,
            # Substance Painter imports OBJ files as Y-up. Convert from the
            # Blender/NWN2 scene orientation so outfits do not arrive lying down.
            forward_axis='Z',
            up_axis='Y'
        )

    def execute(self, context):
        import os
        nwn2_set_vanilla_body_visible(context, False)
        nwn2_set_vanilla_accessories_visible(context, False)

        mat_name = context.scene.nwn2_material_name.strip()
        if not mat_name:
            self.report({'ERROR'}, "Build/setup the material name before exporting to Substance.")
            return {'CANCELLED'}

        lp_obj = bpy.data.objects.get("LowPoly_Mesh")
        hp_obj = bpy.data.objects.get("HighPoly_Mesh")
        if not lp_obj or not hp_obj:
            self.report({'ERROR'}, "Requires LowPoly_Mesh and HighPoly_Mesh. Export before Step 8 cleanup.")
            return {'CANCELLED'}

        export_root = bpy.path.abspath(self.filepath)
        if not export_root:
            self.report({'ERROR'}, "Choose an export folder.")
            return {'CANCELLED'}

        safe_name = self.clean_filename(mat_name)
        export_dir = os.path.join(export_root, safe_name)
        os.makedirs(export_dir, exist_ok=True)

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        temp_objs = []
        exported = []
        warnings = []

        try:
            low_dup = self.make_export_duplicate(lp_obj, mat_name, mat_name)
            high_dup = self.make_export_duplicate(hp_obj, f"{mat_name}_high", f"{mat_name}_high")
            temp_objs.extend([low_dup, high_dup])

            low_obj_path = os.path.join(export_dir, f"{safe_name}.obj")
            high_obj_path = os.path.join(export_dir, f"{safe_name}_high.obj")
            self.export_obj(low_dup, low_obj_path)
            self.export_obj(high_dup, high_obj_path)
            exported.extend([os.path.basename(low_obj_path), os.path.basename(high_obj_path)])

            d_img = self.find_image(f"{mat_name}_D.png", f"{mat_name}_D")
            if d_img:
                self.save_image_copy(
                    d_img,
                    os.path.join(export_dir, f"{safe_name}_BaseColor.png"),
                    colorspace='sRGB'
                )
                exported.append(f"{safe_name}_BaseColor.png")
            else:
                warnings.append("_D/BaseColor image not found")

            rough_img = self.find_image(f"{mat_name}_R.png", f"{mat_name}_Roughness.png", f"{mat_name}_Roughness")
            if rough_img:
                self.save_image_copy(
                    rough_img,
                    os.path.join(export_dir, f"{safe_name}_Roughness.png"),
                    colorspace='Non-Color'
                )
            else:
                spec_img = self.find_image(f"{mat_name}_S.png", f"{mat_name}_S")
                if spec_img:
                    self.save_image_copy(
                        spec_img,
                        os.path.join(export_dir, f"{safe_name}_Roughness.png"),
                        colorspace='Non-Color',
                        invert_rgb=True
                    )
                    warnings.append("Roughness exported by inverting NWN2 _S/specular")
                else:
                    self.save_image_copy(
                        None,
                        os.path.join(export_dir, f"{safe_name}_Roughness.png"),
                        colorspace='Non-Color',
                        default_rgb=(0.5, 0.5, 0.5),
                        size=int(context.scene.nwn2_bake_resolution)
                    )
                    warnings.append("Roughness missing; wrote neutral 50% roughness")
            exported.append(f"{safe_name}_Roughness.png")

            m_img = self.find_image(f"{mat_name}_M.png", f"{mat_name}_M", f"{mat_name}_Metallic.png", f"{mat_name}_Metallic")
            if m_img:
                self.save_image_copy(
                    m_img,
                    os.path.join(export_dir, f"{safe_name}_Metallic.png"),
                    colorspace='Non-Color'
                )
            else:
                self.save_image_copy(
                    None,
                    os.path.join(export_dir, f"{safe_name}_Metallic.png"),
                    colorspace='Non-Color',
                    default_rgb=(0.0, 0.0, 0.0),
                    size=int(context.scene.nwn2_bake_resolution)
                )
                warnings.append("Metallic missing; wrote black non-metal map")
            exported.append(f"{safe_name}_Metallic.png")

        except Exception as e:
            self.report({'ERROR'}, f"Substance handoff export failed: {e}")
            return {'CANCELLED'}
        finally:
            for obj in temp_objs:
                if obj and obj.name in bpy.data.objects:
                    bpy.data.objects.remove(obj, do_unlink=True)

        msg = f"Substance handoff exported: {', '.join(exported)}"
        if warnings:
            msg += f". Notes: {'; '.join(warnings)}"
            nwn2_set_workflow_next_step(context, "step8_cleanup")
            self.report({'WARNING'}, msg)
        else:
            nwn2_set_workflow_next_step(context, "step8_cleanup")
            self.report({'INFO'}, msg)
        return {'FINISHED'}


class NWN2_OT_Step8_CleanUp(bpy.types.Operator):
    """Remove temp objects and send finished mesh to Repository"""
    bl_idname = "nwn2.step8_cleanup"
    bl_label = "Step 8: Clean Up & Send to Repository"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

    def execute(self, context):
        nwn2_set_vanilla_body_visible(context, False)
        nwn2_set_vanilla_accessories_visible(context, False)
        TEMP_NAMES = list(nwn2_temp_profile_asset_names()) + [
            "Ai_Rig", "HighPoly_Mesh", "LowPoly_Mesh",
            "NWN2_WeightMannequin", "WeightTransfer_Mannequin",
            "Fallback_Mannequin", "NWN2_Fallback_Mannequin",
        ]

        mesh_obj = bpy.data.objects.get("newModel_Mesh")
        if not mesh_obj:
            self.report({'ERROR'}, "newModel_Mesh not found. Complete the workflow first.")
            return {'CANCELLED'}
        nwn2_stamp_profile(mesh_obj, context)

        # Remove temp objects
        for name in TEMP_NAMES:
            obj = bpy.data.objects.get(name)
            if obj:
                bpy.data.objects.remove(obj, do_unlink=True)

        # Remove studio lights
        for obj in list(bpy.data.objects):
            if (
                obj.name.startswith("__studio_light__") or
                obj.name.startswith("__nwn2_weight") or
                "WeightMannequin" in obj.name
            ):
                bpy.data.objects.remove(obj, do_unlink=True)

        # Get collections — create only if missing (should exist from Load Starter)
        def ensure_collection(name):
            col = bpy.data.collections.get(name)
            if not col:
                col = bpy.data.collections.new(name)
                if name not in [c.name for c in context.scene.collection.children]:
                    context.scene.collection.children.link(col)
            return col

        repo_col    = ensure_collection("NWN2_Repository")
        working_col = ensure_collection("NWN2_Working")

        # --- AUTO-FIX: match object name, mesh data name, material name ---
        mat_name = context.scene.nwn2_material_name.strip()
        if mat_name:
            mesh_obj.name = mat_name
            mesh_obj.data.name = mat_name
            if mesh_obj.data.materials:
                mat = mesh_obj.data.materials[0]
                if mat and mat.name != mat_name:
                    mat.name = mat_name

        # Clear parent and armature modifier before sending to Repository
        mesh_obj.parent = None
        for arm_mod in [m for m in mesh_obj.modifiers if m.type == 'ARMATURE']:
            mesh_obj.modifiers.remove(arm_mod)

        # Move from Working to Repository
        if working_col and mesh_obj.name in working_col.objects:
            working_col.objects.unlink(mesh_obj)
        if mesh_obj.name not in repo_col.objects:
            repo_col.objects.link(mesh_obj)

        # Remove from scene root if it ended up there
        if mesh_obj.name in context.scene.collection.objects:
            context.scene.collection.objects.unlink(mesh_obj)

        nwn2_set_workflow_next_step(context, "step8_send_export")
        self.report({'INFO'}, f"'{mesh_obj.name}' cleaned up and sent to Repository.")
        return {'FINISHED'}


class NWN2_OT_Step8_SendToExport(bpy.types.Operator):
    """Move selected Repository mesh to Export slot, send current Export back to Repository"""
    bl_idname = "nwn2.step8_send_to_export"
    bl_label = "Send to Export"
    bl_options = {'REGISTER', 'UNDO'}

    mesh_name: bpy.props.StringProperty()

    def execute(self, context):
        mesh_obj = bpy.data.objects.get(self.mesh_name)
        if not mesh_obj:
            self.report({'ERROR'}, f"'{self.mesh_name}' not found.")
            return {'CANCELLED'}
        nwn2_stamp_profile(mesh_obj, context, nwn2_profile_key(context, mesh_obj))
        target_skel = nwn2_profile_object(context, "skeleton", mesh_obj)
        if not target_skel:
            self.report({'ERROR'}, f"{nwn2_profile(context, mesh_obj)['skeleton']} not found.")
            return {'CANCELLED'}

        def ensure_collection(name):
            col = bpy.data.collections.get(name)
            if not col:
                col = bpy.data.collections.new(name)
                if name not in [c.name for c in context.scene.collection.children]:
                    context.scene.collection.children.link(col)
            return col

        repo_col   = ensure_collection("NWN2_Repository")
        export_col = ensure_collection("NWN2_Export")

        # Send current Export mesh back to Repository
        for obj in list(export_col.objects):
            if obj.type == 'MESH':
                export_col.objects.unlink(obj)
                if obj.name not in repo_col.objects:
                    repo_col.objects.link(obj)
                # Remove armature modifier and unparent
                obj.parent = None
                for m in [mod for mod in obj.modifiers if mod.type == 'ARMATURE']:
                    obj.modifiers.remove(m)

        # Move chosen mesh from Repository to Export
        if mesh_obj.name in repo_col.objects:
            repo_col.objects.unlink(mesh_obj)
        if mesh_obj.name not in export_col.objects:
            export_col.objects.link(mesh_obj)

        # Parent to the stored profile skeleton and add armature modifier
        mesh_obj.parent = target_skel
        has_arm = any(m.type == 'ARMATURE' and m.object == target_skel for m in mesh_obj.modifiers)
        if not has_arm:
            arm_mod = mesh_obj.modifiers.new(name="Armature", type='ARMATURE')
            arm_mod.object = target_skel
            arm_mod.use_vertex_groups = True

        nwn2_set_workflow_next_step(context, "step8_export")
        self.report({'INFO'}, f"'{mesh_obj.name}' sent to Export slot.")
        return {'FINISHED'}


class NWN2_OT_Step8_Export(bpy.types.Operator):
    """Validate and export the mesh in NWN2_Export collection as .mdb"""
    bl_idname = "nwn2.step8_export"
    bl_label = "Export .mdb"
    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(subtype='FILE_PATH')
    filter_glob: bpy.props.StringProperty(default="*.mdb", options={'HIDDEN'})

    def invoke(self, context, event):
        import os

        def clean_filename(name):
            invalid = '<>:"/\\|?*'
            cleaned = ''.join('_' if ch in invalid else ch for ch in name.strip())
            return cleaned or "NWN2_Export"

        def strip_blender_suffix(name):
            while len(name) > 4 and name[-4] == '.' and name[-3:].isdigit():
                name = name[:-4]
            return name

        export_col = bpy.data.collections.get("NWN2_Export")
        mesh_obj = next((o for o in export_col.objects if o.type == 'MESH'), None) if export_col else None

        export_name = ""
        if mesh_obj and mesh_obj.data.materials:
            mat = mesh_obj.data.materials[0]
            export_name = mat.name if mat else ""
        if not export_name and mesh_obj:
            export_name = mesh_obj.name
        if export_name in {"newModel_Mesh", "LowPoly_Mesh", "HighPoly_Mesh"}:
            export_name = context.scene.nwn2_material_name.strip()
        if not export_name and bpy.data.filepath:
            export_name = os.path.splitext(os.path.basename(bpy.data.filepath))[0]
        export_name = clean_filename(strip_blender_suffix(export_name or "NWN2_Export"))

        start_dir = ""
        if self.filepath:
            current_path = bpy.path.abspath(self.filepath)
            start_dir = current_path if os.path.isdir(current_path) else os.path.dirname(current_path)
        if not start_dir:
            start_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else os.path.expanduser("~")

        self.filepath = os.path.join(start_dir, export_name + ".mdb")
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def execute(self, context):
        import os

        def find_image(*names):
            for name in names:
                img = bpy.data.images.get(name)
                if img:
                    return img
            return None

        def resolve_export_dir(path):
            export_dir = bpy.path.abspath(path).strip()
            if not export_dir:
                return ""
            # DIR_PATH usually returns the chosen folder, but normalize both
            # folder paths and accidental file-like paths from the file browser.
            if os.path.isdir(export_dir):
                return os.path.normpath(export_dir)
            if export_dir.endswith((os.sep, os.altsep or os.sep)):
                return os.path.normpath(export_dir)
            if os.path.splitext(export_dir)[1]:
                export_dir = os.path.dirname(export_dir)
            return os.path.normpath(export_dir)

        def strip_blender_suffix(name):
            while len(name) > 4 and name[-4] == '.' and name[-3:].isdigit():
                name = name[:-4]
            return name

        def make_temp_name(id_collection, base_name):
            temp_base = "__nwn2_export_name_conflict_" + base_name
            temp_name = temp_base
            index = 1
            while id_collection.get(temp_name):
                temp_name = f"{temp_base}_{index:03d}"
                index += 1
            return temp_name

        def force_exact_id_name(id_collection, target_id, desired_name):
            if not target_id:
                return
            existing = id_collection.get(desired_name)
            if existing and existing != target_id:
                existing.name = make_temp_name(id_collection, desired_name)
            target_id.name = desired_name

        def hide_export_helpers(target_skel=None):
            for obj in bpy.data.objects:
                if obj.name.startswith("COLS"):
                    obj.hide_viewport = True
                    obj.hide_set(True)
            if target_skel:
                target_skel.hide_viewport = True
                target_skel.hide_set(True)

        export_col = bpy.data.collections.get("NWN2_Export")
        nwn2_set_vanilla_body_visible(context, False)
        nwn2_set_vanilla_accessories_visible(context, False)
        if not export_col:
            self.report({'ERROR'}, "NWN2_Export collection not found.")
            return {'CANCELLED'}

        # Find the outfit mesh in export collection
        mesh_obj = next((o for o in export_col.objects if o.type == 'MESH'), None)
        if not mesh_obj:
            self.report({'ERROR'}, "No mesh found in NWN2_Export collection.")
            return {'CANCELLED'}

        # --- AUTO-FIX: match object name, mesh data name, material name ---
        mat_name = ""
        if mesh_obj.data.materials:
            mat = mesh_obj.data.materials[0]
            mat_name = mat.name if mat else ""
        if not mat_name:
            mat_name = mesh_obj.name
        if mat_name in {"newModel_Mesh", "LowPoly_Mesh", "HighPoly_Mesh"}:
            mat_name = context.scene.nwn2_material_name.strip()
        if not mat_name:
            mat_name = mesh_obj.name
        mat_name = strip_blender_suffix(mat_name)

        force_exact_id_name(bpy.data.objects, mesh_obj, mat_name)
        force_exact_id_name(bpy.data.meshes, mesh_obj.data, mat_name)
        if not mesh_obj.data.materials:
            mesh_obj.data.materials.append(bpy.data.materials.new(mat_name))
        mat = mesh_obj.data.materials[0]
        force_exact_id_name(bpy.data.materials, mat, mat_name)

        if mesh_obj.name != mat_name or mesh_obj.data.name != mat_name or not mat or mat.name != mat_name:
            self.report({'ERROR'}, "Exact MDB names could not be reserved. Check for locked linked data or duplicate names.")
            return {'CANCELLED'}
        nwn2_stamp_profile(mesh_obj, context, nwn2_profile_key(context, mesh_obj))
        target_skel = nwn2_profile_object(context, "skeleton", mesh_obj)
        if not target_skel:
            self.report({'ERROR'}, f"{nwn2_profile(context, mesh_obj)['skeleton']} not found.")
            return {'CANCELLED'}

        # --- SET NWN2 MDK OBJECT TYPE TO SKIN (prevents RIGD export) ---
        if hasattr(mesh_obj, 'nwn2mdk'):
            mesh_obj.nwn2mdk.object_type = 'MESH'

        # --- SET NWN2 MDK MATERIAL TEXTURE MAPS ---
        if mesh_obj.data.materials:
            mat = mesh_obj.data.materials[0]
            if mat and hasattr(mat, 'nwn2mdk'):
                mat.nwn2mdk.diffusemap  = f"{mat_name}_D"
                mat.nwn2mdk.normalmap   = f"{mat_name}_N"

        # --- AUTO-FIX: ensure armature modifier present and not applied ---
        has_arm = any(m.type == 'ARMATURE' and m.object == target_skel for m in mesh_obj.modifiers)
        if not has_arm:
            arm_mod = mesh_obj.modifiers.new(name="Armature", type='ARMATURE')
            arm_mod.object = target_skel
            arm_mod.use_vertex_groups = True

        # --- AUTO-FIX: apply transforms to the export representative only ---
        was_hidden = mesh_obj.hide_viewport
        mesh_obj.hide_viewport = False
        mesh_obj.hide_set(False)
        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj
        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        mesh_obj.hide_viewport = was_hidden
        mesh_obj.select_set(False)

        # --- TEMPORARILY WIRE _D DIRECTLY TO BASE COLOR FOR MDK EXPORT ---
        # The MDK exporter reads texture names from the BSDF Base Color input directly.
        # Our node tree has AO multiply sitting in between, so we bypass it temporarily.
        # We also temporarily rename images to strip .png so MDK writes clean DDS names.
        mat = mesh_obj.data.materials[0] if mesh_obj.data.materials else None
        restore_links = []
        restore_normal_links = []
        renamed_images = []  # track (image, old_name) for restore
        d_export_img = None
        n_export_img = None

        if mat and mat.use_nodes:
            nodes = mat.node_tree.nodes
            links = mat.node_tree.links
            bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
            d_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_D')), None)
            n_node = next((n for n in nodes if n.type == 'TEX_IMAGE' and (n.label or '').endswith('_N')), None)
            d_export_img = d_node.image if d_node else None
            n_export_img = n_node.image if n_node else None
            ao_mix = nodes.get('__ao_multiply__')
            dx_sep = nodes.get('__dx_invert_sep__')
            normal_map_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)

            # Rename images to strip .png extension so MDK writes matname_D not matname_D_png
            for node in [d_node, n_node]:
                if node and node.image and node.image.name.endswith('.png'):
                    old_img_name = node.image.name
                    new_img_name = old_img_name[:-4]  # strip .png
                    node.image.name = new_img_name
                    renamed_images.append((node.image, old_img_name))

            # Bypass AO multiply — wire _D directly to Base Color
            if bsdf and d_node and ao_mix:
                base_color = bsdf.inputs.get('Base Color')
                for lnk in list(base_color.links):
                    restore_links.append((lnk.from_socket, lnk.to_socket))
                    links.remove(lnk)
                links.new(d_node.outputs['Color'], base_color)

            # Bypass DX invert chain — wire _N directly to Normal Map
            if n_node and dx_sep and normal_map_node:
                nm_input = normal_map_node.inputs['Color']
                for lnk in list(nm_input.links):
                    restore_normal_links.append((lnk.from_socket, lnk.to_socket))
                    links.remove(lnk)
                links.new(n_node.outputs['Color'], nm_input)

        # --- FIX UNWEIGHTED VERTICES ---
        # NWN2 MDK refuses to export vertices with zero total weight.
        # Find any unweighted verts and assign them to the nearest bone group.
        unweighted = []
        for vert in mesh_obj.data.vertices:
            total = sum(g.weight for g in vert.groups)
            if total < 0.001:
                unweighted.append(vert.index)

        if unweighted:
            # Find the most-used vertex group as fallback (likely Spine or Ribcage)
            group_usage = {}
            for vert in mesh_obj.data.vertices:
                for g in vert.groups:
                    group_usage[g.group] = group_usage.get(g.group, 0) + g.weight
            if group_usage:
                fallback_group_idx = max(group_usage, key=group_usage.get)
                fallback_vg = mesh_obj.vertex_groups[fallback_group_idx]
                fallback_vg.add(unweighted, 1.0, 'REPLACE')

        # --- LIMIT TOTAL WEIGHTS TO 4 ---
        for obj in context.view_layer.objects:
            obj.select_set(False)
        mesh_obj.hide_viewport = False
        mesh_obj.select_set(True)
        context.view_layer.objects.active = mesh_obj

        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        bpy.ops.object.vertex_group_limit_total(group_select_mode='ALL', limit=4)
        bpy.ops.object.mode_set(mode='OBJECT')

        # --- SELECT ALL OBJECTS FOR EXPORT: mesh + COLS + profile skeleton ---
        for obj in context.view_layer.objects:
            obj.select_set(False)

        # Select only the export representative mesh from NWN2_Export.
        mesh_obj.hide_viewport = False
        mesh_obj.hide_set(False)
        mesh_obj.select_set(True)

        # Also select COLS hierarchy (required by NWN2)
        for obj in bpy.data.objects:
            if obj.name.startswith("COLS"):
                obj.hide_viewport = False
                obj.hide_set(False)
                obj.select_set(True)

        # Also select the matching profile skeleton and keep any other profile
        # skeleton out of the export selection.
        for profile in NWN2_BODY_PROFILES.values():
            skel = bpy.data.objects.get(profile["skeleton"])
            if skel and skel != target_skel:
                skel.select_set(False)
                skel.hide_viewport = True
                skel.hide_set(True)

        target_skel.hide_viewport = False
        target_skel.hide_set(False)
        target_skel.select_set(True)

        export_dir = resolve_export_dir(self.filepath)
        if not export_dir:
            hide_export_helpers(target_skel)
            self.report({'ERROR'}, "Choose an export folder.")
            return {'CANCELLED'}
        os.makedirs(export_dir, exist_ok=True)
        textures_saved = []

        # --- EXPORT TEXTURES (only if checkbox enabled) ---
        if context.scene.nwn2_export_textures:
            import subprocess, tempfile

            addon_dir = os.path.dirname(os.path.abspath(__file__))
            texconv = os.path.join(addon_dir, "texconv.exe")
            has_texconv = os.path.isfile(texconv)

            tmp_dir = tempfile.gettempdir()

            # 1. Build _D with alpha = 1.0 (fully opaque) and save as TGA
            d_img = d_export_img or find_image(f"{mat_name}_D.png", f"{mat_name}_D")
            if d_img:
                try:
                    d_w, d_h = d_img.size[0], d_img.size[1]
                    d_px = list(d_img.pixels)
                    # Force alpha to 1.0
                    d_rgba = []
                    for i in range(0, len(d_px), 4):
                        d_rgba.append(d_px[i])
                        d_rgba.append(d_px[i + 1])
                        d_rgba.append(d_px[i + 2])
                        d_rgba.append(1.0)
                    tmp_d = bpy.data.images.new("__tmp_D__", d_w, d_h, alpha=True)
                    tmp_d.colorspace_settings.name = 'sRGB'
                    tmp_d.pixels = d_rgba
                    d_tga = os.path.join(tmp_dir, f"{mat_name}_D.tga")
                    tmp_d.filepath_raw = d_tga
                    tmp_d.file_format = 'TARGA'
                    tmp_d.save()
                    bpy.data.images.remove(tmp_d)

                    if has_texconv:
                        d_dds = os.path.join(export_dir, f"{mat_name}_D.dds")
                        if os.path.isfile(d_dds):
                            os.remove(d_dds)
                        ret = subprocess.run(
                            [texconv, d_tga, "-f", "BC3_UNORM", "-o", export_dir, "-y", "-nologo"],
                            capture_output=True, text=True
                        )
                        if ret.returncode == 0 and os.path.isfile(d_dds):
                            textures_saved.append(f"{mat_name}_D.dds (DXT5)")
                        else:
                            err = (ret.stderr or ret.stdout or "unknown texconv error").strip()
                            textures_saved.append(f"_D DDS failed: {err[:160]}")
                    else:
                        # Fallback: save TGA if no texconv
                        import shutil
                        shutil.copy(d_tga, os.path.join(export_dir, f"{mat_name}_D.tga"))
                        textures_saved.append(f"{mat_name}_D.tga (texconv not found)")
                except Exception as e:
                    textures_saved.append(f"_D failed: {e}")
            else:
                textures_saved.append(f"_D image not found: expected {mat_name}_D.png")

            # 2. Channel pack _N (RGB) + _S (Alpha) — save as TGA then convert to DDS
            n_img = n_export_img or find_image(f"{mat_name}_N.png", f"{mat_name}_N")
            s_img = find_image(f"{mat_name}_S.png", f"{mat_name}_S")
            if n_img:
                try:
                    n_w, n_h = n_img.size[0], n_img.size[1]
                    n_px = list(n_img.pixels)
                    s_px = list(s_img.pixels) if (s_img and s_img.size[0] == n_w) else None

                    packed = []
                    for i in range(0, len(n_px), 4):
                        packed.append(n_px[i])
                        packed.append(n_px[i + 1])
                        packed.append(n_px[i + 2])
                        packed.append(s_px[i] if s_px else 1.0)  # Specular in alpha

                    tmp_n = bpy.data.images.new("__tmp_N__", n_w, n_h, alpha=True)
                    tmp_n.colorspace_settings.name = 'Non-Color'
                    tmp_n.pixels = packed
                    n_tga = os.path.join(tmp_dir, f"{mat_name}_N.tga")
                    tmp_n.filepath_raw = n_tga
                    tmp_n.file_format = 'TARGA'
                    tmp_n.save()
                    bpy.data.images.remove(tmp_n)

                    if has_texconv:
                        n_dds = os.path.join(export_dir, f"{mat_name}_N.dds")
                        if os.path.isfile(n_dds):
                            os.remove(n_dds)
                        ret = subprocess.run(
                            [texconv, n_tga, "-f", "BC3_UNORM", "-o", export_dir, "-y", "-nologo"],
                            capture_output=True, text=True
                        )
                        if ret.returncode == 0 and os.path.isfile(n_dds):
                            textures_saved.append(f"{mat_name}_N.dds (DXT5 + Specular in Alpha)")
                        else:
                            err = (ret.stderr or ret.stdout or "unknown texconv error").strip()
                            textures_saved.append(f"_N DDS failed: {err[:160]}")
                    else:
                        import shutil
                        shutil.copy(n_tga, os.path.join(export_dir, f"{mat_name}_N.tga"))
                        textures_saved.append(f"{mat_name}_N.tga (texconv not found)")
                except Exception as e:
                    textures_saved.append(f"_N failed: {e}")
            else:
                textures_saved.append(f"_N image not found: expected {mat_name}_N.png")

        # --- EXPORT .MDB ---
        export_path = os.path.join(export_dir, mat_name + ".mdb")
        export_error = None
        try:
            bpy.ops.export_scene.nwn2mdk_mdb(filepath=export_path, use_selection=True)
        except Exception as e:
            export_error = e

        # --- RESTORE NODE LINKS AND IMAGE NAMES AFTER EXPORT ---
        # Restore image names back to .png
        for img, old_name in renamed_images:
            img.name = old_name

        if mat and mat.use_nodes and restore_links:
            nodes = mat.node_tree.nodes
            links = mat.node_tree.links
            bsdf = next((n for n in nodes if n.type == 'BSDF_PRINCIPLED'), None)
            if bsdf:
                base_color = bsdf.inputs.get('Base Color')
                for lnk in list(base_color.links):
                    links.remove(lnk)
                for from_sock, to_sock in restore_links:
                    links.new(from_sock, to_sock)
        if mat and mat.use_nodes and restore_normal_links:
            normal_map_node = next((n for n in mat.node_tree.nodes if n.type == 'NORMAL_MAP'), None)
            if normal_map_node:
                nm_input = normal_map_node.inputs['Color']
                for lnk in list(nm_input.links):
                    mat.node_tree.links.remove(lnk)
                for from_sock, to_sock in restore_normal_links:
                    mat.node_tree.links.new(from_sock, to_sock)

        # Hide COLS and the profile skeleton back after export
        hide_export_helpers(target_skel)

        if export_error:
            self.report({'ERROR'}, f"MDB export failed: {export_error}")
            return {'CANCELLED'}

        if textures_saved:
            self.report({'INFO'}, f"Exported: {mat_name}.mdb + {', '.join(textures_saved)}")
        else:
            self.report({'INFO'}, f"Exported: {mat_name}.mdb (no textures exported).")
        nwn2_set_workflow_next_step(context, "done")
        return {'FINISHED'}

class NWN2_OT_Step8_BatchExportRepository(bpy.types.Operator):
    """Batch export every mesh in NWN2_Repository, one folder per outfit"""
    bl_idname = "nwn2.step8_batch_export_repository"
    bl_label = "Batch Export Repository"
    bl_options = {'REGISTER'}

    filepath: bpy.props.StringProperty(subtype='DIR_PATH')

    def clean_filename(self, name):
        invalid = '<>:"/\\|?*'
        cleaned = ''.join('_' if ch in invalid else ch for ch in name.strip())
        return cleaned or "NWN2_Export"

    def export_name_for_mesh(self, context, mesh_obj):
        mat_name = ""
        if mesh_obj.data.materials:
            mat = mesh_obj.data.materials[0]
            mat_name = mat.name if mat else ""
        if not mat_name:
            mat_name = mesh_obj.name
        if mat_name in {"newModel_Mesh", "LowPoly_Mesh", "HighPoly_Mesh"}:
            mat_name = context.scene.nwn2_material_name.strip()
        if not mat_name:
            mat_name = mesh_obj.name
        return self.clean_filename(nwn2_strip_blender_suffix(mat_name))

    def draw(self, context):
        repo_col = bpy.data.collections.get("NWN2_Repository")
        repo_meshes = [o for o in repo_col.objects if o.type == 'MESH'] if repo_col else []
        count = len(repo_meshes)
        minutes_low = max(1, int((count * 30) / 60)) if count else 0
        minutes_high = max(1, count) if count else 0

        layout = self.layout
        layout.label(text="Batch export may take time.", icon='TIME')
        layout.label(text="Blender may appear busy while MDB files export.")
        layout.label(text="Do not close Blender during processing.")
        if count:
            layout.label(text=f"Repository meshes: {count}")
            layout.label(text=f"Estimated time: about {minutes_low}-{minutes_high} minutes.")
        else:
            layout.label(text="No repository meshes detected.", icon='ERROR')

    def invoke(self, context, event):
        self.filepath = ""
        return context.window_manager.invoke_props_dialog(self, width=520)

    def preflight(self, context, repo_meshes, export_root):
        import os

        errors = []
        warnings = []
        export_names = {}

        if not repo_meshes:
            errors.append("No meshes found in NWN2_Repository.")

        if not any(obj.name.startswith("COLS") for obj in bpy.data.objects):
            errors.append("COLS hierarchy not found.")

        addon_dir = os.path.dirname(os.path.abspath(__file__))
        texconv = os.path.join(addon_dir, "texconv.exe")
        if context.scene.nwn2_export_textures and not os.path.isfile(texconv):
            warnings.append("texconv.exe not found; texture export will fall back to TGA.")

        for mesh_obj in repo_meshes:
            export_name = self.export_name_for_mesh(context, mesh_obj)
            if export_name in export_names:
                errors.append(f"Duplicate export name: {export_name}")
            export_names[export_name] = mesh_obj.name

            profile_key = nwn2_profile_key(context, mesh_obj)
            profile = NWN2_BODY_PROFILES.get(profile_key)
            skel = nwn2_profile_object(context, "skeleton", mesh_obj)
            if not profile or not skel:
                expected = profile["skeleton"] if profile else profile_key
                errors.append(f"{mesh_obj.name}: missing profile skeleton {expected}.")

            if not mesh_obj.data:
                errors.append(f"{mesh_obj.name}: missing mesh data.")
            if not mesh_obj.vertex_groups:
                errors.append(f"{mesh_obj.name}: no vertex groups found.")

            if context.scene.nwn2_export_textures:
                d_img = bpy.data.images.get(f"{export_name}_D.png") or bpy.data.images.get(f"{export_name}_D")
                n_img = bpy.data.images.get(f"{export_name}_N.png") or bpy.data.images.get(f"{export_name}_N")
                if not d_img:
                    warnings.append(f"{export_name}: diffuse image _D not found.")
                if not n_img:
                    warnings.append(f"{export_name}: normal image _N not found.")

            outfit_dir = os.path.join(export_root, export_name)
            if os.path.isfile(outfit_dir):
                errors.append(f"{export_name}: export folder path is blocked by an existing file.")

        return errors, warnings

    def execute(self, context):
        import os

        if not self.filepath:
            start_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else os.path.expanduser("~")
            self.filepath = start_dir
            context.window_manager.fileselect_add(self)
            return {'RUNNING_MODAL'}

        export_root = bpy.path.abspath(self.filepath).strip()
        if os.path.splitext(export_root)[1]:
            export_root = os.path.dirname(export_root)
        export_root = os.path.normpath(export_root)

        repo_col = bpy.data.collections.get("NWN2_Repository")
        export_col = bpy.data.collections.get("NWN2_Export")
        if not repo_col:
            self.report({'ERROR'}, "NWN2_Repository collection not found.")
            return {'CANCELLED'}
        if not export_col:
            export_col = bpy.data.collections.new("NWN2_Export")
            if "NWN2_Export" not in [c.name for c in context.scene.collection.children]:
                context.scene.collection.children.link(export_col)

        repo_meshes = [o for o in repo_col.objects if o.type == 'MESH']
        errors, warnings = self.preflight(context, repo_meshes, export_root)
        if errors:
            self.report({'ERROR'}, "Batch preflight failed: " + " | ".join(errors[:3]))
            return {'CANCELLED'}

        os.makedirs(export_root, exist_ok=True)
        initial_export_meshes = [o for o in export_col.objects if o.type == 'MESH']
        exported = []
        failed = None
        wm = context.window_manager

        def clear_export_slot():
            for obj in list(export_col.objects):
                if obj.type == 'MESH':
                    export_col.objects.unlink(obj)

        def restore_export_slot():
            clear_export_slot()
            for obj in initial_export_meshes:
                if obj.name in bpy.data.objects and obj.name not in export_col.objects.keys():
                    export_col.objects.link(obj)

        try:
            wm.progress_begin(0, len(repo_meshes))
            for index, mesh_obj in enumerate(repo_meshes, start=1):
                wm.progress_update(index - 1)
                export_name = self.export_name_for_mesh(context, mesh_obj)
                outfit_dir = os.path.join(export_root, export_name)
                os.makedirs(outfit_dir, exist_ok=True)

                clear_export_slot()
                if mesh_obj.name not in export_col.objects.keys():
                    export_col.objects.link(mesh_obj)

                try:
                    result = bpy.ops.nwn2.step8_export(filepath=outfit_dir)
                except Exception as exc:
                    failed = f"{export_name}: {exc}"
                    break

                if 'FINISHED' not in result:
                    failed = f"{export_name}: export cancelled or failed"
                    break

                if mesh_obj.name in export_col.objects.keys():
                    export_col.objects.unlink(mesh_obj)
                mesh_obj.parent = None
                for modifier in [m for m in mesh_obj.modifiers if m.type == 'ARMATURE']:
                    mesh_obj.modifiers.remove(modifier)
                mesh_obj.hide_viewport = False
                nwn2_safe_hide_set(context, mesh_obj, False)
                mesh_obj.hide_render = False
                exported.append(export_name)

            wm.progress_update(len(repo_meshes))
        finally:
            wm.progress_end()
            for mesh_obj in repo_meshes:
                if mesh_obj.name not in bpy.data.objects.keys():
                    continue
                if mesh_obj.name in export_col.objects.keys():
                    export_col.objects.unlink(mesh_obj)
                mesh_obj.parent = None
                for modifier in [m for m in mesh_obj.modifiers if m.type == 'ARMATURE']:
                    mesh_obj.modifiers.remove(modifier)
                mesh_obj.hide_viewport = False
                nwn2_safe_hide_set(context, mesh_obj, False)
                mesh_obj.hide_render = False
            restore_export_slot()

        if failed:
            self.report({'ERROR'}, f"Batch stopped after {len(exported)} export(s). {failed}")
            return {'CANCELLED'}

        msg = f"Batch exported {len(exported)} outfit(s) to {export_root}."
        if warnings:
            msg += f" Warnings: {len(warnings)}"
            print("NWN2 batch export warnings:")
            for warning in warnings:
                print(" - " + warning)
        nwn2_set_workflow_next_step(context, "done")
        self.report({'INFO'}, msg)
        return {'FINISHED'}


# ---------------------------------------------------------------------------
# Panel
# ---------------------------------------------------------------------------

class NWN2_OT_PBRPreview(bpy.types.Operator):
    """Toggle Material Preview with 3-light studio setup"""
    bl_idname = "nwn2.pbr_preview"
    bl_label = "View Model with PBR"
    bl_options = {'REGISTER'}

    def execute(self, context):
        import mathutils

        win = context.window
        scr = win.screen
        area_3d = next((a for a in scr.areas if a.type == 'VIEW_3D'), None)
        if not area_3d:
            self.report({'ERROR'}, "No 3D viewport found.")
            return {'CANCELLED'}

        space = next((s for s in area_3d.spaces if s.type == 'VIEW_3D'), None)
        studio_lights_exist = any(o.name.startswith("__studio_light__") for o in bpy.data.objects)

        if studio_lights_exist:
            # Turn off — restore solid, remove lights
            space.shading.type = 'SOLID'
            space.shading.use_scene_lights = False
            for obj in list(bpy.data.objects):
                if obj.name.startswith("__studio_light__"):
                    bpy.data.objects.remove(obj, do_unlink=True)
            # Remove DirectX invert nodes and restore direct connection
            mesh_obj = bpy.data.objects.get("newModel_Mesh")
            if mesh_obj and mesh_obj.data.materials:
                for mat in mesh_obj.data.materials:
                    if not mat or not mat.use_nodes:
                        continue
                    nodes = mat.node_tree.nodes
                    links = mat.node_tree.links
                    sep  = nodes.get('__dx_invert_sep__')
                    inv  = nodes.get('__dx_invert_math__')
                    comb = nodes.get('__dx_invert_comb__')
                    if not (sep and inv and comb):
                        continue
                    # Find the original source (what feeds into sep)
                    if sep.inputs['Color'].links:
                        orig_socket = sep.inputs['Color'].links[0].from_socket
                        normal_map_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
                        if normal_map_node:
                            links.new(orig_socket, normal_map_node.inputs['Color'])
                    nodes.remove(comb)
                    nodes.remove(inv)
                    nodes.remove(sep)

            self.report({'INFO'}, "PBR Preview off.")
        else:
            # Turn on — Material Preview with scene lights and world
            space.shading.type = 'MATERIAL'
            space.shading.use_scene_lights = True
            space.shading.use_scene_world = True

            # Remove any old studio lights
            for obj in list(bpy.data.objects):
                if obj.name.startswith("__studio_light__"):
                    bpy.data.objects.remove(obj, do_unlink=True)

            # Create 3-point studio lights
            scene = bpy.context.scene
            mesh_obj = bpy.data.objects.get("newModel_Mesh")
            center = list(mesh_obj.location) if mesh_obj else [0, 0, 1]

            lights = [
                ("__studio_light__key",  (4, -4, 6),  1200, (1.0, 0.98, 0.95)),
                ("__studio_light__fill", (-4, -3, 3),  400, (0.8, 0.88, 1.0)),
                ("__studio_light__back", (0,  5,  4),  600, (1.0, 0.95, 0.8)),
            ]
            for name, pos, energy, color in lights:
                light_data = bpy.data.lights.new(name=name, type='AREA')
                light_data.energy = energy
                light_data.color = color
                light_data.size = 2.0
                light_obj = bpy.data.objects.new(name=name, object_data=light_data)
                scene.collection.objects.link(light_obj)
                light_obj.location = pos
                direction = mathutils.Vector(center) - mathutils.Vector(pos)
                rot = direction.to_track_quat('-Z', 'Y')
                light_obj.rotation_euler = rot.to_euler()

            # DirectX correction: invert green channel on Normal Map node input
            mesh_obj = bpy.data.objects.get("newModel_Mesh")
            if mesh_obj and mesh_obj.data.materials:
                for mat in mesh_obj.data.materials:
                    if not mat or not mat.use_nodes:
                        continue
                    nodes = mat.node_tree.nodes
                    links = mat.node_tree.links
                    normal_map_node = next((n for n in nodes if n.type == 'NORMAL_MAP'), None)
                    if not normal_map_node:
                        continue
                    # Find what's feeding into the Normal Map Color input
                    nm_input = normal_map_node.inputs['Color']
                    if not nm_input.links:
                        continue
                    source_socket = nm_input.links[0].from_socket
                    # Only add invert if not already there
                    if not any(n.name == '__dx_invert_sep__' for n in nodes):
                        sep = nodes.new('ShaderNodeSeparateColor')
                        sep.name = '__dx_invert_sep__'
                        sep.location = (normal_map_node.location.x - 350, normal_map_node.location.y - 100)
                        inv = nodes.new('ShaderNodeMath')
                        inv.name = '__dx_invert_math__'
                        inv.operation = 'SUBTRACT'
                        inv.inputs[0].default_value = 1.0
                        inv.location = (normal_map_node.location.x - 200, normal_map_node.location.y - 200)
                        comb = nodes.new('ShaderNodeCombineColor')
                        comb.name = '__dx_invert_comb__'
                        comb.location = (normal_map_node.location.x - 50, normal_map_node.location.y - 100)
                        links.new(source_socket, sep.inputs['Color'])
                        links.new(sep.outputs['Red'], comb.inputs['Red'])
                        links.new(sep.outputs['Green'], inv.inputs[1])
                        links.new(inv.outputs['Value'], comb.inputs['Green'])
                        links.new(sep.outputs['Blue'], comb.inputs['Blue'])
                        links.new(comb.outputs['Color'], nm_input)

            self.report({'INFO'}, "PBR Preview on — 3-light studio active.")

        for area in scr.areas:
            area.tag_redraw()

        return {'FINISHED'}

class NWN2_PT_MainPanel(bpy.types.Panel):
    """Main panel for Jude's AI to NwN2 Outfit Creator"""
    bl_label = "Jude's AI to NwN2 Outfit Creator"
    bl_idname = "NWN2_PT_MainPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NWN2 Outfit"

    def draw(self, context):
        layout = self.layout
        next_step = nwn2_workflow_next_step(context)
        next_label = NWN2_WORKFLOW_STEP_LABELS.get(next_step, "Continue Workflow")

        box = layout.box()
        box.label(text="AI Outfit -> NwN2 Workflow", icon='ARMATURE_DATA')
        box.label(text=f"Next: {next_label}", icon='RIGHTARROW')
        pie_row = box.row()
        pie_row.scale_y = 1.4
        pie_row.operator("nwn2.open_workflow_pie", text="Open Workflow Pie (J)", icon='MENU_PANEL')
        layout.separator()

        # --- Pre-Setup (collapsible) ---
        pre_header = layout.row()
        pre_header.prop(
            context.scene, "nwn2_presetup_expanded",
            icon='TRIA_DOWN' if context.scene.nwn2_presetup_expanded else 'TRIA_RIGHT',
            icon_only=True, emboss=False
        )
        pre_header.label(text="Pre-Setup — Import High Poly", icon='IMPORT')

        if context.scene.nwn2_presetup_expanded:
            pre_box = layout.box()

            hp_name = context.scene.nwn2_highpoly_name
            lp_obj  = bpy.data.objects.get("newModel_Mesh")

            if hp_name:
                pre_box.label(text=f"High Poly: {hp_name}", icon='CHECKMARK')
            else:
                pre_box.label(text="Import your high poly AI mesh first.", icon='INFO')

            profile_row = pre_box.row()
            profile_row.label(text="Body Profile:")
            profile_row.prop(context.scene, "nwn2_body_profile", text="")

            # Load starter scene
            starter_loaded = nwn2_profile_object(context, "skeleton") is not None
            if starter_loaded:
                pre_box.label(text="✓ Starter scene loaded.", icon='CHECKMARK')
            else:
                load_row = pre_box.row()
                load_row.alert = True
                load_row.scale_y = 1.5
                load_row.operator("nwn2.presetup_load_starter", icon='APPEND_BLEND')
                pre_box.separator()

            # If references are missing (post-cleanup), show restore button
            refs_missing = any(
                bpy.data.objects.get(n) is None
                for n in [nwn2_profile(context)[role] for role in ("body", "boots", "gloves", "head", "mannequin")]
            )
            if refs_missing and nwn2_profile_object(context, "skeleton"):
                restore_row = pre_box.row()
                restore_row.alert = True
                restore_row.scale_y = 1.3
                restore_row.operator("nwn2.presetup_load_starter", text="↺ Restore References for New Outfit", icon='APPEND_BLEND')
                pre_box.separator()

            import_row = pre_box.row()
            import_row.alert = next_step == "presetup_import_highpoly"
            import_row.operator("nwn2.presetup_import_highpoly", icon='IMPORT')
            pre_box.separator()

            if lp_obj:
                pre_box.label(text="Low Poly: newModel_Mesh ready.", icon='CHECKMARK')
            else:
                pre_box.label(text="Decimate to create low poly mesh.", icon='INFO')

            # Decimation
            dec_box = pre_box.box()
            dec_box.label(text="Quadric Edge Collapse Decimation:", icon='MOD_DECIM')

            if lp_obj:
                warn = dec_box.box()
                warn.label(text="newModel_Mesh already exists!", icon='ERROR')
                warn.label(text="Undo (Ctrl+Z) or reset below before")
                warn.label(text="decimating again to avoid quality loss.")
                dec_box.separator()
                dec_box.operator("nwn2.presetup_reset_lowpoly", icon='TRASH')
            else:
                # Check if PyMeshLab is available
                try:
                    import pymeshlab
                    dec_box.label(text="✓ PyMeshLab ready.", icon='CHECKMARK')
                except ImportError:
                    warn = dec_box.box()
                    warn.label(text="PyMeshLab not installed.", icon='ERROR')
                    warn.label(text="Will auto-install on first Decimate click.")
                    warn.label(text="Requires internet connection.")

                dec_box.label(text="Target Face Count:")
                dec_box.prop(context.scene, "nwn2_decimate_face_count", text="")
                warn_row = dec_box.box()
                warn_row.label(text="⚠ Blender will freeze during this step.", icon='INFO')
                warn_row.label(text="This is normal — hang tight, it's working!")
                dec_row = dec_box.row()
                dec_row.alert = next_step == "presetup_decimate"
                dec_row.enabled = bool(hp_name)
                dec_row.scale_y = 1.3
                dec_row.operator("nwn2.presetup_decimate", icon='MOD_DECIM')

            pre_box.separator()

            # UV Unwrap
            uv_box = pre_box.box()
            uv_box.label(text="UV Unwrap — MinistryOfFlat", icon='UV')

            if lp_obj and lp_obj.data.uv_layers:
                uv_box.label(text="UVMap already applied.", icon='CHECKMARK')
                uv_box.label(text="Re-unwrap will replace existing UVs.")

            import os
            addon_dir = os.path.dirname(os.path.abspath(__file__))
            if os.path.isfile(os.path.join(addon_dir, "UnWrapConsole3.exe")):
                uv_box.label(text="✓ UnWrapConsole3.exe bundled.", icon='CHECKMARK')
            else:
                uv_box.label(text="Dev: set UnWrapConsole3.exe path:", icon='INFO')
                uv_box.prop(context.scene, "nwn2_mof_exe_path", text="")

            uv_box.separator()
            settings_box = uv_box.box()
            settings_box.label(text="Settings:", icon='SETTINGS')
            res_row = settings_box.row()
            res_row.label(text="Resolution:")
            res_row.prop(context.scene, "nwn2_mof_resolution", expand=True)
            settings_box.prop(context.scene, "nwn2_mof_separate_hard")
            settings_box.prop(context.scene, "nwn2_mof_overlap_identical")
            settings_box.prop(context.scene, "nwn2_mof_overlap_mirrored")
            uv_box.separator()
            uv_row = uv_box.row()
            uv_row.alert = next_step == "presetup_uv"
            uv_row.enabled = bool(lp_obj)
            uv_row.scale_y = 1.3
            uv_row.operator("nwn2.presetup_uv_unwrap", icon='UV')

            # Lock Reference
            ref_box = pre_box.box()
            ref_box.label(text="Lock Bake Reference", icon='LOCKED')

            lp_ref = bpy.data.objects.get("LowPoly_Mesh")
            if lp_ref:
                ref_box.label(text="LowPoly_Mesh locked and hidden.", icon='CHECKMARK')
                ref_box.label(text="HighPoly + LowPoly ready for baking.")
                ref_box.label(text="Click below to re-lock if needed.", icon='INFO')
            else:
                ref_box.label(text="Duplicate newModel_Mesh as static", icon='INFO')
                ref_box.label(text="bake reference before proceeding.")

            ref_box.separator()
            lock_row = ref_box.row()
            lock_row.alert = next_step == "presetup_lock"
            lock_row.scale_y = 1.5
            lock_row.operator("nwn2.lock_bake_reference", icon='LOCKED')

        layout.separator()

        # Step 1
        step1_box = layout.box()
        step1_header = step1_box.row()
        step1_header.label(text="Step 1 — Identify AI Mesh", icon='CHECKMARK')
        step1_action = step1_box.row()
        step1_action.alert = next_step == "step1"
        step1_action.operator("nwn2.step1_identify_mesh", icon='OUTLINER_OB_MESH')
        row = step1_box.row()
        row.scale_y = 0.8
        row.operator("nwn2.rotate_mesh_around", icon='FILE_REFRESH')
        dir_row = step1_box.row()
        dir_row.enabled = False
        dir_row.label(text=f"MeshFrontDirection: {context.scene.nwn2_mesh_front_direction}", icon='ORIENTATION_GLOBAL')
        layout.separator()

        # Step 2
        step2_box = layout.box()
        step2_header = step2_box.row()
        step2_header.label(text="Step 2 — Prepare to Rig", icon='CHECKMARK')
        step2_action = step2_box.row()
        step2_action.alert = next_step == "step2"
        step2_action.operator("nwn2.step2_prepare_to_rig", icon='VIEW_CAMERA')
        layout.separator()

        # Step 3
        step3_box = layout.box()
        step3_header = step3_box.row()
        step3_header.label(text="Step 3 — Fit Rig to Mesh", icon='CHECKMARK')
        step3_action = step3_box.row()
        step3_action.alert = next_step == "step3"
        step3_action.operator("nwn2.step3_fit_rig_instructions", icon='QUESTION')

        if context.scene.nwn2_step3_active:
            layout.separator()
            inst_box = layout.box()
            inst_box.label(text="FIT Ai_RIG TO MESH", icon='INFO')
            inst_box.separator()

            a = inst_box.box()
            a.label(text="A — Rig Auto-Scaled", icon='FULLSCREEN_ENTER')
            a.label(text="Ai_Rig scaled to mesh height.")
            a.label(text="Scale resets to (1,1,1) in Step 4.")
            inst_box.separator()

            b = inst_box.box()
            b.label(text="B — Adjust Arms (Pose Mode)", icon='BONE_DATA')
            b.label(text="RED: RArm110 and LArm010 (upper arms).")
            b.label(text="Rotate with R to fit through arm mesh.")
            inst_box.separator()

            c = inst_box.box()
            c.label(text="C — Adjust Legs (Pose Mode)", icon='BONE_DATA')
            c.label(text="YELLOW: RLeg1 and LLeg1 (upper legs).")
            c.label(text="Rotate/move to sit within leg mesh.")
            inst_box.separator()

            d = inst_box.box()
            d.label(text="D — When Done", icon='CHECKMARK')
            d.label(text="Click Done below to auto-weight mesh.")
            inst_box.separator()

            done_row = inst_box.row()
            done_row.alert = next_step == "step3_done"
            done_row.scale_y = 1.5
            done_row.operator("nwn2.step3_done", icon='MOD_ARMATURE')

        layout.separator()

        # Step 4
        step4_box = layout.box()
        step4_header = step4_box.row()
        step4_header.label(text="Step 4 — Restore to NWN2 Scale", icon='CHECKMARK')
        step4_action = step4_box.row()
        step4_action.alert = next_step == "step4"
        step4_action.operator("nwn2.step4_finalize", icon='ARMATURE_DATA')

        # Scale adjustment buttons — visible after step 4
        if bpy.data.objects.get("Ai_Rig") and bpy.data.objects.get("newModel_Mesh"):
            scale_box = step4_box.box()
            scale_box.label(text=f"Scale Adjustment: {context.scene.nwn2_scale_adjustment:.3f}", icon='FULLSCREEN_ENTER')
            scale_row = scale_box.row(align=True)
            scale_row.scale_y = 1.3
            op_down = scale_row.operator("nwn2.step4_scale_adjust", text="- Smaller", icon='REMOVE')
            op_down.direction = -1
            op_up = scale_row.operator("nwn2.step4_scale_adjust", text="+ Bigger", icon='ADD')
            op_up.direction = 1

            shift_box = step4_box.box()
            shift_box.label(text=f"Forward Shift: {context.scene.nwn2_shift_adjustment:.3f}", icon='EMPTY_ARROWS')
            shift_row = shift_box.row(align=True)
            shift_row.scale_y = 1.3
            op_shift_back = shift_row.operator("nwn2.step4_shift_adjust", text="- Shift Back", icon='TRIA_DOWN')
            op_shift_back.direction = -1
            op_shift_fwd = shift_row.operator("nwn2.step4_shift_adjust", text="+ Shift Forward", icon='TRIA_UP')
            op_shift_fwd.direction = 1

            vertical_shift_box = step4_box.box()
            vertical_shift_box.label(text=f"Vertical Shift: {context.scene.nwn2_vertical_shift_adjustment:.3f}", icon='EMPTY_SINGLE_ARROW')
            vertical_shift_row = vertical_shift_box.row(align=True)
            vertical_shift_row.scale_y = 1.3
            op_shift_down = vertical_shift_row.operator("nwn2.step4_vertical_shift_adjust", text="- Shift Down", icon='TRIA_DOWN')
            op_shift_down.direction = -1
            op_shift_up = vertical_shift_row.operator("nwn2.step4_vertical_shift_adjust", text="+ Shift Up", icon='TRIA_UP')
            op_shift_up.direction = 1

            active_profile_key = nwn2_profile_key(context, bpy.data.objects.get("newModel_Mesh"))
            shape_preset = NWN2_PROFILE_SHAPE_PRESETS.get(active_profile_key)
            if shape_preset:
                shape_box = step4_box.box()
                shape_box.label(text=f"Profile Shape: {shape_preset['label']}", icon='OUTLINER_OB_ARMATURE')
                shape_row = shape_box.row(align=True)
                shape_row.scale_y = 1.3
                shape_row.operator("nwn2.step4_profile_shape", text=f"Shape to {active_profile_key}", icon='MOD_ARMATURE')

            # Tilt adjustment
            tilt_box = step4_box.box()
            tilt_box.label(text=f"Tilt Adjustment: {context.scene.nwn2_tilt_adjustment:.1f}°", icon='DRIVER_ROTATIONAL_DIFFERENCE')
            tilt_row = tilt_box.row(align=True)
            tilt_row.scale_y = 1.3
            op_back = tilt_row.operator("nwn2.step4_tilt_adjust", text="- Tilt Back", icon='REMOVE')
            op_back.direction = 1
            op_fwd = tilt_row.operator("nwn2.step4_tilt_adjust", text="+ Tilt Forward", icon='ADD')
            op_fwd.direction = -1
            tilt_box.label(text="You may enter Pose Mode to repose the final output before clicking Done.", icon='INFO')

        layout.separator()

        # Step 5
        step5_box = layout.box()
        step5_header = step5_box.row()
        step5_header.label(text="Step 5 — Final Fitting", icon='CHECKMARK')
        step5_action = step5_box.row()
        step5_action.alert = next_step == "step5"
        step5_action.operator("nwn2.step5_final_fitting", icon='BONE_DATA')
        if context.scene.nwn2_step5_active:
            reset_row = step5_box.row()
            reset_row.operator("nwn2.step5_reset_pose", text="Reset Pose", icon='FILE_REFRESH')

        if context.scene.nwn2_step5_active:
            layout.separator()
            inst_box = layout.box()
            inst_box.label(text="FINAL FITTING", icon='INFO')
            inst_box.separator()

            inst_box.operator("nwn2.step5_action_a", text="A — Scale Arms (S then Y)", icon='FULLSCREEN_ENTER')
            inst_box.operator("nwn2.step5_action_b", text="B — Rotate Arms Right View (R)", icon='FILE_REFRESH')

            c_row = inst_box.row()
            c_row.label(text="C — Arms Individually:")
            c_row = inst_box.row()
            c_row.scale_y = 1.1
            c_row.operator("nwn2.step5_action_c_left", text="◀ Left Arm", icon='TRIA_LEFT')
            c_row.operator("nwn2.step5_action_c_right", text="Right Arm ▶", icon='TRIA_RIGHT')

            e_box = inst_box.box()
            e_box.label(text="D — Align Feet (BLUE bones, global Z):", icon='BONE_DATA')
            lf_row = e_box.row()
            lf_row.label(text="L Foot:")
            op = lf_row.operator("nwn2.step5_foot_rotate", text="◀ 5°", icon='TRIA_LEFT')
            op.bone_name = "LLegAnkle"; op.direction = 1
            op = lf_row.operator("nwn2.step5_foot_rotate", text="5° ▶", icon='TRIA_RIGHT')
            op.bone_name = "LLegAnkle"; op.direction = -1
            rf_row = e_box.row()
            rf_row.label(text="R Foot:")
            op = rf_row.operator("nwn2.step5_foot_rotate", text="◀ 5°", icon='TRIA_LEFT')
            op.bone_name = "RLegAnkle"; op.direction = 1
            op = rf_row.operator("nwn2.step5_foot_rotate", text="5° ▶", icon='TRIA_RIGHT')
            op.bone_name = "RLegAnkle"; op.direction = -1

            inst_box.separator()
            inst_box.operator("nwn2.step5_action_d", text="E — Sculpt / Elastic Deform", icon='SCULPTMODE_HLT')
            vanilla_label = "Hide Vanilla Body" if context.scene.nwn2_show_vanilla_body else "Show Vanilla Body"
            inst_box.operator("nwn2.step5_toggle_vanilla_body", text=vanilla_label, icon='MESH_DATA')
            vanilla_accessories_label = (
                "Hide Vanilla Gloves/Boots"
                if context.scene.nwn2_show_vanilla_accessories
                else "Show Vanilla Gloves/Boots"
            )
            inst_box.operator(
                "nwn2.step5_toggle_vanilla_accessories",
                text=vanilla_accessories_label,
                icon='MESH_DATA'
            )
            inst_box.separator()
            done_row = inst_box.row()
            done_row.alert = next_step == "step5_done"
            done_row.scale_y = 1.5
            done_row.operator("nwn2.step5_done", icon='ARMATURE_DATA')

        layout.separator()

        # Step 6
        step6_box = layout.box()
        step6_header = step6_box.row()
        step6_header.label(text="Step 6 — Material & Shader Setup", icon='CHECKMARK')

        profile_row = step6_box.row()
        profile_row.label(text="Body Profile:")
        profile_row.prop(context.scene, "nwn2_body_profile", text="")

        # Armor Code — dropdown to save space
        armor_row = step6_box.row()
        armor_row.label(text="Armor:")
        armor_row.prop(context.scene, "nwn2_armor_code", text="")

        # Part Type — horizontal radio
        type_row = step6_box.row()
        type_row.label(text="Part:")
        type_row.prop(context.scene, "nwn2_part_type", expand=True)

        # Part Number + Preview on same row
        num_row = step6_box.row()
        num_row.label(text="Number:")
        num_row.prop(context.scene, "nwn2_part_number", text="")

        prev_row = step6_box.row()
        prev_row.enabled = False
        prev_row.label(text=f"Preview: {context.scene.nwn2_material_name}", icon='NODE_MATERIAL')

        step6_box.label(text="① Build name  ② Setup to commit", icon='INFO')

        btn_row = step6_box.row(align=True)
        btn_row.scale_y = 1.3
        build_col = btn_row.column()
        build_col.alert = next_step == "step6_build"
        build_col.operator("nwn2.step6_build_name", icon='FILE_REFRESH')
        setup_col = btn_row.column()
        setup_col.alert = next_step == "step6_setup"
        setup_col.operator("nwn2.step6_setup_material", icon='NODE_MATERIAL')

        layout.separator()

        # Step 7
        step7_box = layout.box()
        step7_header = step7_box.row()
        step7_header.label(text="Step 7 — Bake Maps", icon='CHECKMARK')

        hp_obj = bpy.data.objects.get("HighPoly_Mesh")
        lp_obj_bake = bpy.data.objects.get("LowPoly_Mesh")

        if not hp_obj or not lp_obj_bake:
            step7_box.label(text="Requires HighPoly_Mesh + LowPoly_Mesh.", icon='INFO')
            step7_box.label(text="Complete Pre-Setup first.")
        else:
            step7_box.label(text=f"Source: HighPoly_Mesh → Target: LowPoly_Mesh", icon='CHECKMARK')
            step7_box.separator()

            # Maps to bake
            maps_box = step7_box.box()
            maps_box.label(text="Maps to Bake:", icon='IMAGE_DATA')
            maps_box.prop(context.scene, "nwn2_bake_diffuse",  text="Diffuse / Base Color (_D)")
            maps_box.prop(context.scene, "nwn2_bake_normal",   text="Normal (_N)")
            maps_box.prop(context.scene, "nwn2_bake_metallic",     text="Roughness (Specular Conversion) (_S)")
            maps_box.prop(context.scene, "nwn2_bake_metallic_map", text="Metallic (_M)")
            maps_box.prop(context.scene, "nwn2_bake_ao",           text="Ambient Occlusion (_AO)")

            step7_box.separator()

            # Resolution
            res_row = step7_box.row()
            res_row.label(text="Resolution:")
            res_row.prop(context.scene, "nwn2_bake_resolution", expand=True)

            # Samples
            samp_row = step7_box.row()
            samp_row.label(text="Samples:")
            samp_row.prop(context.scene, "nwn2_bake_samples", text="")

            # Ray distance
            ray_row = step7_box.row()
            ray_row.label(text="Extrusion:")
            ray_row.prop(context.scene, "nwn2_bake_ray_distance", text="")
            max_row = step7_box.row()
            max_row.label(text="Max Ray Dist:")
            max_row.prop(context.scene, "nwn2_bake_max_ray_distance", text="")

            step7_box.separator()
            step7_box.label(text="⚠ Blender will freeze during baking.", icon='INFO')
            step7_box.label(text="Tip: Bake at 4096 for 8x8 AA equivalent,")
            step7_box.label(text="then scale down in image editor.")
            step7_box.label(text="Run Step 6 Setup before baking.")

            bake_row = step7_box.row()
            bake_row.alert = next_step == "step7_bake"
            bake_row.scale_y = 1.5
            bake_row.operator("nwn2.step7_bake", icon='RENDER_STILL')

            step7_box.separator()
            is_pbr = any(
                any(o.name.startswith('__studio_light__') for o in bpy.data.objects)
                for area in context.screen.areas
            )
            pbr_row = step7_box.row()
            pbr_row.scale_y = 1.3
            pbr_row.operator("nwn2.pbr_preview",
                text="Exit PBR Preview" if is_pbr else "View Model with PBR",
                icon='SHADING_RENDERED' if is_pbr else 'SHADING_SOLID')

            step7_box.separator()
            handoff_box = step7_box.box()
            handoff_box.label(text="Substance Painter Handoff:", icon='EXPORT')
            handoff_box.label(text="Export before Step 8 cleanup.", icon='INFO')
            handoff_row = handoff_box.row()
            handoff_row.alert = next_step == "substance_handoff"
            handoff_row.scale_y = 1.3
            handoff_row.operator("nwn2.export_substance_handoff", icon='EXPORT')

        layout.separator()

        # --- Step 8 ---
        step8_box = layout.box()
        step8_box.label(text="Step 8 — Clean Up & Export", icon='EXPORT')

        repo_col   = bpy.data.collections.get("NWN2_Repository")
        export_col = bpy.data.collections.get("NWN2_Export")

        # Clean Up button — always visible
        cleanup_row = step8_box.row()
        cleanup_row.alert = next_step == "step8_cleanup"
        cleanup_row.scale_y = 1.3
        cleanup_row.operator("nwn2.step8_cleanup", icon='TRASH')

        step8_box.separator()

        # Repository list
        step8_box.label(text="Repository:", icon='ASSET_MANAGER')
        repo_meshes = [o for o in repo_col.objects if o.type == 'MESH'] if repo_col else []
        if repo_meshes:
            for obj in repo_meshes:
                row = step8_box.row(align=True)
                row.alert = next_step == "step8_send_export"
                row.label(text=obj.name, icon='MESH_DATA')
                op = row.operator("nwn2.step8_send_to_export", text="Send to Export", icon='EXPORT')
                op.mesh_name = obj.name
            batch_row = step8_box.row()
            batch_row.scale_y = 1.3
            batch_row.operator("nwn2.step8_batch_export_repository", icon='EXPORT')
        else:
            step8_box.label(text="No outfits in Repository yet.", icon='INFO')
            step8_box.label(text="Clean Up a finished mesh above.")

        step8_box.separator()

        # Export slot
        step8_box.label(text="Export Slot:", icon='RENDER_STILL')
        export_meshes = [o for o in export_col.objects if o.type == 'MESH'] if export_col else []
        if export_meshes:
            for obj in export_meshes:
                step8_box.label(text=f"Ready: {obj.name}", icon='CHECKMARK')
            import os
            addon_dir = os.path.dirname(os.path.abspath(__file__))
            texconv_ok = os.path.isfile(os.path.join(addon_dir, "texconv.exe"))
            exp_options = step8_box.row()
            exp_options.prop(context.scene, "nwn2_export_textures", text="Export Textures with .mdb")
            if context.scene.nwn2_export_textures:
                if texconv_ok:
                    step8_box.label(text="✓ texconv ready — DDS DXT5 export", icon='CHECKMARK')
                else:
                    warn = step8_box.box()
                    warn.label(text="texconv.exe not found!", icon='ERROR')
                    warn.label(text="Run Load Starter Scene to auto-download.")
                    warn.label(text="Fallback: TGA will be exported instead.")
            exp_row = step8_box.row()
            exp_row.alert = next_step == "step8_export"
            exp_row.scale_y = 1.5
            exp_row.operator("nwn2.step8_export", icon='EXPORT')
        else:
            step8_box.label(text="No outfit in Export slot.", icon='INFO')
            step8_box.label(text="Send one from Repository above.")


# ---------------------------------------------------------------------------
# PIE MENUS — Workflow Navigation (Nested)
# ---------------------------------------------------------------------------

addon_keymaps = []


def pie_call(pie, menu_id, text, icon='NONE'):
    op = pie.operator("wm.call_menu_pie", text=text, icon=icon)
    op.name = menu_id
    return op


class NWN2_OT_OpenWorkflowPie(bpy.types.Operator):
    """Open Jude's NWN2 Outfit workflow pie menu"""
    bl_idname = "nwn2.open_workflow_pie"
    bl_label = "Open NWN2 Workflow Pie"
    bl_options = {'REGISTER'}

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="NWN2_MT_WorkflowPie")
        return {'FINISHED'}


class NWN2_MT_WorkflowPie(bpy.types.Menu):
    bl_label = "Jude NWN2 Outfit Workflow"
    bl_idname = "NWN2_MT_WorkflowPie"

    def draw(self, context):
        pie = self.layout.menu_pie()

        pie_call(pie, "NWN2_MT_PreSetupPie", "Pre-Setup", 'IMPORT')
        pie_call(pie, "NWN2_MT_Step1Pie", "Step 1: Identify Mesh", 'OUTLINER_OB_MESH')
        pie_call(pie, "NWN2_MT_Step2Pie", "Step 2: Prepare Rig", 'ARMATURE_DATA')
        pie_call(pie, "NWN2_MT_Step3Pie", "Step 3: Fit / Weight", 'MOD_ARMATURE')
        pie_call(pie, "NWN2_MT_Step4Pie", "Step 4: Restore Scale", 'FULLSCREEN_EXIT')
        pie_call(pie, "NWN2_MT_Step5Pie", "Step 5: Final Fit", 'BONE_DATA')
        pie_call(pie, "NWN2_MT_Step6Pie", "Step 6: Material", 'MATERIAL')
        pie_call(pie, "NWN2_MT_Step7Pie", "Step 7: Bake / Preview", 'RENDER_STILL')
        pie_call(pie, "NWN2_MT_Step8Pie", "Step 8: Clean Up / Export", 'EXPORT')


class NWN2_MT_PreSetupPie(bpy.types.Menu):
    bl_label = "Pre-Setup"
    bl_idname = "NWN2_MT_PreSetupPie"

    def draw(self, context):
        pie = self.layout.menu_pie()

        pie.operator("nwn2.presetup_load_starter", text="Load Starter Scene", icon='APPEND_BLEND')
        pie.operator("nwn2.presetup_import_highpoly", text="Import High Poly", icon='IMPORT')
        pie.operator("nwn2.presetup_decimate", text="PyMeshLab Decimate", icon='MOD_DECIM')

        box = pie.box()
        box.label(text="Target Faces", icon='MOD_DECIM')
        box.prop(context.scene, "nwn2_decimate_face_count", text="")

        pie.operator("nwn2.presetup_uv_unwrap", text="UV Unwrap MOF", icon='UV')
        pie.operator("nwn2.lock_bake_reference", text="Lock LowPoly Ref", icon='LOCKED')
        pie.operator("nwn2.presetup_reset_lowpoly", text="Reset LowPoly", icon='TRASH')
        pie.operator("nwn2.presetup_create_lowpoly", text="Duplicate Low Poly", icon='DUPLICATE')
        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')


class NWN2_MT_Step1Pie(bpy.types.Menu):
    bl_label = "Step 1: Identify Mesh"
    bl_idname = "NWN2_MT_Step1Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step1_identify_mesh", text="Identify AI Mesh", icon='OUTLINER_OB_MESH')
        pie.operator("nwn2.rotate_mesh_around", text="Rotate 90°", icon='FILE_REFRESH')

        box = pie.box()
        box.label(text="Front Direction", icon='ORIENTATION_GLOBAL')
        box.label(text=context.scene.nwn2_mesh_front_direction)

        info = pie.box()
        info.label(text="Tip", icon='INFO')
        info.label(text="Use rotate until the mesh")
        info.label(text="faces the correct direction")

        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')


class NWN2_MT_Step2Pie(bpy.types.Menu):
    bl_label = "Step 2: Prepare Rig"
    bl_idname = "NWN2_MT_Step2Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step2_prepare_to_rig", text="Prepare to Rig", icon='ARMATURE_DATA')
        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')

        info = pie.box()
        info.label(text="What this does", icon='INFO')
        info.label(text="• Back ortho view")
        info.label(text="• Duplicates selected profile skeleton")
        info.label(text="• Builds Ai_Rig")
        info.label(text="• Saves a rig snapshot")


class NWN2_MT_Step3Pie(bpy.types.Menu):
    bl_label = "Step 3: Fit Rig / Auto Weight"
    bl_idname = "NWN2_MT_Step3Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step3_fit_rig_instructions", text="Fit Rig to Mesh", icon='QUESTION')
        pie.operator("nwn2.step3_done", text="Done: Auto Weight", icon='MOD_ARMATURE')

        info = pie.box()
        info.label(text="After Fit Rig", icon='INFO')
        info.label(text="Adjust bones in Pose Mode")
        info.label(text="then choose Done")

        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')


class NWN2_MT_Step4Pie(bpy.types.Menu):
    bl_label = "Step 4: Restore to NWN2 Scale"
    bl_idname = "NWN2_MT_Step4Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step4_finalize", text="Restore to NWN2 Scale", icon='FULLSCREEN_EXIT')
        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')

        info = pie.box()
        info.label(text="What this does", icon='INFO')
        info.label(text="• Restores original rig scale")
        info.label(text="• Reapplies stored pose offsets")
        info.label(text="• Shows selected profile skeleton")


class NWN2_MT_Step5Pie(bpy.types.Menu):
    bl_label = "Step 5: Final Fitting"
    bl_idname = "NWN2_MT_Step5Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step5_final_fitting", text="Start Final Fitting", icon='BONE_DATA')
        pie.operator("nwn2.step5_action_a", text="A: Scale Arms", icon='MOD_ARMATURE')
        pie.operator("nwn2.step5_action_b", text="B: Rotate Arms Right View", icon='DRIVER_ROTATIONAL_DIFFERENCE')
        pie.operator("nwn2.step5_action_c_left", text="C: Left Arm Only", icon='TRIA_LEFT')
        pie.operator("nwn2.step5_action_c_right", text="C: Right Arm Only", icon='TRIA_RIGHT')
        pie_call(pie, "NWN2_MT_Step5FootPie", "D: Align Feet", 'MOD_ARMATURE')
        pie.operator("nwn2.step5_action_d", text="E: Sculpt Elastic Deform", icon='SCULPTMODE_HLT')
        pie.operator("nwn2.step5_done", text="Done: Attach to Game Skeleton", icon='CHECKMARK')


class NWN2_MT_Step5FootPie(bpy.types.Menu):
    bl_label = "Step 5: Foot Rotation"
    bl_idname = "NWN2_MT_Step5FootPie"

    def draw(self, context):
        pie = self.layout.menu_pie()

        op = pie.operator("nwn2.step5_foot_rotate", text="Left Foot +5°", icon='FILE_REFRESH')
        op.bone_name = "LLegAnkle"
        op.direction = 1

        op = pie.operator("nwn2.step5_foot_rotate", text="Left Foot -5°", icon='FILE_REFRESH')
        op.bone_name = "LLegAnkle"
        op.direction = -1

        op = pie.operator("nwn2.step5_foot_rotate", text="Right Foot +5°", icon='FILE_REFRESH')
        op.bone_name = "RLegAnkle"
        op.direction = 1

        op = pie.operator("nwn2.step5_foot_rotate", text="Right Foot -5°", icon='FILE_REFRESH')
        op.bone_name = "RLegAnkle"
        op.direction = -1

        pie.operator("nwn2.step5_reset_pose", text="Reset Step 5 Pose", icon='LOOP_BACK')
        pie_call(pie, "NWN2_MT_Step5Pie", "Back to Step 5", 'BACK')

        info = pie.box()
        info.label(text="Foot Tips", icon='INFO')
        info.label(text="Use small increments")
        info.label(text="while checking deforms")


class NWN2_MT_Step6Pie(bpy.types.Menu):
    bl_label = "Step 6: Material / Shader"
    bl_idname = "NWN2_MT_Step6Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step6_build_name", text="Build Material Name", icon='FILE_TEXT')
        pie.operator("nwn2.step6_setup_material", text="Setup Material", icon='MATERIAL')

        name_box = pie.box()
        name_box.label(text="Material Name", icon='FILE_TEXT')
        name_box.prop(context.scene, "nwn2_material_name", text="")

        pie.operator("nwn2.pbr_preview", text="Toggle PBR Preview", icon='SHADING_RENDERED')

        profile_box = pie.box()
        profile_box.label(text="Body Profile", icon='ARMATURE_DATA')
        profile_box.prop(context.scene, "nwn2_body_profile", text="")

        part_box = pie.box()
        part_box.label(text="Part / Number", icon='OUTLINER_OB_MESH')
        part_box.prop(context.scene, "nwn2_part_type", text="")
        part_box.prop(context.scene, "nwn2_part_number", text="No.")

        armor_box = pie.box()
        armor_box.label(text="Armor", icon='MATERIAL')
        armor_box.prop(context.scene, "nwn2_armor_code", text="")

        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')


class NWN2_MT_Step7Pie(bpy.types.Menu):
    bl_label = "Step 7: Bake / Preview"
    bl_idname = "NWN2_MT_Step7Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step7_bake", text="Bake Maps", icon='RENDER_STILL')
        pie.operator("nwn2.export_substance_handoff", text="Export Substance Handoff", icon='EXPORT')
        pie.operator("nwn2.pbr_preview", text="Toggle PBR Preview", icon='SHADING_RENDERED')

        map_box = pie.box()
        map_box.label(text="Maps", icon='IMAGE_DATA')
        map_box.prop(context.scene, "nwn2_bake_diffuse", text="Diffuse")
        map_box.prop(context.scene, "nwn2_bake_normal", text="Normal")
        map_box.prop(context.scene, "nwn2_bake_metallic", text="Roughness (Specular)")
        map_box.prop(context.scene, "nwn2_bake_ao", text="AO")

        res_box = pie.box()
        res_box.label(text="Bake Resolution", icon='IMAGE_DATA')
        res_box.prop(context.scene, "nwn2_bake_resolution", text="")

        samples_box = pie.box()
        samples_box.label(text="Samples", icon='SETTINGS')
        samples_box.prop(context.scene, "nwn2_bake_samples", text="")

        ray_box = pie.box()
        ray_box.label(text="Ray Settings", icon='SETTINGS')
        ray_box.prop(context.scene, "nwn2_bake_ray_distance", text="Extrusion")
        ray_box.prop(context.scene, "nwn2_bake_max_ray_distance", text="Max")

        pie.operator("nwn2.step6_setup_material", text="Setup Material First", icon='MATERIAL')
        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')

class NWN2_MT_Step8Pie(bpy.types.Menu):
    bl_label = "Step 8: Clean Up / Export"
    bl_idname = "NWN2_MT_Step8Pie"

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator("nwn2.step8_cleanup", text="Clean Up & Send to Repo", icon='TRASH')
        pie.operator("nwn2.step8_export", text="Export .mdb", icon='EXPORT')
        pie.operator("nwn2.step8_batch_export_repository", text="Batch Export Repo", icon='EXPORT')
        info = pie.box()
        info.label(text="Repository", icon='ASSET_MANAGER')
        repo_col = bpy.data.collections.get("NWN2_Repository")
        if repo_col:
            for obj in repo_col.objects:
                if obj.type == 'MESH':
                    op = info.operator("nwn2.step8_send_to_export", text=obj.name, icon='MESH_DATA')
                    op.mesh_name = obj.name
        else:
            info.label(text="Empty")
        pie_call(pie, "NWN2_MT_WorkflowPie", "Back to Main", 'BACK')


classes = (
    NWN2_OT_Step1_IdentifyMesh,
    NWN2_OT_RotateMeshAround,
    NWN2_OT_Step2_PrepareToRig,
    NWN2_OT_Step3_FitRigInstructions,
    NWN2_OT_Step3_Done,
    NWN2_OT_Step4_Finalize,
    NWN2_OT_Step4_TiltAdjust,
    NWN2_OT_Step4_ScaleAdjust,
    NWN2_OT_Step4_ShiftAdjust,
    NWN2_OT_Step4_VerticalShiftAdjust,
    NWN2_OT_Step4_ProfileShape,
    NWN2_OT_Step5_FinalFitting,
    NWN2_OT_Step5_ToggleVanillaBody,
    NWN2_OT_Step5_ToggleVanillaAccessories,
    NWN2_OT_Step5_ResetPose,
    NWN2_OT_Step5_ActionA,
    NWN2_OT_Step5_ActionB,
    NWN2_OT_Step5_ActionC_Left,
    NWN2_OT_Step5_ActionC_Right,
    NWN2_OT_Step5_ActionD,
    NWN2_OT_Step5_FootRotate,
    NWN2_OT_Step5_Done,
    NWN2_OT_Step6_SetupMaterial,
    NWN2_OT_Step6_BuildName,
    NWN2_OT_Step7_Bake,
    NWN2_OT_ExportSubstanceHandoff,
    NWN2_OT_PBRPreview,
    NWN2_OT_FirstTimeSetupPopup,
    NWN2_OT_PreSetup_LoadStarter,
    NWN2_OT_PreSetup_Decimate,
    NWN2_OT_PreSetup_ResetLowPoly,
    NWN2_OT_LockBakeRef,
    NWN2_OT_PreSetup_ImportHighPoly,
    NWN2_OT_PreSetup_CreateLowPoly,
    NWN2_OT_PreSetup_UVUnwrap,
    NWN2_OT_Step8_CleanUp,
    NWN2_OT_Step8_SendToExport,
    NWN2_OT_Step8_Export,
    NWN2_OT_Step8_BatchExportRepository,
    NWN2_OT_OpenWorkflowPie,
    NWN2_MT_WorkflowPie,
    NWN2_MT_PreSetupPie,
    NWN2_MT_Step1Pie,
    NWN2_MT_Step2Pie,
    NWN2_MT_Step3Pie,
    NWN2_MT_Step4Pie,
    NWN2_MT_Step5Pie,
    NWN2_MT_Step5FootPie,
    NWN2_MT_Step6Pie,
    NWN2_MT_Step7Pie,
    NWN2_MT_Step8Pie,
    NWN2_PT_MainPanel,
)


def register():
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except Exception as e:
            print(f"REGISTER ERROR for {cls.__name__}: {e}")

    bpy.types.Scene.nwn2_mesh_rotation_steps = bpy.props.IntProperty(name="NWN2 Mesh Rotation Steps", default=0)
    bpy.types.Scene.nwn2_presetup_expanded = bpy.props.BoolProperty(name="Pre-Setup Expanded", default=True)
    bpy.types.Scene.nwn2_mesh_front_direction = bpy.props.StringProperty(name="NWN2 Mesh Front Direction", default="N/A")
    bpy.types.Scene.nwn2_workflow_next_step = bpy.props.StringProperty(name="NWN2 Workflow Next Step", default="")
    bpy.types.Scene.nwn2_step3_active = bpy.props.BoolProperty(name="NWN2 Step 3 Active", default=False)
    bpy.types.Scene.nwn2_step5_active = bpy.props.BoolProperty(name="NWN2 Step 5 Active", default=False)
    bpy.types.Scene.nwn2_show_vanilla_body = bpy.props.BoolProperty(name="Show Vanilla Body", default=False)
    bpy.types.Scene.nwn2_show_vanilla_accessories = bpy.props.BoolProperty(name="Show Vanilla Gloves/Boots", default=False)
    bpy.types.Scene.nwn2_body_profile = bpy.props.EnumProperty(
        name="Body Profile",
        description="Select the NWN2 body skeleton/reference set for rigging and export",
        items=NWN2_BODY_PROFILE_ITEMS,
        default="HHM"
    )
    bpy.types.Scene.nwn2_tilt_adjustment = bpy.props.FloatProperty(
        name="Tilt Adjustment",
        description="Forward tilt in degrees",
        default=0.0
    )
    bpy.types.Scene.nwn2_scale_adjustment = bpy.props.FloatProperty(
        name="Scale Adjustment",
        description="Fine-tune mesh scale after restoring to NWN2 scale. 1.0 = default.",
        default=1.0, min=0.5, max=2.0, step=1, precision=3
    )
    bpy.types.Scene.nwn2_shift_adjustment = bpy.props.FloatProperty(
        name="Forward Shift",
        description="Fine-tune whole fitted rig forward/backward after restoring to NWN2 scale",
        default=0.0, min=-1.0, max=1.0, step=1, precision=3
    )
    bpy.types.Scene.nwn2_vertical_shift_adjustment = bpy.props.FloatProperty(
        name="Vertical Shift",
        description="Fine-tune whole fitted rig up/down after restoring to NWN2 scale",
        default=0.0, min=-1.0, max=1.0, step=1, precision=3
    )
    bpy.types.Scene.nwn2_ai_rig_snapshot = bpy.props.StringProperty(name="NWN2 Ai_Rig Snapshot", default="")
    bpy.types.Scene.nwn2_pose_snapshot = bpy.props.StringProperty(name="NWN2 Pose Snapshot", default="")
    bpy.types.Scene.nwn2_step5_snapshot = bpy.props.StringProperty(name="NWN2 Step5 Snapshot", default="")
    bpy.types.Scene.nwn2_material_name = bpy.props.StringProperty(name="NWN2 Material Name", default="P_HHM_CL_Body120")
    bpy.types.Scene.nwn2_sex = bpy.props.EnumProperty(name="Sex", items=[('M', 'Male', ''), ('F', 'Female', '')], default='M')
    bpy.types.Scene.nwn2_race_human    = bpy.props.BoolProperty(name="Human",    default=True)
    bpy.types.Scene.nwn2_race_elf      = bpy.props.BoolProperty(name="Elf",      default=False)
    bpy.types.Scene.nwn2_race_halforc  = bpy.props.BoolProperty(name="Half-Orc", default=False)
    bpy.types.Scene.nwn2_race_gnome    = bpy.props.BoolProperty(name="Gnome",    default=False)
    bpy.types.Scene.nwn2_race_dwarf    = bpy.props.BoolProperty(name="Dwarf",    default=False)
    bpy.types.Scene.nwn2_race_halfelf  = bpy.props.BoolProperty(name="Half-Elf", default=False)
    bpy.types.Scene.nwn2_race_drow     = bpy.props.BoolProperty(name="Drow",     default=False)
    bpy.types.Scene.nwn2_race_halfling = bpy.props.BoolProperty(name="Halfling", default=False)
    bpy.types.Scene.nwn2_race_tiefling = bpy.props.BoolProperty(name="Tiefling", default=False)
    bpy.types.Scene.nwn2_armor_code = bpy.props.EnumProperty(
        name="Armor Code",
        items=[
            ('CL', 'Cloth (CL)', ''), ('CP', 'Cloth Padded (CP)', ''),
            ('LE', 'Leather (LE)', ''), ('LS', 'Leather Studded (LS)', ''),
            ('CH', 'Chain (CH)', ''), ('SC', 'Scale (SC)', ''),
            ('BA', 'Banded (BA)', ''), ('PH', 'Half Plate (PH)', ''),
            ('PF', 'Full Plate (PF)', ''), ('HD', 'Hide (HD)', ''),
            ('NK', 'Naked (NK)', ''),
        ],
        default='CL'
    )
    bpy.types.Scene.nwn2_part_type = bpy.props.EnumProperty(
        name="Part Type",
        items=[
            ('Body', 'Body', ''), ('Helm', 'Helm', ''), ('Gloves', 'Gloves', ''),
            ('Boots', 'Boots', ''), ('Belt', 'Belt', ''), ('Cloak', 'Cloak', ''),
        ],
        default='Body'
    )
    bpy.types.Scene.nwn2_part_number = bpy.props.StringProperty(name="Part Number", default="120")
    bpy.types.Scene.nwn2_highpoly_name = bpy.props.StringProperty(name="NWN2 High Poly Name", default="")
    bpy.types.Scene.nwn2_decimate_face_count = bpy.props.IntProperty(name="Target Face Count", default=25000, min=100, max=500000)
    bpy.types.Scene.nwn2_mof_exe_path = bpy.props.StringProperty(name="MOF Exe Path", default="", subtype='FILE_PATH')
    bpy.types.Scene.nwn2_mof_resolution = bpy.props.EnumProperty(
        name="Texture Resolution",
        items=[('512', '512', ''), ('1024', '1024', ''), ('2048', '2048', ''), ('4096', '4096', '')],
        default='1024'
    )
    bpy.types.Scene.nwn2_mof_separate_hard = bpy.props.BoolProperty(name="Separate Hard Edges", default=True)
    bpy.types.Scene.nwn2_bake_samples = bpy.props.IntProperty(
        name="Bake Samples",
        description="Cycles samples — higher = better quality. 512+ recommended for final bakes",
        default=512,
        min=1,
        max=4096
    )
    bpy.types.Scene.nwn2_bake_diffuse = bpy.props.BoolProperty(name="Bake Diffuse", default=True)
    bpy.types.Scene.nwn2_bake_normal = bpy.props.BoolProperty(name="Bake Normal", default=True)
    bpy.types.Scene.nwn2_bake_metallic = bpy.props.BoolProperty(name="Bake Roughness Specular", default=True)
    bpy.types.Scene.nwn2_bake_metallic_map = bpy.props.BoolProperty(name="Bake Metallic", default=False)
    bpy.types.Scene.nwn2_bake_ao = bpy.props.BoolProperty(name="Bake AO", default=False)
    bpy.types.Scene.nwn2_export_textures = bpy.props.BoolProperty(
        name="Export Textures",
        description="Save baked texture files to export folder alongside the .mdb",
        default=True
    )
    bpy.types.Scene.nwn2_bake_resolution = bpy.props.EnumProperty(
        name="Bake Resolution",
        items=[('512','512',''),('1024','1024',''),('2048','2048',''),('4096','4096','')],
        default='2048'
    )
    bpy.types.Scene.nwn2_bake_ray_distance = bpy.props.FloatProperty(
        name="Extrusion",
        description="Cage extrusion — Substance Designer default is 0.01",
        default=0.01,
        min=0.0,
        max=1.0,
        step=1,
        precision=3
    )
    bpy.types.Scene.nwn2_bake_max_ray_distance = bpy.props.FloatProperty(
        name="Max Ray Distance",
        description="Max ray distance — 0 means unlimited",
        default=0.0,
        min=0.0,
        max=1.0,
        step=1,
        precision=3
    )
    bpy.types.Scene.nwn2_mof_overlap_identical = bpy.props.BoolProperty(name="Overlap Identical Parts", default=False)
    bpy.types.Scene.nwn2_mof_overlap_mirrored = bpy.props.BoolProperty(name="Overlap Mirrored Parts", default=False)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')
        kmi = km.keymap_items.new(
            "wm.call_menu_pie",
            type='J',
            value='PRESS',
        )
        kmi.properties.name = "NWN2_MT_WorkflowPie"
        addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except Exception:
            pass
    addon_keymaps.clear()

    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except:
            pass
    for prop in [
        'nwn2_mesh_rotation_steps', 'nwn2_presetup_expanded', 'nwn2_mesh_front_direction',
        'nwn2_workflow_next_step',
        'nwn2_step3_active', 'nwn2_step5_active', 'nwn2_show_vanilla_body',
        'nwn2_show_vanilla_accessories', 'nwn2_body_profile',
        'nwn2_ai_rig_snapshot', 'nwn2_pose_snapshot', 'nwn2_step5_snapshot',
        'nwn2_material_name', 'nwn2_sex',
        'nwn2_race_human', 'nwn2_race_elf', 'nwn2_race_halforc',
        'nwn2_race_gnome', 'nwn2_race_dwarf', 'nwn2_race_halfelf',
        'nwn2_race_drow', 'nwn2_race_halfling', 'nwn2_race_tiefling',
        'nwn2_armor_code', 'nwn2_part_type', 'nwn2_part_number',
        'nwn2_highpoly_name', 'nwn2_decimate_face_count',
        'nwn2_mof_exe_path', 'nwn2_mof_resolution',
        'nwn2_mof_separate_hard', 'nwn2_mof_overlap_identical',
        'nwn2_mof_overlap_mirrored',
        'nwn2_bake_diffuse', 'nwn2_bake_normal', 'nwn2_bake_metallic', 'nwn2_bake_ao',
        'nwn2_bake_metallic_map', 'nwn2_export_textures',
        'nwn2_tilt_adjustment',
        'nwn2_scale_adjustment',
        'nwn2_shift_adjustment',
        'nwn2_vertical_shift_adjustment',
        'nwn2_bake_resolution', 'nwn2_bake_ray_distance', 'nwn2_bake_max_ray_distance', 'nwn2_bake_samples',
    ]:
        try:
            delattr(bpy.types.Scene, prop)
        except:
            pass


if __name__ == "__main__":
    register()
