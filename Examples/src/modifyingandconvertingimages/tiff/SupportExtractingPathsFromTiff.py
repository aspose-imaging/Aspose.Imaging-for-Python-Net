import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.core.vectorpaths import *
from aspose.imaging.fileformats.tiff import *
from aspose.imaging.fileformats.tiff.enums import *
from aspose.imaging.fileformats.tiff.pathresources import *
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
data_dir = os.path.join(get_data_root_dir(), 'tiff')

print("Running example SupportExtractingPathsFromTiff")


def create_records(coordinates):
	records = list(create_bezier_records(coordinates))
	obj_init3 = LengthRecord()
	obj_init3.is_open = False
	obj_init3.record_count = len(records)
	records.insert(0, obj_init3)
	return records


def create_bezier_records(coordinates):
	for index in range(0, len(coordinates), 2):
		point = PointF(coordinates[index], coordinates[index + 1])
		obj_init4 = BezierKnotRecord()
		obj_init4.path_points = [point, point, point]
		yield obj_init4


file_path = data_dir
out_file = os.path.join(get_output_dir(), "SampleWithPaths.psd")

with aspycore.as_of(Image.load(os.path.join(file_path, "Sample.tif")), TiffImage) as image:
	for path in image.active_frame.path_resources:
		print(path.name)

	image.save(out_file, PsdOptions())

out_file2 = os.path.join(get_output_dir(), "ImageWithPath.tif")
# Create Clipping Path manually
with aspycore.as_of(Image.load(os.path.join(file_path, "Sample.tif")), TiffImage) as image:
	obj_init = PathResource()
	obj_init.block_id = 2000
	obj_init.name = "My Clipping Path"
	obj_init.records = create_records([0.2, 0.2, 0.8, 0.2, 0.8, 0.8, 0.2, 0.8])
	obj_init2 = [obj_init]
	image.active_frame.path_resources = obj_init2
	image.save(out_file2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	os.remove(out_file2)
	
print("Finished example SupportExtractingPathsFromTiff")

