from django.shortcuts import render, redirect
import string
import random

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'random_app/index.html')

def id_generator(size=14, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create(request):
    if request.method == 'POST':
        request.session['random'] = id_generator()
        request.session['count'] += 1
        return redirect('/')
    else:
        return redirect('/')
