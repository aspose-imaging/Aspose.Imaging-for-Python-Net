import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.png import PngImage
from aspose.imaging.fileformats.jpeg import JpegImage, JpegCompressionMode
from aspose.imaging.imageoptions import PngOptions, JpegOptions
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
print("Running example SupportForJPEG")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
bpp = 2
# The origin PNG with 8 bits per sample
origin_png_file_name = os.path.join(data_dir, "lena_16g_lin.png")
# The output JPEG-LS with 2 bits per sample.
output_jpeg_file_name = os.path.join(get_output_dir(), f"lena24b {bpp}-bit Gold.jls")
with aspycore.as_of(Image.load(origin_png_file_name), PngImage) as png_image:
	jpeg_options = JpegOptions()
	jpeg_options.bits_per_channel = bpp
	jpeg_options.compression_type = JpegCompressionMode.JPEG_LS
	png_image.save(output_jpeg_file_name, jpeg_options)

# The output PNG is produced from JPEG-LS to check image visually.
output_png_file_name = os.path.join(get_output_dir(), f"lena24b {bpp}-bit Gold.png")
with aspycore.as_of(Image.load(output_jpeg_file_name), JpegImage) as jpeg_image:
	jpeg_image.save(output_png_file_name, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_jpeg_file_name)
	os.remove(output_png_file_name)

print("Finished example SupportForJPEG")
