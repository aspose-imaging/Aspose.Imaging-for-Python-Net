# GROUP: MEMORY_STRATEGIES
import aspose.pycore as aspycore
from aspose.imaging import Image, LoadOptions
from aspose.imaging.imageoptions import TiffOptions
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
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
print("Running example OptimizationStrategyInTiff")
obj_init = LoadOptions()
obj_init.buffer_size_hint = 10
out_file = os.path.join(get_output_dir(), "optimizationStrategy_tiff_out.tiff")
with Image.load(os.path.join(data_dir, "sample.tif"), obj_init) as image:
	image.save(out_file, TiffOptions(TiffExpectedFormat.DEFAULT))

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example OptimizationStrategyInTiff")
