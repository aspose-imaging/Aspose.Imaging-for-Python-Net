# GROUP: ADDITIONAL_FEATURES
import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.png import PngColorType
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.masking import *
from aspose.imaging.masking.options import *
from aspose.imaging.masking.result import *
from aspose.imaging.sources import StreamSource
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
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
print("Running example GraphCutAutoMasking")
input_file = os.path.join(data_dir, "input.png")
output_file = os.path.join(get_output_dir(), "output.png")
results = None
with aspycore.as_of(Image.load(input_file), RasterImage) as image:
	# To use Graph Cut with auto calculated strokes, AutoMaskingGraphCutOptions is used.
	with PngOptions() as png_options:
		png_options.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
		png_options.source = StreamSource()
		options = AutoMaskingGraphCutOptions()
		options.calculate_default_strokes = True
		options.feathering_radius = (max(image.width, image.height) // 500) + 1
		options.method = SegmentationMethod.GRAPH_CUT
		options.decompose = False
		options.export_options = png_options
		options.background_replacement_color = Color.transparent
		results = ImageMasking(image).decompose(options)
		with aspycore.as_of(results[1].get_image(), RasterImage) as result_image:
			obj_init3 = PngOptions()
			obj_init3.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
			result_image.save(output_file, obj_init3)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file)
	
print("Finished example GraphCutAutoMasking")
