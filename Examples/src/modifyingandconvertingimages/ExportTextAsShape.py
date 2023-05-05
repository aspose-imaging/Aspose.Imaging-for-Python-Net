import aspose.pycore as aspycore
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import SvgOptions, EmfRasterizationOptions
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), "TextAsShapes_out.svg")
out_file2 = os.path.join(get_output_dir(), "TextAsShapesFalse_out.svg")
print("Running example ExportTextAsShape")
with Image.load(os.path.join(data_dir, "Picture1.emf")) as image:
	emf_rasterization_options = EmfRasterizationOptions()
	emf_rasterization_options.background_color = Color.white
	emf_rasterization_options.page_width  = float(image.width)
	emf_rasterization_options.page_height = float(image.height)
	obj_init = SvgOptions()
	obj_init.vector_rasterization_options = emf_rasterization_options
	obj_init.text_as_shapes = True
	image.save(out_file, obj_init)
	obj_init2 = SvgOptions()
	obj_init2.vector_rasterization_options = emf_rasterization_options
	obj_init2.text_as_shapes = False
	image.save(out_file2, obj_init2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	os.remove(out_file2)

print("Finished example ExportTextAsShape")
