from pathlib import Path
from django.http import HttpResponseNotFound, FileResponse
from .generator.video_generator import create_scrolling_text

def send_file(request):

    text = request.GET.get('text')
    file_location = 'video_generator/generator/video/scrolling_text.mp4'
    create_scrolling_text(text, 'arial.ttf', font_size=55, output_file=file_location)

    try:
        response = FileResponse(open(file_location, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{Path(file_location).stem}.mp4"'
    except IOError:
        response = HttpResponseNotFound('<h1>File does not exist, sorry :(</h1>')

    return response
