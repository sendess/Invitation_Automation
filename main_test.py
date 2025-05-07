import qrcode
from PIL import Image, ImageDraw, ImageFont
import csv
import os

def QR_generate(data):
    """Generates a QR code for the given data and saves it as a PNG file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    resized_img = img.resize((245, 245))
    qr_code_folder = "QR_Codes"
    os.makedirs(qr_code_folder, exist_ok=True)
    file_name = os.path.join(qr_code_folder, f"{data}_QR.png")
    resized_img.save(file_name)
    print(f"QR code saved as {file_name}")

def insert_QRnName_in_card(image_file, person_name, output_path):
    """Inserts a QR code (generated from the person's name) and the person's name onto the invitation card."""
    QR_generate(person_name) # Generate QR code with the person's name
    try:
        invitation_img = Image.open(image_file)
        qr_code_img = Image.open(os.path.join("QR_Codes", f"{person_name}_QR.png"))
        flag_img = Image.open(r"flag-assets\flag_2.png")
        flag_img = flag_img.resize((57,70))
        position = (297, 54)
        position_flag = (410,134)
        invitation_img.paste(qr_code_img, position, qr_code_img if qr_code_img.mode == 'RGBA' else None)
        invitation_img.paste(flag_img, position_flag, flag_img if flag_img.mode == 'RGBA' else None)

        draw = ImageDraw.Draw(invitation_img)
        font_path = "Fonts/ARIALBD 1.TTF"
        try:
            font = ImageFont.truetype(font_path, 38)
        except OSError:
            print(f"Error: Font file '{font_path}' not found. Using a default font.")
            font = ImageFont.load_default()
        text_color = (255, 0, 0)
        box_left = 610
        box_top = 310
        box_right = 1329
        box_bottom = 362
        box_width = box_right - box_left
        box_height = box_bottom - box_top
        bbox = draw.textbbox((0, 0), person_name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = box_left + (box_width - text_width) / 2
        text_y = box_top + (box_height - text_height) / 2
        draw.text((text_x, text_y), person_name, font=font, fill=text_color)
        cards_folder = "Cards"
        os.makedirs(cards_folder, exist_ok=True)
        final_output_path = os.path.join(cards_folder, f"{person_name}.png")
        invitation_img.save(final_output_path)
        print(f"Image with centered name saved as: {final_output_path}")
        print("QR code and name have been successfully overlaid onto the invitation!")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    image_file = "invitation.png"
    csv_file = "to_send_1.csv"  

    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'name' not in reader.fieldnames:
                print("Error: The CSV file must have a column named 'name'.")
            else:
                for row in reader:
                    name = row['name'].strip()
                    output_name = os.path.join("Cards", f"{name}.png")
                    insert_QRnName_in_card(image_file, name, output_name)
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")