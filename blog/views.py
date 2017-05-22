from django.shortcuts import render


def getIndex(req):

    return render(request=req, template_name='../templates/blog/index.html')