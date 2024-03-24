from django.urls import path
from .views import Members, MemberDetail

urlpatterns = [
    path('members', Members.as_view(), name='member_list'),
    path('members/<int:id>', MemberDetail.as_view(), name='member_detail')
]
