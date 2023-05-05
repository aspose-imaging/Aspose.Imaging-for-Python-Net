# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.apng import ApngImage
from aspose.imaging.imageoptions import ApngOptions
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
print("Running example GetOriginalOptions")
data_dir = os.path.join(get_data_root_dir(), 'apng')
with aspycore.as_of(Image.load(os.path.join(data_dir, "SteamEngine.png")), ApngImage) as image:
	options = aspycore.as_of(image.get_original_options(), ApngOptions)
	if options.num_plays != 0 or options.default_frame_time != 10 or options.bit_depth != 8:
		print("Exist some errors in default options")

print("Finished example GetOriginalOptions")
