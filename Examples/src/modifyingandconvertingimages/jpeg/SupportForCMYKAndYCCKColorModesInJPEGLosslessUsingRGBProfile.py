import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.sources import FileOpenSource
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
cmyk_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), '056_cmyk_custom_profiles.png')

with StreamExtensions.create_memory_stream() as jpeg_stream:
	with open(os.path.join(cmyk_dir, "eciRGB_v2.icc"), "rb") \
			as rgb_profile_stream, \
			open(os.path.join(cmyk_dir, "ISOcoated_v2_FullGamut4.icc"), "rb") \
			as cmyk_profile_stream:
		rgb_color_profile = StreamSource(rgb_profile_stream)
		cmyk_color_profile = StreamSource(cmyk_profile_stream)
		# Save to JPEG Lossless CMYK
		with aspycore.as_of(Image.load(os.path.join(data_dir, "test.jpg")),
							JpegImage) as image:
			with JpegOptions() as options:
				options.color_type = JpegCompressionColorMode.CMYK
				options.compression_type = JpegCompressionMode.LOSSLESS
				# The custom profiles will be used.
				options.rgb_color_profile = rgb_color_profile
				options.cmyk_color_profile = cmyk_color_profile
				image.save(jpeg_stream, options)

		# Load from JPEG Lossless CMYK
		jpeg_stream.seek(0)
		rgb_profile_stream.seek(0)
		cmyk_profile_stream.seek(0)
		with aspycore.as_of(Image.load(jpeg_stream), JpegImage) as image:
			image.rgb_color_profile = rgb_color_profile
			image.cmyk_color_profile = cmyk_color_profile
			image.save(out_file, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
