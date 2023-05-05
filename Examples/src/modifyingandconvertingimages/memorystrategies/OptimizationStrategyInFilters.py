# GROUP: MEMORY_STRATEGIES
import aspose.pycore as aspycore
from aspose.imaging import Image, LoadOptions, RasterImage
from aspose.imaging.imagefilters.filteroptions import MedianFilterOptions
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
print("Running example OptimizationStrategyInFilters")
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
file_name = "SampleTiff1.tiff"
output = os.path.join(get_output_dir(), "SampleTiff1.out.tiff")
input_file_name = os.path.join(data_dir, file_name)
print("Memory optimization in Filters started..")
obj_init = LoadOptions()
obj_init.buffer_size_hint = 50
with aspycore.as_of(Image.load(input_file_name, obj_init), RasterImage) as raster_image:
	filter_options = MedianFilterOptions(6)
	raster_image.filter(raster_image.bounds, filter_options)
	raster_image.save(output)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output)
	
print("Finished example OptimizationStrategyInFilters")
