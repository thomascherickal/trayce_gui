import typing
from PyQt6 import QtCore
from network.flow import Flow


class FlowsTableModel(QtCore.QAbstractTableModel):
    flows: list[Flow]

    def __init__(self, parent: typing.Optional[QtCore.QObject] = None):
        super().__init__(parent)
        self.columns = ["#", "Protocol", "Source", "Destination", "Operation", "Response"]
        self.flows = []

    def set_flows(self, flows: list[Flow]):
        self.flows = flows
        self.layoutChanged.emit()

    def add_flows(self, flows: list[Flow]):
        for flow in flows:
            self.__add_flow(flow)
        self.layoutChanged.emit()

    def __add_flow(self, flow: Flow):
        if flow.is_request():
            self.flows.append(flow)
            return

        matching_request_flows = [f for f in self.flows if f.uuid == flow.uuid]
        if len(matching_request_flows) > 0:
            matching_request_flows[0].add_response(flow)

    def rowCount(self, parent: QtCore.QModelIndex = QtCore.QModelIndex()):
        return len(self.flows)

    def columnCount(self, parent: QtCore.QModelIndex = QtCore.QModelIndex()):
        return len(self.columns)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = 0) -> typing.Any:
        if role == QtCore.Qt.ItemDataRole.DisplayRole and orientation == QtCore.Qt.Orientation.Horizontal:
            return self.columns[section]

        return QtCore.QVariant()

    def data(self, index: QtCore.QModelIndex, role: int = 0) -> typing.Any:
        if not index.isValid():
            return None

        if index.row() > len(self.flows):
            return None

        flow = self.flows[index.row()]

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return str(flow.uuid)
            elif index.column() == 1:
                return flow.l7_protocol
            elif index.column() == 2:
                return flow.remote_addr
            elif index.column() == 3:
                return flow.local_addr
            elif index.column() == 4:
                return "TODO"
            elif index.column() == 5:
                return "TODO"

        return QtCore.QVariant()
