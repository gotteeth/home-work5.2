class Event:
    def __init__(self, name, date, participants=0 ):
        self.name = name
        self.date = date
        self.participants = participants

    def add(self):
        self.participants += 1

    def count(self):
        return self.participants
    
event = Event("""~~~~~~~~~~~~~~
              city marathon
              09-26-205~~~~~~~~~~~~~""")
print(f"participants count before adding:", {event.count()})
event.add()
print(f"participants count after adding:" , {event.count()})
