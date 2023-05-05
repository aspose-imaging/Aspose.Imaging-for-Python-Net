import aspose.pycore as aspycore
from aspose.imaging import Image, IntRange, IMultipageImage
from aspose.imaging.fileformats.djvu import DjvuImage
from aspose.imaging.fileformats.tiff.enums import TiffExpectedFormat
from aspose.imaging.imageoptions import PngOptions, MultiPageOptions, TiffOptions
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
data_dir = os.path.join(get_data_root_dir(), 'djvu')
print("Running example CommonMultipageImageExample")
out_path = os.path.join(get_output_dir(), "multipageExportSingle_out.png")
out_path2 = os.path.join(get_output_dir(), "multipageExportMultiple_out.tiff")
with aspycore.as_of(Image.load(os.path.join(data_dir, "Sample.djvu")),
					DjvuImage) as image:
	if aspycore.is_assignable(image, IMultipageImage):
		pages = (aspycore.as_of(image, IMultipageImage)).pages
		print("Pages count in document is", pages.length)

	start_page = 3
	count_page = 1
	png_options = PngOptions()
	png_options.multi_page_options = MultiPageOptions(IntRange(start_page, count_page))
	image.save(out_path, png_options)
	start_page = 0
	count_page = 2
	tiff_options = TiffOptions(TiffExpectedFormat.TIFF_DEFLATE_RGB)
	tiff_options.multi_page_options = MultiPageOptions(IntRange(start_page, count_page))
	image.save(out_path2, tiff_options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_path)
	os.remove(out_path2)

print("Finished example CommonMultipageImageExample")
