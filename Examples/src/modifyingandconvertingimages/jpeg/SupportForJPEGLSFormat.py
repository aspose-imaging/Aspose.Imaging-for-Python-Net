import aspose.pycore as aspycore
from aspose.imaging import Image, Rectangle
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.fileformats.jpeg import JpegImage
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

source_jpeg_file_name = os.path.join(data_dir, "lena24b.jls")
output_png_file_name = os.path.join(get_output_dir(), "lena24b.png")
output_png_rect_file_name = os.path.join(get_output_dir(), "lena24b_rect.png")
# Decoding
with aspycore.as_of(Image.load(source_jpeg_file_name), JpegImage) as jpeg_image:
	jpeg_options = jpeg_image.jpeg_options
	# You can read new options:
	System.print("Compression type:           {0}", jpeg_options.compression_type)
	System.print("Allowed lossy error (NEAR): {0}", jpeg_options.jpeg_ls_allowed_lossy_error)
	System.print("Interleaved mode (ILV):     {0}", jpeg_options.jpeg_ls_interleave_mode)
	System.print("Horizontal sampling:        {0}", jpeg_options.horizontal_sampling)
	System.print("Vertical sampling:          {0}", jpeg_options.vertical_sampling)
	# Save the original JPEG-LS image to PNG.
	jpeg_image.save(output_png_file_name, PngOptions())
	# Save the bottom-right quarter of the original JPEG-LS to PNG
	quarter = Rectangle(jpeg_image.width // 2, jpeg_image.height // 2, jpeg_image.width // 2, jpeg_image.height // 2)
	jpeg_image.save(output_png_rect_file_name, PngOptions(), quarter)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_png_file_name)
	os.remove(output_png_rect_file_name)
