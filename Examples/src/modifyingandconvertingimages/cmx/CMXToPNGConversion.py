# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, SmoothingMode
from aspose.imaging.imageoptions import CmxRasterizationOptions, PngOptions, PositioningTypes
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
print("Running example CMXToPNGConversion")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cmx')
file_names = ["Rectangle.cmx", "Rectangle+Fill.cmx", "Ellipse.cmx", "Ellipse+fill.cmx", "brushes.cmx", "outlines.cmx", "order.cmx", "many_images.cmx"]
for file_name in file_names:
	out_file = os.path.join(get_output_dir(), file_name + ".docpage.png")
	with Image.load(os.path.join(data_dir, file_name)) as image:
		obj_init = CmxRasterizationOptions()
		obj_init.positioning = PositioningTypes.DEFINED_BY_DOCUMENT
		obj_init.smoothing_mode = SmoothingMode.ANTI_ALIAS
		obj_init2 = PngOptions()
		obj_init2.vector_rasterization_options = obj_init
		image.save(out_file, obj_init2)

	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(out_file)

print("Finished example CMXToPNGConversion")
