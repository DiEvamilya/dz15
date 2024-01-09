from django import forms

from program.models import Course, Module, Lesson


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'average_time')
        exclude = ('slug',)
        widgets = {
            'descriptions': forms.Textarea(attrs={'cols': 30, 'rows': 10})
        }
class ModuleModelForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ('course', 'title', 'description', 'average_time')
        exclude = ('slug',)
        widgets = {
            'descriptions': forms.Textarea(attrs={'cols': 30, 'rows': 10})
        }


class LessonModelForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('module', 'title', 'content', 'duration_time')
        exclude = ('slug',)
        widgets = {
            'content': forms.Textarea(attrs={'cols': 30, 'rows': 10})
        }