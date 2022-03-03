from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def dinner(request, menu, nums):
    context = {
        'menu' : menu,
        'nums' : nums,
    }
    return render(request, 'dinner.html', context)