import add
import math

add.axes([0, 0, 0])

# Simple Car Model - Correct orientation
# Y-axis is up, X-axis is forward, Z-axis is sideways
# Main body (chassis) - extends along X (length=5), Y (height=1.5), Z (width=2)
add.rectangle3D([0, 0.75, 0], [5, 1.5, 2], [107, 112, 121]) 

# Cabin (top part)
add.rectangle3D([0, 2, 0], [3, 1, 2], [107, 112, 121])  # Same color as body
M1 = add.layer()  # Save first piece
# Create and rotate the second cabin piece
add.rectangle3D([-2, 1.865, 0], [0.05, 1.42, 2], [203, 218, 245])
M2 = add.layer()  # Capture second piece
M2_rotated = add.rotateZ(M2, math.pi/-4, [-1.85, 1.9, 0])  # Rotate 270 degrees
add.mesh(M1)  # Add back first piece
add.mesh(M2_rotated)  # Add back rotated second piece 

# Fill the gap between cabin pieces
add.newface([[-1.5, 1.5, 1], [-1.5, 2.5, 1], [-2.5, 1.5, 1]], [203, 218, 245])  # Right side gap
add.newface([[-2.5, 1.5, -1], [-1.5, 2.5, -1], [-1.5, 1.5, -1]], [203, 218, 245])  # Left side gap

# Windshield (front)
#add.rectangle3D([1.5, 2.1, 0], [0.8, 0.8, 2], [100, 150, 255])  # Light blue glass


# Wheels - cylinders with axis along Y (vertical)
wheel_radius = 0.7
wheel_detail = 12

# Rear left wheel
add.cylinder([-1.5, 0.2, -0.6], [-1.5, 0.2, -1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Front left wheel
add.cylinder([1.5, 0.2, -0.6], [1.5, 0.2, -1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Back right wheel
add.cylinder([-1.5, 0.2, 0.6], [-1.5, 0.2, 1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Front right wheel
add.cylinder([1.5, 0.2, 0.6], [1.5, 0.2, 1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Headlight
add.rectangle3D([-2.3, 1.1, 0], [0.5, 0.2, 1.99], [255, 255, 255])
# Taillight
add.rectangle3D([2.3, 1.425, 0], [0.5, 0.05, 1.99], [255, 50, 50])
add.rectangle3D([2.3, 1.474, 0], [0.5, 0.05, 1.99], [0, 0, 0])
add.rectangle3D([2.3, 1.35, 0], [0.5, 0.1, 1.99], [0, 0, 0])
add.rectangle3D([2.3, 0.65, 0], [0.5, 1.3, 1.99], [107, 112, 121])

add.off("car_model.off")