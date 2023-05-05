# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging.fileformats.png import PngImage
from aspose.imaging import Image
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
print("Running example Imagetransparency")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "ModifyingAndConvertingImages")
file_path = os.path.join(data_dir, "sample.png")
with aspycore.as_of(Image.load(file_path), PngImage) as image:
	opacity = image.image_opacity
	print(opacity)
	if opacity == 0:
		# Do something
		pass

print("Finished example Imagetransparency")
