from django.contrib import admin

from cours.models import Cours


class CourseAdmin(admin.ModelAdmin):
    list_display = ("titre", "prix", "est_gratuit",)
    list_filter = ["est_gratuit"]


admin.site.register(Cours, CourseAdmin)
