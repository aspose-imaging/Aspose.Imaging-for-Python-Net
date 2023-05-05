# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.fileformats.png import PngImage, PngColorType
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
output_file = os.path.join(get_output_dir(), "SpecifyBitDepth_out.png")
print("Running example SpecifyBitDepth")
# Load an existing PNG image
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.png")),
					PngImage) as png:
	# Create an instance of PngOptions, Set the desired color_type, bit_depth according to the specified color_type and save image
	options = PngOptions()
	options.color_type = PngColorType.GRAYSCALE
	options.bit_depth = 1
	png.save(output_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
	
print("Finished example SpecifyBitDepth")
