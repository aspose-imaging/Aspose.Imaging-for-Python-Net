# GROUP: MEMORY_STRATEGIES
import aspose.pycore as aspycore
from aspose.imaging import Image, Color, Graphics
from aspose.imaging.brushes import SolidBrush
from aspose.imaging.fileformats.dicom import DicomImage
from aspose.imaging.imageoptions import DicomOptions
from aspose.imaging.sources import StreamSource
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
out_path = os.path.join(get_output_dir(), "temp_dicom_created.dcm")

print("Running example OptimizationStrategyInDicom")
with DicomOptions() as obj_init:
	obj_init.source = StreamSource()
	with aspycore.as_of(Image.create(obj_init, 100, 100), DicomImage) as image:
		# Draw something using vector graphics
		graphics = Graphics(image)
		graphics.fill_rectangle(SolidBrush(Color.blue_violet), image.bounds)
		graphics.fill_rectangle(SolidBrush(Color.aqua), 10, 20, 50, 20)
		graphics.fill_ellipse(SolidBrush(Color.orange), 30, 50, 70, 30)
		# Save the pixels of the drawn image. They are now on the first page of the Dicom image.
		pixels = image.load_argb_32_pixels(image.bounds)
		# Add a few pages after, making them darker
		for i in range(1, 5):
			page = image.add_page()
			page.save_argb_32_pixels(page.bounds, pixels)
			page.adjust_brightness(i * 30)

		# Add a few pages in front of the main page, making them brighter
		for i in range(1, 5):
			page = image.insert_page(0)
			page.save_argb_32_pixels(page.bounds, pixels)
			page.adjust_brightness(-i * 30)

		# Save the created multi-page image to the output file
		image.save(out_path)
	
if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_path)

print("Finished example OptimizationStrategyInDicom")
