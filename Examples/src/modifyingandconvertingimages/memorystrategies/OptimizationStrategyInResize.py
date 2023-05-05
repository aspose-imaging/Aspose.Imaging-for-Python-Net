# GROUP: MEMORY_STRATEGIES
from aspose.imaging import Image, LoadOptions, ResizeType
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
print("Running example OptimizationStrategyInResize")
file_name = "SampleTiff1.tiff"
output = os.path.join(get_output_dir(), "SampleTiff1.out.tiff")
input_file_name = os.path.join(data_dir, file_name)
# Setting a memory limit of 50 megabytes for target loaded image
obj_init = LoadOptions()
obj_init.buffer_size_hint = 50
with Image.load(input_file_name, obj_init) as image:
	# perform Resize operation
	image.resize(300, 200, ResizeType.LANCZOS_RESAMPLE)
	image.save(output)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output)

print("Finished example OptimizationStrategyInResize")
