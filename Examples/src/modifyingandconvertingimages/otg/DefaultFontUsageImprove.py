# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, FontSettings
from aspose.imaging.imageoptions import PngOptions, OdgRasterizationOptions
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
data_dir = os.path.join(get_data_root_dir(), 'otg')
print("Running example DefaultFontUsageImprove")


def export_to_png(file_path, default_font_name, outfile_name):
	FontSettings.set_default_font_name(default_font_name)
	with Image.load(file_path) as document:
		save_options = PngOptions()
		save_options.vector_rasterization_options = OdgRasterizationOptions()
		save_options.vector_rasterization_options.page_width = 1000.0
		save_options.vector_rasterization_options.page_height = 1000.0
		document.save(outfile_name, save_options)

	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(outfile_name)


current_folder = data_dir
FontSettings.set_fonts_folder(os.path.join(current_folder, "fonts"))
FontSettings.set_get_system_alternative_font(False)
export_to_png(os.path.join(data_dir, "missing-font2.odg"), "Arial", os.path.join(get_output_dir(), "arial.png"))
export_to_png(os.path.join(data_dir, "missing-font2.odg"), "Courier New", os.path.join(get_output_dir(), "courier.png"))

print("Finished example DefaultFontUsageImprove")
