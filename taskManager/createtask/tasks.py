from celery import shared_task

@shared_task 
def adding_task(x,y):
    return x+y

@shared_tak
def receive_command(command):
    return 
