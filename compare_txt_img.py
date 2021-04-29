import glob, os, shutil

text_folder = r"F:/darknet_training/model_RAK_box_symbols/labels"
images_folder = r"F:/darknet_training/model_RAK_box_symbols/images"

all_image_files = glob.glob(images_folder+os.sep+"*.jpeg")
all_txt_files = glob.glob(text_folder+os.sep+"*.txt")

 # print(all_image_files)
 # print(all_txt_files)

for txt_file in all_txt_files:
    # print("-", txt_file)
    txt_filename = txt_file.split("\\")[-1]
    for img_file in all_image_files:
        # print(">", img_file)
        img_filename = img_file.split("\\")[-1]
        if txt_filename[:-4] == img_filename[:-4]:
            print(txt_filename[:-4],img_filename[:-4])
            # shutil.copy(src, dst)
            # print(text_folder+os.sep+img_filename)
            shutil.copy(img_file, text_folder+os.sep+img_filename)
            
