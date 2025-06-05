# GROUP: TEST_FILE_FORMATS

import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import PngOptions, PngCompressionLevel
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

print("Running example PngCompressionLevelExample")

with Image.load(os.path.join(data_dir, "aspose_logo.png")) as image:
	for compression in range(11):
		output_file = os.path.join(get_output_dir(), f"compressionTest{compression}.png")
		out_options = PngOptions()
		out_options.png_compression_level = PngCompressionLevel(compression)
		image.save(output_file, out_options)

		if 'SAVE_OUTPUT' not in os.environ:
			os.remove(output_file)
	
print("Finished example PngCompressionLevelExample")
