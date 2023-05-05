# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.gif import GifImage
from aspose.imaging.fileformats.gif.blocks import GifFrameBlock
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
print("Running example SupportGifFrameDurationAndNumberOfCycles")
data_dir = os.path.join(get_data_root_dir(), 'gif')
filepath = os.path.join(data_dir, "ezgif.com-gif-maker(1)___.gif")
output_path = os.path.join(get_output_dir(), "output.gif")
with aspycore.as_of(Image.load(filepath), GifImage) as image:
	image.set_frame_time(2000)
	(aspycore.as_of(image.pages[0], GifFrameBlock)).frame_time = 200
	obj_init = GifOptions()
	obj_init.loops_count = 4
	image.save(output_path, obj_init)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)

print("Finished example SupportGifFrameDurationAndNumberOfCycles")
