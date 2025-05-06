import qrcode
from PIL import Image
from PIL import Image, ImageDraw, ImageFont


def QR_generate(dat):
    data = dat
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
    file_name = str("QR_Codes" + "\\" + dat + "QR.png")
    resized_img.save(file_name)
    print("QR code saved as my_qrcode.png with resolution 980x980.")

def insert_QRnName_in_card(image_file, company_name , output_path):
    QR_generate(company_name)  # Generate QR code with the company name
    try:
        invitation_img = Image.open(image_file)
        qr_code_img = Image.open(str("QR_Codes\\" + company_name + "QR.png"))
        flag_img = Image.open(r"flag-assets\flag_2.png")
        flag_img = flag_img.resize((57,70))
        position = (297, 54)
        position_flag = (410,134)
        invitation_img.paste(qr_code_img, position, qr_code_img if qr_code_img.mode == 'RGBA' else None)
        invitation_img.paste(flag_img, position_flag, flag_img if flag_img.mode == 'RGBA' else None)

        draw = ImageDraw.Draw(invitation_img)
        font_path = "Fonts/ARIALBD 1.TTF"  
        font = ImageFont.truetype(font_path, 38)
        text_color = (255, 0, 0) 
        box_left = 610
        box_top = 310
        box_right = 1329
        box_bottom = 362
        box_width = box_right - box_left
        box_height = box_bottom - box_top
        bbox = draw.textbbox((0, 0), company_name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_x = box_left + (box_width - text_width) / 2
        text_y = box_top + (box_height - text_height) / 2
        draw.text((text_x, text_y), company_name, font=font, fill=text_color)
        invitation_img.save(output_path)
        print(f"Image with centered company name saved as: {output_path}")
        print("QR code has been successfully overlaid onto the invitation!")
        print("The result is saved as final_invitation.png")

    except FileNotFoundError:
        print("Error: Make sure 'invitation.png' and 'qr_code.png' are in the same directory as the script, or provide the full path.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    image_file = "invitation.png"

    list_of_names = ["Mr. Naresh Khapangi", "Ms. Janaki Rijal", "Mr. Ram Bahadur", "Mr. Ram Chandra", "Mr. Ram Kumar"]
    for name in list_of_names:
        output_name = str("Cards\\" + name + ".png")
        insert_QRnName_in_card(image_file, name , output_name)
