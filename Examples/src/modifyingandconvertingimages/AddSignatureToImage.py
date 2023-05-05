from aspose.imaging import Image, Graphics, Point
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
data_dir = os.path.join(get_data_root_dir(), 'ModifyingAndConvertingImages')
out_file = os.path.join(get_output_dir(), "AddSignatureToImage_out.png")
print("Running example AddSignatureToImage")
# Create an instance of Image and load the primary image
with Image.load(os.path.join(data_dir, "SampleTiff1.tiff")) as canvas:
	# Create another instance of Image and load the secondary image containing the signature graphics
	with Image.load(os.path.join(data_dir, "signature.gif")) as signature:
		# Create an instance of Graphics class and initialize it using the object of the primary image
		graphics = Graphics(canvas)
		# Call the DrawImage method while passing the instance of secondary image and appropriate location. The following snippet tries to draw the secondary image at the right bottom of the primary image
		graphics.draw_image(signature, Point(canvas.height - signature.height, canvas.width - signature.width))
		canvas.save(out_file, PngOptions())

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example AddSignatureToImage")
