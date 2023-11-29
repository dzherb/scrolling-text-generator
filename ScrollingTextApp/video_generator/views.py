from django.http import HttpResponse, HttpResponseNotFound, FileResponse

def send_file(request):

    file_location = 'video_generator/generator/video/scrolling_text.mp4'

    try:
        response = FileResponse(open(file_location, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="scrolling_text.mp4"'
    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File does not exist</h1>')

    return response
