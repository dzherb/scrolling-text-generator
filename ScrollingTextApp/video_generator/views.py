from pathlib import Path
from django.http import HttpResponseNotFound, FileResponse
from .generator.video_generator import create_scrolling_text

def send_file(request):
    """Makes a video file from user's input and sends it back"""
    try:
        # Getting 'text' parameter from url
        text = request.GET.get('text')

        # Generating video
        file_location = 'video_generator/generator/video/scrolling_text.mp4'
        create_scrolling_text(text, 'arial.ttf', font_size=55, file_path=file_location)

        # Creating a response
        response = FileResponse(open(file_location, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{Path(file_location).stem}.mp4"'

    except (IOError, TypeError):
        response = HttpResponseNotFound('<h1>Something went wrong, sorry :(</h1>')

    return response
