from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def index(re):
    return render(re, 'index.html')

def manage(re):
    return render(re, 'manage.html')

def log(re):
    if re.method == 'POST':
        f = re.POST['n1']
        g = re.POST['n2']
        try:
            d = user.objects.get(email=f)
            if d.password == g:
                if d.status == '1':         # user
                    re.session['id0'] = f
                    print('101')
                    return redirect(home)
                else:                       # admin
                    re.session['id1'] = f
                    print('102')
                    return redirect(manage)
            else:
                messages.error(re, 'Incorrect Password')
                return redirect(log)
        except Exception:
            messages.error(re, 'Incorrect Email')
            return redirect(log)
    else:
        return render(re, 'login.html')



def signup(request):
    if request.method == 'POST':
        email = request.POST.get('n2')
        if user.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists.')
            return render(request, 'signup.html')
        a = request.POST['n1']
        b = email
        d = request.POST['n4']
        data = user.objects.create(name=a, email=b, password=d, status=1)
        data.save()
        return redirect(log)
    else:
        return render(request, 'signup.html')


def logout(re):
    if 'id0' in re.session:
        re.session.flush()
        return redirect(index)
    if 'id1' in re.session:
        re.session.flush()
        return redirect(index)
    else:
        re.session.flush()
        return redirect(index)


def completed(request):
    if request.method == 'POST':
        h = request.POST['n']
        d = task.objects.filter(title=h)
        d.update(status='completed')
        return redirect(home)
    else:
        return HttpResponse('error')


def add(request):
    if request.method == 'POST':
        email = request.session['id0']
        title = request.POST['n1']
        description = request.POST['n2']
        d = task.objects.create(email=email, title=title, description=description, status='pending')
        d.save()
        return redirect(home)
    else:
        return HttpResponse('error')


def remove(request):
    if request.method == 'POST':
        h = request.POST['n']
        d = task.objects.filter(title=h)
        d.delete()
        return redirect(home)
    else:
        return HttpResponse('error')


def update(request):
    if request.method == 'POST':
        email = request.session['id0']
        title = request.POST['n1']
        description = request.POST['n2']
        d = task.objects.filter(email=email)
        d.update(title=title, description=description)
        return HttpResponse("success")
    else:
        return redirect(home)


def home(request):
    if request.method == 'GET':
        email = request.session['id0']
        d = task.objects.filter(email=email)
        return render(request, 'home.html', {'r': d})
    else:
        return redirect(manage)


