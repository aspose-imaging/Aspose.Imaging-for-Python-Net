# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, FileFormat
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
print("Running example SupportOfCDR")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'cdr')
input_file_name = os.path.join(data_dir, "test.cdr")
expected_file_format = FileFormat.CDR.value
with Image.load(input_file_name) as image:
	if expected_file_format != image.file_format:
		raise Exception(f"Image FileFormat is not {expectedFileFormat}")

print("Finished example SupportOfCDR")
