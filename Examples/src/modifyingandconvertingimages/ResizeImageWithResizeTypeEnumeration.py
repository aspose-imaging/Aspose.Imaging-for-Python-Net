import aspose.pycore as aspycore
from aspose.imaging import Image, ResizeType
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
output_path = os.path.join(get_output_dir(), "ResizeImageWithResizeTypeEnumeration_out.png")
print("Running example ResizeImageWithResizeTypeEnumeration")
# Load an image from disk
with Image.load(os.path.join(data_dir, "aspose-logo.jpg")) as image:
	if not image.is_cached:
		image.cache_data()

	# Specifying only height, width and ResizeType
	new_width = image.width // 2
	image.resize_width_proportionally(new_width, ResizeType.LANCZOS_RESAMPLE)
	new_height = image.height // 2
	image.resize_height_proportionally(new_height, ResizeType.NEAREST_NEIGHBOUR_RESAMPLE)
	image.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example ResizeImageWithResizeTypeEnumeration")
