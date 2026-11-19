# GROUP: MODIFYING_AND_CONVERTING_IMAGES
from aspose.pycore import as_of
from aspose.imaging import Image, RasterImage, Rectangle
from aspose.imaging.lut.cubelut import CubeLut
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
out_file = os.path.join(get_output_dir(), "result-rectangle.tiff")


rectangle = Rectangle(0, 0, 720, 960)

with as_of(Image.load(os.path.join(data_dir, "multipage.tiff")), RasterImage) as image:
    image.apply_cube_lut(os.path.join(data_dir, "bleach-bypass.cube"), rectangle)
    image.save(out_file)

cubeLut = CubeLut.load(os.path.join(data_dir, "bleach-bypass.cube"))

with as_of(Image.load(os.path.join(data_dir, "multipage.tiff")), RasterImage) as image:
    image.apply_cube_lut(cubeLut, rectangle)
    image.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
