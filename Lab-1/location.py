# CPE 202 Location Class, Lab 1

# Represents a location using name, latitude and longitude
class Location:
    # Purpose: Initialize location object
    def __init__(self, name, lat, lon):
        self.name = name   
        self.lat = lat     
        self.lon = lon      

    # Purpose: Define string representation of Location objects
    def __repr__(self):
        return "Location('" + self.name + "', " + str(self.lat) + ", " + str(self.lon) + ")"

    # Purpose: Define equality between Location objects
    def __eq__(self, other):
        if type(self) == type(other) and \
            self.name == other.name and \
            self.lat == other.lat and \
            self.lon == other.lon:
                return True
        return False

def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:",loc1)
    print("Location 2:",loc2)
    print("Location 3:",loc3)
    print("Location 4:",loc4)

    print("\nLocation 1 equals Location 2:",loc1==loc2)
    print("Location 1 equals Location 3:",loc1==loc3)
    print("Location 1 equals Location 4:",loc1==loc4)

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)

if __name__ == "__main__":
    main()