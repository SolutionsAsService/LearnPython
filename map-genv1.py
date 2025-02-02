from PIL import Image, ImageDraw
import random

# Define map size
map_width, map_height = 800, 600  # Size of the map

def generate_map():
    image = Image.new("RGB", (map_width, map_height), "blue")
    draw = ImageDraw.Draw(image)

    # Define terrain colors
    grass_color = (34, 139, 34)    # Green for grass islands
    sand_color = (210, 180, 140)   # Sandy color for desert islands

    # Number of islands
    num_islands = random.randint(5, 15)

    for _ in range(num_islands):
        # Random island size
        island_width = random.randint(50, 150)
        island_height = random.randint(50, 150)

        # Random position for the island
        x = random.randint(0, map_width - island_width)
        y = random.randint(0, map_height - island_height)

        # Randomly choose terrain type
        terrain_color = random.choice([grass_color, sand_color])

        # Draw the island
        draw.ellipse([x, y, x + island_width, y + island_height], fill=terrain_color, outline="black")

    return image
