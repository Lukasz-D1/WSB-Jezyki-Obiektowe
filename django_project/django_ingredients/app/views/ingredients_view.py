from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

from app.models import Nutrients
from app.models import Ingredient
from app import logger


class AllIngredientView(LoginRequiredMixin, ListView):
    model = Ingredient
    login_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        logger.debug('AllIngredientView.get_context_data')
        context = super().get_context_data(**kwargs)
        return context


class DetailIngredientView(LoginRequiredMixin, DetailView):
    model = Ingredient
    login_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        nutrients = Nutrients.objects.filter(ingredient=self.get_object()).values()
        for info in nutrients:
            context['calories'] = info['calories_per_100g']
            context['fats'] = info['fats_per_100g']
            context['protein'] = info['protein_per_100g']
            context['carbs'] = info['carbs_per_100g']
        return context


class CreateIngredientView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Ingredient
    fields = ['name', 'type', 'description']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_ingredients')
    login_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateIngredientView, self).form_valid(form)


class UpdateIngredientView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Ingredient
    fields = ['name', 'type', 'description']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_ingredients')
    login_url = reverse_lazy('index')

    def get_object(self, *args, **kwargs):
        obj = super(UpdateIngredientView, self).get_object(*args, **kwargs)
        if not obj.author == self.request.user:
            raise PermissionDenied
        return obj


class UpdateIngredientStatusView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Ingredient
    fields = ['status']
    success_message = "Entry was updated successfully"
    success_url = reverse_lazy('all_ingredients')
    login_url = reverse_lazy('index')
    permission_required = ('change_ingredient_status')


class DeleteIngredientView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Ingredient
    login_url = reverse_lazy('index')
    permission_required = ('app.delete_ingredient')

    def get_success_url(self):
        return reverse('all_ingredients')
