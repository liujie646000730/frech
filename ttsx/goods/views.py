from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# 创建视图，返回index页面
def index(request):
    # return HttpResponse('你好')
    return render(request,'goods/index.html')