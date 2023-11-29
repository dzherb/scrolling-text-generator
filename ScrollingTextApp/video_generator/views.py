from django.http import HttpResponse, HttpResponseNotFound, FileResponse

def send_file(request):

    file_location = '/generator/video/scrolling_text.mp4'

    try:
        response = FileResponse(open(file_location, 'rb'))
        #response = HttpResponse(file_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="scrolling_text.mp4"'
    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response