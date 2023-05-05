# GROUP: ADDITIONAL_FEATURES
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Color
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
print("Running example Deskew")
file_name = "skewed.png"
output = "skewed.out.png"
input_file_name = os.path.join(data_dir, file_name)
out_file = os.path.join(get_output_dir(), output)
# Get rid of the skewed scan with default parameters
with aspycore.as_of(Image.load(input_file_name), RasterImage) as image:
	image.normalize_angle(False, Color.light_gray)
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example Deskew")
