# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

from qsc.core.qrlnode import QRLNode
from qsc.generated.qsc_pb2_grpc import AdminAPIServicer


class AdminAPIService(AdminAPIServicer):
    # TODO: Separate the Service from the node model
    def __init__(self, qrlnode: QRLNode):
        self.qrlnode = qrlnode
