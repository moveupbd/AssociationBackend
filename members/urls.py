from django.urls import path
from .views import Members, MemberDetail, PhotoGallaryAPI, SliderView, EventView, MediaView, EventDetail, MediaDetail, SliderDetail, StatsAPI, ActivityView, ActivityDetail

urlpatterns = [
    path('members/', Members.as_view(), name='member_list'),
    path('members/<int:id>', MemberDetail.as_view(), name='member_detail'),
    path('sliders/', SliderView.as_view(), name='sliders'),
    path('sliders/<int:id>', SliderDetail.as_view(), name='slider_detail'),
    path('events/', EventView.as_view(), name='events'),
    path('events/<int:id>', EventDetail.as_view(), name='event_detail'),
    path('medias/', MediaView.as_view(), name='medias'),
    path('medias/<int:id>', MediaDetail.as_view(), name='media_detail'),
    path('activites/', ActivityView.as_view(), name='medias'),
    path('activites/<int:id>', ActivityDetail.as_view(), name='media_detail'),
    path('stats/', StatsAPI.as_view(), name='stats_api'),
    path('photo-gallary/', PhotoGallaryAPI.as_view(), name='photo_gallary_api'),
]
