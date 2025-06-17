from PIL import Image
#Encryption
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image has been encrypted successfully!")
# Decription 
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image has been decrypted successfully!")

 # image path
input_image = r"C:\Users\avvar\OneDrive\Desktop\Tamizan intern\image.jpg"
encrypted_image = r"C:\Users\avvar\OneDrive\Desktop\Tamizan intern\decrypted_image.jpg"
decrypted_image = r"C:\Users\avvar\OneDrive\Desktop\Tamizan intern\encrypted_image.jpg"


# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)