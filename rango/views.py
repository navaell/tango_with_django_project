from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    # Construct a dictionary to pass to the template engine as its context
    # Note the key boldmessage matches to {{ boldmessage }} in the template!

    category_list = Category.objects.order_by('-likes')[:5]

    pages_list = Page.objects.order_by('-views')[:5]

    context_dict = {}

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    'mostviewedpages': 'Most Viewed Pages',
                    'mostlikedcats': 'Most Liked Categories'}

    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list

    #Return a rendered response to send to the client.
    # We make use of the shortcut function tomake our lives easier
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
    #return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>" )


def about(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)



