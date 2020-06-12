from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from app.models import Type


class TypeListView(LoginRequiredMixin, ListView):
    model = Type
    login_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CreateTypeView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Type
    fields = ['name']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_types')
    login_url = reverse_lazy('index')


class UpdateTypeView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Type
    fields = ['name']
    permission_required = ('app.change_type')
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_types')
    login_url = reverse_lazy('index')


class DeleteTypeView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Type
    login_url = reverse_lazy('index')
    permission_required = ('app.delete_type')

    def get_success_url(self):
        return reverse('all_types')
