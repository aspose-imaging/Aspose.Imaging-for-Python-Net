import aspose.pycore as aspycore
from aspose.imaging import *
from aspose.imaging.brushes import *
from aspose.imaging.fileformats.apng import *
from aspose.imaging.fileformats.png import *
from aspose.imaging.imageoptions import *
from aspose.imaging.sources import *


# Initialization
def get_data_root_dir_local():
	if 'BASE_DIR' in os.environ:
		return os.environ["BASE_DIR"]
	return "."


if 'get_output_dir' not in dir():
	get_output_dir = get_data_root_dir_local

### Classes 

# The graphics scene
class Scene:

	def __init__(self):
		self.graphics_objects = []
		self.auto_animation = None

	@property
	def animation(self):
		return self.auto_animation

	@animation.setter
	def animation(self, value):
		self.auto_animation = value

	# Adds the graphics object.
	# graphicsObject - The graphics object
	def add_object(self, graphics_object):
		self.graphics_objects.append(graphics_object)

	# Plays scene on the specified animation image.
	#   animationImage - The animation image.
	#   totalDuration - The total duration.
	def play(self, animation_image, total_duration):
		frame_duration = animation_image.default_frame_time
		num_frames = total_duration / frame_duration
		total_elapsed = 0
		# for loop
		for_first_step = True
		frame_index = 0
		while frame_index < num_frames:
			if for_first_step:
				for_first_step = False
			else:
				frame_index += 1
				if not (frame_index < num_frames):
					break

			if self.animation is not None:
				self.animation.update(total_elapsed)

			frame = animation_image.add_frame() if animation_image.page_count == 0 or frame_index > 0 else animation_image.pages[0]
			graphics = Graphics(frame)
			for graphics_object in self.graphics_objects:
				graphics_object.render(graphics)

			total_elapsed += frame_duration

# The graphics object
class IGraphicsObject:
    # Renders this instance using specified graphics.
    # graphics - The graphics.
    def render(self, graphics):
        pass


# The line
class Line(IGraphicsObject):

    def __init__(self):
        self.auto_start_point = None
        self.auto_end_point = None
        self.auto_line_width = None
        self.auto_color = None

    @property
    def start_point(self):
        return self.auto_start_point

    @start_point.setter
    def start_point(self, value):
        self.auto_start_point = value

    @property
    def end_point(self):
        return self.auto_end_point

    @end_point.setter
    def end_point(self, value):
        self.auto_end_point = value

    @property
    def line_width(self):
        return self.auto_line_width

    @line_width.setter
    def line_width(self, value):
        self.auto_line_width = value

    @property
    def color(self):
        return self.auto_color

    @color.setter
    def color(self, value):
        self.auto_color = value

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def render(self, graphics):
        graphics.draw_line(Pen(self.color, self.line_width), self.start_point, self.end_point)


# The ellipse
class Ellipse(IGraphicsObject):

    def __init__(self):
        self.auto_fill_color = None
        self.auto_center_point = None
        self.auto_radius_x = None
        self.auto_radius_y = None

    @property
    def fill_color(self):
        return self.auto_fill_color

    @fill_color.setter
    def fill_color(self, value):
        self.auto_fill_color = value

    @property
    def center_point(self):
        return self.auto_center_point

    @center_point.setter
    def center_point(self, value):
        self.auto_center_point = value

    @property
    def radius_x(self):
        return self.auto_radius_x

    @radius_x.setter
    def radius_x(self, value):
        self.auto_radius_x = value

    @property
    def radius_y(self):
        return self.auto_radius_y

    @radius_y.setter
    def radius_y(self, value):
        self.auto_radius_y = value

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def render(self, graphics):
        graphics.fill_ellipse(SolidBrush(self.fill_color), self.center_point.x - self.radius_x,
                              self.center_point.y - self.radius_y, self.radius_x * 2, self.radius_y * 2)

# The animation
class IAnimation:
    def __init__(self):
        self.auto_duration = None

    @property
    def duration(self):
        return self.auto_duration

    @duration.setter
    def duration(self, value):
        self.auto_duration = value

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def update(self, elapsed):
        pass


# The simple delay between other animations
class Delay(IAnimation):

    def init_fields(self):
        self.auto_duration = None

    @property
    def duration(self):
        return self.auto_duration

    @duration.setter
    def duration(self, value):
        self.auto_duration = value

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def update(self, elapsed):
        pass


# The linear animation
class LinearAnimation(IAnimation):

    def __init__(self, progress_handler):
        super(LinearAnimation, self).__init__()
        self.progress_handler = None
        self.auto_duration = None
        if progress_handler is None:
            raise RuntimeError("progressHandler")

        self.progress_handler = progress_handler

    @property
    def duration(self):
        return self.auto_duration

    @duration.setter
    def duration(self, value):
        self.auto_duration = value

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def update(self, elapsed):
        if elapsed <= self.duration:
            self.progress_handler(elapsed / self.duration)


# <summary>
# The sequential animation processor
# </summary>
#
class SequentialAnimation(list):

    def __init__(self, animations=None):
        super().__init__(animations)

    @property
    def duration(self):
        summ_duration = 0
        for animation in self:
            summ_duration += animation.duration

        return summ_duration

    @duration.setter
    def duration(self, value):
        raise NotImplementedError()

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def update(self, elapsed):
        total_duration = 0
        for animation in self:
            if total_duration > elapsed:
                break

            animation.update(elapsed - total_duration)
            total_duration += animation.duration


# <summary>
# The parallel animation processor
# </summary>
# 
class ParallelAnimation(list):

    def __init__(self, animations=None):
        super().__init__(animations)

    @property
    def duration(self):
        max_duration = 0
        for animation in self:
            if max_duration < animation.duration:
                max_duration = animation.duration

        return max_duration

    @duration.setter
    def duration(self, value):
        raise NotImplementedError()

    # Updates the animation progress.
    # elapsed - The elapsed time, in milliseconds.
    def update(self, elapsed):
        for animation in self:
            animation.update(elapsed)

# functions

def line_closure(line, scene_width, scene_height):
    def line_lambda(progress):
        line.start_point = PointF(30.0 + (progress * (scene_width - 60.0)), 30.0 + (progress * (scene_height - 60.0)))
        line.color = Color.from_argb(round(progress * 255), 0, 255 - round(progress * 255))

    return line_lambda


def line2_closure(line, scene_width, scene_height):
    def line_lambda(progress):
        line.end_point = PointF(scene_width - 30.0 - (progress * (scene_width - 60.0)),
                                30.0 + (progress * (scene_height - 60.0)))
        line.color = Color.from_argb(255, round(progress * 255), 0)

    return line_lambda


def line3_closure(line, scene_width, scene_height):
    def line_lambda(progress):
        line.start_point = PointF(scene_width - 30.0 - round(progress * (scene_width - 60.0)),
                                  scene_height - 30.0 - round(progress * (scene_height - 60.0)))
        line.color = Color.from_argb(255 - round(progress * 255), 255, 0)

    return line_lambda


def line4_closure(line, scene_width, scene_height):
    def line_lambda(progress):
        line.end_point = PointF(30.0 + (progress * round(scene_width - 60.0)),
                                scene_height - 30.0 - round(progress * (scene_height - 60.0)))
        line.color = Color.from_argb(0, 255 - round(progress * 255), round(progress * 255))

    return line_lambda


def ellipse_1_closure(ellipse):
    def ellipse_lambda(progress):
        ellipse.radius_x += progress * 10
        ellipse.radius_y += progress * 10
        comp_value = round(128 + (progress * 112))
        ellipse.fill_color = Color.from_argb(comp_value, comp_value, comp_value)

    return ellipse_lambda


def ellipse_3_closure(ellipse):
    def ellipse_lambda(progress):
        ellipse.radius_x -= progress * 10
        comp_value = round(240 - (progress * 224))
        ellipse.fill_color = Color.from_argb(comp_value, comp_value, comp_value)

    return ellipse_lambda


def ellipse_4_closure(ellipse):
    def ellipse_lambda(progress):
        ellipse.radius_y -= progress * 10
        comp_value = round(16 + (progress * 112))
        ellipse.fill_color = Color.from_argb(comp_value, comp_value, comp_value)

    return ellipse_lambda

# Example code:
print("Running example CreateAPNGAnimationFromGraphics")

# preparing the animation scene
scene_width = 400
scene_height = 400
act_duration = 1000
total_duration = 4000
frame_duration = 50
scene = Scene()
ellipse = Ellipse()
ellipse.fill_color = Color.from_argb(128, 128, 128)
ellipse.center_point = PointF(scene_width / 2.0, scene_height / 2.0)
ellipse.radius_x = 80.0
ellipse.radius_y = 80.0
scene.add_object(ellipse)
line = Line()
line.color = Color.blue
line.line_width = 10.0
line.start_point = PointF(30.0, 30.0)
line.end_point = PointF(scene_width - 30.0, 30.0)
scene.add_object(line)

line_animation1 = LinearAnimation(line_closure(line, scene_width, scene_height))
line_animation1.duration = act_duration

line_animation2 = LinearAnimation(line2_closure(line, scene_width, scene_height))
line_animation2.duration = act_duration

line_animation3 = LinearAnimation(line3_closure(line, scene_width, scene_height))
line_animation3.duration = act_duration
line_animation4 = LinearAnimation(line4_closure(line, scene_width, scene_height))
line_animation4.duration = act_duration
# Animation
full_line_animation = SequentialAnimation([line_animation1, line_animation2, line_animation3, line_animation4])
ellipse_animation1 = LinearAnimation(ellipse_1_closure(ellipse))
ellipse_animation1.duration = act_duration
ellipse_animation2 = Delay()
ellipse_animation2.duration = act_duration
ellipse_animation3 = LinearAnimation(ellipse_3_closure)
ellipse_animation3.duration = act_duration
ellipse_animation4 = LinearAnimation(ellipse_4_closure(ellipse))
ellipse_animation4.duration = act_duration
full_ellipse_animation = SequentialAnimation([ellipse_animation1, ellipse_animation2, ellipse_animation3, ellipse_animation4])
pan = ParallelAnimation([full_line_animation, full_ellipse_animation])
scene.animation = pan
# playing the scene on the newly created ApngImage
output_file_path = os.path.join(get_output_dir(), "result.png")
with ApngOptions() as create_options:
	create_options.source = FileCreateSource(output_file_path, False)
	create_options.color_type = PngColorType.TRUECOLOR_WITH_ALPHA
	with aspycore.as_of(Image.create(create_options, scene_width, scene_height), ApngImage) as image:
		image.default_frame_time = frame_duration
		scene.play(image, total_duration)
		image.save()

if 'SAVE_OUTPUT' not in os.environ:
	os.remove(output_file_path)

print("Finished example CreateAPNGAnimationFromGraphics")
