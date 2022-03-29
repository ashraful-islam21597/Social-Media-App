from django.contrib import admin

from Users.models import profile, CustomUser, profession, Graduate_school, school, college

admin.site.register(CustomUser)
admin.site.register(profile)
admin.site.register(profession)
admin.site.register(Graduate_school)
admin.site.register(school)
admin.site.register(college)


