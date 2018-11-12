from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
#from .forms import HelloForm
from .models import Friend, Message
from .forms import FriendForm
from .forms import FindForm
from .forms import CheckForm, MessageForm
from django.db.models import Q #条件検索
from django.core.paginator import Paginator


# Create your views here.

def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title':'Hello',
        'message':'',
        'data':page.get_page(num),
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
        val = str.split()
        #data = Friend.objects.filter(age__gte=val[0], age__lte=val[1])
        #data = Friend.objects \
        #    .filter(age__gte=val[0]) \
        #    .filter(age__lte=val[1])
        data = Friend.objects.filter(Q(name__contains=str)|Q(mail__contains=str))
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

# check model
def check(request):
    params = {
        'title':'Hello',
        'message':'check validation',
        'form':CheckForm(),
    }
    if(request.method=='POST'):
        form = CheckForm(request.POST)
        params['form'] = form
        if(form.is_valid()):
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)

#message
def message(request, page=1):
    if(request.method=='POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 3)
    params = {
        'title':'Message',
        'form':MessageForm(),
        'data':paginator.get_page(page)
    }
    return render(request,'hello/message.html',params)