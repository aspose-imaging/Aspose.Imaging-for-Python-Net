# GROUP: MEMORY_STRATEGIES
import aspose.pycore as aspycore
from aspose.imaging import Image, LoadOptions
from aspose.imaging.sources import FileCreateSource
from aspose.imaging.imageoptions import Jpeg2000Options
from aspose.imaging.fileformats.jpeg2000 import Jpeg2000Codec
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
print("Running example OptimizationStrategyInJPEG2000")
# Setting a memory limit of 100 megabytes for target loaded image
# JP2 codec
obj_init = LoadOptions()
obj_init.buffer_size_hint = 100
out_file = os.path.join(get_output_dir(), "outputFile.jp2")
out_file2 = os.path.join(get_output_dir(), "createdFile.jp2")
with Image.load(os.path.join(data_dir, "inputFile.jp2"), obj_init) as image:
	image.save(out_file)

# Setting a memory limit of 100 megabytes for target created image
# JP2 codec
create_options = Jpeg2000Options()
create_options.codec = Jpeg2000Codec.JP2
create_options.buffer_size_hint = 100
create_options.source = FileCreateSource(out_file2, False)
with Image.create(create_options, 1000, 1000) as image:
	image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	os.remove(out_file2)

print("Finished example OptimizationStrategyInJPEG2000")
