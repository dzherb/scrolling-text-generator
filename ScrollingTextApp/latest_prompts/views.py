from django.shortcuts import render
from video_generator.models import Prompt


def latest_prompts(request):
    """Return page with list of latest prompts"""
    PROMPTS_ON_PAGE = 10

    context = {'prompts': Prompt.objects.all()[:PROMPTS_ON_PAGE]}
    return render(request,'latest_prompts/main.html', context=context)