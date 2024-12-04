# GROUP: MODIFYING_AND_CONVERTING_IMAGES

import aspose.pycore as aspycore
from aspose.imaging import Image, TextRenderingHint, SmoothingMode, SizeF, Rectangle
from aspose.imaging.fileformats.opendocument import OdImage
from aspose.imaging.imageoptions import VectorRasterizationOptions, PngOptions
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
print("Running example UnifyUsageOfCommonOperations")
data_dir = os.path.join(get_data_root_dir(), 'cdr')
file_name = "test.cdr"
input_file_name = os.path.join(data_dir, file_name)
output_file_name_png = os.path.join(get_output_dir(), "output.png")
with Image.load(input_file_name) as image:
	if aspycore.is_assignable(image, OdImage):
		image.crop(Rectangle(92, 179, 260, 197))
	else:
		image.crop(Rectangle(88, 171, 250, 190))

	vector_options = VectorRasterizationOptions()
	vector_options.page_size = aspycore.cast(SizeF, image.size)
	vector_options.text_rendering_hint = TextRenderingHint.SINGLE_BIT_PER_PIXEL
	vector_options.smoothing_mode = SmoothingMode.NONE
	png_options = PngOptions()
	png_options.vector_rasterization_options = vector_options
	image.save(output_file_name_png, png_options)
	
if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name_png)
	
print("Finished example UnifyUsageOfCommonOperations")
