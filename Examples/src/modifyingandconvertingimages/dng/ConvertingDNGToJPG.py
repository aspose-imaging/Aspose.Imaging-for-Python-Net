import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.dng import DngImage
from aspose.imaging.imageoptions import JpegOptions
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
# Declare variables to store file paths for input and output images.
source_files = os.path.join(get_data_root_dir(), "HDR - 3c.dng")
dest_path = os.path.join(get_output_dir(), "result.jpg")
# Create an instance of Image class and load an exiting DNG file.
# Convert the image to DngImage object.
with aspycore.as_of(Image.load(source_files), DngImage) as image:
	# Create an instance of JpegOptions class.
	# convert and save to disk in Jpeg file format.
	image.save(dest_path, JpegOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(dest_path)
