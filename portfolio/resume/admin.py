from django.contrib import admin
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

# Register your models here.
class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created_on"]
    list_filter = ["value"]
    search_fields = ["name"]


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date", "end_date", "is_current", "degree", "thesis_title"]
    list_filter = ["degree"]
    search_fields = ["university_name"]


class WorkAdmin(admin.ModelAdmin):
    list_display = ["company_name", "start_date", "end_date", "is_current", "position"]
    list_filter = ["start_date"]
    search_fields = ["company_name"]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter = ["value"]
    search_fields = ["name"]


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "image"]
    search_fields = ["title"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    search_fields = ["title"]


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["link"]
    search_fields = ["link"]


class NavbarAdmin(admin.ModelAdmin):
    list_display = ["section_name"]


admin.site.register(Skill, SkillAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(WorkExperience, WorkAdmin)
admin.site.register(Languages, LanguageAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(PersonalInfo)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Navbar, NavbarAdmin)


