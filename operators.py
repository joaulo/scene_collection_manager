import json
import pprint
import bpy


def get_collections_state(collection, cstate):
    for child in collection.children:
        cstate.append(get_collections_state(child, cstate))
    return [collection.name, collection.exclude]


def set_collections_state(collection, plist):
    # print('search', collection.name, 'in', plist)
    value = plist.get(collection.name, None)
    # print('setting value to:', value)
    if value is not None:
        # print("found collection: ", collection.name)
        collection.exclude = value
        # print(collection.name, " set to: ", collection.exclude)

    for child in collection.children:
        set_collections_state(child, plist)


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class JSWK_OT_load_collections_settings(bpy.types.Operator):
    """Load collections settings previously saved to configuration file"""
    bl_idname = "jswk.load_collections_settings"
    bl_label = "Load Collections Settings"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        print("load configuration from file and set values to scene")
        scene = context.scene
        with open(scene.scene_collections_manager.load_collections_settings, 'r', encoding='utf-8') as f:
            pl = json.load(f)
            pprint.pprint(pl)

            # check scene name
            if pl['scene'] != scene.name:
                print('WARNING: scene name is different!')

            # set collections
            plist = pl['collections']
            set_collections_state(context.view_layer.layer_collection, plist)

        print('loading completed')
        return {'FINISHED'}


class JSWK_OT_save_collections_settings(bpy.types.Operator):
    """Save collections settings to configuration file"""
    bl_idname = "jswk.save_collections_settings"
    bl_label = "Save Collections Settings"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene
        print('-> save collections settings to file:',
              scene.scene_collections_manager.save_collections_settings)

        # get properties list
        # p = {sett: getattr(scene.render, sett) for sett in dir(scene.render)}
        pl = {}
        # current scene
        pl['scene'] = scene.name

        # container for collection settings
        print('reading collections settings...')
        cstate = []
        get_collections_state(context.view_layer.layer_collection, cstate)

        # print(cstate)

        pl['collections'] = {}
        pl['collections'].update(cstate)

        pprint.pprint(pl)

        # if len(bpy.data.collections) > 0:
        #     print('COLLECTIONS')
        #     for col in bpy.data.collections:
        #         if len(col.objects) > 0:
        #             print ("True")
        #             for obj in col.objects:
        #                 print(obj)
        #         else:
        #             print ("False")
        #         print(col)
        # else:
        #     print('NO_COLLECTIONS')

        with open(scene.scene_collections_manager.save_collections_settings, 'w', encoding='utf-8') as f:
            json.dump(pl, f, ensure_ascii=False, indent=4)

        print('saving completed')
        return {'FINISHED'}


classes = (
    JSWK_OT_load_collections_settings,
    JSWK_OT_save_collections_settings,
)
