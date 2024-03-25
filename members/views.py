from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Member, Slider, Event, Media
from .serializers import MemberSerializer, MemberDetailSerializer, MediaSerializer, EventSerializer, SliderSerializer

# class Posts(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request,'home.html', {"posts":posts})

class Members(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class MemberDetail(ListAPIView):
    serializer_class = MemberDetailSerializer
    
    def get_queryset(self):
        member_id = self.kwargs['id']
        queryset= Member.objects.filter(id=member_id)
        return queryset
    
class SliderView(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    

class EventView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

class EventDetail(ListAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        event_id = self.kwargs['id']
        queryset= Event.objects.filter(id=event_id)
        return queryset
    

class MediaView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    

class MediaDetail(ListAPIView):
    serializer_class = MediaSerializer
    
    def get_queryset(self):
        media_id = self.kwargs['id']
        queryset= Media.objects.filter(id=media_id)
        return queryset