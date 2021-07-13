from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accountapp.models import NEWMODEL


def hello_world(request):
    if request.method=="POST":

        temp=request.POST.get('input_text')
        model_instance=NEWMODEL()
        model_instance.text=temp
        model_instance.save()
        model_instance.save()
        from django.urls import reverse
        return HttpResponseRedirect(reverse('accountapp:hello_world'))  #GET방식으로 전환하여
                                                                                                                    # F5버튼을 눌러도 계속 축적되지 않는다.
    else :
        data_list=NEWMODEL.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={'data_list' : data_list})