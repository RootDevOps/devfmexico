from django.shortcuts import render, redirect

from .models import Store
from .serializers import StoreModelSerializer,StoreAssistantSerializer
from django.http import Http404 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status

from .forms import StoreForm

class StoreList(APIView):
    #METHOD GET
    def get(self, request, format=None): 
        store = Store.objects.all() 
        serializer =StoreModelSerializer(store, many=True) 
        return Response(serializer.data) 

    #METHOD POST
    def post(self, request, format=None): 
        serializer = StoreModelSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StoreDetail(APIView):
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
    
class StoreAssistantList(APIView):
    def get(self,request):
        stores = Store.objects.all()
        serializer = StoreAssistantSerializer(stores, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class StoreSearch(APIView):
    def get(self,request,state):
        stores = Store.objects.filter(state_store = state)
        serializer = StoreAssistantSerializer(stores, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
def StoreRegister(request):
    title = "Add Store"
    form = StoreForm(request.POST or None, initial={'username': request.session['username']} )
    if form.is_valid():
        store = form.save(commit = False)
        store.save()
        return redirect("/")
    return render(request, "stores.html", {"form":form, "title":title, "contents": Store.objects.filter(username=request.session['username']) })    

    