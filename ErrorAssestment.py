from FileReader import FileReader
from Point import Point
from Point import OriginalPoint
from UTMmodule import UTMmodule
from ErrorCalculation import ErrorCalculation
from PathGenerator import PathGenerator
from Visualize import Visualize
from Line import Line

path = "E:\\New folder\\BK\\HK221\\Luan_van_tot_nghiep\\Software\\ErrorAssessment\\data\\10-12_3.txt"
path_write = "E:\\New folder\\BK\\HK221\\Luan_van_tot_nghiep\\Software\\ErrorAssessment\\result\\10-12_3.txt"

utm = UTMmodule()

og_points = []
og_points_converted = []
positions = []
positions_converted = []
line = []
error = []


data = FileReader.readFromText(path)
result_write = open(path_write, "a")
#print(data)
ps_indices = []
for i in range(0, len(data)):
    if data[i] == "Waypoints":
        start_waypoint_set = i
    elif data[i] == "Positions":
        end_waypoint_set = start_position_set = i
    elif data[i] == "REACHED WAYPOINT":
        ps_indices.append(i - end_waypoint_set)
        print("Found a waypoint")

print(start_waypoint_set)
print(start_position_set)
print(ps_indices)

# Original points appended
for i in range(start_waypoint_set + 1, end_waypoint_set):
    splitted = data[i].split(',')
    og_points.append(OriginalPoint(data[i]))
    
for i in range(0, len(og_points)):
    print(og_points[i].getLat(), og_points[i].getLon())

# Cart positions appending

if(len(ps_indices) == 1):
    for j in range(start_position_set + 1, start_position_set + 1 + ps_indices[0] - 1):
            #print(j)
            positions.append(OriginalPoint(data[j]))
else:
    for i in range(0, len(ps_indices)):
        if(i == 0):
            for j in range(start_position_set + 1, start_position_set + 1 + ps_indices[i] - 1):
                #print(data[j])
                positions.append(OriginalPoint(data[j]))

        else:
            for j in range(start_position_set + ps_indices[i-1] + 1, start_position_set + 1 + ps_indices[i] - 1):
                #print(data[j])
                positions.append(OriginalPoint(data[j]))
                #print(j)

# data process

### The waypoints - done
for i in range(0, len(og_points)):
    x, y = utm.fromLatlon(og_points[i].getLat(), og_points[i].getLon())
    og_points_converted.append(Point(x, y))

# offset the waypoints
offset = Point(og_points_converted[0].x, og_points_converted[0].y)
for i in range(0, len(og_points_converted)):
    og_points_converted[i].x -= offset.x
    og_points_converted[i].y -= offset.y

# for i in range(0, len(og_points_converted)):
#     print(str(og_points_converted[i].x) + " " + str(og_points_converted[i].y))

### The positions points - Done
for i in range(0, len(positions)):
    x, y = utm.fromLatlon(positions[i].getLat(), positions[i].getLon())
    x -= offset.x
    y -= offset.y
    positions_converted.append(Point(x, y))

# for i in range(0, len(positions_converted)):
#     print(str(positions_converted[i].x) + " " + str(positions_converted[i].y))

### Assess the error

#Make the lines:
if(len(og_points_converted) == 2):
    line.append(Line(og_points_converted[0], og_points_converted[1]))
    for j in range(0, len(positions_converted)):
            error.append(line[0].distanceToPoint(positions_converted[j]))

else:
    for i in range(0, len(og_points_converted)-1):
        line.append(Line(og_points_converted[i], og_points_converted[i+1]))

    print("There are " + str(len(line)) + " lines")
    print("There are " + str(len(og_points)) + " waypoints")
    print("There are " + str(len(positions_converted)) + " positions")

    for i in range(0, len(line)):
        print("Line #" + str(i + 1))
        if(i == 0):
            for j in range(0, ps_indices[i] - 1):
                error_tmp = line[i].distanceToPoint(positions_converted[j])
                #print(error_tmp)
                error.append(error_tmp)
                #error.append(line[i].distanceToPoint(positions_converted[j]))
        else:
            for j in range(ps_indices[i-1], ps_indices[i] - i - 1):
                error_tmp = line[i].distanceToPoint(positions_converted[j])
                #print(error_tmp)
                error.append(error_tmp)
                #error.append(line[i].distanceToPoint(positions_converted[j]))
        # else:
        #     for j in range(ps_indices[i], ps_indices[i+1]):
        #         error_tmp = line[i].distanceToPoint(positions_converted[j])
        #         #print(error_tmp)
        #         error.append(error_tmp)
        #         #error.append(line[i].distanceToPoint(positions_converted[j]))

# write to file
for i in range(0, len(error)):
    print(error[i])
    result_write.write(str(error[i]) + '\r')

average = ErrorCalculation.average(error)
print("The average error is: " + str(average))
result_write.write("The average error is: " + str(average) + "\r")

Visualize.scattered(positions_converted)
Visualize.line(og_points_converted)
Visualize.plot()
