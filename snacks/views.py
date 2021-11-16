from django.urls.base import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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
    fields = ["title", "purchaser", "discription"]


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = "snack_Update.html"
    fields = ["title", "purchaser", "discription"]


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_DeleteView.html"
    success_url = reverse_lazy("snack_list")
