from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.forms import todoform
from todoapp.models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class new(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'task'
class new3(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name = 'task'
class new1(UpdateView):
    model=task
    template_name = 'detail.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':object.id})
class new2(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('classbase')
def home(request):
    obj = task.objects.all()
    if request.method=='POST':
        obj1=request.POST.get('name','')
        obj2=request.POST.get('priority','')
        obj3=request.POST.get('date','')
        task1=task(name=obj1,priority=obj2,date=obj3)
        task1.save()
    return render(request,'home.html',{'task':obj})
# def detail(request):
#
#     return render(request,'detail.html',)
def delete(request,taskid):
    obj=task.objects.get(id=taskid)
    if request.method=='POST':
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    obj1=task.objects.get(id=id)
    form1=todoform(request.POST or None,instance=obj1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'name':obj1,'form':form1})


