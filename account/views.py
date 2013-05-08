from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def hello_world(request):
    t = get_template("hello_world.html")
    context = Context()
    html = t.render(context)
    return HttpResponse(html)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            pass
            #reutnr a 'disabled account' error message
    else:
        pass
        #return an 'invalid login' error message

def logout(request):
    logout(request)





