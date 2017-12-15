from django.shortcuts import render, redirect
from .forms import AssistantForm
from .models import Assistants

from .serializers import AssistantModelSerializer
from .models import Store
from django.http import Http404 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

# Create your views here.
def AssistantRegister(request):
    title = "Add Assistant"
    form = AssistantForm(request.POST or None)
    if form.is_valid():
        assistant = form.save(commit = False)
        assistant.save()
        return redirect("assistants.html")
    return render(request, "assistants.html", {"form":form, "title":title, "contents": Assistants.objects.all() })    

'''
class AssistantDetail(APIView):
    def _get_store(self, id):
        try:
            store = Store.objects.get(id=id)
            return store
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, id):
        store = self._get_store(id)
        serializer = StoreModelSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)
'''