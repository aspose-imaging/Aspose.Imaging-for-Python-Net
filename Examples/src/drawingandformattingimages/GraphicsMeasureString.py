# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import Image, Graphics, Font, SizeF, StringFormat
import os


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

# Example code:
print("Running example GraphicsMeasureString")
data_dir = os.path.join(get_data_root_dir(), "jpeg")
filepath = os.path.join(data_dir, "input.jpg")
with Image.load(filepath) as backgound_image:
	gr = Graphics(backgound_image)
	format_ = StringFormat()
	size = gr.measure_string("Test", Font("Arial", 10), SizeF.empty, format_)

print("Finished example GraphicsMeasureString")
