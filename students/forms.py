from django import forms
from courses.models import Course


# зачисление студентов на курсы
class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.HiddenInput)