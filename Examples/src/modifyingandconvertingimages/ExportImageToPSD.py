import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.psd import ColorModes, CompressionMethod
from aspose.imaging.imageoptions import PsdOptions
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
out_file = os.path.join(get_output_dir(), "ExportImageToPSD_output.psd")
print("Running example ExportImageToPSD")
# Load an existing image
with Image.load(os.path.join(data_dir, "sample.bmp")) as image:
	# Create an instance of PsdOptions, Set it`s various properties Save image to disk in PSD format
	psd_options = PsdOptions()
	psd_options.color_mode = ColorModes.RGB
	psd_options.compression_method = CompressionMethod.RAW
	psd_options.version = 4
	image.save(out_file, psd_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ExportImageToPSD")
