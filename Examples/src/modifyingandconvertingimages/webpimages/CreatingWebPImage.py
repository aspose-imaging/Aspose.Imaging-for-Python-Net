# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Image
from aspose.imaging.sources import FileCreateSource
from aspose.imaging.imageoptions import WebPOptions
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
print("Running example CreatingWebPImage")
out_file = os.path.join(get_output_dir(), "CreatingWebPImage_out.webp")
# Create an instance of WebPOptions class and set properties
with WebPOptions() as image_options:
	image_options.lossless = True
	image_options.source = FileCreateSource(out_file, False)
	# Create an instance of image class by using WebOptions instance that you have just created.
	with Image.create(image_options, 500, 500) as image:
		image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CreatingWebPImage")
