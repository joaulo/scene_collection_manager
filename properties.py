# ------------------------------------------------------------------------
#    Render Properties
# ------------------------------------------------------------------------
import bpy
from bpy.props import StringProperty


class LayerCollectionsManagerProperties(bpy.types.PropertyGroup):

    path_dir: StringProperty(
        name="Output dir:",
        description="Choose a directory to save config files",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
    )

    save_render_settings: StringProperty(
        name="Save collections settings to file:",
        description="Choose a file to save collections settings",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

    load_render_settings: StringProperty(
        name="Load collections settings from file:",
        description="Choose a file to load collection settings",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )


classes = (LayerCollectionsManagerProperties,)
