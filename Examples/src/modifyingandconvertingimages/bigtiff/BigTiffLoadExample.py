import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import BigTiffOptions
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
print("Running example BigTiffLoadExample")
data_dir = os.path.join(get_data_root_dir(), 'tiff')
file_name = "input-BigTiff.tif"
input_file_path = os.path.join(data_dir, file_name)
output_file_path = os.path.join(get_output_dir(), "result.tiff")
with Image.load(input_file_path) as image:
	image.save(output_file_path, BigTiffOptions(TiffExpectedFormat.TIFF_LZW_RGBA))

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)

print("Finished example BigTiffLoadExample")
