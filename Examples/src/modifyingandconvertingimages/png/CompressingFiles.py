# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image
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
data_dir = os.path.join(get_data_root_dir(), 'png')
output_file = os.path.join(get_output_dir(), "result")
print("Running example CompressingFiles")
# Load an image from file (or stream)
with Image.load(os.path.join(data_dir, "aspose_logo.png")) as image:
	# Loop over possible CompressionLevel range
	for i in range(9):
		# Create an instance of PngOptions for each resultant PNG, Set CompressionLevel and Save result on disk
		options = PngOptions()
		options.compression_level = i
		path = output_file + f"{i}_out.png"
		image.save(path, options)
				
		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(path)

print("Finished example CompressingFiles")
