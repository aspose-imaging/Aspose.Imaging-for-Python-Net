# GROUP: MEMORY_STRATEGIES
from aspose.imaging import Image, LoadOptions, RotateFlipType
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
print("Running example OptimizationStrategyInRotate")
file_name = "SampleTiff1.tiff"
input_file_name = os.path.join(data_dir, file_name)
# Setting a memory limit of 50 megabytes for target loaded image
obj_init = LoadOptions()
obj_init.buffer_size_hint = 50
with Image.load(input_file_name, obj_init) as image:
	# perform RotateFlip operation
	image.rotate_flip(RotateFlipType.ROTATE_90_FLIP_NONE)
	# perform Rotate operation
	(aspycore.as_of(image, RasterImage)).rotate(60)

print("Finished example OptimizationStrategyInRotate")
