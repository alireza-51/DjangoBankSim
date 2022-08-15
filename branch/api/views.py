import imp
from rest_framework.viewsets import ModelViewSet
# from rest_framework import views, mixins
from branch.models import Branch
from .serializers import BranchSerializer


class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer