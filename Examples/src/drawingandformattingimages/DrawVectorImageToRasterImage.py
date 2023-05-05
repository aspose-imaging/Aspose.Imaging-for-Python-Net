# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import RasterImage, Image, Point, SizeF, Size
from aspose.imaging.extensions import StreamExtensions
from aspose.imaging.fileformats.svg import *
from aspose.imaging.fileformats.svg.graphics import SvgGraphics2D
from aspose.imaging.imageoptions import *
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
print("Running example DrawVectorImageToRasterImage")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), "DrawingAndFormattingImages")
out_file = os.path.join(get_output_dir(), "asposenet_220_src02.DrawVectorImage.svg")
with StreamExtensions.create_memory_stream() as drawn_image_stream:
	# First, rasterize Svg to Png and write the result to a stream.
	with aspycore.as_of(Image.load(os.path.join(data_dir, "asposenet_220_src02.svg")),
		                SvgImage) as svg_image:
		rasterization_options = SvgRasterizationOptions()
		rasterization_options.page_size = aspycore.cast(SizeF, svg_image.size)
		save_options = PngOptions()
		save_options.vector_rasterization_options = rasterization_options
		svg_image.save(drawn_image_stream, save_options)
		# Now load a Png image from stream for further drawing.
		drawn_image_stream.seek(0)
		with aspycore.as_of(Image.load(drawn_image_stream), RasterImage) \
			 as image_to_draw:
			# Drawing on the existing Svg image.
			graphics = SvgGraphics2D(svg_image)
			# Scale down the entire drawn image by 2 times and draw it to the center of the drawing surface.
			width = image_to_draw.width // 2
			height = image_to_draw.height // 2
			origin = Point((svg_image.width - width) // 2, 
						   (svg_image.height - height) // 2)
			size = Size(width, height)
			graphics.draw_image(image_to_draw, origin, size)
			# Save the result image
			with graphics.end_recording() as result_image:
				result_image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example DrawVectorImageToRasterImage")
