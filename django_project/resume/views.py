from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import ResumeTemplates

# Create your views here.

def resume_home(request):
    return render(request , 'resume/home.html')

def chooseTemplate(request):
    if request.method == "POST" and 'sample' in request.POST:
        print("request is ",request.POST)
        id = request.POST.get('sample')
        return HttpResponseRedirect('/resume/details/' + id)

    context = {"resume_templates" : ResumeTemplates.objects.all()}
    return render(request , 'resume/choosetemplates.html', context)

def details(request, id):
    resume = ResumeTemplates.objects.get(id = id)
    print("resume is ", resume)
    context = {'resume' : resume}
    if (request.method == 'POST' ):
        print("request recieved")
        return redirect('resume-complete')
    return render(request, 'resume/detailsform.html', context)

def complete(request):
    return render(request, 'resume/complete.html')