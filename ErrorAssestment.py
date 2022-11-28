from FileReader import FileReader
from Point import Point
from Point import OriginalPoint

path = "E:\\New folder\\BK\\HK221\\Luan_van_tot_nghiep\\Temporary\\data\\test.txt"

og_points = []
positions = []

data = FileReader.readFromText(path)
#print(data)
ps_indices = []
for i in range(0, len(data)):
    if data[i] == "Waypoints":
        start_waypoint_set = i
    elif data[i] == "Positions":
        end_waypoint_set = start_position_set = i
    elif data[i] == "REACHED WAYPOINT":
        ps_indices.append(i - end_waypoint_set)

print(start_waypoint_set)
print(start_position_set)
print(ps_indices)

# Original points appended
for i in range(start_waypoint_set + 1, end_waypoint_set):
    splitted = data[i].split(',')
    og_points.append(Point(splitted[0], splitted[1]))
    
for i in range(0, len(og_points)):
    print(og_points[i].x, og_points[i].y)

# Cart positions appending
for i in range(0, len(ps_indices)-1):
    if(i == 0):
        for j in range(start_position_set + 1, start_position_set +1 + ps_indices[i] - 1):
            #print(data[j])
            positions.append(OriginalPoint(data[j]))

    else:
        for j in range(ps_indices[i-1] + 1, start_position_set + 1 + ps_indices[i] - 1):
            #print(data[j])
            positions.append(OriginalPoint(data[j]))



for i in range(0, len(positions)):
    print(str(positions[i].getLat()) + " " + str(positions[i].getLon()))

print(len(positions))


