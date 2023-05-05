# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, SizeF
from aspose.imaging.imageoptions import PngOptions, OdgRasterizationOptions
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
data_dir = os.path.join(get_data_root_dir(), 'otg')

print("Running example SupportOfFODG")
file_name = "sample.fodg"
input_file_name = os.path.join(data_dir, file_name)
out_file = os.path.join(get_output_dir(), file_name + ".png")
with Image.load(input_file_name) as image:
	obj_init = OdgRasterizationOptions()
	obj_init.page_size = aspycore.cast(SizeF, image.size)
	obj_init2 = PngOptions()
	obj_init2.vector_rasterization_options = obj_init
	image.save(out_file, obj_init2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example SupportOfFODG")
