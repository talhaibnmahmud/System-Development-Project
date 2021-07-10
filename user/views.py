from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render

from house.models import House
from user.models import User


# Create your views here.
class UserCreateView(CreateView):
    model = User
    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'phone',
        'password',
    ]

    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(self.request.POST['password'])
        user.save()

        return super(UserCreateView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super(UserCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        return super(UserCreateView, self).post(request, *args, **kwargs)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=kwargs.get('pk'))
        houses = House.objects.filter(owner=user)

        return render(request, template_name='user/profile.html', context={'user': user, 'houses': houses})
