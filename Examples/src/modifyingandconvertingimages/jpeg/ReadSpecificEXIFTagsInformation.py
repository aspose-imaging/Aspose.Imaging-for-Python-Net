# GROUP: TEST_FILE_FORMATS
from aspose.imaging.exif import *
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.jpeg import JpegImage
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
print("Running example ReadSpecificEXIFTagsInformation")
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")), JpegImage) as image:
	# Get image's EXIF information
	exif = image.exif_data
	# Check if image has any EXIF entries defined and Display a few EXIF entries
	if exif is not None:
		print("Exif WhiteBalance: ", exif.white_balance)
		print("Exif PixelXDimension: ", exif.pixel_x_dimension)
		print("Exif PixelYDimension: ", exif.pixel_y_dimension)
		print("Exif ISOSpeed: ", exif.iso_speed)
		print("Exif FocalLength: ", exif.focal_length)

print("Finished example ReadSpecificEXIFTagsInformation")
