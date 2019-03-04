from datetime import datetime

from rest_framework import serializers


class TimestampField(serializers.DateTimeField):
    def to_representation(self, value):
        timestring = super(TimestampField, self).to_representation(value)
        return int(timestring)

    def to_internal_value(self, value):
        time = datetime.utcfromtimestamp(value)
        return super(TimestampField, self).to_internal_value(str(time))


class TruncatedField(serializers.CharField):
    def to_representation(self, value):
        if len(value) > 500:
            return value[:500]
        return value


class TruncatedHintField(serializers.CharField):
    def to_representation(self, value):
        if len(value) > 500:
            return True
        return False
