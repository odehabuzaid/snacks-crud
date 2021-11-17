from django.urls.base import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Snack


class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"
    context_object_name = "snack_list"


class SnackDetailView(DetailView):
    model = Snack
    template_name = "snack_details.html"
    context_object_name = "snack_details"


class SnackCreateView(CreateView):
    model = Snack
    template_name = "snack_create.html"
    fields = ["title", "purchaser", "description"]


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = "snack_update.html"
    fields = ["title", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_delete.html"
    success_url = reverse_lazy("snack_list")
