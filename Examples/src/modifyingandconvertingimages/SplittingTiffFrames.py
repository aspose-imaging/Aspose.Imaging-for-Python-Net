import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.tiff import TiffImage
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
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
print("Running example SplittingTiffFrames")
# Create an instance of TiffImage and load the file from disc
with aspycore.as_of(Image.load(os.path.join(data_dir, "SampleTiff1.tiff")),
					TiffImage) as multi_image:
	# Initialize a variable to keep track of the frames in the image, Iterate over the tiff frame collection and Save the image
	i = 0
	for tiff_frame in multi_image.frames:
		output_path = os.path.join(get_output_dir(), f"{i}_out.tiff")
		tiff_frame.save(output_path, TiffOptions(TiffExpectedFormat.TIFF_JPEG_RGB))

		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(output_path)

print("Finished example SplittingTiffFrames")
