import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import GifOptions
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
print("Running example ExportAPNGToGif")
data_dir = os.path.join(get_data_root_dir(), 'apng')
file_name = "elephant.png"
input_file_path = os.path.join(data_dir, file_name)
output_file_path = os.path.join(get_output_dir(), "elephant_out.png.gif")
with Image.load(input_file_path) as image:
	# Export to the other animated format
	image.save(output_file_path, GifOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)

print("Finished example ExportAPNGToGif")
