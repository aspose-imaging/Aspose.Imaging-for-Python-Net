from aspose.imaging import Image
from aspose.imaging.imageoptions import SvgOptions, SvgRasterizationOptions
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
# ExStart:ExportRasterImageToSvg
paths = ["butterfly.gif", "33715-cmyk.jpeg", "3.JPG", "test.j2k", "Rings.png", "3layers_maximized_comp.psd", "img4.TIF", "Lossy5.webp"]
out_files = []
for path in paths:
	in_file = os.path.join(data_dir, path)
	if not os.path.exists(in_file):
		continue
	dest_path = os.path.join(get_output_dir(), path + ".svg")
	with Image.load(in_file) as image:
		svg_rasterization_options = SvgRasterizationOptions()
		svg_rasterization_options.page_width = float(image.width)
		svg_rasterization_options.page_height = float(image.height)
		svg_options = SvgOptions()
		svg_options.vector_rasterization_options = svg_rasterization_options
		image.save(dest_path, svg_options)
		out_files.append(dest_path)

if 'SAVE_OUTPUT' not in os.environ:
	for file in out_files:
		os.remove(file)
