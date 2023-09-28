from aspose.pycore import as_of
from aspose.imaging import Image, GraphicsPath, Figure, RectangleF
from aspose.imaging.shapes import EllipseShape
from aspose.imaging.fileformats.png import PngImage
from aspose.imaging.watermark import WatermarkRemover
from aspose.imaging.watermark.options import ContentAwareFillWatermarkOptions
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
data_dir = os.path.join(get_data_root_dir(), 'png')

imageFilePath = os.path.join(data_dir, "ball.png")
output_path = os.path.join(get_output_dir(), "result.png")
with Image.load(imageFilePath) as image:
    pngImage = as_of(image, PngImage)
    mask = GraphicsPath()
    firstFigure = Figure()
    firstFigure.add_shape(EllipseShape(RectangleF(350, 170, 570 - 350, 400 - 170)))
    mask.add_figure(firstFigure)
    options = ContentAwareFillWatermarkOptions(mask)
    options.max_painting_attempts = 4
    result = WatermarkRemover.paint_over(pngImage, options)
    result.save(output_path)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_path)
