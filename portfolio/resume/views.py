from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Skill, Education, WorkExperience, Languages, Photo, Service

# Create your views here.


def home(request) -> HttpResponse:
    skills = Skill.objects.all()
    studies = Education.objects.all()
    jobs = WorkExperience.objects.all()
    languages = Languages.objects.all()
    photos = Photo.objects.all()
    services = Service.objects.all()



    return render(request, "index.html", context={"name": "Lilit", "surname": "Khachatryan", 
                                                  "quote": "Be a voice, not an echo...", 
                                                  "email": "lilit.khachatryan.botany@gmail.com",
                                                  "phone": "+374 94 864060",
                                                  "skills": skills,
                                                  "study": studies,
                                                  "jobs": jobs, 
                                                  "languages": languages,
                                                  "photo": photos,
                                                  "services": services}
                                                  )