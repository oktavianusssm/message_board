from django.views.generic import ListView
from .models import Post
# Create your views here.

class HomepageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list' # to know what is contained in the template
