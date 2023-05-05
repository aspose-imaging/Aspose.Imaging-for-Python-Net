# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image
from aspose.imaging.imageoptions import BmpOptions
from aspose.imaging.sources import StreamSource
import os

# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."
	
def get_output_dir_local():
	return get_data_root_dir_local()

if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

if 'get_output_dir' not in dir():
	get_output_dir = get_output_dir_local

# Example code:

print("Running example CreatingImageUsingStream")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
# Creates an instance of BmpOptions and set its various properties
with BmpOptions() as image_options:
	image_options.bits_per_pixel = 24
	# Create an instance of System.IO.Stream
	out_file = os.path.join(get_output_dir(), "sample_out.bmp")
	with open(out_file, "wb") as stream:
		# Define the source property for the instance of BmpOptions Second boolean parameter determines if the Stream is disposed once get out of scope
		image_options.source = StreamSource(stream, True)
		# Creates an instance of Image and call Create method by passing the BmpOptions object
		with Image.create(image_options, 500, 500) as image:
			# Do some image processing
			out_file2 = os.path.join(get_output_dir(), "CreatingImageUsingStream_out.bmp")
			image.save(out_file2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	os.remove(out_file2)
	
print("Finished example CreatingImageUsingStream")
