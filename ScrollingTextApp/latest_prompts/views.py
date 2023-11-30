from django.shortcuts import render
from django.http import HttpResponse
from video_generator.models import Prompt


def latest_prompts(request):
    AMOUNT_OF_LATEST_PROMPTS = 10

    context = {'prompts': Prompt.objects.all()[:AMOUNT_OF_LATEST_PROMPTS]}
    return render(request,'latest_prompts/main.html', context=context)