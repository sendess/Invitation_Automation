from PIL import Image, ImageDraw, ImageFont

def add_name_to_invitation(image_path, company_name, output_path="invitation_with_name.png"):
    """
    Adds a company name to an invitation card image, specifically placing it on the red line.

    Args:
        image_path (str): Path to the invitation card image.
        company_name (str): The name of the company to add.
        output_path (str, optional): Path to save the modified image. Defaults to "invitation_with_name.png".
    """
    # 1. Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # 2. Define text properties
    #    -  Font:  You'll need to choose a font that looks good on your card.
    #       I'm using a TrueType font (.ttf).  If you don't have "arial.ttf",
    #       you can download it or use a different font file.  Make sure the font
    #       file is in the same directory as your script, or provide the full path.
    #    - Size: Adjust the size (30) as needed to fit the red line on your card.
    #    - Color: Black (0, 0, 0)
    font_path = "Fonts\ARIALBD 1.TTF"  #  <--  Change this to the path of your font file
    try:
        font = ImageFont.truetype(font_path, 38)
    except OSError:
        print(f"Error: Font file '{font_path}' not found. Using a default font.")
        font = ImageFont.load_default()  # Use a default font if the specified one isn't found.

    text_color = (255, 0, 0)  # Black

    # 3. Define text position
    #    - These coordinates (x, y) need to be adjusted to place the name
    #      correctly on the red line in your image.  I've made a guess,
    #      and you will almost certainly need to change these values.
    #    - The (x, y) coordinates represent the top-left corner of the text box.
    text_position = (610, 310)  # <---  **Adjust these coordinates!**

    # 4. Add the text
    #    - 'company_name' is the text to be drawn.
    #    - 'font' is the font object we created.
    #    - 'fill' is the color of the text.
    draw.text(text_position, company_name, font=font, fill=text_color)

    # 5. Save the modified image
    img.save(output_path)
    print(f"Image with company name saved as: {output_path}")

if __name__ == "__main__":
    image_file = "final_invitation.png"  # Replace with the actual path to your image
    # company_name = "Back-Roads Touring Company Limited"
    company_name = "Ms. Janaki Rijal"  # Replace with the actual company name
    add_name_to_invitation(image_file, company_name)
