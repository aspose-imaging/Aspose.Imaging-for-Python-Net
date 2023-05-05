# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.fileformats.png import PngColorType
from aspose.imaging.fileformats.cdr import CdrImage
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
print("Running example CdrToPngExample")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cdr')
input_file_name = os.path.join(data_dir, "SimpleShapes.cdr")
out_file = os.path.join(get_output_dir(), "SimpleShapes.png")
with aspycore.as_of(Image.load(input_file_name), CdrImage) as image:
	options = PngOptions()
	options.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
	# Set rasterization options for file format
	options.vector_rasterization_options = aspycore.as_of(
		image.get_default_options(
			[Color.white, image.width, image.height]),
			VectorRasterizationOptions)
	options.vector_rasterization_options.text_rendering_hint = TextRenderingHint.SINGLE_BIT_PER_PIXEL
	options.vector_rasterization_options.smoothing_mode = SmoothingMode.NONE
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CdrToPngExample")

