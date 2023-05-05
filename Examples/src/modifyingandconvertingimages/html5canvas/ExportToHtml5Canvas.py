import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import SvgRasterizationOptions, Html5CanvasOptions
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
print("Running example ExportToHtml5Canvas")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'svg')
out_file = os.path.join(get_output_dir(), "Sample.html")
with Image.load(os.path.join(data_dir, "Sample.svg")) as image:
	obj_init = SvgRasterizationOptions()
	obj_init.page_width = 100
	obj_init.page_height = 100
	obj_init2 = Html5CanvasOptions()
	obj_init2.vector_rasterization_options = obj_init
	image.save(out_file, obj_init2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ExportToHtml5Canvas")
