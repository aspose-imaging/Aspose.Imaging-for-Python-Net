import aspose.pycore as aspycore
from aspose.imaging.fileformats.tiff import TiffImage, TiffFrame
from aspose.imaging import Image
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
out_file = os.path.join(get_output_dir(), "ConcatenatingTIFFImagesfromStream_out.tiff")

print("Running example ConcatenatingTIFFImagesfromStream")
# Create instances of FileStream and initialize with Tiff images
with open(os.path.join(data_dir, "TestDemo.tif"), "rb") as file_stream, \
	open(os.path.join(data_dir, "sample1.tif"), "rb") as file_stream1:
	# Create an instance of TiffImage and load the destination image from filestream
	with aspycore.as_of(Image.load(file_stream), TiffImage) as image:
		# Create an instance of TiffImage and load the source image from filestream
		with aspycore.as_of(Image.load(file_stream1), TiffImage) as image1:
			# Create an instance of TIffFrame and copy active frame of source image
			frame = TiffFrame.copy_frame(image1.active_frame)
			# Add copied frame to destination image
			image.add_frame(frame)

		# Save the image with changes
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConcatenatingTIFFImagesfromStream")
