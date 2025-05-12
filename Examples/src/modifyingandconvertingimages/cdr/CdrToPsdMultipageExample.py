# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, TextRenderingHint, SmoothingMode
from aspose.imaging.fileformats.cdr import CdrImage
from aspose.imaging.imageoptions import PsdOptions, MultiPageOptions, VectorRasterizationOptions
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
print("Running example CdrToPsdMultipageExample")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cdr')
input_file_name = os.path.join(data_dir, "MultiPage.cdr")
out_file = os.path.join(get_output_dir(), "MultiPageOut.psd")
with aspycore.as_of(Image.load(input_file_name), CdrImage) as image:
	options = PsdOptions()
	# By default if image is multipage image all pages exported
	options.multi_page_options = MultiPageOptions()
	# Optional parameter that indicates to export multipage image as one
	# layer (page) otherwise it will be exported page to page
	options.multi_page_options.merge_layers = True
	# Set rasterization options for file format
	options.vector_rasterization_options = image.get_default_options(
			[Color.white, image.width, image.height]).vector_rasterization_options
	options.vector_rasterization_options.text_rendering_hint = TextRenderingHint.SINGLE_BIT_PER_PIXEL
	options.vector_rasterization_options.smoothing_mode = SmoothingMode.NONE
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CdrToPsdMultipageExample")
