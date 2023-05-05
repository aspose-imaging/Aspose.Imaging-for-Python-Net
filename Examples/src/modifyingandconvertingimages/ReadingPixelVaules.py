import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, LoadOptions
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
data_dir = os.path.join(get_data_root_dir(), 'tiff')
file_name = "16bit Uncompressed, BigEndian, Rgb, Contiguous Gamma1.0.Small.tif"
# ICC profile is not applied for 16-bit color components at the moment, so disable that option explicitly.
load_options = LoadOptions()
load_options.use_icc_profile_conversion = False
with aspycore.as_of(Image.load(os.path.join(data_dir, file_name), load_options),
					RasterImage) as image:
	desired_area = image.bounds
	colors64_bit = image.load_argb_64_pixels(desired_area)	
	image_width = image.width
	for y in range(desired_area.top, desired_area.bottom):
		for x in range(desired_area.left, desired_area.right):
			offset = y * image_width + x
			color64 = colors64_bit[offset]
			alpha = ((color64 >> 48) & 0xfff)
			red = ((color64 >> 32) & 0xfff)
			green = ((color64 >> 16) & 0xfff)
			blue = (color64 & 0xfff)
			print(f"A={alpha}, R={red}, G={green}, B={blue}")
