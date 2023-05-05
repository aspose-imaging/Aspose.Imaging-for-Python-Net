import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.bmp import BmpImage
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
out_file = os.path.join(get_output_dir(), "binarized_out.png")
print("Running example Bradleythreshold")
data_dir = os.path.join(data_dir, "sample.bmp")
# Load an existing image.
with aspycore.as_of(Image.load(data_dir), BmpImage) as objimage:
	# Define threshold value, Call binarize_bradley method and pass the threshold value as parameter and Save the output image
	threshold = 0.15
	objimage.binarize_bradley(threshold)
	objimage.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example Bradleythreshold")
