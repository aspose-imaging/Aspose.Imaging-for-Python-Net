# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Rectangle, RasterImage, GraphicsUnit
from aspose.imaging.fileformats.emf import EmfImage
from aspose.imaging.fileformats.emf.graphics import EmfRecorderGraphics2D
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
print("Running example DrawRasterImageOnEMF")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
out_file = os.path.join(get_output_dir(), "input.DrawImage.emf")
# Load the image to be drawn
with aspycore.as_of(Image.load(os.path.join(data_dir, "asposenet_220_src01.png")), RasterImage) as image_to_draw:
	# Load the image for drawing on it (drawing surface)
	with aspycore.as_of(Image.load(os.path.join(data_dir, "input.emf")), EmfImage) \
		as canvas_image:
		graphics = EmfRecorderGraphics2D.from_emf_image(canvas_image)
		# Draw a rectangular part of the raster image within the specified bounds of the vector image (drawing surface).
		# Note that because the source size is not equal to the destination one, the drawn image is stretched horizontally and vertically.
		graphics.draw_image(image_to_draw, 
							Rectangle(67, 67, canvas_image.width, canvas_image.height), 
							Rectangle(0, 0, image_to_draw.width, image_to_draw.height), 
							GraphicsUnit.PIXEL)
		# Save the result image
		with graphics.end_recording() as result_image:
			result_image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example DrawRasterImageOnEMF")
