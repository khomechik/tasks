from django.shortcuts import render
from django.views import View

# Create your views here.

SERVER_VERSION = "0.0.7"


class AboutView(View):
    def get(self, request):
        context = {"server_version": SERVER_VERSION, "user": request.user}
        return render(request, 'about.html', context=context)
