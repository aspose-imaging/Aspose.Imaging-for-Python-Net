# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Rectangle, RasterImage
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
out_file = os.path.join(get_output_dir(), 'CroppingByRectangle_out.jpg')
print("Running example CroppingByRectangle")
# Load an existing image into an instance of RasterImage class
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")),
							   RasterImage) as raster_image:
	if not raster_image.is_cached:
		raster_image.cache_data()

	# Create an instance of Rectangle class with desired size, Perform the crop operation on object of Rectangle class and Save the results to disk
	rectangle = Rectangle(20, 20, 20, 20)
	raster_image.crop(rectangle)
	raster_image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CroppingByRectangle")
