from aspose.imaging import Image, RasterImage
from aspose.imaging.magicwand import *
from aspose.imaging.magicwand.imagemasks import *
from aspose.pycore import as_of
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
output_path = os.path.join(get_output_dir(), "result.png")

with as_of(Image.load(os.path.join(data_dir, "src.png")), RasterImage) as image:
	wand_settings = MagicWandSettings(1482, 346)
	wand_settings.threshold = 69
	feather_settings = FeatheringSettings()
	feather_settings.size = 3
	
	# Create a new mask using magic wand tool based on tone and color of pixel {845, 128}
	wand_tool = MagicWandTool.select(image, MagicWandSettings(845, 128))
	# Union the existing mask with the specified one created by magic wand tool
	wand_tool.union(MagicWandSettings(416, 387))
	# Invert the existing mask
	wand_tool.invert()
	# Subtract the specified mask created by magic wand tool from the existing one 
	wand_tool.subtract(wand_settings)
	# Subtract four specified rectangle masks from the existing mask one by one
	wand_tool.subtract(RectangleMask(0, 0, 800, 150))\
		.subtract(RectangleMask(0, 380, 600, 220))\
		.subtract(RectangleMask(930, 520, 110, 40))\
		.subtract(RectangleMask(1370, 400, 120, 200))
	# Feather mask with specified settings
	wand_tool.get_feathered(feather_settings)
	# Apply mask to the image
	wand_tool.apply()
	image.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)
