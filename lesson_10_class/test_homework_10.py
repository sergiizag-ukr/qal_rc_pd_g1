import pytest
from homework_10 import QuestRoom

def test_constructor():
    room = QuestRoom("Code", 5, 7)
    assert room.questRoom == "Code"
    assert room.level == 5
    assert room.limit == 7
    assert room.players == []
    assert room.status == "waiting"
    assert room.events_log == []

def test_add_player():
    room = QuestRoom("Play", 4, 4)
    room.add_player("Serg")
    assert "Serg" in room.players
    room.add_player("Julia")
    room.add_player("Sofia")
    room.add_player("Julii")
    assert room.players == ["Serg", "Julia", "Sofia", "Julii"]
    assert room.add_player("Sima") == "No free slots!"
    assert  "Player Julii joined" in room.events_log

def test_remove_player():
    room = QuestRoom("Star", 4, 4)
    room.add_player("Mark")
    room.add_player("Maria")
    room.remove_player("Maria")
    assert "Maria" not in room.players
    assert room.remove_player("Makar") == "Player not found!"
    room.remove_player("Mark")
    assert room.remove_player("Misha") == "Player not found!"
    assert "Player Mark left" in room.events_log

def test_is_full_or_free():
    room = QuestRoom("Mega", 4, 4)
    room.add_player("Mark")
    assert room.free_slots() == 3
    room.add_player("Maria")
    assert room.free_slots() == 2
    assert room.free_slots() > 0
    room.add_player("Masha")
    assert room.free_slots() == 1
    room.add_player("Mira")
    assert room.free_slots() == 0
    assert room.is_full() == True

def test_start():
    room = QuestRoom("Alfa", 2, 2)
    assert "Room is empty!" in room.start()
    room.add_player("Andrii")
    room.start()
    assert room.status == "active"
    assert f"Quest: '{room.questRoom}' started with {len(room.players)} players!" in room.start()
    assert "Quest started" in room.events_log 

def test_reset_room():
    room = QuestRoom("Beta", 4, 4)
    room.add_player("Mark")
    room.add_player("Maria")
    room.reset_room()
    assert room.players == []
    assert room.status == "waiting"
    assert "Room reset" in room.events_log

def test_imitation1():
    room = QuestRoom("Zeta", 4, 4)
    assert room.status == "waiting"
    assert room.events_log == []
    room.add_player("Mark")
    assert "Player Mark joined" in room.events_log
    room.add_player("Maria")
    assert room.status == "waiting"
    assert "Player Maria joined" in room.events_log
    room.start()
    assert room.status == "active"
    assert "Quest started" in room.events_log
    room.reset_room()
    assert room.status == "waiting"
    assert "Room reset" in room.events_log
    assert room.players == []


def test_imitation2():
    room = QuestRoom("Star", 4, 4)
    room.add_player("Mark")
    room.add_player("Maria")
    room.add_player("Masha")
    room.add_player("Misha")
    assert room.is_full()
    room.add_player("Mira")
    room.remove_player("Misha")
    room.add_player("Mavka")
    assert room.players == ["Mark", "Maria", "Masha", "Mavka"]


def test_numbers():
    room = QuestRoom("Team", 4, 2000)
    for i in range(1, 1001):
        room.add_player(str(i))
    assert len(room.players) == 1000
    room.reset_room()
    room.reset_room()
    assert room.status == "waiting"
    room.add_player("")
    room.add_player("   ")
    assert room.players == ["", "   "]
