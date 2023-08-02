# GROUP: MODIFYING_AND_CONVERTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Point
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
data_dir = os.path.join(get_data_root_dir(), 'png')
out_file = os.path.join(get_output_dir(), "blended.png")

print("Running example AddAlphaBlendingForImage")
with aspycore.as_of(Image.load(os.path.join(data_dir, "image0.png")), RasterImage) as background:
	with aspycore.as_of(Image.load(os.path.join(data_dir, "aspose_logo.png")), RasterImage) as overlay:
		center = Point((background.width - overlay.width) // 2, (background.height - overlay.height) // 2)
		background.blend(center, overlay, overlay.bounds, 127)
		background.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ApplyFilterMethod")
