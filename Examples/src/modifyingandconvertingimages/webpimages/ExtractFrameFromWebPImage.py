# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import RasterImage
from aspose.imaging.fileformats.webp import WebPImage
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
data_dir = os.path.join(get_data_root_dir(), 'WebPImage')
out_file = os.path.join(get_output_dir(), "ExtractFrameFromWebPImage.bmp")
print("Running example ExtractFrameFromWebPImage")
# Load an existing WebP image into the instance of WebPImage class.
with WebPImage(os.path.join(data_dir, "asposelogo.webp")) as image:
	if image.page_count > 2:
		# Access a particular frame from WebP image and cast it to RasterImage
		block = aspycore.as_of(image.pages[2], RasterImage)
		# Save the RasterImage to a BMP image.
		block.save(out_file, BmpOptions())

if 'SAVE_OUTPUT' not in os.environ:
	if os.path.exists(out_file):
		os.remove(out_file)

print("Finished example ExtractFrameFromWebPImage")
