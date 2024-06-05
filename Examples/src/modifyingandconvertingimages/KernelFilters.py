# GROUP: MODIFYING_AND_CONVERTING_IMAGES
import os, random
import aspose.pycore as aspycore
from aspose.imaging import Image, RasterImage, VectorImage
from aspose.imaging.imagefilters.complexutils import Complex
from aspose.imaging.imagefilters.convolution import *
from aspose.imaging.imagefilters.filteroptions import *


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_data_root_dir' not in dir():
	get_data_root_dir = get_data_root_dir_local
if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

delete_output = 'SAVE_OUTPUT' not in os.environ


def delete_file(file):
	if delete_output:
		os.remove(file)
		
		
# Example code:
def filter(raster, options, output_path):
  raster.filter(raster.bounds, options)
  raster.save(output_path)


def get_random_kernel(cols, rows):
  custom_kernel = [0.0] * (cols * rows)
  for y in range(rows):
    for x in range(cols):
      custom_kernel[y*cols + x] = random.random()

  return custom_kernel

		
size: int = 5
sigma: float = 1.5
angle: float = 45
custom_kernel = get_random_kernel(size, 7)
custom_complex = ConvolutionFilter.to_complex(custom_kernel)
kernel_filters = [
	# convolution filters
	ConvolutionFilterOptions(ConvolutionFilter.get_emboss_3x3()),
	ConvolutionFilterOptions(ConvolutionFilter.get_emboss_5x5()),
	ConvolutionFilterOptions(ConvolutionFilter.get_sharpen_3x3()),
	ConvolutionFilterOptions(ConvolutionFilter.get_sharpen_5x5()),
	ConvolutionFilterOptions(ConvolutionFilter.get_blur_box(size)),
	ConvolutionFilterOptions(ConvolutionFilter.get_blur_motion(size, angle)),
	ConvolutionFilterOptions(ConvolutionFilter.get_gaussian(size, sigma)),
	ConvolutionFilterOptions(custom_kernel), 
	GaussianBlurFilterOptions(size, sigma),
	SharpenFilterOptions(size, sigma),
	MedianFilterOptions(size),
	# deconvolution filters
	DeconvolutionFilterOptions(ConvolutionFilter.get_gaussian(size, sigma)),
	DeconvolutionFilterOptions(custom_kernel),
	DeconvolutionFilterOptions(custom_complex),
	GaussWienerFilterOptions(size, sigma),
	MotionWienerFilterOptions(size, sigma, angle)
]

data_dir = os.path.join(get_data_root_dir(), 'png')
input_paths = [
	os.path.join(data_dir, "template.png")
]
outputs = []
for input_path in input_paths:
  for i, options in enumerate(kernel_filters):
    with Image.load(input_path) as image:
      output_path = f"{input_path}-{i}.png"
      if aspycore.is_assignable(image, RasterImage):
        raster = aspycore.as_of(image, RasterImage)
        filter(raster, options, output_path)
        outputs.append(output_path)
      elif aspycore.is_assignable(image, VectorImage):
        vector = aspycore.as_of(image, VectorImage)
        vector_as_png = input_path + ".png"
        if not os.path.exists(vector_as_png):
          vector.save(vector_as_png)
          outputs.append(vector_as_png)

        with Image.load(vector_as_png) as png:
          filter(aspycore.as_of(png, RasterImage), options, output_path)
          outputs.append(output_path)

# Removing all output files
for p in outputs:
	delete_file(p)
