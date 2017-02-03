from django.shortcuts import render_to_response

def home(request):
    args = {}
    return render_to_response("home.html", args)

# This is the view for JAKE MY MAN
def jake(request):
    args = {}
    return render_to_response('jake.html', args)