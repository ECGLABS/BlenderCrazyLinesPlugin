bl_info = {
    "name": "Crazy Lines",
    "author": "Johnathan Farmer",
    "version": (0, 7),
    "blender": (3, 3, 1),
    "location": "context.space_data",
    "description": "Adds randomized line art to scene",
    "warning": "",
    "doc_url": "",
    "category": "Object",
}


import bpy
import random
from bpy.app.handlers import persistent
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
    




#Variables
 


"""Start of Initialization code"""

def button_01(context):
    #This check if there is already a camera, then adds one if there is not a camera, also sets it's position
    Camera = bpy.context.scene.objects.get("Camera")
    if Camera:
        print ("Do Nothing")
    else:
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(7.35,-6.92,4.95), rotation=(1.1,0,0.81), scale=(1, 1, 1))
        

    #The next 2 lines add in a stroke line and move it out the way
    Stroke = bpy.context.scene.objects.get("EEnE Line Art")
    if Stroke:
        print ("Do Nothing")
    else:
        bpy.ops.object.gpencil_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1), type='STROKE') 
        bpy.ops.transform.translate(value=(9.97301, 0, 0), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False, release_confirm=True)
        bpy.data.objects["Stroke"].name = "EEnE Line Art"
        #This adds in the LineArt Modifer and sets it up
        bpy.ops.object.gpencil_modifier_add(type='GP_LINEART')
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].source_type= 'SCENE'
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].target_layer = "Lines"
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].target_material = bpy.data.materials["Black"]
        #This adds in the Noise modifier to the line art
        bpy.ops.object.gpencil_modifier_add(type='GP_NOISE')
        #This adds in the Offset modifier to the line art
        bpy.ops.object.gpencil_modifier_add(type='GP_OFFSET')
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].thickness = random.randint(20,25)
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].silhouette_filtering
        #These next 2 lines are comnented out but they're more modifier lines    
        #bpy.data.objects["Stroke"].grease_pencil_modifiers["Line Art"].level_start = random.randint(0,1)
        #bpy.data.objects["Stroke"].grease_pencil_modifiers["Line Art"].crease_threshold = random.randint(120,140)
        #The Next Few Lines will make changes the noise modifier
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor = random.uniform(0.25,0.30) 
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor_strength = random.uniform(0.07,0.10)
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor_thickness = random.uniform(0.90,1.00)
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor_uvs = random.uniform(0.45,0.60)
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].noise_scale = random.uniform(0.90,1.00)
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].noise_offset = 100
        bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].seed = 10000
            


    



class Add_EEnE(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "begin.eene"
    bl_label = "Initalize Crazy Lines"


    def execute(self, context):
        button_01(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SimpleOperator.bl_idname, text=SimpleOperator.bl_label)




"""End of Initialization code"""



#########################################################################################





"""This part is the actual UI Script"""

class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "Layout Demo"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        scene = context.scene
        
        # Run EEnE Button Code
        layout.label(text="Crazy Lines:")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("begin.eene")

        

"""This  is the end of the UI Script"""




def register():
    bpy.utils.register_class(LayoutDemoPanel)
    bpy.utils.register_class(Add_EEnE)
    bpy.types.VIEW3D_MT_object.append(menu_func)



def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)
    bpy.utils.unregister_class(Add_EEnE)
    bpy.types.VIEW3D_MT_object.remove(menu_func)



if __name__ == "__main__":
    register()


def handler(scene):
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].thickness = random.randint(20,25)
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Line Art"].silhouette_filtering
    #These next 2 lines are comnented out but they're more modifier lines    
    #bpy.data.objects["Stroke"].grease_pencil_modifiers["Line Art"].level_start = random.randint(0,1)
    #bpy.data.objects["Stroke"].grease_pencil_modifiers["Line Art"].crease_threshold = random.randint(120,140)
    #The Next Few Lines will make changes the noise modifier
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor = random.uniform(0.25,0.30) 
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor_strength = random.uniform(0.07,0.10)
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor_thickness = random.uniform(0.90,1.00)
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].factor_uvs = random.uniform(0.45,0.60)
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].noise_scale = random.uniform(0.90,1.00)
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].noise_offset = 100
    bpy.data.objects["EEnE Line Art"].grease_pencil_modifiers["Noise"].seed = 100
    
    

bpy.app.handlers.frame_change_post.append(handler)
