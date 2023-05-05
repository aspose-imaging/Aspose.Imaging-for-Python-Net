import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Rectangle
from aspose.imaging.imageoptions import JpegOptions
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
out_file = os.path.join(get_output_dir(), "changed_out.jpg")
print("Running example ExpandOrCropAnImage")
# Load an image in an instance of Image and Setting for image data to be cashed
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")),
					RasterImage) as raster_image:
	raster_image.cache_data()
	# Create an instance of Rectangle class and define X,Y and Width, 
	# height of the rectangle, and Save output image
	dest_rect = Rectangle()
	dest_rect.x = -200
	dest_rect.y = -200
	dest_rect.width = 300
	dest_rect.height = 300
	raster_image.save(out_file, JpegOptions(), dest_rect)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ExpandOrCropAnImage")
