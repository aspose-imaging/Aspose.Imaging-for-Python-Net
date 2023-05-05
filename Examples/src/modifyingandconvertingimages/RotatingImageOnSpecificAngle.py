import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Color
from aspose.imaging.imageoptions import PdfOptions
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
output_path = os.path.join(get_output_dir(), "RotatingImageOnSpecificAngle_out.jpg")
print("Running example RotatingImageOnSpecificAngle")
# Load an image to be rotated in an instance of RasterImage
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")), 
					RasterImage) as image:
	# Before rotation, the image should be cached for better performance
	if not image.is_cached:
		image.cache_data()

	# Perform the rotation on 20 degree while keeping the image size proportional with red background color and Save the result to a new file
	image.rotate(20.0, True, Color.red)
	image.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example RotatingImageOnSpecificAngle")
