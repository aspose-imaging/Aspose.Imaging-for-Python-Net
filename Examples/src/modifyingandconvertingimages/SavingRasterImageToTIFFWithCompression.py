import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage
from aspose.imaging.fileformats.tiff import *
from aspose.imaging.fileformats.tiff.enums import *
from aspose.imaging.imageoptions import TiffOptions
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
output_path = os.path.join(get_output_dir(), "SavingRasterImage_out.tiff")
print("Running example SavingRasterImageToTIFFWithCompression")
# Create an instance of TiffOptions and set its various properties
options = TiffOptions(TiffExpectedFormat.DEFAULT)
options.bits_per_sample = [8, 8, 8]
options.photometric = TiffPhotometrics.RGB
options.xresolution = TiffRational(72)
options.yresolution = TiffRational(72)
options.resolution_unit = TiffResolutionUnits.INCH
options.planar_configuration = TiffPlanarConfigs.CONTIGUOUS
# Set the Compression to AdobeDeflate
options.compression = TiffCompressions.ADOBE_DEFLATE
# Or Deflate         
# Options.compression = TiffCompressions.DEFLATE;
# Load an existing image in an instance of RasterImage
with aspycore.as_of(Image.load(os.path.join(data_dir, "SampleTiff1.tiff")),
					RasterImage) as image:
	# Create a new TiffImage from the RasterImage and Save the resultant image while passing the instance of TiffOptions
	with TiffImage(TiffFrame(image)) as tiff_image:
		tiff_image.save(output_path, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example SavingRasterImageToTIFFWithCompression")
