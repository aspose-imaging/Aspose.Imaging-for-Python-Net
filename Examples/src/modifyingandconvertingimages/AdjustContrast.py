from aspose.imaging import Image, RasterImage
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat, TiffPhotometrics
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
out_file = os.path.join(get_output_dir(), "AdjustContrast_out.tiff")
print("Running example AdjustBrightness")
# Load an image in an instance of Image
with Image.load(os.path.join(data_dir, "aspose-logo.jpg")) as image__1:
	# Cast object of Image to RasterImage
	raster_image = aspycore.as_of(image__1, RasterImage)
	# Check if RasterImage is cached and Cache RasterImage for better performance
	if not raster_image.is_cached:
		raster_image.cache_data()

	# Adjust the contrast
	raster_image.adjust_contrast(10)
	# Create an instance of TiffOptions for the resultant image, Set various properties for the object of TiffOptions and Save the resultant image to TIFF format
	tiff_options = TiffOptions(TiffExpectedFormat.DEFAULT)
	tiff_options.bits_per_sample = [8, 8, 8]
	tiff_options.photometric = TiffPhotometrics.RGB
	raster_image.save(out_file, tiff_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example AdjustContrast")
