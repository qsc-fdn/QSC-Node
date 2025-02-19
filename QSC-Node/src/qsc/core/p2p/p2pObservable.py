from qsc.core.notification.Observable import Observable
from qsc.generated import qsclegacy_pb2


class P2PObservable(Observable):
    def __init__(self, source):
        # FIXME: Add mutexes
        super().__init__(source)

    def notify(self, message: qsclegacy_pb2.LegacyMessage):
        # TODO: Add some p2p specific validation?
        super().notify(message)
