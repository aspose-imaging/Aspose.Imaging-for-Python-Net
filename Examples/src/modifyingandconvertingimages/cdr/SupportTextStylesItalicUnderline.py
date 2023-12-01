# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Image, FontSettings
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
print("Running example SupportTextStylesItalicUnderline")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cdr')
input_file_name = os.path.join(data_dir, "test3.cdr")
out_file = os.path.join(get_output_dir(), "test3.cdr.jpg")
FontSettings.set_fonts_folder(os.path.join(get_data_root_dir(), 'Fonts'))

with Image.load(input_file_name) as image:
	image.save(out_file)
	
if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example SupportTextStylesItalicUnderline")
