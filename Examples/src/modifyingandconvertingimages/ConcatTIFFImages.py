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
out_file = os.path.join(get_output_dir(), "ConcatTIFFImages_out.tiff")

print("Running example ConcatTIFFImages")
# Create an instance of TiffImage and load the copied destination image
with aspycore.as_of(Image.load(os.path.join(data_dir, "TestDemo.tif")),
					TiffImage) as image:
	# Create an instance of TiffImage and load the source image
	with aspycore.as_of(Image.load(os.path.join(data_dir, "sample.tif")),
						TiffImage) as image1:
		# Create an instance of TIffFrame and copy active frame of source image, Add copied frame to destination image and  Save the image with changes.
		frame = TiffFrame.copy_frame(image1.active_frame)
		image.add_frame(frame)
		image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ConcatTIFFImages")
