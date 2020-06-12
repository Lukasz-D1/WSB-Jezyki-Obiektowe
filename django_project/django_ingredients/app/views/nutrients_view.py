from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from app.models import Nutrients


class NutrientsListView(LoginRequiredMixin, ListView):
    model = Nutrients
    login_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreateNutrientsView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Nutrients
    fields = ['ingredient', 'calories_per_100g', 'fats_per_100g', 'protein_per_100g', 'carbs_per_100g']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_nutrients')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateNutrientsView, self).form_valid(form)


class UpdateNutrientsView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Nutrients
    fields = ['ingredient', 'calories_per_100g', 'fats_per_100g', 'protein_per_100g', 'carbs_per_100g']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_nutrients')
    login_url = reverse_lazy('index')

    def get_object(self, *args, **kwargs):
        obj = super(UpdateNutrientsView, self).get_object(*args, **kwargs)
        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj


class DeleteNutrientsView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Nutrients
    login_url = reverse_lazy('index')
    permission_required = ('app.delete_nutritions')

    def get_success_url(self):
        return reverse('all_ingredients')
