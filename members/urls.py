from django.urls import path
from .views import Members, MemberDetail, SliderView, EventView, MediaView, EventDetail, MediaDetail

urlpatterns = [
    path('members/', Members.as_view(), name='member_list'),
    path('members/<int:id>', MemberDetail.as_view(), name='member_detail'),
    path('sliders/', SliderView.as_view(), name='sliders'),
    path('events/', EventView.as_view(), name='events'),
    path('events/<int:id>', EventDetail.as_view(), name='event_detail'),
    path('medias/', MediaView.as_view(), name='medias'),
    path('medias/<int:id>', MediaDetail.as_view(), name='media_detail'),
]
