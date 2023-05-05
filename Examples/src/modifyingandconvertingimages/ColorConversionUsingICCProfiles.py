import aspose.pycore as aspycore
from aspose.imaging import Image, Rectangle
from aspose.imaging.fileformats.jpeg import JpegImage
from aspose.imaging.sources import StreamSource
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
print("Running example ColorConversionUsingICCProfiles")
# Load an existing JPG image
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo_tn.jpg")),
					JpegImage) as image:
	with open(os.path.join(data_dir, "rgb.icc"), "rb") as rgb, \
		open(os.path.join(data_dir, "cmyk.icc"), "rb") as cmyk:
		cmykprofile = StreamSource(cmyk)
		rgbprofile = StreamSource(rgb)
		image.rgb_color_profile = rgbprofile
		image.cmyk_color_profile = cmykprofile
		colors = image.load_pixels(Rectangle(0, 0, image.width, image.height))
		print(colors)

print("Finished example ColorConversionUsingICCProfiles")
