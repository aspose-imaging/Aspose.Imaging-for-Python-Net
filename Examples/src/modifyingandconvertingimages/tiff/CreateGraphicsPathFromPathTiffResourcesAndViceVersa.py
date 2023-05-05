import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.fileformats.tiff import *
from aspose.imaging.fileformats.tiff.pathresources import *
from aspose.imaging.shapes import *
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

print("Running example CreateGraphicsPathFromPathTiffResourcesAndViceVersa")


def create_bezier_shape(coordinates):
	bezier_points = list(coordinates_to_bezier_points(coordinates))
	return BezierShape(bezier_points, True)

def coordinates_to_bezier_points(coordinates):
	for coordinateIndex in range(0, len(coordinates), 2):
		for index in range(3):
			yield PointF(coordinates[coordinateIndex] + 100, coordinates[coordinateIndex + 1] + 100)


# Run
out_file = os.path.join(get_output_dir(), "BottleWithRedBorder.tif")
with aspycore.as_of(Image.load(os.path.join(data_dir, "Bottle.tif")), TiffImage) as image:
	# Create the GraphicsPath using PathResources from TIFF image
	graphics_path = PathResourceConverter.to_graphics_path(list(image.active_frame.path_resources), image.active_frame.size)
	graphics = Graphics(image)
	# Draw red line and save the image
	graphics.draw_path(Pen(Color.red, 10.0), graphics_path)
	image.save(out_file)

out_file2 = os.path.join(get_output_dir(), "BottleWithRectanglePath.tif")
with aspycore.as_of(Image.load(os.path.join(data_dir, "Bottle.tif")), TiffImage) as image:
	# Create rectangular Figure for GraphicsPath
	figure = Figure()
	figure.add_shape(create_bezier_shape([100.0, 100.0, 500.0, 100.0, 500.0, 1000.0, 100.0, 1000.0]))
	# Create GraphicsPath using our Figure
	graphics_path = GraphicsPath()
	graphics_path.add_figure(figure)
	# Set PathResources using GraphicsPath
	path_resouze = PathResourceConverter.from_graphics_path(graphics_path, image.size)
	image.active_frame.path_resources = list(path_resouze)
	# Save the image
	image.save(out_file2)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
	os.remove(out_file2)
	
print("Finished example CreateGraphicsPathFromPathTiffResourcesAndViceVersa")
