# GROUP: TEST_FILE_FORMATS
from aspose.pycore import as_of
from aspose.imaging.fileformats.dicom import DicomImage
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
print("Running example ModifyDicomTags")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'dicom')
out_file = os.path.join(get_output_dir(), 'output.dcm')

with as_of(Image.load(dataDir + "file.dcm"), DicomImage) as image:
	image.file_info.update_tag_at(33, "Test Patient") # "Patient's Name"
	image.file_info.add_tag("Angular View Vector", 234)
	image.file_info.remove_tag_at(29) # "Station Name"
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ModifyDicomTags")
