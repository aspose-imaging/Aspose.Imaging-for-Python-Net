from aspose.imaging import Image
from aspose.imaging.imageoptions import PngOptions
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
output_path = os.path.join(get_output_dir(), "sample.png")
print("Running example SupportOfDIB")
with Image.load(os.path.join(data_dir, "sample.dib")) as image:
	print(image.file_format)
	image.save(output_path, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example SupportOfDIB")

