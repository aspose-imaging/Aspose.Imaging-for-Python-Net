from aspose.imaging import Image, SizeF
from aspose.imaging.imageoptions import OdgRasterizationOptions, PngOptions, PdfOptions
import os
import aspose.pycore as aspycore


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

files = ["SmoothingTest.odg", "TextHintTest.odg"]
rasterization_options = OdgRasterizationOptions()
out_files = []
for file in files:
	file_name = os.path.join(data_dir, file)
	with Image.load(file_name) as image:
		rasterization_options.page_size = aspycore.cast(SizeF, image.size)
		out_file_name = os.path.join(get_output_dir(), file_name + ".png")
		obj_init = PngOptions()
		obj_init.vector_rasterization_options = rasterization_options
		image.save(out_file_name, obj_init)
		out_files.append(out_file_name)
		out_file_name = os.path.join(get_output_dir(), file_name + ".pdf")
		obj_init2 = PdfOptions()
		obj_init2.vector_rasterization_options = rasterization_options
		image.save(out_file_name, obj_init2)
		out_files.append(out_file_name)

if 'SAVE_OUTPUT' not in os.environ:
	for file in out_files:
		os.remove(file)
