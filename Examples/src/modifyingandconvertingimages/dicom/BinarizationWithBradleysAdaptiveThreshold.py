# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import BmpOptions
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
out_file = os.path.join(get_output_dir(), 'BinarizationWithBradleysAdaptiveThreshold_out.bmp')
print("Running example BinarizationWithBradleysAdaptiveThreshold")
with open(os.path.join(data_dir, "file.dcm"), "rb") as file_stream:
	with DicomImage(file_stream) as image:
		# Adjust the contrast and Create an instance of BmpOptions for the resultant image and Save the resultant image
		image.binarize_bradley(10)
		image.save(out_file, BmpOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example BinarizationWithBradleysAdaptiveThreshold")
