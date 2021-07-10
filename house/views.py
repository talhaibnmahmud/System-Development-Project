from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.utils import IntegrityError
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls.base import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django_filters.views import FilterView

from area.models import District, Division
from house.filters import HouseFilter, HouseSearchFilter
from house.forms import HouseCreateForm
from house.models import Favourite, House, Photo


# Create your views here.
class HouseListView(ListView):
    model = House
    context_object_name = 'houses'
    ordering = ['-created', ]
    paginate_by = 12
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            favourites = Favourite.objects.values_list('house_id', flat=True).filter(user=request.user)
            self.extra_context = {'favourites': favourites, }

            return super(HouseListView, self).get(request, *args, **kwargs)

        return super(HouseListView, self).get(request, *args, **kwargs)


class HouseDetailView(DetailView):
    model = House

    def get(self, request, *args, **kwargs):
        photos = Photo.objects.filter(house=kwargs['pk'])
        self.extra_context = {'photos': photos, }

        return super(HouseDetailView, self).get(request, *args, **kwargs)


class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'

    districts = District.objects.all()
    divisions = Division.objects.all()
    extra_context = {'divisions': divisions, 'districts': districts, }

    # def form_valid(self, form):
    #     # print(self.request.POST)
    #     house = form.save(commit=False)
    #     # district = District.objects.get(name=self.request.POST['district'])
    #     # division = District.objects.get(name=self.request.POST['division'])
    #     house.owner = self.request.user.id
    #     # house.district = district
    #     # house.division = division
    #     form.save()
    #     print('Form Valid Called')
    #
    #     return super(HouseCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(kwargs)
        form = HouseCreateForm(request.POST)
        images = request.FILES.getlist('images')
        # print(images)

        # print(form)
        # print(form.is_valid())
        if form.is_valid():
            form.instance.owner = request.user
            house = form.save()

            for image in images:
                photo = Photo.objects.create(photo=image, house=house)
                photo.save()
                # print(photo)
                # print(image)
            return redirect(reverse_lazy('house:home'))
        # print(form.is_invalid())
        # print(self.request.user)

        return super(HouseCreateView, self).post(request, *args, **kwargs)


class HouseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = House
    form_class = HouseCreateForm
    template_name = 'house/house_update_form.html'

    districts = District.objects.all()
    divisions = Division.objects.all()
    extra_context = {'divisions': divisions, 'districts': districts, }

    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().owner


# TODO: Add to favourites list from default view
class HouseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = House
    success_url = reverse_lazy('house:home')

    def test_func(self):
        return self.request.user == self.get_object().owner


@method_decorator(csrf_exempt, name='dispatch')
class HouseSearchView(FilterView):
    filterset_class = HouseSearchFilter
    template_name = 'house/house_search.html'


# TODO: Add to favourites list from search view
@method_decorator(csrf_exempt, name='dispatch')
class HouseFilterView(FilterView):
    filterset_class = HouseFilter
    model = House

    divisions = Division.objects.all()
    districts = District.objects.all()
    extra_context = {'divisions': divisions, 'districts': districts, }
    ordering = ['-created', ]
    paginate_by = 12


@method_decorator(csrf_exempt, name='dispatch')
class AddFavouriteView(LoginRequiredMixin, View):
    @staticmethod
    def post(request, *args, **kwargs):
        # print('Add PK', kwargs)

        house = get_object_or_404(House, id=kwargs['pk'])
        # print(house)
        favourite = Favourite(user=request.user, house=house)

        try:
            favourite.save()
        except IntegrityError:
            favourite = {}
        return HttpResponse(favourite)


@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavouriteView(LoginRequiredMixin, View):
    @staticmethod
    def post(request, *args, **kwargs):
        print('Delete PK', kwargs)
        house = get_object_or_404(House, id=kwargs['pk'])

        try:
            favourite = Favourite.objects.get(user=request.user, house=house).delete()
        except Favourite.DoesNotExist:
            favourite = {}

        return HttpResponse(favourite)


class HouseFavouriteListView(LoginRequiredMixin, ListView):
    model = House
    context_object_name = 'houses'
    paginate_by = 12
    template_name = 'index.html'

    def get_queryset(self):
        return House.objects.filter(favourite__user=self.request.user).order_by('-created')

    def get(self, request, *args, **kwargs):
        favourites = Favourite.objects.values_list('house_id', flat=True).filter(user=request.user)
        self.extra_context = {'favourites': favourites, }

        return super(HouseFavouriteListView, self).get(request, *args, **kwargs)
