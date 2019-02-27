import json
import base58
import hashlib

from rest_framework import serializers

from utils.serializers import TruncatedField
from users.serializers import UserField
from utils.signature import recover_user_id

from .models import *


class LastReplyField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        if value:
            return PostBriefSerializer(Post.objects.get(payload_id=value)).data
        else:
            return None


class PostSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='payload_id', read_only=True)
    title = serializers.CharField(required=False, allow_null=True, allow_blank=False)
    reply_to = serializers.CharField(required=False, allow_null=True, allow_blank=False)
    last_reply = LastReplyField(read_only=True)
    user = UserField(read_only=True, source='user_id')

    class Meta:
        model = Post
        exclude = ('payload_id',)
        read_only_fields = (
            'id', 'replies', 'last_reply', 'block_height', 'block_time', 'payload_id'
        )
        extra_kwargs = {'user_id': {'write_only': True}}

    def validate(self, attrs):
        # reply_to = attrs.get('reply_to')
        # title = attrs.get('title')
        # if (not reply_to or len(reply_to) == 0) and (not title or len(title) == 0):
        #     raise serializers.ValidationError({'title': ['This field may not be blank when reply_to is blank.']})

        data = dict(self.initial_data)
        signature = data.pop('signature')
        user_id = data.pop('user_id')
        payload_id = data.pop('id', None)
        data.pop('block_height', None)
        data.pop('block_time', None)

        json_data = json.JSONEncoder(separators=(',', ':'), sort_keys=True, ensure_ascii=False).encode(data)
        if user_id != recover_user_id(json_data, signature):
            raise serializers.ValidationError({'signature': ['invalid signature']})

        if not payload_id:
            attrs['payload_id'] = base58.b58encode(hashlib.sha256(json_data.encode('utf8')).digest()).decode('ascii')
        else:
            attrs['payload_id'] = payload_id

        return attrs


class PostBriefSerializer(PostSerializer):
    content = TruncatedField()

    class Meta(PostSerializer.Meta):
        exclude = None
        fields = ('id', 'title', 'date_submitted', 'last_reply', 'user', 'replies', 'content')


class PostImportSerializer(PostSerializer):
    id = serializers.CharField(source='payload_id')

    class Meta(PostSerializer.Meta):
        read_only_fields = ()


class PostBlockchainSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        exclude = None
        fields = ('id', 'title', 'date_submitted', 'user_id', 'content', 'reply_to', 'signature')
        extra_kwargs = {}


class ReplySerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        exclude = None
        fields = ('id', 'date_submitted', 'block_time',
                  'user', 'content', 'signature', 'block_height')
