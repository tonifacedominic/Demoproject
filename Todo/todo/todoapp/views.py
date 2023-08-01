from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from .forms import Todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
    model = task
    template_name = 'home.html'
    context_object_name = 'details'

class Taskdetailview(DetailView):
    model = task
    template_name = 'details.html'
    context_object_name = 'task'

class Taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')







def add(request):
    details = task.objects.all()
    if request.method=='POST':

        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        addtask=task(name=name,priority=priority,date=date)
        addtask.save()
        return redirect('/')
    return render(request,'home.html',{'details':details})

def delete(request,id):
    if request.method=='POST':
        delete=task.objects.get(id=id)
        delete.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    update=task.objects.get(id=id)
    upform=Todoform(request.POST or None, instance=update)
    if upform.is_valid():
        upform.save()
        return redirect('/')
    return render(request,'update.html',{'upform':upform,'update':update})

# def details(request):
#     details=task.objects.all()
#     return render(request,'details.html',{'details':details})

