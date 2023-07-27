from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .forms import MessageForm
from .models import (
    Skill, 
    Education, 
    WorkExperience, 
    Languages, 
    Photo, 
    Service, 
    PersonalInfo,
    SocialLink,
    Navbar)

# Create your views here.


def home(request) -> HttpResponse:

    status = 200

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/#contact")


    skills = Skill.objects.all()
    studies = Education.objects.all()
    jobs = WorkExperience.objects.all()
    languages = Languages.objects.all()
    photos = Photo.objects.all()
    services = Service.objects.all()
    personal_info = PersonalInfo.objects.filter(user__username="admin").first()
    age = personal_info.age() if personal_info else None
    socials = SocialLink.objects.all()
    navbars = Navbar.objects.all()
    messageForm = MessageForm()




    return render(request, "index.html", context={"skills": skills,
                                                  "study": studies,
                                                  "jobs": jobs, 
                                                  "languages": languages,
                                                  "photo": photos,
                                                  "services": services,
                                                  "personal_info": personal_info,
                                                  "age": age,
                                                  "socials": socials,
                                                  "navbars": navbars,
                                                  "messageForm": messageForm}
                                                  )

def portfolio_project(request, pk):
    project = get_object_or_404(PortfolioProject, id=pk)
    return render(request, "portfolio_details.html", context={"project": project})