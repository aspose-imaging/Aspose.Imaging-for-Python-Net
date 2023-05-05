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

input_file_name = os.path.join(data_dir, "thistlegirl_wmfsample.wmf")
output_file_name_svg = os.path.join(get_output_dir(), "thistlegirl_wmfsample.svg")
print("Running example ConvertWMFToSVG")
with Image.load(input_file_name) as image:
	rasterization_options = WmfRasterizationOptions()
	rasterization_options.background_color = Color.white_smoke
	rasterization_options.page_width = float(image.width)
	rasterization_options.page_height = float(image.height)
	obj_init = SvgOptions()
	obj_init.vector_rasterization_options = rasterization_options
	image.save(output_file_name_svg, obj_init)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name_svg)
	
print("Finished example ConvertWMFToSVG")

