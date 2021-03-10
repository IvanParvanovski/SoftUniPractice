from abc import ABC, abstractmethod


class Connect(ABC):
    @abstractmethod
    def connect(self, device):
        pass


class PowerConnector(Connect):
    def connect(self, device):
        self.connect_device_to_power_outlet(device)

    def connect_device_to_power_outlet(self, device): pass


class HDMIConnector(Connect):
    def connect(self, device):
        self.connect_to_device_via_hdmi_cable(device)

    def connect_to_device_via_hdmi_cable(self, device): pass


class RCAConnector(Connect):
    def connect(self, device):
        self.connect_to_device_via_rca_cable(device)

    def connect_to_device_via_rca_cable(self, device): pass


class VIAConnector(Connect):
    def connect(self, device):
        self.connect_to_device_via_ethernet_cable(device)

    def connect_to_device_via_ethernet_cable(self, device): pass


class Television(PowerConnector,
                 HDMIConnector,
                 RCAConnector):

    def connect(self, device):
        PowerConnector.connect(self, device)
        HDMIConnector.connect(self, device)
        RCAConnector.connect(self, device)


class dvd_player(PowerConnector,
                 HDMIConnector):

    def connect(self, device):
        PowerConnector.connect(self, device)
        HDMIConnector.connect(self, device)


class GameConsole(PowerConnector,
                  HDMIConnector,
                  VIAConnector):

    def connect(self, device):
        PowerConnector.connect(self, device)
        HDMIConnector.connect(self, device)
        VIAConnector.connect(self, device)


class Router(PowerConnector,
             VIAConnector):

    def connect(self, device):
        PowerConnector.connect(self, device)
        VIAConnector.connect(self, device)
