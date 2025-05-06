from PIL import Image, ImageDraw, ImageFont

def add_name_to_invitation(image_path, company_name, output_path="invitation_with_name.png"):
    
    # 1. Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # 2. Define text properties
    font_path = "Fonts/ARIALBD 1.TTF"  # <-- Change this to the path of your font file
    try:
        font = ImageFont.truetype(font_path, 38)
    except OSError:
        print(f"Error: Font file '{font_path}' not found. Using a default font.")
        font = ImageFont.load_default()

    text_color = (255, 0, 0)  # Red

    # 3. Define the text box
    #    - These coordinates define a rectangle where the text will be centered.
    #    -  You MUST adjust these values to match the red line area on your card.
    box_left = 610
    box_top = 310
    box_right = 1329
    box_bottom = 362
    box_width = box_right - box_left
    box_height = box_bottom - box_top

    # 4. Get text size using textbbox
    bbox = draw.textbbox((0, 0), company_name, font=font)  # Use a dummy position (0, 0)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 5. Calculate centered position
    text_x = box_left + (box_width - text_width) / 2
    text_y = box_top + (box_height - text_height) / 2

    # 6. Add the text
    draw.text((text_x, text_y), company_name, font=font, fill=text_color)

    # 7. Save the modified image
    img.save(output_path)
    print(f"Image with centered company name saved as: {output_path}")

if __name__ == "__main__":
    image_file = "final_invitation.png"
    # company_name = "Just You"
    company_name = "Ms. Janaki Rijal"  # Replace with the actual company name
    add_name_to_invitation(image_file, company_name)
