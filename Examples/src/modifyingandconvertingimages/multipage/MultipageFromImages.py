import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import TiffOptions
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
print("Running example MultipageFromImages")
# The path to the documents directory.
base_folder = os.path.join(get_data_root_dir(), 'Multipage')
out_file_name = "MultipageImageCreateTest.tif"
output_file_path = os.path.join(get_output_dir(), out_file_name)
files = ["33266.tif", "Animation.gif", "elephant.png", "MultiPage.cdr"]
images = []
for file in files:
	file_path = os.path.join(base_folder, file)
	images.append(Image.load(file_path))

with Image.create(images, True) as image:
	image.save(output_file_path, TiffOptions(TiffExpectedFormat.TIFF_JPEG_RGB))

# disposing the images
for image in images:
	with image as _:
		pass

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)

print("Finished example MultipageFromImages")
