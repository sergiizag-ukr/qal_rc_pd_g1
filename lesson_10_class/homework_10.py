class QuestRoom:

    def __init__(self, questRoom: str, level: int, limit: int ):
        self.questRoom = questRoom
        self.level = level
        self.limit = limit
        self.players = []
        self.status = "waiting"
        self.events_log = []

    def add_player(self, name):
        if len(self.players) >= self.limit:
            return "No free slots!"
            
        else:
            self.players.append(name)
            self.events_log.append(f"Player {name} joined")

    def start(self):
        if len(self.players) == 0:
            return "Room is empty!"
        else:
            self.status = "active"
            self.events_log.append("Quest started")
            return f"Quest: '{self.questRoom}' started with {len(self.players)} players!"

    def remove_player(self, name_r):

        if name_r in self.players:
            self.players.remove(name_r)
            self.events_log.append(f"Player {name_r} left")
        else:
            return "Player not found!"

    def is_full(self):
        if len(self.players) == self.limit:
            return True
        else:
            return False

    def free_slots(self):
        return self.limit - len(self.players)

    def reset_room(self):
        self.status = "finished"
        self.players.clear()
        self.status = "waiting"
        self.events_log.append("Room reset")

    def show_log(self):
        return self.events_log



    def __str__(self):
        return f"QuestRoom: {self.questRoom} | Difficulty: {self.level} | Players: {len(self.players)}/{self.limit} | Status: {self.status}"

room = QuestRoom("qwerty", 3, 4)
print(room)
room.add_player("Serg")
print(room)
room.start()
print(room)
log = room.show_log()
print(log)

