### README.md

```markdown
# QR Code Generator

This is a simple Python application that helps you create a QR code from a given link. The user can customize various aspects of the QR code, such as its size, the number of pixels, the border thickness, and the colors of the QR code and its background.

## Requirements

- Python 3.x
- `qrcode` library

You can install the `qrcode` library using pip:
```sh
pip install qrcode[pil]
```

## Usage

1. Run the script:
```sh
python qr_code_generator.py
```

2. Follow the prompts:

   - When asked if you are ready, type `yes` to continue or `no` to exit.
   - Provide the link you want to convert into a QR code.
   - Specify the QR code size by entering a number between 1 and 40.
   - Enter the number of pixels you want for the QR code.
   - Specify the border thickness in boxes.
   - Choose the fill color and background color for the QR code.

3. The generated QR code will be saved as `youtube_qr.png` in the same directory as the script.

4. If you need to generate another QR code, type `yes` when prompted. Otherwise, type `no` to exit the program.

## Example

Here's an example of how the prompts and responses might look:

```
Hi there!🤓 This simple App will help you to create a QR code with a given link
If you're ready type 'yes' otherwise type 'no': yes
Please write or paste your link here: https://www.example.com
Write a number between 1 or 40 to specify the QR code size: 10
How many pixels do you want?: 10
How many boxes thick the border should be?: 4
What would be the fill color?: black
What would be the background color?: white
Enjoy your QR code!👌
Need another one? type 'yes' otherwise type 'no': no
Hasta la vista baby 🤖
```

## Note

- Ensure that the colors you enter are recognized by the `qrcode` library. Common color names like `black`, `white`, `red`, `blue`, etc., should work fine.

- The QR code image will be saved with the name `youtube_qr.png`. You can modify the script to allow users to specify a different file name if desired.

Enjoy creating QR codes! 🚀
```
