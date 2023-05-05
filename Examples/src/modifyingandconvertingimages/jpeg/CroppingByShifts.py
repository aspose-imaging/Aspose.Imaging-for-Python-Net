# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
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
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
out_file = os.path.join(get_output_dir(), 'CroppingByShifts_out.jpg')
print("Running example CroppingByShifts")
# Load an existing image into an instance of RasterImage class
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")),
							   RasterImage) as raster_image:
	# Before cropping, the image should be cached for better performance
	if not raster_image.is_cached:
		raster_image.cache_data()

	# Define shift values for all four sides
	left_shift = 10
	right_shift = 10
	top_shift = 10
	bottom_shift = 10
	# Based on the shift values, apply the cropping on image Crop method will shift the image bounds toward the center of image and Save the results to disk
	raster_image.crop(left_shift, right_shift, top_shift, bottom_shift)
	raster_image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CroppingByShifts")
