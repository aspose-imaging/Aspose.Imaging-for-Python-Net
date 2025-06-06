﻿import aspose.pycore as aspycore
from aspose.imaging.imagefilters.filteroptions import GaussWienerFilterOptions
from aspose.imaging import Image, RasterImage
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), "ApplyGaussWienerFilter_out.gif")
print("Running example ApplyGaussWienerFilterForColoredImage")
# Load the image
with Image.load(os.path.join(data_dir, "asposelogo.gif")) as image:
	# Cast the image into RasterImage
	if not aspycore.is_assignable(image, RasterImage):
		exit()
	raster_image = aspycore.as_of(image, RasterImage)

	# Create an instance of GaussWienerFilterOptions class and set the radius size and smooth value.
	options = GaussWienerFilterOptions(5, 1.5)
	options.brightness = 1
	# Apply MedianFilterOptions filter to RasterImage object and Save the resultant image
	raster_image.filter(image.bounds, options)
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ApplyGaussWienerFilterForColoredImage")
