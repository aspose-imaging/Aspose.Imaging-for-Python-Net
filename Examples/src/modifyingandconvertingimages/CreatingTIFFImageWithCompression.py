import aspose.pycore as aspycore
from aspose.imaging.fileformats.tiff import *
from aspose.imaging.fileformats.tiff.enums import *
from aspose.imaging import Image, Color
from aspose.imaging.imageoptions import TiffOptions
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
out_file = os.path.join(get_output_dir(), 
						"SavingRasterImageToTIFFWithCompression_out.tiff")
print("Running example CreatingTIFFImageWithCompression")
# Create an instance of TiffOptions and set its various properties
options = TiffOptions(TiffExpectedFormat.DEFAULT)
options.bits_per_sample = [8, 8, 8]
options.photometric = TiffPhotometrics.RGB
options.xresolution = TiffRational(72)
options.yresolution = TiffRational(72)
options.resolution_unit = TiffResolutionUnits.INCH
options.planar_configuration = TiffPlanarConfigs.CONTIGUOUS
# Set the compression to AdobeDeflate
options.compression = TiffCompressions.ADOBE_DEFLATE
# Or Deflate              
# options.compression = TiffCompressions.DEFLATE;

# Create a new TiffImage with specific size and TiffOptions settings
with TiffImage(TiffFrame(options, 100, 100)) as tiff_image:
	# Loop over the pixels to set the color to red
	for i in range(100):
		tiff_image.active_frame.set_pixel(i, i, Color.red)

	# Save resultant image
	tiff_image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CreatingTIFFImageWithCompression")
