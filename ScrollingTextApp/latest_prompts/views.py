from django.shortcuts import render
from video_generator.models import Prompt


def latest_prompts(request):
    """Return page with list of latest prompts"""
    PROMPTS_ON_PAGE = 10
    prompts_to_show = Prompt.objects.all()[:PROMPTS_ON_PAGE]
    context = {'prompts': prompts_to_show,
               'max_prompts': PROMPTS_ON_PAGE,
               'amount_of_prompts': len(prompts_to_show)}

    return render(request,'latest_prompts/main.html', context=context)