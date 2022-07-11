import bpy
import csv

def csv_to_arrays(csv_file):
    lines = []
    output = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)

    # Create lists for each blendshape
    for index in lines[0][2:]:
        # We have to convert the first letter to lowercase to match the shapekey names in Blender.
        name = index[0].lower() + index[1:]
        output.append((name, []))


    for line in lines[1:]:
        for idx, val in enumerate(line[2:]):
            output[idx][1].append(float(val))
    return output

def animate_armature(file="", frame_step=1):
    blendshapes = csv_to_arrays(file)
    shape_keys =  bpy.data.shape_keys

    for tupl in blendshapes:
        blendshape, data = tupl

        for idx, val in enumerate(data):
            for shape_key in shape_keys:
                key_block = shape_key.key_blocks.get(blendshape)
                if(key_block):
                    key_block.value = val
                    key_block.keyframe_insert("value", frame=idx)



animate_armature(file="ARkit/BlendShapeData.csv")

