from aspose.imaging import Image, Graphics, Color, StringAlignment, \
	StringFormatFlags, Matrix, Font, FontStyle, StringFormat
from aspose.imaging.brushes import SolidBrush
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
out_file = os.path.join(get_output_dir(), "AddDiagonalWatermarkToImage_out.jpg")
print("Running example AddDiagonalWatermarkToImage")
# Load an existing JPG image
with Image.load(os.path.join(data_dir, "SampleTiff1.tiff")) as image:
	# Declare a String object with Watermark Text
	the_string = "45 Degree Rotated Text"
	# Create and initialize an instance of Graphics class and Initialize an object of SizeF to store image Size
	graphics = Graphics(image)
	sz = image.size
	# Creates an instance of Font, initialize it with Font Face, Size and Style
	font = Font("Times New Roman", 20.0, FontStyle.BOLD)
	# Create an instance of SolidBrush and set its various properties
	brush = SolidBrush()
	brush.color = Color.red
	brush.opacity = 0
	# Initialize an object of StringFormat class and set its various properties
	format_ = StringFormat()
	format_.alignment = StringAlignment.CENTER
	format_.format_flags = StringFormatFlags.MEASURE_TRAILING_SPACES
	# Create an object of Matrix class for transformation
	matrix = Matrix()
	# First a translation then a rotation                
	matrix.translate(sz.width / 2, sz.height / 2)
	matrix.rotate(-45.0)
	# Set the Transformation through Matrix
	graphics.transform = matrix
	# Draw the string on Image Save output to disk
	graphics.draw_string(the_string, font, brush, 0, 0, format_)
	image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	
print("Finished example AddDiagonalWatermarkToImage")

