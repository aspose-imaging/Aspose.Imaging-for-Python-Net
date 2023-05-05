# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.png import PngFilterType, PngImage
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
data_dir = os.path.join(get_data_root_dir(), 'png')
out_file = os.path.join(get_output_dir(), "ApplyFilterMethod_out.png")

print("Running example ApplyFilterMethod")
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.png")),
					PngImage) as png:
	# Create an instance of PngOptions, Set the PNG filter method and Save changes to the disc
	options = PngOptions()
	options.filter_type = PngFilterType.PAETH
	png.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ApplyFilterMethod")
