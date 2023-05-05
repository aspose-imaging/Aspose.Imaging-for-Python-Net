# GROUP: MEMORY_STRATEGIES
import aspose.pycore as aspycore
from aspose.imaging import Image, LoadOptions
from aspose.imaging.imageoptions import JpegOptions
from aspose.imaging.fileformats.jpeg import JpegCompressionMode, \
	JpegCompressionColorMode, JpegLsInterleaveMode
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
print("Running example OptimizationStrategyInJPEG")
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
file_name = "aspose-logo.jpg"
output_files = []
input_file_name = os.path.join(data_dir, file_name)
print("Memory optimization in JPEG format started..")
obj_init = LoadOptions()
obj_init.buffer_size_hint = 50
with Image.load(input_file_name, obj_init) as image:
	obj_init2 = JpegOptions()
	obj_init2.compression_type = JpegCompressionMode.BASELINE
	obj_init2.quality = 100
	file = os.path.join(get_output_dir(), "outputFile_Baseline.jpg")
	image.save(file, obj_init2)
	output_files.append(file)
	obj_init3 = JpegOptions()
	obj_init3.compression_type = JpegCompressionMode.PROGRESSIVE
	file = os.path.join(get_output_dir(), "outputFile_Progressive.jpg")
	image.save(file, obj_init3)
	output_files.append(file)
	obj_init4 = JpegOptions()
	obj_init4.color_type = JpegCompressionColorMode.Y_CB_CR
	obj_init4.compression_type = JpegCompressionMode.LOSSLESS
	obj_init4.bits_per_channel = 4
	file = os.path.join(get_output_dir(), "outputFile_Lossless.jpg")
	image.save(file, obj_init4)
	output_files.append(file)
	obj_init5 = JpegOptions()
	obj_init5.color_type = JpegCompressionColorMode.Y_CB_CR
	obj_init5.compression_type = JpegCompressionMode.JPEG_LS
	obj_init5.jpeg_ls_interleave_mode = JpegLsInterleaveMode.NONE
	obj_init5.jpeg_ls_allowed_lossy_error = 3
	obj_init5.jpeg_ls_preset = None
	file = os.path.join(get_output_dir(), "outputFile_JpegLs.jpg")
	image.save(file, obj_init5)
	output_files.append(file)

if 'SAVE_OUTPUT' not in os.environ:
	for file in output_files:
		os.remove(file)

print("Finished example OptimizationStrategyInJPEG")
