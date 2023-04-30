from datetime import datetime, timedelta

from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from .tasks import hello, printer


class IndexView(View):
    def get(self, request):
        printer.apply_async([10], eta=datetime.now() + timedelta(seconds=7))
        hello.delay()
        return HttpResponse('Hello!')


# команда запуска celery
# celery -A project worker -l info -P threads --concurrency 4