import add

add.axes([0, 0, 0])

# Simple Car Model - Correct orientation
# Y-axis is up, X-axis is forward, Z-axis is sideways
# Main body (chassis) - extends along X (length=5), Y (height=1.5), Z (width=2)
add.rectangle3D([0, 0.75, 0], [5, 1.5, 2], [200, 50, 50])  # Red-brown body

# Cabin (top part)
add.rectangle3D([0, 1.85, 0], [3, 1.2, 1.8], [200, 50, 50])  # Same color as body

# Windshield (front)
add.rectangle3D([1.5, 2.1, 0], [0.8, 0.8, 1.8], [100, 150, 255])  # Light blue glass

# Wheels - cylinders with axis along Y (vertical)
wheel_radius = 0.7
wheel_detail = 12

# Front left wheel
add.cylinder([-1.5, 0, -1.2], [-1.5, 1, -1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Front right wheel
add.cylinder([1.5, 0, -1.2], [1.5, 1.4, -1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Back left wheel
add.cylinder([-1.5, 0, 1.2], [-1.5, 1.4, 1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Back right wheel
add.cylinder([1.5, 0, 1.2], [1.5, 1.4, 1.2], wheel_radius, wheel_detail, [50, 50, 50])

# Headlights (small boxes)
add.rectangle3D([-2.5, 0.8, -0.8], [0.4, 0.4, 0.4], [255, 255, 100])  # Left headlight
add.rectangle3D([-2.5, 0.8, 0.8], [0.4, 0.4, 0.4], [255, 255, 100])   # Right headlight

# Taillights (small boxes)
add.rectangle3D([2.5, 0.8, -0.8], [0.4, 0.4, 0.4], [255, 50, 50])  # Left taillight
add.rectangle3D([2.5, 0.8, 0.8], [0.4, 0.4, 0.4], [255, 50, 50])   # Right taillight

add.off("car_model.off")