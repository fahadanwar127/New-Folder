class Model_Agent:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.current_temp = None
        self.last_action = None

    def percept(self, current_temp):
        self.current_temp = temp

    def act(self):
        if self.current_temp > self.desired_temp:
            self.last_action = "Turn off the heater"
        elif self.current_temp < self.desired_temp:
            self.last_action = "Turn on the heater"
        else:
            self.last_action = "Heater is off"

        return self.last_action

agent = Model_Agent(29)

rooms = {
    "Living Room": 20,
    "Bedroom": 19,
    "Kitchen": 30
}

for room, temp in rooms.items():
    agent.percept(temp)
    print(f"{room}: {temp} ==> {agent.act()}")
