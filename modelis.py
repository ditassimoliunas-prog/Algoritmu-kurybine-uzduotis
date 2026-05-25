import add
import math

add.axes([0, 0, 0])

# Simple Car Model - Correct orientation
# Y-axis is up, X-axis is forward, Z-axis is sideways
# Main body (chassis) - extends along X (length=1.5), Y (height=0.75), Z (width=1.35)
add.rectangle3D([0, 0.375, 0], [1.5, 0.75, 1.35], [107, 112, 121]) 

# Cabin (top part)
#add.rectangle3D([-0.25, 2, 0], [2.5, 1, 2], [107, 112, 121])  # Same color as body
# M1 = add.layer()  # Save first piece
# # Create and rotate the second cabin piece
# add.rectangle3D([-2, 1.865, 0], [0.05, 1.42, 2], [203, 218, 245])
# M2 = add.layer()  # Capture second piece
# M2_rotated = add.rotateZ(M2, math.pi/-4, [-1.85, 1.9, 0])  # Rotate 270 degrees
# add.mesh(M1)  # Add back first piece
# add.mesh(M2_rotated)  # Add back rotated second piece 



# Frontglass and side windows
add.newface ([[-0.75, 0.75, -0.675], [-0.75, 0.75, 0.675], [-0.25, 1.25, 0.675], [-0.25, 1.25, -0.675]], [203, 218, 245])  # Front glass
add.newface([[-0.375, 0.75, 0.675], [-0.375, 1.125, 0.675], [-0.75, 0.75, 0.675]], [203, 218, 245])  # Right side gap
add.newface([[-0.75, 0.75, -0.675], [-0.375, 1.125, -0.675], [-0.375, 0.75, -0.675]], [203, 218, 245])  # Left side gap

# Frunk
add.newface ([[-0.75, 0.75, 0.675], [-0.75, 0.75, -0.675], [-1.1, 0.65, -0.675], [-1.1, 0.65, 0.675]], [107, 112, 121]) #Frunk lid
add.rectangle3D([-0.925, 0.325, 0], [0.35, 0.65, 1.35], [107, 112, 121]) #frunk body
#add.newface ([[-0.12, 1.375, 0.675], [-0.12, 1.375, -0.675], [-0.75, 1, -0.675], [-0.75, 1, 0.675]], [107, 112, 121])
# Wheels - cylinders with axis along Y (vertical)
wheel_radius = 0.25
wheel_detail = 12

# Front left wheel
add.cylinder([-0.7, 0, -0.405], [-0.7, 0, -0.81], wheel_radius, wheel_detail, [50, 50, 50])

# Rear left wheel
add.cylinder([0.45, 0, -0.405], [0.45, 0, -0.81], wheel_radius, wheel_detail, [50, 50, 50])

# Front right wheel
add.cylinder([-0.7, 0, 0.405], [-0.7, 0, 0.81], wheel_radius, wheel_detail, [50, 50, 50])

# Rear right wheel
add.cylinder([0.45, 0, 0.405], [0.45, 0, 0.81], wheel_radius, wheel_detail, [50, 50, 50])

# Headlight
add.rectangle3D([-1.1125, 0.55, 0], [0.025, 0.1, 1.343], [255, 255, 255])
# Taillight
add.rectangle3D([0.675, 0.7135, 0], [0.375, 0.0275, 1.343], [255, 50, 50])
add.rectangle3D([0.675, 0.74, 0], [0.375, 0.025, 1.343], [0, 0, 0])
add.rectangle3D([0.675, 0.675, 0], [0.375, 0.05, 1.343], [0, 0, 0])
add.rectangle3D([0.675, 0.325, 0], [0.375, 0.65, 1.343], [107, 112, 121])

#Trunk
add.newface ([[0.8625, 0.745, 0.675], [0.8625, 0.755, -0.675], [0.2, 1.1, -0.675], [0.2, 1.1, 0.675]], [46,48,52])  # Trunk back face
add.newface ([[-0.25, 1.25, -0.675], [-0.25, 1.25, 0.675], [0.2, 1.1, 0.675], [0.2, 1.1, -0.675]], [107, 112, 121])  # Trunk back face extension
add.newface ([[0.2, 0.75, -0.675], [0.2, 1.1, -0.675], [0.86, 0.75, -0.675]], [107, 112, 121]) #Trunk right side
add.newface ([[0.8, 0.75, 0.675], [0.2, 1.25, 0.675], [0.2, 0.75, 0.675]], [107, 112, 121]) #Trunk left side


add.off("car_model.off")