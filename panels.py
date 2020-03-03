import bpy


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class LayerCollectionManagerPanel:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"  # UI
    bl_category = "JSWK"
    bl_context = "scene"
    bl_options = {'DEFAULT_CLOSED'}


class Jswk_PT_layer_collections_manager(LayerCollectionManagerPanel, bpy.types.Panel):
    bl_idname = "Jswk_PT_layer_collections_manager"
    bl_label = "Layer Collections Settings"

#    @classmethod
#    def poll(self,context):
#        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rcc = scene.layer_collections_manager

        layout.prop(rcc, "path_dir")
        layout.separator()


class Jswk_PT_lcm_load_settings(LayerCollectionManagerPanel, bpy.types.Panel):
    bl_parent_id = "Jswk_PT_layer_collections_manager"
    bl_label = "Load Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rcc = scene.layer_collections_manager

        layout.prop(rcc, "load_collections_settings")
        layout.operator("load.collections_settings")


class Jswk_PT_lcm_save_settings(LayerCollectionManagerPanel, bpy.types.Panel):
    bl_parent_id = "Jswk_PT_layer_collections_manager"
    bl_label = "Save Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rcc = scene.layer_collections_manager

        layout.prop(rcc, "save_collections_settings")
        layout.operator("save.collections_settings")


classes = (
    Jswk_PT_layer_collections_manager,
    Jswk_PT_lcm_load_settings,
    Jswk_PT_lcm_save_settings,
)