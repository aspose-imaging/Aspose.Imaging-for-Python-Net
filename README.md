![GitHub all releases](https://img.shields.io/github/downloads/aspose-imaging/Aspose.imaging-for-Python-NET/total) ![GitHub](https://img.shields.io/github/license/aspose-imaging/Aspose.imaging-for-Python-NET)
----

# API for Image Processing

[Aspose.Imaging for Python via .NET](https://products.aspose.com/imaging/python-net) is a library offering advanced image processing features. Developers can create, edit or convert images in their own application. Also **Aspose.Imaging** library supports drawing and work with graphic primitives. Image exporting and conversion (including uniform multi-page image processing) is the one of API core features along with image transformations (resize, crop, flip&rotate, binarization, grayscale, adjust), advanced image manipulation features (filtering, dithering, masking, deskewing) and memory optimization strategies.

<p align="center"> 
  <a title="Download ZIP" href="https://github.com/aspose-imaging/Aspose.Imaging-for-Python-NET/archive/main.zip">
     <img src="http://i.imgur.com/hwNhrGZ.png" />
  </a>
</p>

Directory | Description
--------- | -----------
[Examples](Examples)  | A collection of Python examples that help you learn the product features.

## Imaging Features

- [Draw raster images with graphics](https://docs.aspose.com/imaging/python-net/drawing-images-using-graphics/).
- [Draw vector images](https://docs.aspose.com/imaging/python-net/drawing-vector-images/).
- [Convert images to various formats](https://docs.aspose.com/imaging/python-net/converting-images/).
- [Apply masking](https://docs.aspose.com/imaging/python-net/applying-masking-to-images/) as well as [Median & Wiener](https://docs.aspose.com/imaging/python-net/applying-median-and-wiener-filters/) filters.
- [Crop, rotate & resize images via API](https://docs.aspose.com/imaging/python-net/crop-rotate-and-resize-images/).
- [De-skew & transform images](https://docs.aspose.com/imaging/python-net/deskew-image/).
- [Set image properties](https://docs.aspose.com/imaging/python-net/setting-properties-on-images/).
- [Work with multipage image formats](https://docs.aspose.com/imaging/python-net/working-with-multipage-image-formats/).

## Load & Save Image Formats

**Raster Formats:** JPEG2000, JPEG, BMP, TIFF, GIF, PNG, DICOM, TGA, ICO\
**Metafiles:** EMF, WMF\
**Compressed metafiles:** EMZ, WMZ\
**Other:** WebP, Svg, Svgz (compressed Svg), DXF\
**Animation:** Apng

## Save Images As
**Fixed-layout:** PDF\
**Photoshop:** PSD\
**Web:** Html5 Canvas

## Load Images

**Various:** DjVu, DNG, ODG, EPS, CMX, CDR, DIB, OTG, FODG

## Platform Independence

Aspose.Imaging for Python via .NET can be used to develop applications on Windows Desktop (x86, x64), Windows Server (x86, x64), Windows Azure, as well as Linux x64. Aspose.Imaging for Python is based on .NET Core 3.1 platform, so you need install it as well.

## Get Started with Aspose.Imaging for Python via .NET

Are you ready to give Aspose.Imaging for Python via .NET a try? Simply execute run this command: `pip install aspose-imaging-python-net`.

## Resize a JPG Image

``` python
with Image.load("template.jpg") as image:
    image.resize(300, 300)
    image.save("output.jpg")
```

## Create & Manipulate PNG via API

``` python
# image width and height
width = 500
height = 300

# where created image to store
path = "createdImage.png"
# create options
options = PngOptions()
options.source = FileCreateSource(path, False)
with Image.create(options, width, height) as image:
    # create and initialize an instance of Graphics class 
    # and clear Graphics surface
    graphic = Graphics(image)
    graphic.clear(Color.green)
    # draw line on image
    graphic.draw_line(Pen(Color.blue), 9, 9, 90, 90)  

    # resize image
    new_width = 400
    image.resize_width_proportionally(new_width, ResizeType.LANCZOS_RESAMPLE);  

    # crop the image to specified area
    area = Rectangle(10, 10, 200, 200)
    image.crop(area)
   
    image.save()
}
```

----
[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/imaging/python-net) | [Docs](https://docs.aspose.com/imaging/python-net/) | [Demos](https://products.aspose.app/imaging/family) | [API Reference](https://reference.aspose.com/imaging/python-net) | [Examples](https://github.com/aspose-imaging/Aspose.Imaging-for-Python-NET) | [Blog](https://blog.aspose.com/category/imaging/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/imaging) | [Temporary License](https://purchase.aspose.com/temporary-license) | [Package page](https://pypi.org/project/aspose-imaging-python-net/)
