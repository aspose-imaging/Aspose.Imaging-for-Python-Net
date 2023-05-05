from aspose.imaging import Image
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
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
output_path = os.path.join(get_output_dir(), "SampleTiff_out.tiff")
print("Running example TiffOptionsConfiguration")
# Load an image through file path location or stream
with Image.load(os.path.join(data_dir, "SampleTiff1.tiff")) as image:
	# Create an instance of TiffOptions while specifying desired format
	# Passing TiffExpectedFormat.TiffJpegRGB will set the compression to 
	# Jpeg and BitsPerPixel according to the RGB color space.
	options = TiffOptions(TiffExpectedFormat.TIFF_JPEG_RGB)
	image.save(output_path, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)
	
print("Finished example TiffOptionsConfiguration")
