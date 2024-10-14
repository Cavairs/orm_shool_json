from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teachers


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all()
    obj_list = Teachers.objects.all()
    context = {

        'object_list': object_list,
        'obj_list': obj_list
    }
    print(context)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
