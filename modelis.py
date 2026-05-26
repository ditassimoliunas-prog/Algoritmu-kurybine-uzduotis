import add
import math

#add.axes([0, 0, 0])

# Function to build a car at the standard position [12, 0.25, 0]
def build_car(body_color=[107, 112, 121]):
    # Main body (chassis)
    add.rectangle3D([12, 0.25, 15], [1.5, 0.75, 1.35], body_color)

    # Frontglass and side windows
    add.newface([[11.25, 0.625, 14.325], [11.25, 0.625, 15.675], [11.75, 0.975, 15.675], [11.75, 0.975, 14.325]], [203, 218, 245])
    add.newface([[11.625, 0.625, 15.675], [11.625, 0.8875, 15.675], [11.25, 0.625, 15.675]], [203, 218, 245])
    add.newface([[11.25, 0.625, 14.325], [11.625, 0.8875, 14.325], [11.625, 0.625, 14.325]], [203, 218, 245])

    # Panel between side and rear windows
    add.newface ([[11.625, 0.625, 14.325], [11.625, 0.8875, 14.325], [11.9, 0.925, 14.325], [11.9, 0.625, 14.325]], [203, 218, 245])
    add.newface ([[11.9, 0.625, 15.675], [11.9, 0.925, 15.675], [11.625, 0.8875, 15.675], [11.625, 0.625, 15.675]], [203, 218, 245])
    add.newface ([[11.9, 0.925, 15.675], [11.75, 0.975, 15.675], [11.625, 0.8875, 15.675]], body_color)
    add.newface ([[11.625, 0.8875, 14.325], [11.75, 0.975, 14.325], [11.9, 0.925, 14.325]], body_color)

    # Rear windows
    add.newface ([[11.9, 0.625, 14.325], [11.9, 0.925, 14.325], [12.2, 0.825, 14.325], [12.2, 0.625, 14.325]], [203, 218, 245])
    add.newface ([[11.9, 0.925, 15.675], [11.9, 0.625, 15.675], [12.2, 0.625, 15.675], [12.2, 0.825, 15.675]], [203, 218, 245])

    # Frunk
    add.newface ([[11.25, 0.625, 15.675], [11.25, 0.625, 14.325], [10.9, 0.525, 14.325], [10.9, 0.525, 15.675]], body_color)
    add.rectangle3D([11.075, 0.2, 15], [0.35, 0.65, 1.35], body_color)
    add.newface([[11.25, 0.525, 15.675], [11.25, 0.625, 15.675], [10.9, 0.525, 15.675]], body_color)
    add.newface([[10.9, 0.525, 14.325], [11.25, 0.625, 14.325], [11.25, 0.525, 14.325]], body_color)

    # Wheels
    wheel_radius = 0.25
    wheel_detail = 12
    add.cylinder([11.3, -0.125, 14.595], [11.3, -0.125, 14.19], wheel_radius, wheel_detail, [50, 50, 50])
    add.cylinder([12.45, -0.125, 14.595], [12.45, -0.125, 14.19], wheel_radius, wheel_detail, [50, 50, 50])
    add.cylinder([11.3, -0.125, 15.405], [11.3, -0.125, 15.81], wheel_radius, wheel_detail, [50, 50, 50])
    add.cylinder([12.45, -0.125, 15.405], [12.45, -0.125, 15.81], wheel_radius, wheel_detail, [50, 50, 50])

    # Headlight
    add.rectangle3D([10.8875, 0.425, 15], [0.025, 0.1, 1.345], [255, 255, 255])
    # Taillight
    add.rectangle3D([12.80625, 0.5875, 15], [0.1125, 0.025, 1.35], [255, 50, 50])
    add.rectangle3D([12.80625, 0.6125, 15], [0.1125, 0.025, 1.35], [0, 0, 0])
    add.rectangle3D([12.80625, 0.55, 15], [0.1125, 0.05, 1.35], [0, 0, 0])
    add.rectangle3D([12.80625, 0.2, 15], [0.1125, 0.65, 1.35], body_color)

    # Trunk
    add.newface ([[12.8625, 0.625, 15.675], [12.8625, 0.625, 14.325], [12.2, 0.825, 14.325], [12.2, 0.825, 15.675]], [46,48,52])
    add.newface ([[11.75, 0.975, 14.325], [11.75, 0.975, 15.675], [12.2, 0.825, 15.675], [12.2, 0.825, 14.325]], body_color)
    add.newface ([[12.2, 0.625, 14.325], [12.2, 0.825, 14.325], [12.8625, 0.625, 14.325]], body_color)
    add.newface ([[12.8625, 0.625, 15.675], [12.2, 0.825, 15.675], [12.2, 0.625, 15.675]], body_color)


outer_radius = 25
inner_radius = 10
segments = 32
height_top = -0.375
height_bottom = -0.575

# Track segment colors
track_colors = [
    [101, 95, 69],
    [216, 174, 109],
    [255, 225, 171],
    [219, 181, 124],
    [184, 156, 114]
]

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
    
    # Cycle through colors
    color = track_colors[i % len(track_colors)]
    
    # Top surface of ring
    add.newface([[outer1_x, height_top, outer1_z], [outer2_x, height_top, outer2_z], 
                 [inner2_x, height_top, inner2_z], [inner1_x, height_top, inner1_z]], color)
    
    # Bottom surface of ring
    add.newface([[outer1_x, height_bottom, outer1_z], [inner1_x, height_bottom, inner1_z], 
                 [inner2_x, height_bottom, inner2_z], [outer2_x, height_bottom, outer2_z]], color)
    
    # Outer edge (side face)
    add.newface([[outer1_x, height_top, outer1_z], [outer2_x, height_top, outer2_z],
                 [outer2_x, height_bottom, outer2_z], [outer1_x, height_bottom, outer1_z]], color)
    
    # Inner edge (side face)
    add.newface([[inner1_x, height_top, inner1_z], [inner2_x, height_top, inner2_z],
                 [inner2_x, height_bottom, inner2_z], [inner1_x, height_bottom, inner1_z]], color)
    
    # Start radial face (at angle1)
    add.newface([[outer1_x, height_top, outer1_z], [inner1_x, height_top, inner1_z],
                 [inner1_x, height_bottom, inner1_z], [outer1_x, height_bottom, outer1_z]], color)
    
    # End radial face (at angle2)
    add.newface([[inner2_x, height_top, inner2_z], [outer2_x, height_top, outer2_z],
                 [outer2_x, height_bottom, outer2_z], [inner2_x, height_bottom, inner2_z]], color)

# Capture roundabout and clear
ROUNDABOUT = add.layer()

# Build multiple cars on the track
num_cars = 32
car_track_radius = 1.2

# Pastel color palette for alternating cars
all_colors = [
    [107, 112, 121],   # Gray
    [255, 179, 186],  # Pastel red
    [255, 223, 186],  # Pastel peach
    [255, 250, 200],  # Pastel yellow
    [186, 255, 201],  # Pastel green
    [186, 225, 255],  # Pastel blue
    [220, 198, 255],   # Pastel purple
    [255, 200, 255]    # Pastel pink
]

for car_num in range(num_cars):
    angle = 2 * math.pi * car_num / num_cars
    
    # Start new layer for this car
    CAR = add.layer()
    
    # Cycle through all colors equally
    car_color = all_colors[car_num % len(all_colors)]
    build_car(car_color)
    
    # Rotate around the center of the track and
    # add a 90° offset so the truck points along the track.
    CAR = add.rotateY(
        CAR,
        angle + math.pi / 2,
        [1, 0, -1]
    )
    
    # Only move every second car (odd-numbered cars)
    if car_num % 2 == 1:
        # Translate to position on the track
        # Alternate left/right based on car number
        car_x = car_track_radius * math.cos(angle)
        car_z = car_track_radius * math.sin(angle)
        
        # Side offset: even cars go right (outward), odd cars go left (inward)
        side_offset = 1 if car_num % 2 == 0 else -1.75
        
        # Calculate perpendicular direction (radial) for lateral offset
        offset_x = side_offset * math.cos(angle)
        offset_z = side_offset * math.sin(angle)
        
        CAR = add.move(CAR, [car_x + offset_x, 0, car_z + 0.425 + offset_z])

    add.mesh(CAR)

# Render roundabout after all cars
add.mesh(ROUNDABOUT)

# Add sphere in the center (after roundabout so it doesn't rotate)
add.sphere([0, 0, 0], 10, 20, [237,219,173])

add.off("car_model.off")