from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from profileapp.decorators import profile_ownership_required

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):     #form안에 이미지 닉네임 메시지가 담겨이씅ㅁ
        form.instance.user=self.request.user    #요청을 보낸 유저가 객체가 된다
        return  super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})



@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'

    template_name = 'profileapp/update.html'

    def get_success_url(self):

        from django.urls import reverse
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})