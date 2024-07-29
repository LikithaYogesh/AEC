from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encryption(plaintext: bytes, key: bytes) -> bytes:
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(plaintext, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return iv + encrypted_data

def decryption(encrypted_data: bytes, key: bytes) -> bytes:
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = cipher.decrypt(encrypted_data)
    plaintext = unpad(padded_data, AES.block_size)
    return plaintext

def read_file(file_path: str) -> bytes:
    with open(file_path, 'rb') as f:
        return f.read()

def write_file(file_path: str, data: bytes):
    with open(file_path, 'wb') as f:
        f.write(data)

def main():
    key = b'16byteslongkey!l'  # Key must be 16, 24, or 32 bytes long for AES
    original_content = read_file('ex.txt')
    print("Original content:")
    print(original_content.decode())

    encrypted_content = encryption(original_content, key)
    print("Encrypted content in hex:")
    print(encrypted_content.hex())

    decrypted_content = decryption(encrypted_content, key)
    print("Decrypted content:")
    print(decrypted_content.decode())

    write_file('encrypted_ex.txt', encrypted_content)
    write_file('decrypted_ex.txt', decrypted_content)

if __name__ == "__main__":
    main()

