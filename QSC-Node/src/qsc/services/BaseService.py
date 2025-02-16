# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

# FIXME: This is odd...
import sys

import os
from grpc._cython.cygrpc import StatusCode

from qsc.core.qrlnode import QRLNode
from qsc.generated.qscbase_pb2 import GetNodeInfoReq, GetNodeInfoResp
from qsc.generated.qscbase_pb2_grpc import BaseServicer


class BaseService(BaseServicer):
    def __init__(self, qrlnode: QRLNode):
        self.qrlnode = qrlnode

    def GetNodeInfo(self, request: GetNodeInfoReq, context) -> GetNodeInfoResp:
        try:
            resp = GetNodeInfoResp()
            resp.version = self.qrlnode.version

            pkgdir = os.path.dirname(sys.modules['qsc'].__file__)
            grpcprotopath = os.path.join(pkgdir, "protos", "qsc.proto")
            with open(grpcprotopath, 'r') as infile:
                resp.grpcProto = infile.read()

            return resp
        except Exception as e:
            print(f'-> GetNodeInfo error: {e}')
            context.set_code(StatusCode.unknown)
            context.set_details(e)
            return GetNodeInfoResp()
