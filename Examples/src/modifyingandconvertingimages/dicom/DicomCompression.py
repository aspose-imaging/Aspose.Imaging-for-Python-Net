# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.dicom import *
from aspose.imaging.fileformats.jpeg2000 import *
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

# To get proper output please apply a valid Aspose.Imaging License. You can purchase full license or get 30 day temporary license from https:// www.aspose.com/purchase/default.aspx.");
print("Running example DicomCompression")
# The path to the documents directory.
data_dir = os.path.join(get_data_root_dir(), 'dicom')
input_file = os.path.join(data_dir, "original.jpg")
output1 = os.path.join(get_output_dir(), "original_Uncompressed.dcm")
output2 = os.path.join(get_output_dir(), "original_JPEG.dcm")
output3 = os.path.join(get_output_dir(), "original_JPEG2000.dcm")
output4 = os.path.join(get_output_dir(), "original_RLE.dcm")
with Image.load(input_file) as input_image:
	obj_init = Compression()
	obj_init.type = CompressionType.NONE
	options = DicomOptions()
	options.color_type = ColorType.RGB_24_BIT
	options.compression = obj_init
	input_image.save(output1, options)

with Image.load(input_file) as input_image:
	obj_init3 = Compression()
	obj_init3.type = CompressionType.JPEG
	options = DicomOptions()
	options.color_type = ColorType.RGB_24_BIT
	options.compression = obj_init3
	input_image.save(output2, options)

with Image.load(input_file) as input_image:
	obj_init5 = Jpeg2000Options()
	obj_init5.codec = Jpeg2000Codec.JP2
	obj_init5.irreversible = False
	obj_init6 = Compression()
	obj_init6.type = CompressionType.JPEG2000
	obj_init6.jpeg2000 = obj_init5
	options = DicomOptions()
	options.color_type = ColorType.RGB_24_BIT
	options.compression = obj_init6
	input_image.save(output3, options)

with Image.load(input_file) as input_image:
	obj_init8 = Compression()
	obj_init8.type = CompressionType.RLE
	options = DicomOptions()
	options.color_type = ColorType.RGB_24_BIT
	options.compression = obj_init8
	input_image.save(output4, options)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output1)
	os.remove(output2)
	os.remove(output3)
	os.remove(output4)

print("Finished example DicomCompression")
