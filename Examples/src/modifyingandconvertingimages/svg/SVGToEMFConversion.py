# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, SizeF
from aspose.imaging.imageoptions import EmfOptions, SvgRasterizationOptions
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
output_path = get_output_dir()

test_files = ["mysvg.svg"]

print("Running example SVGToEMFConversion")
for file_name in test_files:
	input_file_name = os.path.join(data_dir, file_name)
	output_file_name = os.path.join(output_path, file_name + ".emf")
	with Image.load(input_file_name) as image:
		svg_opt = SvgRasterizationOptions()
		svg_opt.page_size = aspycore.cast(SizeF, image.size)
		emf_opt = EmfOptions()
		emf_opt.vector_rasterization_options = svg_opt
		image.save(output_file_name, emf_opt)

	if 'SAVE_OUTPUT' not in os.environ:
		os.remove(output_file_name)

print("Finished example SVGToEMFConversion")

