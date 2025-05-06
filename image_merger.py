from PIL import Image

try:
    # 1. Open the background image (your invitation)
    invitation_img = Image.open("invitation.png")

    # 2. Open the foreground image (your QR code)
    qr_code_img = Image.open("qr_code.png")
    flag_img = Image.open("flag_2.png")
    flag_img = flag_img.resize((57,70))

    # Optional: If your QR code PNG has transparency (an alpha channel),
    # you'll want to make sure you use it when pasting.
    # The .paste() method handles this automatically if the foreground image has an alpha mask.

    # 3. Define the position where you want to place the QR code
    #    (x, y) coordinates from the top-left corner of the invitation.
    #    You'll need to adjust these values to suit your invitation layout.
    position = (297, 54)  # Example: 50 pixels from left, 100 pixels from top
    position_flag = (410,134)

    # 4. Paste the QR code onto the invitation
    #    If qr_code_img has an alpha channel for transparency, it will be used.
    invitation_img.paste(qr_code_img, position, qr_code_img if qr_code_img.mode == 'RGBA' else None)
    invitation_img.paste(flag_img, position_flag, flag_img if flag_img.mode == 'RGBA' else None)

    # 5. Save the result
    invitation_img.save("final_invitation.png")

    # Or, if you want to just display it (e.g., in a Jupyter Notebook or image viewer)
    # invitation_img.show()

    print("QR code has been successfully overlaid onto the invitation!")
    print("The result is saved as final_invitation.png")

except FileNotFoundError:
    print("Error: Make sure 'invitation.png' and 'qr_code.png' are in the same directory as the script, or provide the full path.")
except Exception as e:
    print(f"An error occurred: {e}")