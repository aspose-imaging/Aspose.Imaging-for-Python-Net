import aspose.pycore as aspycore
from aspose.imaging import FontSettings
from aspose.imaging.fileformats.emf import EmfImage
from aspose.imaging.fileformats.emf.emf.consts import *
from aspose.imaging.fileformats.emf.emf.objects import *
from aspose.imaging.fileformats.emf.emf.records import *
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
print("Running example SpecifyFont")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'Fonts')
out_file = os.path.join(get_output_dir(), "result.png")
base_folder = data_dir
font_name = "Cambria Math"
symbol_count = 40
start_index = 2001
font_folder = base_folder
FontSettings.set_fonts_folder(font_folder)
# Fill GlyphIndex buffer
glyph_codes = list(range(start_index, symbol_count))

# create emf
with EmfImage(700, 100) as emf:
	# font record
	font = EmfExtCreateFontIndirectW()
	font.elw = EmfLogFont()
	font.elw.facename = font_name
	font.elw.height = 30
	# text record
	text = EmfExtTextOutW()
	text.w_emr_text = EmfText()
	text.w_emr_text.options = EmfExtTextOutOptions.ETO_GLYPH_INDEX
	text.w_emr_text.chars = symbol_count
	text.w_emr_text.glyph_index_buffer = glyph_codes
	emf.records.append(font)
	obj_init = EmfSelectObject()
	obj_init.object_handle = 0
	emf.records.append(obj_init)
	emf.records.append(text)
	emf.save(out_file)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example SpecifyFont")
