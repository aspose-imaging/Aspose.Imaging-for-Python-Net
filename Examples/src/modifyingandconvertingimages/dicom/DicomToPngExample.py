# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import PngOptions
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
print("Running example DicomToPngExample")
input_file = os.path.join(data_dir, "MultiframePage1.dicom")
out_file = os.path.join(get_output_dir(), "MultiframePage1.png")
with aspycore.as_of(Image.load(input_file), DicomImage) as image:
	options = PngOptions()
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example DicomToPngExample")
