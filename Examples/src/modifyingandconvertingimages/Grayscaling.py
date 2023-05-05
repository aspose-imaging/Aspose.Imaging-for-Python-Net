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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
output_path = os.path.join(get_output_dir(), "Grayscaling_out.jpg")
print("Running example Grayscaling")
# Load an image
with Image.load(os.path.join(data_dir, "aspose-logo.jpg")) as image:
	# Cast the image to RasterImage and Check if image is cached
	raster_cached_image = aspycore.as_of(image, RasterImage)
	if not raster_cached_image.is_cached:
		# Cache image if not already cached
		raster_cached_image.cache_data()

	# Transform image to its grayscale representation and Save the resultant image
	raster_cached_image.grayscale()
	raster_cached_image.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example Grayscaling")
