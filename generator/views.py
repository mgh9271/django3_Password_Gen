from django.shortcuts import render
from django.http import HttpResponse
import random
def about(request):
    return render(request, 'generator/about.html')
def home(request):
    return render(request, 'generator/home.html', {'password':"wfdklvnwekn[wk]"})
def password(request):

    char=list('abcdefghijklmnopqrstuwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
       char.extend(list('!@#$%^&*()_+<>?:":|}{{*/-}"'))
    if request.GET.get('numbers'):
       char.extend(list("1234567890"))
    length=int(request.GET.get('length',12))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(char)


    return render(request, 'generator/password.html', {'password':thepassword})
