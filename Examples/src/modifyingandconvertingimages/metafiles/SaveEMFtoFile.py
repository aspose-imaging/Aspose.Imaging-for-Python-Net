# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.fileformats.emf import MetaImage
from aspose.imaging.imageoptions import EmfOptions
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
path = os.path.join(data_dir, "TestEmfBezier.emf")
out_path = os.path.join(get_output_dir(), "TestEmfBezier.emf.emf")
print("Running example SaveEMFtoFile")
with aspycore.as_of(Image.load(path), MetaImage) as image:
	image.save(out_path, EmfOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_path)

print("Finished example SaveEMFtoFile")
