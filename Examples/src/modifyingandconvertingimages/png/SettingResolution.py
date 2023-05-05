# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, ResolutionSetting, Rectangle
from aspose.imaging.imageoptions import PngOptions
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

print("Running example SettingResolution")
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

output_file = os.path.join(get_output_dir(), "SettingResolution_output.png")
# Create & initialize an instance of PngImage while specifying size and PngColorType
with PngImage(width, height) as png:
	# Save the previously loaded pixels on to the new PngImage
	png.save_pixels(Rectangle(0, 0, width, height), pixels)
	# Create an instance of PngOptions, Set the horizontal & vertical resolutions and Save the result on disc
	options = PngOptions()
	options.resolution_settings = ResolutionSetting(72, 96)
	png.save(output_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
	
print("Finished example SettingResolution")
