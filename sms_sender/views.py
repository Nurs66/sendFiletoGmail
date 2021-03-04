from rest_framework import viewsets, mixins

from sms_sender.models import Person
from sms_sender.serializers import PersonSerializer


class PersonViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
