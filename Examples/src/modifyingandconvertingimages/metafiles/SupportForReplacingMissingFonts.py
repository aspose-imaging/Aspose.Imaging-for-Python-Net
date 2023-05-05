# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, Color, FontSettings
from aspose.imaging.imageoptions import *
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
data_dir = os.path.join(get_data_root_dir(), 'metafiles')

FontSettings.set_default_font_name("Comic Sans MS")
files = ["Fonts.emf"]
options = [EmfRasterizationOptions()]
print("Running example SupportForReplacingMissingFonts")
i = 0
for file in files:
	out_file = os.path.join(get_output_dir(), file + ".png")
	with Image.load(os.path.join(data_dir, file)) as img:
		options[i].page_width = round(img.width)
		options[i].page_height = round(img.height)
		obj_init = PngOptions()
		obj_init.vector_rasterization_options = options[i]
		img.save(out_file, obj_init)
	i += 1
	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(out_file)

print("Finished example SupportForReplacingMissingFonts")
