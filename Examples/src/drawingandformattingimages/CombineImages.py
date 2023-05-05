# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color
from aspose.imaging.imageoptions import JpegOptions
from aspose.imaging.sources import FileCreateSource
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

base_dir = get_data_root_dir()

print("Running example CombineImages")
# The path to the documents directory.
data_dir = os.path.join(base_dir, "DrawingAndFormattingImages")
# Create an instance of JpegOptions and set its various properties
with JpegOptions() as image_options:
	# Create an instance of FileCreateSource and assign it to Source property
	out_file = os.path.join(get_output_dir(), "Two_images_result_out.jpg")
	image_options.source = FileCreateSource(out_file, False)
	# Create an instance of Image and define canvas size
	with Image.create(image_options, 600, 600) as image:
		# Create and initialize an instance of Graphics, Clear the image surface with white color and Draw Image
		graphics = Graphics(image)
		graphics.clear(Color.white)
		with Image.load(os.path.join(data_dir, "sample_1.bmp")) as img1:
			graphics.draw_image(img1, 0, 0, 600, 300)
		
		with Image.load(os.path.join(data_dir, "File1.bmp")) as img2:
			graphics.draw_image(img2, 0, 300, 600, 300)
		
		image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example CombineImages")
