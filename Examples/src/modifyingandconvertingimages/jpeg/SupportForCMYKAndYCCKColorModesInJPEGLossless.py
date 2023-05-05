import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.jpeg import JpegImage, JpegCompressionColorMode, \
	JpegCompressionMode
from aspose.imaging.imageoptions import JpegOptions, PngOptions
from aspose.imaging.extensions import StreamExtensions
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
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
out_file = os.path.join(get_output_dir(), '056_cmyk.png')
with StreamExtensions.create_memory_stream() as jpeg_stream:
	# Save to JPEG Lossless CMYK
	with aspycore.as_of(Image.load(os.path.join(data_dir, "056.jpg")),
						JpegImage) as image:
		options = JpegOptions()
		options.color_type = JpegCompressionColorMode.CMYK
		options.compression_type = JpegCompressionMode.LOSSLESS
		# The default profiles will be used.
		options.rgb_color_profile = None
		options.cmyk_color_profile = None
		image.save(jpeg_stream, options)

	# Load from JPEG Lossless CMYK
	jpeg_stream.seek(0)
	with aspycore.as_of(Image.load(jpeg_stream), JpegImage) as image:
		image.save(out_file, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
