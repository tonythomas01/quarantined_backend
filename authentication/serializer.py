from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from drf_extra_fields import geo_fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from authentication.models import User
from management.models import Participant


class EmailAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"), style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"), email=email, password=password
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ParticipantSerializer(ModelSerializer):
    user = UserSerializer()
    position = geo_fields.PointField(str_points=True)

    class Meta:
        model = Participant
        fields = (
            "id",
            "user",
            "position",
            "type",
            "first_line_of_address",
            "second_line_of_address",
            "country",
            "place_id",
            "post_code",
            "city",
            "phone",
        )
