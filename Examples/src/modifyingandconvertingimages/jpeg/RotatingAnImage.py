# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, RotateFlipType
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
out_file = os.path.join(get_output_dir(), 'RotatingAnImage_out.jpg')
print("Running example RotatingAnImage")
# Loading and Rotating Image
with Image.load(os.path.join(data_dir, "aspose-logo.jpg")) as image:
	image.rotate_flip(RotateFlipType.ROTATE_270_FLIP_NONE)
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example RotatingAnImage")
