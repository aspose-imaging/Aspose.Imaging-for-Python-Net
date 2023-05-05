import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage
from aspose.imaging.imagefilters.filteroptions import GaussianBlurFilterOptions
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
out_file = os.path.join(get_output_dir(), "BlurAnImage_out.gif")
print("Running example BlurAnImage")
# To get proper output please apply a valid Aspose.Imaging License. You can purchase full license or get 30 day temporary license from https:// www.aspose.com/purchase/default.aspx.");
# Load the image
with Image.load(os.path.join(data_dir, "asposelogo.gif")) as image:
	# Convert the image into RasterImage, Pass Bounds[rectangle] of image and GaussianBlurFilterOptions instance to Filter method and Save the results
	raster_image = aspycore.as_of(image, RasterImage)
	raster_image.filter(raster_image.bounds, GaussianBlurFilterOptions(5, 5))
	raster_image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example BlurAnImage")
