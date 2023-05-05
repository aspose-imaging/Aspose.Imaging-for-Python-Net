# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Color
from aspose.imaging.imageoptions import PngOptions
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
data_dir = os.path.join(get_data_root_dir(), 'png')
output_file = os.path.join(get_output_dir(), "SpecifyTransparencyforPNGImagesUsingRasterImage_out.png")

print("Running example SpecifyTransparencyUsingRasterImage")
# Initialize variables to hold width & height values
width = 0
height = 0
# Create an instance of RasterImage and load a BMP image
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.png")),
					RasterImage) as image:
	# Store the width & height in variables for later use
	width = image.width
	height = image.height
	# Set the background_color, transparent_color, has_transparent_color & has_background_color properties for the image
	image.background_color = Color.white
	image.transparent_color = Color.black
	image.has_transparent_color = True
	image.has_background_color = True
	image.save(output_file, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
	
print("Running example SpecifyTransparencyUsingRasterImage")
