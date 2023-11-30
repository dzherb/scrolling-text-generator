from pathlib import Path
from django.http import HttpResponseNotFound, FileResponse
from django.shortcuts import render
from .generator.video_generator import create_scrolling_text

def send_file(request):
    """Makes a video file from user's input and sends it back"""
    try:
        # Getting parameters from url.
        text = request.GET.get('text', 'No input :(').strip()
        font_size = int(request.GET.get('font_size', '55'))

        # image_size = (image_width, image_height) in pixels
        image_size = request.GET.get('image_size', '100,100').split(',')
        image_size = tuple(int(dimension.strip()) for dimension in image_size)

        # Background color in rgb format.
        bg_color = request.GET.get('bg_color', '0,0,0').split(',')
        bg_color = tuple(int(color.strip()) for color in bg_color)
        # Same with text.
        text_color = request.GET.get('text_color', '255,255,255').split(',')
        text_color = tuple(int(color.strip()) for color in text_color)

        # Duration of a video in seconds.
        duration = int(request.GET.get('d', '3').strip())

        # Direction of a text can be 'left' or 'right'
        direction = request.GET.get('dir', 'left').strip()

        # Generating a video.
        file_location = 'video_generator/generator/video/scrolling_text.mp4'
        create_scrolling_text(text=text,
                              font_size=font_size, file_path=file_location, image_size=image_size,
                              bg_color=bg_color, text_color=text_color, duration=duration, direction=direction)

        # Creating a response.
        response = FileResponse(open(file_location, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{Path(file_location).stem}.mp4"'

    except (IOError, TypeError):
        response = HttpResponseNotFound('<h1>Something went wrong, sorry :(</h1>')

    return response

def home(request):
    return render(request, 'video_generator/home.html')