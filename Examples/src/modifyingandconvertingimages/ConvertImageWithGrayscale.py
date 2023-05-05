import aspose.pycore as aspycore
from aspose.imaging.fileformats.jpeg import JpegCompressionColorMode
from aspose.imaging import Image
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
print("Running example ConvertImageWithGrayscale")
color_types = [JpegCompressionColorMode.GRAYSCALE,
			   JpegCompressionColorMode.Y_CB_CR,
			   JpegCompressionColorMode.RGB,
			   JpegCompressionColorMode.CMYK,
			   JpegCompressionColorMode.YCCK]
source_file_names = ["Grayscale.jpg", "Grayscale.jpg", "Grayscale.jpg", 
					 "Grayscale.jpg", "Grayscale.jpg"]
options = JpegOptions()
options.bits_per_channel = 12
for color_type in color_types:
	options.color_type = color_type
	file_name = os.path.join(get_output_dir(), color_type.name + " 12-bit.jpg")
	with Image.load(os.path.join(data_dir, source_file_names[i])) as image:
		image.save(file_name, options)

	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(file_name)

print("Finished example ConvertImageWithGrayscale")
