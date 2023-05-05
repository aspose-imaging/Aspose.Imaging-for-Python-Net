# GROUP: TEST_FILE_FORMATS
from aspose.imaging import Image
from aspose.imaging.imageoptions import DxfOptions
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
print("Running example ExportToDxf")
data_dir = os.path.join(get_data_root_dir(), 'eps')
out_file = os.path.join(get_output_dir(), "output.dxf")
with Image.load(os.path.join(data_dir, "Pooh group.eps")) as image:
	options = DxfOptions()
	options.text_as_lines = True
	options.convert_text_beziers = True
	options.bezier_point_count = 20
	image.save(out_file, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)

print("Finished example ExportToDxf")
