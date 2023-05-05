import aspose.pycore as aspycore
from aspose.imaging import Image, TextRenderingHint, SizeF, FileFormat
from aspose.imaging.imageoptions import *
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
print("Running example SupportOfTextRenderingHint")
files = ["TextHintTest.cdr", "TextHintTest.cmx", "TextHintTest.emf", "TextHintTest.wmf", "TextHintTest.odg", "TextHintTest.svg"]
text_rendering_hints = [TextRenderingHint.ANTI_ALIAS,
						TextRenderingHint.ANTI_ALIAS_GRID_FIT,
						TextRenderingHint.CLEAR_TYPE_GRID_FIT,
						TextRenderingHint.SINGLE_BIT_PER_PIXEL,
						TextRenderingHint.SINGLE_BIT_PER_PIXEL_GRID_FIT]
out_files = []						
for file_name in files:
	with Image.load(os.path.join(data_dir, file_name)) as image:
		vector_rasterization_options = None
		file_format = image.file_format
		if file_format == FileFormat.CDR:
			vector_rasterization_options = CdrRasterizationOptions()
		elif file_format == FileFormat.CMX:
			vector_rasterization_options = CmxRasterizationOptions()
		elif file_format == FileFormat.EMF:
			vector_rasterization_options = EmfRasterizationOptions()
		elif file_format == FileFormat.WMF:
			vector_rasterization_options = WmfRasterizationOptions()
		elif file_format == FileFormat.ODG:
			vector_rasterization_options = OdgRasterizationOptions()
		elif file_format == FileFormat.SVG:
			vector_rasterization_options = SvgRasterizationOptions()
		else:
			raise Exception("This is image is not supported in this example")

		vector_rasterization_options.page_size = aspycore.cast(SizeF, image.size)
		for text_rendering_hint in text_rendering_hints:
			output_file_name = os.path.join(get_output_dir(), "image_" + text_rendering_hint.name + "_" + file_name + ".png")
			vector_rasterization_options.text_rendering_hint = text_rendering_hint
			obj_init = PngOptions()
			obj_init.vector_rasterization_options = vector_rasterization_options
			image.save(output_file_name, obj_init)
			out_files.append(output_file_name)

if 'SAVE_OUTPUT' not in os.environ:
	for file in out_files:
		os.remove(file)

print("Finished example SupportOfTextRenderingHint")
