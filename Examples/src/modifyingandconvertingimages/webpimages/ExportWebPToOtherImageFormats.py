# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Image
from aspose.imaging.imageoptions import BmpOptions
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
data_dir = os.path.join(get_data_root_dir(), 'WebPImage')
out_file = os.path.join(get_output_dir(), "ExportWebPToOtherImageFormats_out.bmp")
print("Running example ExportWebPToOtherImageFormats")
# Load WebP image into the instance of image class.
with Image.load(os.path.join(data_dir, "asposelogo.webp")) as image:
	# Save the image in WebP format.
	image.save(out_file, BmpOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ExportWebPToOtherImageFormats")
