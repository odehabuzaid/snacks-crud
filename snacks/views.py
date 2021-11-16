from django.views.generic import ListView

from .models import Snack

class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"
    context_object_name = "snack_list"
    
