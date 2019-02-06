import grpc
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from blockchain.codegen.manage_pb2 import BlockRequest, ChainRequest
from blockchain.codegen.manage_pb2_grpc import IFCManageStub
from posts.serializers import PostImportSerializer
from users.serializers import UserImportSerializer
from posts.models import Post
from users.models import User


class Command(BaseCommand):
    @staticmethod
    def handle_note(block):
        info = json.JSONDecoder().decode(block.payload.decode('utf8'))
        info['block_height'] = block.height
        info['block_time'] = block.time
        serializer = PostImportSerializer(data=info)
        if serializer.is_valid():
            Post.objects.update_or_create(defaults=serializer.validated_data, payload_id=info['id'])
        else:
            print(serializer.errors)

    @staticmethod
    def handle_user(block):
        info = json.JSONDecoder().decode(block.payload.decode('utf8'))
        info['block_height'] = block.height
        info['block_time'] = block.time
        serializer = UserImportSerializer(data=info)
        if serializer.is_valid():
            User.objects.update_or_create(defaults=serializer.validated_data, user_id=info['user_id'])
        else:
            print(serializer.errors)

    def handle(self, *args, **options):
        with grpc.insecure_channel('localhost:32700') as channel:
            stub = IFCManageStub(channel)
            for chain in stub.GetChains(ChainRequest(id=settings.USER_CHAIN_ID)):
                req = BlockRequest(**{'chainID': settings.USER_CHAIN_ID, 'from': 1, 'to': chain.count-1})
                for block in stub.GetBlocks(req):
                    self.handle_user(block)

            for chain in stub.GetChains(ChainRequest(id=settings.POST_CHAIN_ID)):
                req = BlockRequest(**{'chainID': settings.POST_CHAIN_ID, 'from': 1, 'to': chain.count-1})
                for block in stub.GetBlocks(req):
                    self.handle_note(block)
