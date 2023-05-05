# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Rectangle, Color
from aspose.imaging.fileformats.png import PngImage
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
output_file = os.path.join(get_output_dir(), "SpecifyTransparencyforPNGImages_out.png")

print("Running example SpecifyTransparency")
# Initialize variables to hold width & height values
width = 0
height = 0
# Initialize an array of type Color to hold the pixel data
pixels = None
# Create an instance of RasterImage and load a BMP image
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.png")),
					RasterImage) as raster:
	# Store the width & height in variables for later use
	width = raster.width
	height = raster.height
	# Load the pixels of RasterImage into the array of type Color
	pixels = raster.load_pixels(Rectangle(0, 0, width, height))

# Create & initialize an instance of PngImage while specifying size and PngColorType
with PngImage(width, height, PngColorType.TRUECOLOR_WITH_ALPHA) as png:
	# Save the previously loaded pixels on to the new PngImage and Set TransparentColor property to specify which color to be rendered as transparent
	png.save_pixels(Rectangle(0, 0, width, height), pixels)
	png.transparent_color = Color.black
	png.has_transparent_color = True
	png.save(output_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)

print("Finished example SpecifyTransparency")
