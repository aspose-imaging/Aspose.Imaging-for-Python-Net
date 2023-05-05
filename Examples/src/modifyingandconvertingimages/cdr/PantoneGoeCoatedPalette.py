# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.cdr import CdrImage
from aspose.imaging.imageoptions import *
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
print("Running example PantoneGoeCoatedPalette")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cdr')
input_file_name = os.path.join(data_dir, "test2.cdr")
out_file = os.path.join(get_output_dir(), "result.png")
with aspycore.as_of(Image.load(input_file_name), CdrImage) as image:
	obj_init = CdrRasterizationOptions()
	obj_init.positioning = PositioningTypes.RELATIVE
	obj_init2 = PngOptions()
	obj_init2.vector_rasterization_options = obj_init
	image.save(out_file, obj_init2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example PantoneGoeCoatedPalette")
