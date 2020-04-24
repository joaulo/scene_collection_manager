import bpy


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class LayerCollectionsManagerPanel:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"  # UI
    bl_category = "JSWK"
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}


class JSWK_PT_layer_collections_manager(LayerCollectionsManagerPanel, bpy.types.Panel):
    bl_idname = "JSWK_PT_layer_collections_manager"
    bl_label = "Layer Collections Settings"

#    @classmethod
#    def poll(self,context):
#        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        lcm = scene.layer_collections_manager

        # layout.prop(lcm, "path_dir")
        layout.separator()
        layout.prop(lcm, "load_collections_settings")
        layout.operator("jswk.load_collections_settings")
        layout.separator()
        layout.prop(lcm, "save_collections_settings")
        layout.operator("jswk.save_collections_settings")


# class JSWK_PT_lcm_load_settings(LayerCollectionsManagerPanel, bpy.types.Panel):
#     bl_parent_id = "JSWK_PT_layer_collections_manager"
#     bl_label = "Load Settings"
#
#     def draw(self, context):
#         layout = self.layout
#         scene = context.scene
#         lcm = scene.layer_collections_manager
#
#         layout.prop(lcm, "load_collections_settings")
#         layout.operator("load.collections_settings")
#
#
# class JSWK_PT_lcm_save_settings(LayerCollectionsManagerPanel, bpy.types.Panel):
#     bl_parent_id = "JSWK_PT_layer_collections_manager"
#     bl_label = "Save Settings"
#
#     def draw(self, context):
#         layout = self.layout
#         scene = context.scene
#         lcm = scene.layer_collections_manager
#
#         layout.prop(lcm, "save_collections_settings")
#         layout.operator("save.collections_settings")


classes = (
    JSWK_PT_layer_collections_manager,
    # JSWK_PT_lcm_load_settings,
    # JSWK_PT_lcm_save_settings,
)
