# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# This addon was created with the Serpens - Visual Scripting Addon.
# This code is generated from nodes and is not intended for manual editing.
# You can find out more about Serpens at <https://blendermarket.com/products/serpens>.

bl_info = {
    "name": "Apply Dynaics Hair",
    "description": "",
    "author": "Frost Crack Studio",
    "version": (1, 0, 1),
    "blender": (2, 93, 1),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}

##   IMPORTS
import bpy
from bpy.utils import previews
import os
import math

##   INITALIZE VARIABLES
apply_dynaics_hair = {
    "new_variable": "Apply Current Dynamic Hair and set cureosr to 0", 
    }

##   SERPENS FUNCTIONS
def exec_line(line):
    exec(line)

def sn_print(tree_name, *args):
    if tree_name in bpy.data.node_groups:
        item = bpy.data.node_groups[tree_name].sn_graphs[0].prints.add()
        for arg in args:
            item.value += str(arg) + ";;;"
        for area in bpy.context.screen.areas:
            area.tag_redraw()
    print(*args)

def sn_cast_string(value):
    return str(value)

def sn_cast_boolean(value):
    if type(value) == tuple:
        for data in value:
            if bool(data):
                return True
        return False
    return bool(value)

def sn_cast_float(value):
    if type(value) == str:
        try:
            value = float(value)
            return value
        except:
            return float(bool(value))
    elif type(value) == tuple:
        return float(value[0])
    elif type(value) == list:
        return float(len(value))
    elif not type(value) in [float, int, bool]:
        try:
            value = len(value)
            return float(value)
        except:
            return float(bool(value))
    return float(value)

def sn_cast_int(value):
    return int(sn_cast_float(value))

def sn_cast_boolean_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(bool(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(bool(value[i]) if len(value) > i else bool(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_boolean_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_boolean_vector(value, size)
        except:
            return sn_cast_boolean_vector(bool(value), size)

def sn_cast_float_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value[i]) if len(value) > i else sn_cast_float(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_float_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_float_vector(value, size)
        except:
            return sn_cast_float_vector(sn_cast_float(value), size)

def sn_cast_int_vector(value, size):
    return tuple(map(int, sn_cast_float_vector(value, size)))

def sn_cast_color(value, use_alpha):
    length = 4 if use_alpha else 3
    value = sn_cast_float_vector(value, length)
    tuple_list = []
    for data in range(length):
        data = value[data] if len(value) > data else value[0]
        tuple_list.append(sn_cast_float(min(1, max(0, data))))
    return tuple(tuple_list)

def sn_cast_list(value):
    if type(value) in [str, tuple, list]:
        return list(value)
    elif type(value) in [int, float, bool]:
        return [value]
    else:
        try:
            value = list(value)
            return value
        except:
            return [value]

def sn_cast_blend_data(value):
    if hasattr(value, "bl_rna"):
        return value
    elif type(value) in [tuple, bool, int, float, list]:
        return None
    elif type(value) == str:
        try:
            value = eval(value)
            return value
        except:
            return None
    else:
        return None

def sn_cast_enum(string, enum_values):
    for item in enum_values:
        if item[1] == string:
            return item[0]
        elif item[0] == string.upper():
            return item[0]
    return string

##   IMPERATIVE CODE
##   EVALUATED CODE
##   Apply Dynaics Hair
def sn_prepend_panel_CE1F2(self,context):
    try:
        layout = self.layout
        op = layout.operator("sna.apply_hair_d",text=r"Apply Hair Dynaics",emboss=True,depress=False,icon_value=bpy.context.scene.apply_dynaics_hair_icons['NEW_ICON'].icon_id)
    except Exception as exc:
        print(str(exc) + " | Error in Particle Hair Dynamics when adding to panel")

class SNA_OT_Apply_Hair_D(bpy.types.Operator):
    bl_idname = "sna.apply_hair_d"
    bl_label = "Apply Hair D"
    bl_description = "Apply Current Dynamic Hair frame and set curent frame to 1"
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of Apply Hair D")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass # Apply Dynaics Hair Script Start
            import bpy
            # get the depsgraph and the evaluated object   
            deps_graph = bpy.context.evaluated_depsgraph_get()
            evaluated_object = bpy.context.object.evaluated_get(deps_graph)
            # assume context object has a particle system (warning, no check), use active
            particle_system = evaluated_object.particle_systems.active
            # Variable to hold hair-verticies-coordinats
            hairs = []
            # At current frame
            # For each particle (hair)
            #   For each vertex
            #     Store XYZ coordinates
            for p in particle_system.particles:
                hair = []
                for v in p.hair_keys:
                    hair.append([v.co[0], v.co[1], v.co[2]])
                hairs.append(hair)
            # Deactivate hair dynamics
            particle_system.use_hair_dynamics = False
            # On static hair system
            # For each particle (hair)
            #   For each vertex
            #     Overwrite XYZ coordinates
            for p,hair in zip(particle_system.particles,hairs):
                for v,h in zip(p.hair_keys,hair):
                    #print(v.co, h)
                    v.co[0] = h[0]
                    v.co[1] = h[1]
                    v.co[2] = h[2]
                    #print(v.co, h)
            # Update view and UI
            bpy.context.scene.frame_set(bpy.context.scene.frame_current)
            bpy.context.scene.frame_current = 1
            pass # Apply Dynaics Hair Script End
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of Apply Hair D")
        return self.execute(context)

##   REGISTER ICONS
def sn_register_icons():
    icons = ["NEW_ICON",]
    bpy.types.Scene.apply_dynaics_hair_icons = bpy.utils.previews.new()
    icons_dir = os.path.join( os.path.dirname( __file__ ), "icons" )
    for icon in icons:
        bpy.types.Scene.apply_dynaics_hair_icons.load( icon, os.path.join( icons_dir, icon + ".png" ), 'IMAGE' )

def sn_unregister_icons():
    bpy.utils.previews.remove( bpy.types.Scene.apply_dynaics_hair_icons )

##   REGISTER PROPERTIES
def sn_register_properties():
    pass

def sn_unregister_properties():
    pass

##   REGISTER ADDON
def register():
    sn_register_icons()
    sn_register_properties()
    bpy.utils.register_class(SNA_OT_Apply_Hair_D)
    bpy.types.PARTICLE_PT_hair_dynamics.prepend(sn_prepend_panel_CE1F2)

###   UNREGISTER ADDON
def unregister():
    sn_unregister_icons()
    sn_unregister_properties()
    bpy.types.PARTICLE_PT_hair_dynamics.remove(sn_prepend_panel_CE1F2)
    bpy.utils.unregister_class(SNA_OT_Apply_Hair_D)
