import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.gif import *
from aspose.imaging.fileformats.gif.blocks import *
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
print("Running example CreateGifUsingAddPage")

def load_frames(directory):
	for file_path in os.listdir(directory):
		yield aspycore.as_of(Image.load(os.path.join(directory, file_path)), RasterImage)

# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'png')
out_file = os.path.join(get_output_dir(), "Multipage.gif")
# Load frames
frames = load_frames(os.path.join(data_dir, "Animation frames"))
# Create GIF image using the first frame
with GifImage(GifFrameBlock(next(frames))) as image:
	# Add frames to the GIF image using the AddPage method
	for img in frames:
		image.add_page(img)
	# Save GIF image
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CreateGifUsingAddPage")
