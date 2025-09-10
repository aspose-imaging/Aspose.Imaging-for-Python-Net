# GROUP: MODIFYING_AND_CONVERTING_IMAGES

from aspose.pycore import as_of
from aspose.imaging import Image, RasterImage
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
data_dir = os.path.join(get_data_root_dir(), 'png')

# Signing limitations:
#  - The LSB steganography algorithm requires the image to be at least 8 pixels in width and height, with a minimum of 16,384 total pixels.
#  - Password must be at least 4 characters long.
#
#            var password = "1234";
#            var filePath = "c:\sunflower.jpg";
#
##################################### Example 1 ############################
# Faster checking method with partial data extraction.                     #
# Set detectionThreasholdPercentage value to 75% (default value).          #
############################################################################

password = "123456"

with as_of(Image.load(os.path.join(data_dir, "00020.png")), RasterImage) as image:
	image.embed_digital_signature(password)
	isSigning = image.is_digital_signed(password, -1)
	print(f"Check signing result of file is: {isSigning}")
