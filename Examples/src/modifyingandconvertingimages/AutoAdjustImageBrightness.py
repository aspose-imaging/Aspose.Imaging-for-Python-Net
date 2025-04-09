# GROUP: MODIFYING_AND_CONVERTING_IMAGES

from aspose.pycore import as_of
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
out_file = os.path.join(get_output_dir(), "result.png")
out_file2 = os.path.join(get_output_dir(), "result2.png")
print("Running example AutoAdjustImageBrightness")    

# Load an existing JPG image
with as_of(Image.load(os.path.join(data_dir, "sample.png")), RasterImage) as image:
	image.normalize_histogram();
	image.save(out_file);
	image.adjust_contrast(30);
	image.save(out_file2);

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	os.remove(out_file2)

print("Finished example AutoAdjustImageBrightness")
