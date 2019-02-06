import grpc
import json

from django.conf import settings
from users.serializers import UserBlockchainSerializer
from posts.serializers import PostBlockchainSerializer
from utils.singleton import Singleton

from .codegen.manage_pb2 import BlockCreationRequest
from .codegen.manage_pb2_grpc import IFCManageStub


class Client(metaclass=Singleton):
    def __init__(self):
        self.post_chain = settings.POST_CHAIN_ID
        self.user_chain = settings.USER_CHAIN_ID

    def create_post(self, post):
        post['id'] = post.pop('payload_id')
        return self.create(self.post_chain, post, PostBlockchainSerializer)

    def create_user(self, user):
        return self.create(self.user_chain, user, UserBlockchainSerializer)

    @staticmethod
    def create(chain_id, data, serializer) -> bool:
        with grpc.insecure_channel('localhost:32700') as channel:
            stub = IFCManageStub(channel)
            content = json.JSONEncoder(ensure_ascii=False, separators=(',', ':')).encode(data).encode('utf8')
            response = stub.CreateBlock(BlockCreationRequest(chainID=chain_id, payload=content))
            if data.get('id') is not None:
                data['payload_id'] = data.pop('id', None)
            data['block_time'] = response.time
            data['block_height'] = response.height
            s = serializer(data=data)
            if s.is_valid():
                s.save()
            return True
