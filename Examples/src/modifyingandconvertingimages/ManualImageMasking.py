# GROUP: ADDITIONAL_FEATURES
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, GraphicsPath, Figure, RectangleF, \
	PointF
from aspose.imaging.shapes import *
from aspose.imaging.fileformats.png import PngColorType
from aspose.imaging.imageoptions import PngOptions
from aspose.imaging.sources import StreamSource
from aspose.imaging.masking import *
from aspose.imaging.masking.options import *
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
print("Running example ManualImageMasking")
source_file_name = os.path.join(data_dir, "Colored by Faith_small.png")
output_file_name = os.path.join(get_output_dir(),
								"Colored by Faith_small_manual.png")
manual_mask = GraphicsPath()
first_figure = Figure()
first_figure.add_shape(EllipseShape(RectangleF(100, 30, 40, 40)))
first_figure.add_shape(RectangleShape(RectangleF(10, 200, 50, 30)))
manual_mask.add_figure(first_figure)
sub_path = GraphicsPath()
second_figure = Figure()
second_figure.add_shape(PolygonShape([PointF(310, 100), PointF(350, 200),
									 PointF(250, 200)], True))
second_figure.add_shape(PieShape(RectangleF(10, 10, 80, 80), 30, 120))
sub_path.add_figure(second_figure)
manual_mask.add_path(sub_path)
with aspycore.as_of(Image.load(source_file_name), RasterImage) as image:
	mask_args = ManualMaskingArgs()
	mask_args.mask = manual_mask
	png_opt = PngOptions()
	png_opt.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
	png_opt.source = StreamSource()
	masking_options = MaskingOptions()
	masking_options.method = SegmentationMethod.MANUAL
	masking_options.args = mask_args
	masking_options.decompose = False
	masking_options.export_options = png_opt
	masking_results = ImageMasking(image).decompose(masking_options)
	with masking_results[1].get_image() as result_image:
		result_image.save(output_file_name)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_name)

print("Finished example ManualImageMasking")
