# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
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
data_dir = os.path.join(get_data_root_dir(), 'jpeg')
out_file = os.path.join(get_output_dir(), 'aspose-logo_out.jpg')
print("Running example AutoCorrectOrientationOfJPEGImages")
# Load a Jpeg image from file path location or stream
with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose-logo.jpg")), JpegImage) \
	as image:
	# Perform the automatic rotation on the image depending on the orientation data stored in the EXIF and  Save the result on disc or stream
	image.auto_rotate()
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example AutoCorrectOrientationOfJPEGImages")
