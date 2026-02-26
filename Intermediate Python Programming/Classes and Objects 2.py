# -------------------------------
# ROOM CLASS
# -------------------------------

class Room:
    def __init__(self, id, room_type, price):
        # Unique room number (string)
        self.id = id

        # Room type (single, double, etc.)
        self.room_type = room_type

        # Price per night
        self.price = price

        # Booking status (default = not booked)
        self.isBooked = False


# -------------------------------
# HOTEL CLASS
# -------------------------------

class Hotel:
    def __init__(self, name, location):
        # Hotel name
        self.name = name

        # Hotel location
        self.location = location

        # List that stores Room objects
        self.rooms = []

    # ---------------------------
    # Add a room to the hotel
    # ---------------------------
    def addRoom(self, room):
        # 'room' must be a Room object
        self.rooms.append(room)

    # ---------------------------
    # Find a room by ID
    # ---------------------------
    def findRoom(self, roomID):
        for room in self.rooms:
            if room.id == roomID:
                return room
        return None  # If room not found

    # ---------------------------
    # Book a room
    # ---------------------------
    def bookRoom(self, roomID):
        room = self.findRoom(roomID)

        if room is None:
            print(f"Room {roomID} does not exist.")

        elif room.isBooked:
            print(f"Room {roomID} is already booked.")

        else:
            room.isBooked = True
            print(f"Room {roomID} has been successfully booked.")

    # ---------------------------
    # Release (cancel) a booking
    # ---------------------------
    def releaseRoom(self, roomID):
        room = self.findRoom(roomID)

        if room is None:
            print(f"Room {roomID} does not exist.")

        elif not room.isBooked:
            print(f"Room {roomID} is not currently booked.")

        else:
            room.isBooked = False
            print(f"Room {roomID} has been successfully released.")

    # ---------------------------
    # Show available rooms
    # ---------------------------
    def showAvailableRooms(self):
        available = [room.id for room in self.rooms if not room.isBooked]

        if not available:
            print("No available rooms.")
        else:
            print("Available rooms:", available)

    # ---------------------------
    # Calculate total revenue
    # ---------------------------
    def calculateRevenue(self):
        total = sum(room.price for room in self.rooms if room.isBooked)
        print("Total Revenue:", total)


# ==========================================
# TEST SECTION
# ==========================================

# Create hotel
hotel1 = Hotel("Phoenix Hotel", "San Francisco")

# Create rooms
room1 = Room("101", "single", 60)
room2 = Room("102", "double", 80)
room3 = Room("103", "single", 65)

# Add rooms to hotel
hotel1.addRoom(room1)
hotel1.addRoom(room2)
hotel1.addRoom(room3)

# Book rooms
hotel1.bookRoom("101")
hotel1.bookRoom("102")

# Test double booking
hotel1.bookRoom("101")

# Show available rooms
hotel1.showAvailableRooms()

# Calculate revenue
hotel1.calculateRevenue()

# Release a room
hotel1.releaseRoom("101")

# Show available rooms again
hotel1.showAvailableRooms()