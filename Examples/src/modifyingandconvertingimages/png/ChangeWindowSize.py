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
data_dir = os.path.join(get_data_root_dir(), 'png')
source_file = "template.png"
output_file = os.path.join(get_output_dir(), "result.png")
with aspycore.as_of(Image.load(os.path.join(data_dir, source_file)),
					RasterImage) as image:
	image.binarize_bradley(10, 20)
	image.save(output_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
