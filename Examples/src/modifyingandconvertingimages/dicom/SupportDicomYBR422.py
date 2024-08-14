# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Image
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
data_dir = os.path.join(get_data_root_dir(), 'dicom')
out_file = os.path.join(get_output_dir(), 'SupportDicomYBR422.png')

input_path = os.path.join(data_dir, "input.dcm")
with Image.load(input_path) as image:
	image.save(out_file);

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
