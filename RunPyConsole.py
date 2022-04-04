bl_info = {
    "name": "Run Text File in PyConsole",
    "author": "Fez_Master (with some components taken from CoDEmanX)",
    "version": (1, 0),
    "blender": (3, 1, 2),
    "location": "Console Header",
    "description": "Execute the code in the Text Editor within the python console.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"}

import bpy

def main(self, context):
    '''Fetches text from text editor, formats it, then runs in console'''
    for area in context.screen.areas:
        if area.type == 'TEXT_EDITOR':
            text = area.spaces[0].text
            break
    if text is not None:
        text = "exec(compile(" + repr(text) + ".as_string(), '" + text.name + "', 'exec'))"
        bpy.ops.console.clear_line()
        bpy.ops.console.insert(text=text)
        bpy.ops.console.execute()

class CONSOLE_OT_run_file(bpy.types.Operator):
    bl_idname = 'console.run_file'
    bl_label = ''
    bl_description = 'Run Current Text File in Console'
    
    text = bpy.props.StringProperty()
    
    def execute(self, context):
        main(self, context)
        return {'FINISHED'}

def draw_item(self, context):
    self.layout.operator(CONSOLE_OT_run_file.bl_idname, icon='FILE_SCRIPT')

def register():
    bpy.utils.register_class(CONSOLE_OT_run_file)
    bpy.types.CONSOLE_HT_header.append(draw_item)
    
def unregister():
    bpy.types.CONSOLE_HT_header.remove(draw_item)
    bpy.utils.unregister_class(CONSOLE_OT_run_file)

if __name__ == "__main__":
    register()