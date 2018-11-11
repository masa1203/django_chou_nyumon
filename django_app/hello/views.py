from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#from .forms import HelloForm
from .models import Friend
from .forms import FriendForm
from .forms import FindForm

# Create your views here.

def index(request):
    data = Friend.objects.all()
    params = {
        'title':'Hello',
        'data':data,
    }
    return render(request, 'hello/index.html', params)

#create model
def create(request):
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }

    if(request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)

#edit model
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

# delete Model
def delete(request, num):
    friend = Friend.objects.get(id=num)
    params = {
        'title':'Hello',
        'id':num,
        'obj':friend,
    }
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    return render(request, 'hello/delete.html', params)

# find model
def find(request):
    if(request.method == 'POST'):
        msg = 'search result...'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(age__lte=int(str))
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title':'Hello',
        'message':msg,
        'form':form,
        'data':data,
    }
        
    return render(request, 'hello/find.html', params)