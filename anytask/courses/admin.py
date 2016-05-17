from courses.models import Course, FilenameExtension, DefaultTeacher, MarkField, CourseMark
from django.contrib import admin

class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('teachers', 'groups', 'filename_extensions', 'issue_fields')
    list_display = ('name', 'year', )
    list_filter = ('name', 'year__start_year', 'is_active')
    search_fields = ('name', 'year__start_year', 'teachers__username', 'groups__name', 'filename_extensions_name')

class DefaultTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'group', 'course')
    list_filter = ('group', 'course')

admin.site.register(Course, CourseAdmin)
admin.site.register(FilenameExtension)
admin.site.register(DefaultTeacher, DefaultTeacherAdmin)
admin.site.register(CourseMark)
admin.site.register(MarkField)
