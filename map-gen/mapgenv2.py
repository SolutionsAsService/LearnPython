from PIL import Image, ImageDraw
import random

# Define map size
map_width, map_height = 800, 600  # Size of the map

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_map():
    image = Image.new("RGB", (map_width, map_height), "blue")
    draw = ImageDraw.Draw(image)

    # Define terrain colors
    grass_color = (34, 139, 34)    # Green for grass islands
    sand_color = (210, 180, 140)   # Sandy color for desert islands
    forest_color = (0, 100, 0)     # Dark green for forest
    volcano_color = (139, 69, 19)  # Brown for volcano
    lava_color = (255, 69, 0)      # Red for lava

    # Number of islands
    num_islands = random.randint(3, 8)

    islands = []

    for _ in range(num_islands):
        while True:
            # Random island size
            island_width = random.randint(50, 150)
            island_height = random.randint(50, 150)

            # Random position for the island
            x = random.randint(0, map_width - island_width)
            y = random.randint(0, map_height - island_height)

            # Check if the new island overlaps with existing ones
            overlap = False
            for (ix, iy, iw, ih) in islands:
                if not (x + island_width < ix or x > ix + iw or y + island_height < iy or y > iy + ih):
                    overlap = True
                    break

            if not overlap:
                islands.append((x, y, island_width, island_height))
                break

    for (x, y, island_width, island_height) in islands:
        # Randomly choose terrain type
        terrain_color = random.choice([grass_color, sand_color])
        draw.ellipse([x, y, x + island_width, y + island_height], fill=terrain_color, outline="black")

        # Add details to the island
        detail_type = random.choice(['forest', 'volcano', 'none'])
        
        if detail_type == 'forest':
            # Add forest patches
            for _ in range(random.randint(3, 7)):
                fx = random.randint(x, x + island_width - 10)
                fy = random.randint(y, y + island_height - 10)
                fw = random.randint(10, 20)
                fh = random.randint(10, 20)
                draw.ellipse([fx, fy, fx + fw, fy + fh], fill=forest_color)
        
        elif detail_type == 'volcano':
            # Add a volcano
            vx = x + island_width // 2 - 10
            vy = y + island_height // 2 - 10
            draw.polygon([(vx, vy), (vx + 20, vy), (vx + 10, vy - 20)], fill=volcano_color)
            # Add lava
            draw.ellipse([vx + 5, vy - 10, vx + 15, vy], fill=lava_color)

    return image

# Generate and save the images for testing
if __name__ == '__main__':
    map_image = generate_map()
    map_image.show()  # Opens the generated map image in the default image viewer
    map_image.save("map.png")  # Saves the generated map image to a file
