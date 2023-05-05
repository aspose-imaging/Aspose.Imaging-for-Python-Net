import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import ApngOptions
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
print("Running example CreateAnimationFromMultipageImage")
data_dir = os.path.join(get_data_root_dir(), "apng")
file_name = "img4.tif"
input_file_path = os.path.join(data_dir, file_name)
output_file_path = os.path.join(get_output_dir(), "img4.tif.500ms.png")
with Image.load(input_file_path) as image:
	# Setting up the default frame duration
	options = ApngOptions()
	options.default_frame_time = 500
	image.save(output_file_path, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)
	
print("Finished example CreateAnimationFromMultipageImage")
