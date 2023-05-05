# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Color
from aspose.imaging.imageoptions import BmpOptions
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
print("Running example DrawImagesUsingCoreFunctionality")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
# Create an instance of BmpOptions and set its various properties
with BmpOptions() as image_options:
	image_options.bits_per_pixel = 24
	out_file = os.path.join(get_output_dir(), "DrawImagesUsingCoreFunctionality_out.bmp")
	# Create an instance of FileCreateSource and assign it to Source property
	image_options.source = FileCreateSource(out_file, False)
	# Create an instance of RasterImage and Get the pixels of the image by specifying the area as image boundary
	with aspycore.as_of(Image.create(image_options, 500, 500), RasterImage) as raster_image:
		pixels = raster_image.load_pixels(raster_image.bounds)
		for index in range(pixels.length):
			# Set the indexed pixel color to yellow
			pixels[index] = Color.yellow

		# Apply the pixel changes to the image and Save all changes.
		raster_image.save_pixels(raster_image.bounds, pixels)
		raster_image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example DrawImagesUsingCoreFunctionality")
