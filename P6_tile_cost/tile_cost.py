# Step 1: Get User Input
width = float(input("Enter the width of the floor plan (in meters): "))
height = float(input("Enter the height of the floor plan (in meters): "))
cost_per_tile = float(input("Enter the cost of a single tile (in dollars): "))

# Step 2: Calculate Area
total_area = width * height

# Step 3: Determine Tile Area (Assuming square tiles for simplicity)
tile_side_length = float(input("Enter the side length of a tile (in meters): "))
tile_area = tile_side_length ** 2

# Step 4: Calculate Number of Tiles
num_tiles = total_area / tile_area

# Step 5: Calculate Total Cost
total_cost = num_tiles * cost_per_tile

# Step 6: Display Result
print(f"The total cost to cover the floor plan is ${total_cost:.2f}")
