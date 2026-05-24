from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import room

from rest_framework.response import Response
from .serializers import RoomSerializer
from rest_framework.decorators import api_view

#@api_view(['GET'])
#def test(request):

 #   users = room.objects.all()

   # serializer = RoomSerializer(users, many=True)

    #return Response({
    #    'status': 200,
   #     'user': serializer.data
   # })

# Create your views here.
def test(request):
    user = room.objects.all()
    #.values()
   # return JsonResponse({'status': 200, 'user': list(user)})
    #print("hello world")
    return render(request, 'polls/test.html', {'users': user})
@api_view(['POST'])
def recive(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        image = request.FILES.get('img')
        video = request.FILES.get('video')
        audio = request.FILES.get('audio')
        if room.objects.filter(user=name).exists():
                return Response({
                    "status": 200,
                    "name": "name already used in db",
                })
        else:
            new_user = room.objects.create(user=name, image=image, video=video, audio=audio)
            new_user.save()
            return Response({
            "status": 200,
            "name": "saved in db",
        })
    else:
        return Response({
            "status": 404,
            "name": "ops",
        })