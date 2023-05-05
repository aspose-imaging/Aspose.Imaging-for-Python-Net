import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.jpeg import JpegImage, \
	JpegCompressionColorMode, JpegCompressionMode
from aspose.imaging.imageoptions import JpegOptions
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
data_dir = os.path.join(get_data_root_dir(), 'gif')
out_file = os.path.join(get_output_dir(), 'ezgif.com-gif-maker(1)___.gif.jpg')
with Image.load(os.path.join(data_dir, "ezgif.com-gif-maker(1)___.gif")) \
		as original:
	jpeg_options = JpegOptions()
	jpeg_options.color_type = JpegCompressionColorMode.GRAYSCALE
	jpeg_options.compression_type = JpegCompressionMode.PROGRESSIVE
	original.save(out_file, jpeg_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
