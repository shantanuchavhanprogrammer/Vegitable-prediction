import os
import glob
import shutil

path= os.path.join("Vegetable Images", "validation")
all_folders=glob.glob(path +"/*")

for i in range(len(all_folders)):
    current_folder_name = all_folders[i].split("/")[-1]
    destination_folder_path = os.path.join(os.getcwd(),  "Vegetable Images", "train", current_folder_name)
    for i in glob.glob(all_folders[i]+"/*"):
        shutil.move(os.path.join(os.getcwd(),i),os.path.join(os.getcwd(), "Vegetable Images","train", current_folder_name))
    # shutil.move(os.join.path(os.getcwd(), all_folders[i]))


    

    
