from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Member
from .serializers import MemberSerializer, MemberDetailSerializer

# class Posts(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request,'home.html', {"posts":posts})

class Members(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    
class MemberDetail(ListAPIView):
    serializer_class = MemberSerializer
    
    def get_queryset(self):
        member_id = self.kwargs['id']
        queryset= Member.objects.filter(id=member_id)
        return queryset