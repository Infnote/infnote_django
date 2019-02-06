import json
import re

from rest_framework import serializers
from .models import User

from utils.signature import recover_user_id


class UserSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(max_length=100)
    signature = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('user_id', 'topics', 'replies', 'block_time', 'block_height')

    def validate(self, attrs):
        # email = attrs.get('email')
        # if not re.match('pku.edu.cn$', email):
        #     raise serializers.ValidationError(
        #         'Users only who have a PKU mail address are allow to register at this moment.'
        #     )

        data = dict(attrs)
        user_id = data.pop('user_id')
        signature = data.pop('signature')
        data.pop('block_height', None)
        data.pop('block_time', None)
        json_data = json.JSONEncoder(separators=(',', ':'), sort_keys=True, ensure_ascii=False).encode(data)

        if user_id != recover_user_id(json_data, signature):
            raise serializers.ValidationError({'user_id': ['user_id is not match signature']})

        return attrs


class UserBriefSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('user_id', 'nickname', 'avatar', 'bio')


class UserImportSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = ('topics', 'replies')


class UserBlockchainSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('user_id', 'nickname', 'avatar', 'bio', 'date_created', 'signature')


class UserField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        return UserBriefSerializer(instance=User.objects.get(user_id=value)).data
