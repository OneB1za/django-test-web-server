from django.shortcuts import render
from django.utils import timezone

def home(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    now = timezone.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")

    context = {
        'ip': ip,
        'current_time': current_time,
    }
    context = {'ip': ip, 'current_time': current_time}

    return render(request, 'web/index.html', context)

