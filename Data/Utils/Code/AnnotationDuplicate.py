'''
The project uses a lot of augmented data to prepare the dataset.
This util helps in the annotation part - only the main picture has to be annotated, all other pictures that are
augmented can reuse the same annotations. This script automatically assigns annotations from main picture to all
augmented pictures.

Original Annotation - Should start with Original pictures name and be followed by "_" sign.
Example: MedsPic2_jpg.rf.12412521tt2dasd

Duplicate Pictures - Should contain the name of the original Annotation, eg. mod8_MedsPic2.jpg
'''
import os
import shutil

duplicate_images_folder = os.path.abspath(os.curdir) + "\\Data\\Utils\\Annotation\\ToAnnotate\\Images"
to_annotate_folder = os.path.abspath(os.curdir) + "\\Data\\Utils\\Annotation\\ToAnnotate\\Labels"

for annotation_file in os.listdir(to_annotate_folder):

	for image in os.listdir(duplicate_images_folder):

		if annotation_file.partition("_")[0] in image:
			shutil.copyfile(f"{to_annotate_folder}\\{annotation_file}",
			                f"{duplicate_images_folder}\\{os.path.splitext(image)[0]}.txt")
		else:
			continue
