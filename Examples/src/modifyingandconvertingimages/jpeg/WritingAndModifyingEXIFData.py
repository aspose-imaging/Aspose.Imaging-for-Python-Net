# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.jpeg import JpegImage
from aspose.imaging.exif.enums import ExifWhiteBalance, ExifFlash
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
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
out_file = os.path.join(data_dir, "aspose-logo_out.jpg")
print("Running example WritingAndModifyingEXIFData")
# Load an image using the factory method Load exposed by Image class
with Image.load(os.path.join(data_dir, "aspose-logo.jpg")) as image:
	# Initialize an object of ExifData and fill it will image's EXIF information
	exif = (aspycore.as_of(image, JpegImage)).exif_data
	# Set LensMake, WhiteBalance, Flash information Save the image
	exif.lens_make = "Sony"
	exif.white_balance = ExifWhiteBalance.AUTO
	exif.flash = ExifFlash.FIRED
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example WritingAndModifyingEXIFData")
