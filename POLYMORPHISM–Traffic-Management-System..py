# Parent class
class TrafficDevice:
    def activate(self):
        print("Traffic device is activated.")


# Child class 1
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic light changes to green.")


# Child class 2
class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed camera starts monitoring vehicle speed.")


# Child class 3
class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian signal displays WALK.")


# Child class 4
class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency siren sounds to alert road users.")


# Create objects and store them in a list
devices = [
    TrafficLight(),
    SpeedCamera(),
    PedestrianSignal(),
    EmergencySiren()
]


# Activate all devices using polymorphism
for device in devices:
    device.activate()