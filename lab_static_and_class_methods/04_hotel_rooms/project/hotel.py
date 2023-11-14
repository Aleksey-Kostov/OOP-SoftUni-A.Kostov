from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)
        # for room in self.rooms:
        #     if room.number == room_number:
        #         return room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self):
        free_rooms = [str(free_r.number) for free_r in self.rooms if not free_r.is_taken]
        taken_rooms = [str(take_r.number) for take_r in self.rooms if take_r.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(free_rooms)}\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}"

        return result