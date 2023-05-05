import aspose.pycore as aspycore
from aspose.imaging import Image, ColorPaletteHelper
from aspose.imaging.imageoptions import TiffOptions
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat, \
	TiffCompressions, TiffPhotometrics
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
out_file = os.path.join(get_output_dir(), "SampleTiff_out.tiff")

print("Running example CompressingTIFFImagesWithLZWAlgorithm")
# Load an image through file path location or stream
with Image.load(os.path.join(data_dir, "SampleTiff.tiff")) as image:
	# Create an instance of TiffOptions for the resultant image
	output_settings = TiffOptions(TiffExpectedFormat.DEFAULT)
	# Set BitsPerSample, Compression, Photometric mode and graycale palette
	output_settings.bits_per_sample = [4]
	output_settings.compression = TiffCompressions.LZW
	output_settings.photometric = TiffPhotometrics.PALETTE
	output_settings.palette = ColorPaletteHelper.create_4_bit_grayscale(False)
	image.save(out_file, output_settings)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CompressingTIFFImagesWithLZWAlgorithm")
