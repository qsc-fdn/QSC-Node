# coding=utf-8
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.
from qsc.core import config
from qsc.core.qrlnode import QRLNode
from qsc.generated import qscdebug_pb2
from qsc.generated.qscdebug_pb2_grpc import DebugAPIServicer
from qsc.services.grpcHelper import GrpcExceptionWrapper


class DebugAPIService(DebugAPIServicer):
    MAX_REQUEST_QUANTITY = 100

    def __init__(self, qrlnode: QRLNode):
        self.qrlnode = qrlnode

    @GrpcExceptionWrapper(qscdebug_pb2.GetFullStateResp)
    def GetFullState(self, request: qscdebug_pb2.GetFullStateReq, context) -> qscdebug_pb2.GetFullStateResp:
        return qscdebug_pb2.GetFullStateResp(
            coinbase_state=self.qrlnode.get_address_state(config.dev.coinbase_address).pbdata,
            addresses_state=self.qrlnode.get_all_address_state()
        )
