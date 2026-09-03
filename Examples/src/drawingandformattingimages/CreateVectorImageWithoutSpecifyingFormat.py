# GROUP: DRAWING_AND_FORMATTING_IMAGES
import aspose.pycore as aspycore
from aspose.imaging import VectorImage, GraphicsUnit, Graphics, Pen, Font, PointF, Color, FontStyle, RectangleF
from aspose.imaging.imageoptions import SvgOptions, VectorRasterizationOptions
from aspose.imaging.brushes import SolidBrush
import os

# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."
	
def get_output_dir_local():
	return get_data_root_dir_local()

if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local

if 'get_output_dir' not in dir():
	get_output_dir = get_output_dir_local

# Example code:

out_file = os.path.join(get_output_dir(), "output.svg")

with VectorImage.create(500, 500, GraphicsUnit.PIXEL) as image:
    deviceContext = Graphics(image)
    deviceContext.page_unit = GraphicsUnit.PIXEL
    
    brush = SolidBrush(Color.yellow)
    pen = Pen(Color.blue)

    deviceContext.fill_pie(brush, RectangleF(10, 10, 80, 80), -270, 270)
    deviceContext.draw_pie(pen, RectangleF(10, 10, 80, 80), -270, 270)
    deviceContext.draw_arc(pen, RectangleF(100, 10, 80, 80), 180, 90)
    deviceContext.fill_ellipse(brush, RectangleF(200, 10, 80, 80))
    deviceContext.draw_ellipse(pen, RectangleF(200, 10, 80, 80))
    deviceContext.fill_rectangle(brush, RectangleF(300, 10, 80, 80))
    deviceContext.fill_rectangle(brush, RectangleF(400, 10, 80, 80))
    deviceContext.draw_string("Hello World!", 
        Font("Arial", 16, FontStyle.BOLD), 
        SolidBrush(Color.black), 
        PointF(10, 110))
        
    vec_opts = VectorRasterizationOptions()
    vec_opts.background_color = Color.empty
    svg_opts = SvgOptions()
    svg_opts.vector_rasterization_options = vec_opts
    
    image.save(out_file, svg_opts)

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(out_file)
