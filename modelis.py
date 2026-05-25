import add
import math

#add.axes([0, 0, 0])

# Function to build a car at the standard position [12, 0.25, 0]
def build_car():
    # Main body (chassis)
    add.rectangle3D([12, 0.25, 0], [1.5, 0.75, 1.35], [107, 112, 121])

    # Frontglass and side windows
    add.newface([[11.25, 0.625, -0.675], [11.25, 0.625, 0.675], [11.75, 0.975, 0.675], [11.75, 0.975, -0.675]], [203, 218, 245])
    add.newface([[11.625, 0.625, 0.675], [11.625, 0.8875, 0.675], [11.25, 0.625, 0.675]], [203, 218, 245])
    add.newface([[11.25, 0.625, -0.675], [11.625, 0.8875, -0.675], [11.625, 0.625, -0.675]], [203, 218, 245])

    # Panel between side and rear windows
    add.newface ([[11.625, 0.625, -0.675], [11.625, 0.8875, -0.675], [11.9, 0.925, -0.675], [11.9, 0.625, -0.675]], [203, 218, 245])
    add.newface ([[11.9, 0.625, 0.675], [11.9, 0.925, 0.675], [11.625, 0.8875, 0.675], [11.625, 0.625, 0.675]], [203, 218, 245])
    add.newface ([[11.9, 0.925, 0.675], [11.75, 0.975, 0.675], [11.625, 0.8875, 0.675]], [107, 112, 121])
    add.newface ([[11.625, 0.8875, -0.675], [11.75, 0.975, -0.675], [11.9, 0.925, -0.675]], [107, 112, 121])

    # Rear windows
    add.newface ([[11.9, 0.625, -0.675], [11.9, 0.925, -0.675], [12.2, 0.825, -0.675], [12.2, 0.625, -0.675]], [203, 218, 245])
    add.newface ([[11.9, 0.925, 0.675], [11.9, 0.625, 0.675], [12.2, 0.625, 0.675], [12.2, 0.825, 0.675]], [203, 218, 245])

    # Frunk
    add.newface ([[11.25, 0.625, 0.675], [11.25, 0.625, -0.675], [10.9, 0.525, -0.675], [10.9, 0.525, 0.675]], [107, 112, 121])
    add.rectangle3D([11.075, 0.2, 0], [0.35, 0.65, 1.35], [107, 112, 121])
    add.newface([[11.25, 0.525, 0.675], [11.25, 0.625, 0.675], [10.9, 0.525, 0.675]], [107, 112, 121])
    add.newface([[10.9, 0.525, -0.675], [11.25, 0.625, -0.675], [11.25, 0.525, -0.675]], [107, 112, 121])

    # Wheels
    wheel_radius = 0.25
    wheel_detail = 12
    add.cylinder([11.3, -0.125, -0.405], [11.3, -0.125, -0.81], wheel_radius, wheel_detail, [50, 50, 50])
    add.cylinder([12.45, -0.125, -0.405], [12.45, -0.125, -0.81], wheel_radius, wheel_detail, [50, 50, 50])
    add.cylinder([11.3, -0.125, 0.405], [11.3, -0.125, 0.81], wheel_radius, wheel_detail, [50, 50, 50])
    add.cylinder([12.45, -0.125, 0.405], [12.45, -0.125, 0.81], wheel_radius, wheel_detail, [50, 50, 50])

    # Headlight
    add.rectangle3D([10.8875, 0.425, 0], [0.025, 0.1, 1.345], [255, 255, 255])
    # Taillight
    add.rectangle3D([12.80625, 0.5875, 0], [0.1125, 0.025, 1.35], [255, 50, 50])
    add.rectangle3D([12.80625, 0.6125, 0], [0.1125, 0.025, 1.35], [0, 0, 0])
    add.rectangle3D([12.80625, 0.55, 0], [0.1125, 0.05, 1.35], [0, 0, 0])
    add.rectangle3D([12.80625, 0.2, 0], [0.1125, 0.65, 1.35], [107, 112, 121])

    # Trunk
    add.newface ([[12.8625, 0.625, 0.675], [12.8625, 0.625, -0.675], [12.2, 0.825, -0.675], [12.2, 0.825, 0.675]], [46,48,52])
    add.newface ([[11.75, 0.975, -0.675], [11.75, 0.975, 0.675], [12.2, 0.825, 0.675], [12.2, 0.825, -0.675]], [107, 112, 121])
    add.newface ([[12.2, 0.625, -0.675], [12.2, 0.825, -0.675], [12.8625, 0.625, -0.675]], [107, 112, 121])
    add.newface ([[12.8625, 0.625, 0.675], [12.2, 0.825, 0.675], [12.2, 0.625, 0.675]], [107, 112, 121])


outer_radius = 30
inner_radius = 15
segments = 32
height_top = -0.375
height_bottom = -0.575

for i in range(segments):
    angle1 = 2 * math.pi * i / segments
    angle2 = 2 * math.pi * (i + 1) / segments
    
    # Outer edge points
    outer1_x = outer_radius * math.cos(angle1)
    outer1_z = outer_radius * math.sin(angle1)
    outer2_x = outer_radius * math.cos(angle2)
    outer2_z = outer_radius * math.sin(angle2)
    
    # Inner edge points
    inner1_x = inner_radius * math.cos(angle1)
    inner1_z = inner_radius * math.sin(angle1)
    inner2_x = inner_radius * math.cos(angle2)
    inner2_z = inner_radius * math.sin(angle2)
    
    # Top surface of ring
    add.newface([[outer1_x, height_top, outer1_z], [outer2_x, height_top, outer2_z], 
                 [inner2_x, height_top, inner2_z], [inner1_x, height_top, inner1_z]], [80, 80, 80])
    
    # Bottom surface of ring
    add.newface([[outer1_x, height_bottom, outer1_z], [inner1_x, height_bottom, inner1_z], 
                 [inner2_x, height_bottom, inner2_z], [outer2_x, height_bottom, outer2_z]], [80, 80, 80])
    
    # Outer edge (side face)
    add.newface([[outer1_x, height_top, outer1_z], [outer2_x, height_top, outer2_z],
                 [outer2_x, height_bottom, outer2_z], [outer1_x, height_bottom, outer1_z]], [80, 80, 80])
    
    # Inner edge (side face)
    add.newface([[inner1_x, height_top, inner1_z], [inner2_x, height_top, inner2_z],
                 [inner2_x, height_bottom, inner2_z], [inner1_x, height_bottom, inner1_z]], [80, 80, 80])
    
    # Start radial face (at angle1)
    add.newface([[outer1_x, height_top, outer1_z], [inner1_x, height_top, inner1_z],
                 [inner1_x, height_bottom, inner1_z], [outer1_x, height_bottom, outer1_z]], [80, 80, 80])
    
    # End radial face (at angle2)
    add.newface([[inner2_x, height_top, inner2_z], [outer2_x, height_top, outer2_z],
                 [outer2_x, height_bottom, outer2_z], [inner2_x, height_bottom, inner2_z]], [80, 80, 80])

# Capture roundabout and clear
ROUNDABOUT = add.layer()

# Build multiple cars on the track
num_cars = 1
car_track_radius = 12

for car_num in range(num_cars):
    angle = 2 * math.pi * car_num / num_cars

    build_car()
    CAR = add.layer()

    # Rotate around the center of the track and
    # add a 90° offset so the truck points along the track.
    CAR = add.rotateY(
        CAR,
        angle + math.pi / 2,
        [0, 0.25, 0]
    )

    add.mesh(CAR)

# Render roundabout after all cars
add.mesh(ROUNDABOUT)

add.off("car_model.off")