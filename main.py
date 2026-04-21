class HotelRoom:
    def __init__(self, room_number, is_available):
        self.room_number = room_number
        self.is_available = is_available

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room_number, is_available):
        self.rooms.append(HotelRoom(room_number, is_available))

    def check_availability(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.is_available
        return False

    def update_availability(self, room_number, is_available):
        for room in self.rooms:
            if room.room_number == room_number:
                room.is_available = is_available
                return
        self.add_room(room_number, is_available)

hotel = Hotel()
hotel.add_room(101, True)
hotel.add_room(102, False)
hotel.add_room(103, True)

print(hotel.check_availability(101))  # True
print(hotel.check_availability(102))  # False
print(hotel.check_availability(104))  # False

hotel.update_availability(102, True)
print(hotel.check_availability(102))  # True
