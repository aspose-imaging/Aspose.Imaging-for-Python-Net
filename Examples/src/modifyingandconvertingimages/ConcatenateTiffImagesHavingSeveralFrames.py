import aspose.pycore as aspycore
from aspose.imaging.fileformats.tiff import TiffImage, TiffFrame
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat, \
	TiffOrientations, TiffPhotometrics, TiffCompressions, TiffFillOrders
from aspose.imaging import Image
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
out_file = os.path.join(get_output_dir(), "ConcatenateTiffImagesHavingSeveralFrames_out.tiff")

print("Running example ConcatenateTiffImagesHavingSeveralFrames")
files = [os.path.join(data_dir, "TestDemo.tif"),
		 os.path.join(data_dir, "sample.tif")]
create_options = TiffOptions(TiffExpectedFormat.DEFAULT)
create_options.bits_per_sample = [1]
create_options.orientation = TiffOrientations.TOP_LEFT
create_options.photometric = TiffPhotometrics.MIN_IS_BLACK
create_options.compression = TiffCompressions.CCITT_FAX3
create_options.fill_order = TiffFillOrders.LSB_2_MSB
# Create a new image by passing the TiffOptions and size of first frame, we will remove the first frame at the end, cause it will be empty
output = None
images = []
try:
	for file in files:
		# Create an instance of TiffImage and load the source image
		input_ = aspycore.as_of(Image.load(file), TiffImage)
		images.append(input_)
		for frame in input_.frames:
			if output is None:
				# Create a new tiff image with first frame defined.
				output = TiffImage(TiffFrame.copy_frame(frame))
			else:
				# Add copied frame to destination image
				output.add_frame(TiffFrame.copy_frame(frame))
	if output is not None:
		# Save the result
		output.save(out_file, create_options)
finally:
	for image in images:
		with image as _:
			# do this for disposing
			pass

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConcatenateTiffImagesHavingSeveralFrames")
