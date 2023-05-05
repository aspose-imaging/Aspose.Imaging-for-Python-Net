from aspose.imaging import Image
from aspose.imaging.imageoptions import GifOptions
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
output_path = os.path.join(get_output_dir(), "anim_lossy-80.gif")
# Sets the maximum allowed pixel difference. If greater than zero, lossy compression will be used.
# Recommended value for optimal lossy compression is 80. 30 is very light compression, 200 is heavy.
gif_export = GifOptions()
gif_export.max_diff = 80
with Image.load(os.path.join(data_dir, "Animation.gif")) as image:
	image.save(output_path, gif_export)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)
