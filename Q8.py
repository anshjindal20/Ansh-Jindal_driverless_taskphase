import csv
def calculate_distance_to_origin(cone):
    x=cone[1]
    y=cone[2]
    return x*2 + y*2

def write_cones_to_csv(filename, data_list):
    with open(filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "x", "y", "colour"])
        csv_writer.writerows(data_list)

cones_list = []
with open("cones.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        cone_id = int(row[0])
        x = float(row[1])
        y = float(row[2])
        colour = row[3]
        cones_list.append((cone_id, x, y, colour))    
cones_list.sort(key=calculate_distance_to_origin)
blue_cones = []
yellow_cones = []
for cone in cones_list:
    if cone[3] == 'blue':
        blue_cones.append(cone)
    else:
        yellow_cones.append(cone)
write_cones_to_csv("blue_cones.csv", blue_cones)
write_cones_to_csv("yellow_cones.csv", yellow_cones)
midpoints_list = []
for b_cone in blue_cones:
    b_id, b_x, b_y, _ = b_cone
    
    min_dist_sq = float('inf')
    closest_y_cone = None
    for y_cone in yellow_cones:
        y_id, y_x, y_y, _ = y_cone
        dist_sq = (b_x - y_x)*2 + (b_y - y_y)*2
        
        if dist_sq < min_dist_sq:
            min_dist_sq = dist_sq
            closest_y_cone = y_cone
    _, best_y_x, best_y_y, _ = closest_y_cone
    
    mid_x = (b_x + best_y_x) / 2
    mid_y = (b_y + best_y_y) / 2
    midpoints_list.append((b_id, closest_y_cone[0], mid_x, mid_y))

with open("centreline.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["blue_id", "yellow_id", "mid_x", "mid_y"])
    writer.writerows(midpoints_list)
print("Program complete! All three CSV files have been successfully generated.")