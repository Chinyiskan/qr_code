import qrcode

print("Hi there!🤓 This simple App will help you to create a QR code with a given link")
user_input = str(input("If your ready type 'yes' otherwise type 'no': ").lower())

while True:

    if user_input == "yes":
        website_link = input("Please write or paste your link here: ")
        box_size = int(input("Write a number between 1 or 40 to specify the QR code size: "))
        pixels = int(input("How many pixels do you want?: "))
        border_thick = int(input("how many boxes thick the border should be?: "))
        fill = input("What would be the fill color?: ")
        background = input("What would be the background color?: ")

        qr = qrcode.QRCode(version=box_size, box_size=pixels, border=border_thick)
        qr.add_data(website_link)
        qr.make()

        img = qr.make_image(fill_color=fill, back_color=background)
        img.save('youtube_qr.png')

        print("Enjoy your QR code!👌")
        user_input = str(input("Need another one? type 'yes' otherwise type 'no': ").lower())

    elif user_input == 'no':
        print("Hasta la vista baby 🤖")
        break
