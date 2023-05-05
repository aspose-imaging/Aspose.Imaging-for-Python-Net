from aspose.imaging import Image
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
output_path = os.path.join(get_output_dir(), "output.png")
print("Running example FileExtensionAwareSave")
# Loading and Rotating Image
with Image.load(os.path.join(data_dir, "aspose-logo.jpg")) as image:
	image.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example FileExtensionAwareSave")
