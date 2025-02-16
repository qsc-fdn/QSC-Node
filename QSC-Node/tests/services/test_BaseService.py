# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
import os
from unittest import TestCase

from mock import patch

from qsc.core import config
from qsc.core.misc import logger
from qsc.core.qrlnode import QRLNode
from qsc.generated.qrlbase_pb2 import GetNodeInfoReq
from qsc.services.BaseService import BaseService
from tests.misc.helper import replacement_getTime

logger.initialize_default()


@patch('qsc.core.misc.ntp.getTime', new=replacement_getTime)
class TestBaseAPI(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBaseAPI, self).__init__(*args, **kwargs)

    def test_getNodeInfo(self):
        qrlnode = QRLNode(mining_address=b'')

        service = BaseService(qrlnode)
        response = service.GetNodeInfo(request=GetNodeInfoReq, context=None)

        self.assertEqual(config.dev.version, response.version)

        proto_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  os.path.pardir,
                                                  os.path.pardir,
                                                  "src", "qrl", "protos", "qsc.proto"))

        with open(proto_path, 'r') as content_file:
            proto_content = content_file.read()

        self.assertEqual(proto_content, response.grpcProto)
