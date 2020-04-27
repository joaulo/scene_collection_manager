# local import
from . import (
    properties,
    operators,
    panels,
)

# blender related import
import bpy
from bpy.props import PointerProperty

bl_info = {
    "name": "Scene Collections Manager",
    "author": "joaulo <jsoftworks@joaulo.com>",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "category": "Scene",
    "location": "Scene properties panel",
    "description": "save/load collections exclusions",
    # "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "",
    # "tracker_url": "",
}


classes = properties.classes + operators.classes + panels.classes


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.scene_collections_manager = PointerProperty(
        type=properties.SceneCollectionsManagerProperties)


def unregister():
    del bpy.types.Scene.scene_collections_manager
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
