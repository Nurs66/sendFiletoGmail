from rest_framework import serializers

from sms_sender.models import Person
from sms_sender.tasks import send_info


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"

    def create(self, validated_data):
        person = super().create(validated_data)
        person.save()
        send_info(
            person.fio,
            person.service,
            person.email,
            person.phone_number,
            person.content,
            person.file
        )
        return person
