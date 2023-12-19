# Fungsi untuk mengenkripsi teks menggunakan Vigenere Cipher
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Vigenere Cipher
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - key_shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - key_shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Fungsi untuk mengenkripsi teks menggunakan Affine Cipher
def affine_encrypt(plain_text, a, b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            else:
                encrypted_char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Affine Cipher
def affine_decrypt(encrypted_text, a, b):
    decrypted_text = ""
    a_inverse = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in encrypted_text:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((a_inverse * (ord(char) - ord('A') - b) % 26) + ord('A'))
            else:
                decrypted_char = chr((a_inverse * (ord(char) - ord('a') - b) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Teks yang akan dienkripsi
plain_text = "Success is not final, failure is not fatal, it is the courage to continue that counts"

# Kata kunci untuk Vigenere Cipher
vigenere_key = "ULFI"

# Parameter a dan b untuk Affine Cipher
a = 1
b = 2

# Mengenkripsi teks menggunakan Vigenere Cipher
encrypted_text_vigenere = vigenere_encrypt(plain_text, vigenere_key)

# Mengenkripsi teks menggunakan Affine Cipher
encrypted_text_affine = affine_encrypt(encrypted_text_vigenere, a, b)

# Mencetak teks terenkripsi
print("Teks Terenkripsi:")
print(encrypted_text_affine)

# Mendekripsi teks menggunakan Affine Cipher
decrypted_text_affine = affine_decrypt(encrypted_text_affine, a, b)

# Mendekripsi teks menggunakan Vigenere Cipher
decrypted_text_vigenere = vigenere_decrypt(decrypted_text_affine, vigenere_key)

# Mencetak teks terdekripsi
print("\nTeks Terdekripsi:")
print(decrypted_text_vigenere)