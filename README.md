# Mediapipe To ReadyPlayerMe
This library converts Mediapipe landmark data and ARKit blendshape data to an animation for the ReadyPlayerMe Avatars in blender.
It creates an animation which can be exported to be used in different 3D software.

## How to use the repository
1. Create a blender file in the repository.
2. Re-open this blender file in the repository in order to fix script path issues.
3. Import a ReadyPlayerMe avatar into the blender scene.
4. Open the scripts inside of blender.

### Using the pose_converter.py
1. Import the csv files into the mediapipe_data folder.
2. Change the function parameters to the file names of the csv landmark data.
3. Change the sample rate to the desired quality.
4. Run the script.
5. Bake the animation onto the avatar by selecting the armature, Then selecting the Backe action option in Object->Animation->Bake Action..
6. Deselect Only Selected Bones, Select Visual Keying, Clear Constraints and Clear Parents.
7. In the Bake Data menu, select Pose. Click OK. The animation should now be baked onto the avatar which allows you to delete all the other objects in the scene.

### Using the arkit_blendshapes.py
1. Import the csv file for the blendshape data into the ARkit folder.
2. Change the function parameter to the file name of the blendshape data csv file.
3. Run the script.

### Exporting the animation
1. Select all the meshes and the armature of the avatar, not just the parent armature.
2. File->Export->FBX
3. In Include turn on Limit to Selected Objects.
4. Select Bake Animation and Deselect NLA Strips and All actions.
5. Change Simplify to 0.00
6. Export the FBX.

## Video Tutorial


