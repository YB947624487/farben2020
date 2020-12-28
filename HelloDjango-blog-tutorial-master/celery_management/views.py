from django.shortcuts import render
from django.http import JsonResponse
from . import tasks
# Create your views here.

def demo(requst):
    # 执行异步任务
    print('demo 开始执行异步任务')
    tasks.Demo().delay()
    # tasks.Demo().run()
    print('the end')
    return JsonResponse({'result':"celery is wonderful"})
