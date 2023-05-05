# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.svg import SvgImage
from aspose.imaging.imageoptions import PngOptions, SvgRasterizationOptions
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')

print("Running example SvgNativeResize")
output_file_name_svg = os.path.join(get_output_dir(), "Logotype_10_15_out.png")
# Load the image
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.Svg")),
					SvgImage) as image:
	image.resize(image.width * 10, image.height * 15)
	obj_init = PngOptions()
	obj_init.vector_rasterization_options = SvgRasterizationOptions()
	image.save(output_file_name_svg, obj_init)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name_svg)

print("Finished example SvgNativeResize")
