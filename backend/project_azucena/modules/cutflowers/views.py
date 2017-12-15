from django.shortcuts import render, redirect
from .forms import CutflowerForm
from .models import Cutflowers

# Create your views here.
def CutflowerRegister(request):
    title = "Add Cut Flower"
    form = CutflowerForm(request.POST or None)
    if form.is_valid():
        cutflower = form.save(commit = False)
        cutflower.save()
        return redirect("cutflowers.html")
    return render(request, "cutflowers.html", {"form":form, "title":title, "contents": Cutflowers.objects.all() })    


