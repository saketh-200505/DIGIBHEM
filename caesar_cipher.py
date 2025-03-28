def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
         if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
         else:
            result += char
    return result

print("Welcome to the Caesar Cipher encryption and decryption program!")
message = input("Enter your message to encrypt or decrypt: ")
mode = input("Choose mode of operation (encrypt/decrypt): ").lower()
while mode not in ["encrypt", "decrypt"]:
    mode = input("Invalid choice. Choose mode (encrypt/decrypt): ").lower()

key_value = int(input("Enter key value (an integer): "))

output = caesar_cipher(message, key_value, mode)
print(f"Result: {output}")