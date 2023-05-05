# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import BmpOptions, SvgRasterizationOptions
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
output_file_name_svg = os.path.join(get_output_dir(), "test.svg_out.bmp")

print("Running example SVGToBMPConversion")
with Image.load(os.path.join(data_dir, "test.svg")) as image:
	options = BmpOptions()
	svg_options = SvgRasterizationOptions()
	svg_options.page_width = 100
	svg_options.page_height = 200
	options.vector_rasterization_options = svg_options
	image.save(output_file_name_svg, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name_svg)
	
print("Finished example SVGToBMPConversion")
