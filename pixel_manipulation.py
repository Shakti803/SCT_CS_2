pip install Pillow
from PIL import Image

def swap_pixels(img):
    # Get image dimensions
    width, height = img.size

    # Create a new image to store swapped pixels
    swapped_img = Image.new('RGB', (width, height))

    # Iterate through each pixel and swap red and blue channels
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            swapped_img.putpixel((x, y), (b, g, r))  # Swap red and blue channels

    return swapped_img

def add_value_to_pixels(img, value):
    # Get image dimensions
    width, height = img.size

    # Create a new image to store modified pixels
    modified_img = Image.new('RGB', (width, height))

    # Iterate through each pixel and add the specified value to each channel
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r_new = (r + value) % 256  # Ensure value is within 0-255 range
            g_new = (g + value) % 256
            b_new = (b + value) % 256
            modified_img.putpixel((x, y), (r_new, g_new, b_new))

    return modified_img

def main():
    # Open an image file
    img = Image.open('input_image.jpg')  # Replace 'input_image.jpg' with your image file

    # Example 1: Swap red and blue channels
    swapped_image = swap_pixels(img)
    swapped_image.save('swapped_image.jpg')  # Save the swapped image

    # Example 2: Add a value to each pixel
    value_to_add = 50
    modified_image = add_value_to_pixels(img, value_to_add)
    modified_image.save('modified_image.jpg')  # Save the modified image

    print("Images saved successfully.")

if __name__ == "__main__":
    main()
