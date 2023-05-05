# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.tiff import TiffImage
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
data_dir = os.path.join(get_data_root_dir(), 'tiff')

print("Running example SupportOfGetOriginalOptions")
file_path = data_dir
input_file = "lichee.tif"
output1 = os.path.join(get_output_dir(), "result1.tiff")
output2 = os.path.join(get_output_dir(), "result2.tiff")
with Image.load(os.path.join(file_path, input_file)) as image:
	image.save(output1, image.get_original_options())
	frame = (aspycore.as_of(image, TiffImage)).frames[0]
	frame.save(output2, frame.get_original_options())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output1)
	os.remove(output2)

print("Finished example SupportOfGetOriginalOptions")
