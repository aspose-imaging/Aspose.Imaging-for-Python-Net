# GROUP: MEMORY_STRATEGIES
import aspose.pycore as aspycore
from aspose.imaging import Image, LoadOptions
from aspose.imaging.fileformats.djvu import DjvuImage
from aspose.imaging.imageoptions import PngOptions
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
print("Running example OptimizationStrategyInDJVU")
input_file_name = os.path.join(data_dir, "test.djvu")
# Setting a memory limit of 50 megabytes for target loaded image
obj_init = LoadOptions()
obj_init.buffer_size_hint = 50

with aspycore.as_of(Image.load(input_file_name, obj_init), DjvuImage) as image:
	page_number = 2
	for page_num in range(page_number):
		output = os.path.join(get_output_dir(), f"page{page_num}.png")
		image.pages[page_num].save(output, PngOptions())
		
		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(output)

print("Finished example OptimizationStrategyInDJVU")
