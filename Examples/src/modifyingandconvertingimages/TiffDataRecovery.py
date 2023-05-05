from aspose.imaging import Image, DataRecoveryMode, Color, LoadOptions
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
print("Running example TiffDataRecovery")
# Create an instance of LoadOptions and set LoadOptions properties
load_options = LoadOptions()
load_options.data_recovery_mode = DataRecoveryMode.CONSISTENT_RECOVER
load_options.data_background_color = Color.red
# Create an instance of Image and load a damaged image by passing the instance of LoadOptions
with Image.load(os.path.join(data_dir, "SampleTiff1.tiff"), load_options) as image:
	# do something
	pass

print("Finished example TiffDataRecovery")
