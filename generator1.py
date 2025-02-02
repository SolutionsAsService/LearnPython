from PIL import Image, ImageDraw
import random

# Define image size
width, height = 64, 64  # Larger size for pixel art

def generate_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_fur_color():
    # Constrain fur colors to white, black, and brown
    fur_colors = [(255, 255, 255), (0, 0, 0), (139, 69, 19)]
    return random.choice(fur_colors)

def generate_rodent_image():
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Draw the rodent body
    body_color = generate_random_color()
    draw.rectangle([16, 32, 48, 56], fill=body_color)

    # Draw the rodent head
    head_color = generate_fur_color()
    draw.rectangle([24, 16, 40, 32], fill=head_color)

    # Draw the rodent ears
    ear_color = head_color
    draw.rectangle([20, 12, 24, 16], fill=ear_color)
    draw.rectangle([40, 12, 44, 16], fill=ear_color)

    # Draw the rodent tail
    tail_color = generate_random_color()
    draw.line([48, 44, 60, 44], fill=tail_color, width=4)

    return image

def generate_island_image():
    image = Image.new("RGB", (width, height), "blue")
    draw = ImageDraw.Draw(image)

    # Draw the island base
    island_color = generate_random_color()
    draw.ellipse([8, 32, 56, 56], fill=island_color)

    # Draw a tree on the island
    tree_trunk_color = generate_random_color()
    draw.rectangle([32, 16, 34, 32], fill=tree_trunk_color)
    tree_leaves_color = generate_random_color()
    draw.ellipse([24, 8, 42, 24], fill=tree_leaves_color)

    return image
