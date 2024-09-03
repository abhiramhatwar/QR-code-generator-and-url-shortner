import requests
import qrcode
import webcolors

def generate_qr_code(url, filename, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)

def shorten_url(url):
    try:
        response = requests.get(f"http://tinyurl.com/api-create.php?url={url}")
        if response.status_code == 200:
            return response.text
        else:
            print("Error occurred while shortening URL.")
            return None
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None

if __name__ == "__main__":
    url = input("Enter the URL you want to encode in the QR code: ")
    filename = input("Enter the filename to save the QR code image (with extension): ")
    fill_color = input("Enter the fill color for the QR code (default is black): ") or "black"
    back_color = input("Enter the background color for the QR code (default is white): ") or "white"

    shortened_url = shorten_url(url)
    if shortened_url:
        print("Shortened URL:", shortened_url)
        
        try:
            generate_qr_code(shortened_url, filename, fill_color, back_color)
            print(f"QR Code generated and saved as '{filename}'")
        except Exception as e:
            print(f"Error occurred while generating QR code: {e}")
    else:
        print("Failed to shorten URL.")
