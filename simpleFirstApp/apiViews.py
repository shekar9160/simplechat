from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from simpleFirstApp.models import Subjects

@csrf_exempt
def getSubjects(request):
    subject=Subjects.objects.filter(course_id=request.POST.get('course_id',''))
    subject_obj=serializers.serialize('python',subject)
    return JsonResponse(subject_obj,safe=False)