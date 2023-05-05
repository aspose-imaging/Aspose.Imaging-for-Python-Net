# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import SvgOptions, WmfRasterizationOptions
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
data_dir = os.path.join(get_data_root_dir(), 'svg')
print("Running example ConvOfOtherFormatsToSVG")
output_file_name_svg = os.path.join(get_output_dir(), "yoursvg.svg")
with Image.load(os.path.join(data_dir, "mysvg.svg")) as image:
	with open(output_file_name_svg, "w+b") as fs:
		image.save(fs)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name_svg)
	
print("Finished example ConvOfOtherFormatsToSVG")
