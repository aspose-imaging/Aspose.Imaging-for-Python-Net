import aspose.pycore as aspycore
from aspose.imaging import Image, VectorImage, FileFormat
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
data_dir = os.path.join(get_data_root_dir(), 'svg')


def get_extension(format_):
	tmp_switch = format_
	if tmp_switch == FileFormat.JPEG:
		return ".jpg"
	elif tmp_switch == FileFormat.PNG:
		return ".png"
	elif tmp_switch == FileFormat.BMP:
		return ".bmp"
	else:
		return "." + format_.name.lower()
		

print("Running example UnifyExtractionOfRasterImagesEmbeddedInVectorFormats")
file_name = os.path.join(data_dir, "test2.svg")
output_folder = get_output_dir()
files = []
with Image.load(file_name) as image:
	images = (aspycore.as_of(image, VectorImage)).get_embedded_images()
	i = 0
	for im in images:
		out_file_name = "svg_image{0}{1}".format(i, get_extension(im.image.file_format))
		i += 1
		out_file_path = os.path.join(output_folder, out_file_name)
		files.append(out_file_path)
		with im as _:
			im.image.save(out_file_path)

if 'SAVE_OUTPUT' not in os.environ:
	for file in files:
		os.remove(file)

print("Finished example UnifyExtractionOfRasterImagesEmbeddedInVectorFormats")

