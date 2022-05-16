# clean_train_data_yolo
code for clean missing file for yolo training dataset.

#Uncomment the below line in program
if you want to clean the CVAT Unannotated data(0 bytes of txt file + image).
37. clean_empty_txt(user_input+"/") 

if you want to delete the images which does not have label file(.txt file).
38. clean_image(user_input+"/")
