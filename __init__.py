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
    "name": "Layer Collection Manager",
    "author": "joaulo",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Scene properties panel",
    "description": "save/load collections exclusions",
    # "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "",
    # "tracker_url": "",
    "category": "Scene",
}


classes = properties.classes + operators.classes + panels.classes


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.layer_collection_manager = PointerProperty(
        type=properties.LayerCollectionManagerProperties)


def unregister():
    del bpy.types.Scene.layer_collection_manager
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
