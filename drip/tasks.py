# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from celery.task import task
from drip.models import Drip


@task(name='tasks.send_drips')
def send_drips(messages):
    """
    Celery standard task for sending drip.
    """
    for drip in Drip.objects.filter(enabled=True):
        drip.drip.run()
