import aspose.pycore as aspycore
from aspose.imaging import Image, IntRange
from aspose.imaging.imageoptions import TiffOptions, MultiPageOptions
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
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
print("Running example SupportOfFullFrameGif")
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
file_name = "Animation.gif"
input_file_path = os.path.join(data_dir, file_name)
output_file_path = os.path.join(get_output_dir(), file_name + "_FullFrame.tif")
output_file_path1 = os.path.join(get_output_dir(), file_name + "_NonFullFrame.tif")
with Image.load(input_file_path) as image:
	obj_init = TiffOptions(TiffExpectedFormat.TIFF_DEFLATE_RGB)
	obj_init.multi_page_options = MultiPageOptions(IntRange(2, 5))
	obj_init.full_frame = True
	image.save(output_file_path, obj_init)
	obj_init2 = TiffOptions(TiffExpectedFormat.TIFF_DEFLATE_RGB)
	obj_init2.multi_page_options = MultiPageOptions(IntRange(2, 5))
	image.save(output_file_path1, obj_init2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)
	os.remove(output_file_path1)
	
print("Finished example SupportOfFullFrameGif")
