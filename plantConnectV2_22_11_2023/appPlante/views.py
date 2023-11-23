from rest_framework.viewsets import ModelViewSet
from .models import Plante, Salle, Node, Measure
from .serializers import PlanteSerializer, SalleSerializer, NodeSerializer, MeasureSerializer
from django.shortcuts import render

def BASE(request):
    return render(request, 'base.html')

class PlanteViewset(ModelViewSet):
    serializer_class = PlanteSerializer

    def get_queryset(self):
        return Plante.objects.all()

class SalleViewset(ModelViewSet):
    serializer_class = SalleSerializer

    def get_queryset(self):
        return Salle.objects.all()

class NodeViewset(ModelViewSet):
    serializer_class = NodeSerializer

    def get_queryset(self):
        return Node.objects.all()

class MeasureViewset(ModelViewSet):
    serializer_class = MeasureSerializer

    def get_queryset(self):
        return Measure.objects.all()
