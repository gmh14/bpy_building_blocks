import bpy
import os

def load_obj(path, filename):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path {path} does not exist.")
    if not os.path.exists(os.path.join(path, filename)):
        raise FileNotFoundError(f"File {filename} does not exist in path {path}.")

    bpy.ops.wm.obj_import(filepath=os.path.join(path, filename),
                          directory=path,
                          files=[{"name": filename}],)

def save_obj(path, filename):
    bpy.ops.export_scene.obj(filepath=os.path.join(path, filename))