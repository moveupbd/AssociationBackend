from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Activities, Member, PhotoGallary, Slider, Event, Media
from .serializers import MemberSerializer, MemberDetailSerializer, MediaSerializer, EventSerializer, PhotoGallarySerializer, SliderSerializer, ActivitySerializer




class Members(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    
class MemberDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MemberDetailSerializer
    queryset = Member.objects.all()
    lookup_field = 'id'  # Setting the lookup field as 'id' to solve 'lookup filed' error 
    
    def get_queryset(self):
        member_id = self.kwargs['id']
        queryset= Member.objects.filter(id=member_id)
        return queryset
    

class SliderView(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

    
class SliderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SliderSerializer
    lookup_field = 'id'  # Setting the lookup field as 'id' to solve 'lookup filed' error 

    def get_queryset(self):
        slider_id = self.kwargs['id']
        queryset = Slider.objects.filter(id=slider_id)
        return queryset
    

class EventView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

class EventDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    lookup_field = 'id'  # Setting the lookup field as 'id' to solve 'lookup filed' error 
    
    def get_queryset(self):
        event_id = self.kwargs['id']
        queryset= Event.objects.filter(id=event_id)
        return queryset
    

class MediaView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    

class MediaDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = MediaSerializer
    lookup_field = 'id'  # Setting the lookup field as 'id' to solve 'lookup filed' error 
    
    def get_queryset(self):
        media_id = self.kwargs['id']
        queryset= Media.objects.filter(id=media_id)
        return queryset
    

class ActivityView(ListAPIView):
    queryset = Activities.objects.all()
    serializer_class = ActivitySerializer
    

class ActivityDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ActivitySerializer
    lookup_field = 'id'  # Setting the lookup field as 'id' to solve 'lookup filed' error 
    
    def get_queryset(self):
        media_id = self.kwargs['id']
        queryset= Activities.objects.filter(id=media_id)
        return queryset
    
    
class PhotoGallaryAPI(ListAPIView):
    queryset = PhotoGallary.objects.all()
    serializer_class = PhotoGallarySerializer
    


from django.contrib.sessions.models import Session
from django.utils import timezone

class StatsAPI(APIView):
    def get(self, request):
        # Count unique visited users
        unique_visited_users_count = self.get_unique_visited_users_count(request)

        # Total members count
        total_members_count = Member.objects.count()

        # Female members count
        female_members_count = Member.objects.filter(gender='female').count()

        # Male members count
        male_members_count = Member.objects.filter(gender='male').count()

        # Latest new member
        latest_member = Member.objects.latest('id')  # Assuming the latest member can be identified by the highest ID
        
        data = {
            'unique_visited_users_count': unique_visited_users_count,
            'total_members_count': total_members_count,
            'female_members_count': female_members_count,
            'male_members_count': male_members_count,
            'latest_member': MemberSerializer(latest_member).data
        }
        return Response(data)
    
    def get_unique_visited_users_count(self, request):
        # Get unique visitors count based on IP addresses
        ip_addresses = Session.objects.filter(expire_date__gte=timezone.now()).values_list('session_key', flat=True)
        unique_visited_users_count = len(set(ip_addresses))
        return unique_visited_users_count