from django.views.generic import ListView,DetailView

from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"
    context_object_name = "snack_list"
    
class SnackDetailView(DetailView):
    model = Snack
    template_name = "snack_details.html"
    context_object_name = "snack_details"

