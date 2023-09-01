import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Color, StringAlignment, \
	StringFormat, StringFormatFlags, Font, SizeF, RectangleF, Point, Pen
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.sources import StreamSource
from aspose.imaging.brushes import SolidBrush
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

# Example code:
# The path to the documents directory.
data_dir = os.path.join(get_output_dir(), 'cdr')

print("Running example PixelPerfectTextAlignment")

def draw_string(base_folder, align):
	file_name = f"output_{align}.png"
	output_file_name = os.path.join(get_output_dir(), file_name)
	font_names = ["Arial", "Times New Roman", "Bookman Old Style",
				  "Calibri", "Comic Sans MS", "Courier New",
				  "Microsoft Sans Serif", "Tahoma", "Verdana",
				  "Proxima Nova Rg"]
	font_sizes = [10.0, 22.0, 50.0, 100.0]
	width = 3000
	height = 3500
	# Create an instance of PngOptions and set its various properties
	with PngOptions() as png_options:
		# Set the Source for PngOptions
		png_options.source = StreamSource()
		# Create an instance of Image 
		with Image.create(png_options, width, height) as image:
			# Create and initialize an instance of Graphics class
			graphics = Graphics(image)
			# Clear Graphics surface
			graphics.clear(Color.white)
			# Create a SolidBrush object and set its various properties
			brush = SolidBrush()
			brush.color = Color.black
			x = 10
			line_x = 0
			y = 10
			w = width - 20
			pen = Pen(Color.red, 1.0)
			alignment = StringAlignment.NEAR
			
			if align == "Left":
				alignment = StringAlignment.NEAR
				line_x = int(x)
			elif align == "Center":
				alignment = StringAlignment.CENTER
				line_x = int(x + w // 2)
			elif align == "Right":
				alignment = StringAlignment.FAR
				line_x = int(x + w)

			string_format = StringFormat(StringFormatFlags.EXACT_ALIGNMENT)
			string_format.alignment = alignment
			for font_name in font_names:
				for font_size in font_sizes:
					font = Font(font_name, font_size)
					text = "This is font: {0}, size:{1}".format(font_name, font_size)
					s = graphics.measure_string(text, font, SizeF.empty, None)
					graphics.draw_string(text, font, brush, 
								RectangleF(x, y, w, s.height), string_format)
					y += s.height

				graphics.draw_line(pen, Point(int(x), int(y)), Point(int(x + w), int(y)))

			graphics.draw_line(pen, Point(line_x, 0), Point(line_x, int(y)))
			# save all changes.
			image.save(output_file_name)

	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(output_file_name)


# Run
alignments = ["Left", "Center", "Right"]
for alignment in alignments:
	draw_string(get_output_dir(), alignment)

print("Finished example PixelPerfectTextAlignment")
