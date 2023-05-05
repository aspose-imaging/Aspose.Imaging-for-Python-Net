# GROUP: TEST_FILE_FORMATS
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, Color
from aspose.imaging.fileformats.tga import TgaImage
from aspose.imaging.imageoptions import TgaOptions
import os
from datetime import datetime, timedelta


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
data_dir = os.path.join(get_data_root_dir(), 'tga')

# To get proper output please apply a valid Aspose.Imaging License. You can purchase full license or get 30 day temporary license from https:// www.aspose.com/purchase/default.aspx.");
print("Running example ConvertToTGA")
input_file = os.path.join(data_dir, "test.jpg")
input_file2 = os.path.join(data_dir, "test.png")
input_file3 = os.path.join(data_dir, "test.tga")
output1 = os.path.join(get_output_dir(), "test_.tga")
output2 = os.path.join(get_output_dir(), "test2_.tga")
output3 = os.path.join(get_output_dir(), "test3_.tga")

with Image.load(input_file) as image:
	image.save(output1, TgaOptions())

with aspycore.as_of(Image.load(input_file2), RasterImage) as image:
	with TgaImage(image) as tga_image:
		tga_image.save(output2)

with aspycore.as_of(Image.load(input_file3), TgaImage) as image:
	image.date_time_stamp = datetime.now()
	image.author_name = "John Smith"
	image.author_comments = "Comment"
	image.image_id = "ImageId"
	image.job_name_or_id = "Important Job"
	image.job_time = timedelta(days=10)
	image.transparent_color = Color.from_argb(123)
	image.software_id = "SoftwareId"
	image.software_version = "abc1"
	image.software_version_letter = 'a'
	image.software_version_number = 2
	image.x_origin = 1000
	image.y_origin = 1000
	image.save(output3)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output1)
	os.remove(output2)
	os.remove(output3)

print("Finished example ConvertToTGA")

