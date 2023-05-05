import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
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
data_dir = os.path.join(get_data_root_dir(), 'tiff')
source_file_path = "testTileDeflate.tif"
output_path = os.path.join(get_output_dir(), "testTileDeflate Cmyk Icc.tif")
options = TiffOptions(TiffExpectedFormat.TIFF_LZW_CMYK)
with Image.load(os.path.join(data_dir, source_file_path)) as image:
	image.save(output_path, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)
