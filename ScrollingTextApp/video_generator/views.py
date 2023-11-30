from pathlib import Path
from django.http import HttpResponseNotFound, FileResponse
from django.shortcuts import render
from .generator.video_generator import create_scrolling_text
from . import models


def send_file(request):
    """Makes a video file from user's input and sends it back"""
    DEFAULT_TEXT = 'No input :('
    DEFAULT_FONT_SIZE = 55
    DEFAULT_IMAGE_SIZE = (100, 100)
    DEFAULT_BG_COLOR = (0, 0, 0)
    DEFAULT_TEXT_COLOR = (255, 255, 255)
    DEFAULT_DURATION = 3
    DEFAULT_DIRECTION = 'left'

    try:  # Get parameters from url.
        text = request.GET.get('text', DEFAULT_TEXT).strip()

        font_size = int(request.GET.get('font_size', f'{DEFAULT_FONT_SIZE}'))

        # Get image size as a tuple - (image_width, image_height). Size is in pixels.
        frame_size = request.GET.get('frame_size', f'{",".join(map(str, DEFAULT_IMAGE_SIZE))}')
        frame_size = tuple(int(dimension.strip()) for dimension in frame_size.split(','))

        # Get background color in rgb format as a tuple - (r, g, b)
        bg_color = request.GET.get('bg_color', f'{",".join(map(str, DEFAULT_BG_COLOR))}')
        bg_color = tuple(int(color.strip()) for color in bg_color.split(','))
        # Same with text.
        text_color = request.GET.get('text_color', f'{",".join(map(str, DEFAULT_TEXT_COLOR))}')
        text_color = tuple(int(color.strip()) for color in text_color.split(','))

        # Get duration of a video in seconds.
        duration = int(request.GET.get('d', f'{DEFAULT_DURATION}').strip())
        # We need a reasonable number.
        if duration > 30 or duration <= 0:
            raise ValueError

        # Get a direction of a text. It can move to the 'left' side or to the 'right'.
        direction = request.GET.get('dir', DEFAULT_DIRECTION).strip()

        print(text, font_size, frame_size, bg_color, text_color, duration, direction)

        # Generate a video.
        file_location = 'video_generator/generator/video/scrolling_text.mp4'
        create_scrolling_text(text=text, font_size=font_size, file_path=file_location, frame_size=frame_size,
                              bg_color=bg_color, text_color=text_color, duration=duration, direction=direction)

        # Creating a response.
        response = FileResponse(open(file_location, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{Path(file_location).stem}.mp4"'

        # Save prompt to the database
        prompt = models.Prompt(text=text, font_size=font_size, frame_size=list(frame_size),
                               background_color=list(bg_color), text_color=list(text_color),
                               duration=duration, direction=direction)
        prompt.save()

    except (IOError, TypeError, ValueError) as e:
        print(e)
        response = HttpResponseNotFound('<h1>Something went wrong, sorry :(</h1>')

    return response

def home(request):
    return render(request, 'video_generator/home.html')