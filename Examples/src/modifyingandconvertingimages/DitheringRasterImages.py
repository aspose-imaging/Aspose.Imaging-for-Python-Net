import aspose.pycore as aspycore
from aspose.imaging import Image, DitheringMethod
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), "SampleImage_out.bmp")
print("Running example DitheringRasterImages")
# Create an instance of JpegImage and load an image as of JpegImage
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")),
					JpegImage) as image:
	# Peform Floyd Steinberg dithering on the current image and Save the resultant image
	image.dither(DitheringMethod.THRESHOLD_DITHERING, 4)
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example DitheringRasterImages")
