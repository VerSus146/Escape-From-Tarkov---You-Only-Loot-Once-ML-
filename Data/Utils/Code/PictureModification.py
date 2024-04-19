"""
This utility program modifies the background of images based on provided mask. It creates a random RGB image matching
the size of original images and creates a random solid color image. The program accepts params:
--image : original image to be modified. Absolute Path (Default - All images in ToModify folder)
--mask : mask to be applied to the image. Absolute Path (Default - Matching all images names from ToModify folder in Masks folder)
--samples : number of modified images to be created (Default 10)
"""
import os
import random
import sys

from pathlib import Path, PurePath
from PIL import Image

arguments = sys.argv

prepared_images_path = os.path.abspath(os.curdir) + "\\Data\\Images"
to_modify_images_path = os.path.abspath(os.curdir) + "\\Data\\Utils\\ToModify"
masks_path = os.path.abspath(os.curdir) + "\\Data\\Utils\\ToModify\\Masks"


def modify_image(image_path, mask_path, sample):
	# Load the Image
	image_to_edit = Image.open(Path(image_path))

	# Prepare 2nd image
	random_rgb = (random.randrange(30, 50), random.randrange(30, 50), random.randrange(30, 50))
	solid_color = Image.new(mode="RGB", size=image_to_edit.size, color=random_rgb)

	# Load prepared mask
	mask = Image.open(Path(mask_path)).convert('L')

	# Join images based on mask
	image = Image.composite(solid_color, image_to_edit, mask)

	image.save(f"{prepared_images_path}\\mod{sample}_{PurePath(image_path).name}")



# Parse arguments from CMD Line
image_to_modify = None
mask_to_apply = None
samples = 10

i = 0
for argument in arguments:
	if "image" in argument:
		if os.path.isfile(arguments[i + 1]):
			print(f"Image found. Performing modification on {arguments[i + 1]}.")
			image_to_modify = arguments[i + 1]
		else:
			print("Provided file couldn't be found. Closing.")
			exit(1)
	if "mask" in argument:
		if os.path.isfile(arguments[i + 1]):
			print(f"Mask found. Applying {arguments[i + 1]} mask.")
			mask_to_apply = arguments[i + 1]
		else:
			print("Provided file couldn't be found. Closing.")
			exit(1)
	if "samples" in argument:
		if arguments[i + 1].isnumeric():
			print(f"{arguments[i + 1]} images will be created.")
			samples = int(arguments[i + 1])
		else:
			print("Provided string is not numeric. Closing.")
			exit(1)

	i += 1

if image_to_modify is not None:
	if mask_to_apply is None:
		print("Mask not provided. Closing.")
		exit(1)
	for sample in range(samples):
		modify_image(image_to_modify, mask_to_apply, sample)

	# Move the image and mask after modifying
	os.rename(image_to_modify, f"{prepared_images_path}\\{PurePath(image_to_modify).name}")
	os.rename(mask_to_apply, f"{prepared_images_path}\\Masks\\{PurePath(mask_to_apply).name}")

if image_to_modify is None:
	allowed_ext = [".png", ".jpg"]
	for image in os.listdir(to_modify_images_path):
		# Check if the file is a directory
		if os.path.isdir(image):
			continue
		# Check if the file is an image
		if os.path.splitext(image)[1].lower() not in allowed_ext:
			continue
		for sample in range(samples):
			if image in os.listdir(masks_path):
				modify_image(to_modify_images_path + f"\\{image}", masks_path + f"\\{image}", sample)
			else:
				print(f"Couldn't find mask for {image}.")

		# Move the image and mask after modifying
		os.rename(f"{to_modify_images_path}\\{image}", f"{prepared_images_path}\\{image}")
		os.rename(f"{masks_path}\\{image}", f"{prepared_images_path}\\Masks\\{image}")
