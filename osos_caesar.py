#WELCOME TO CAESAR CIPHER ENCRYPT -DECRYPT Created by Eng: MohamedOusama 
#e-mail:mohamed2018170311@cis.asu.edu.eg
import streamlit as st

def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

# Streamlit UI
st.title("Caesar Cipher Encryption/Decryption")

text = st.text_area("Enter your text:")
shift = st.number_input("Shift Value:", min_value=1, max_value=25, value=3, step=1)

col1, col2 = st.columns(2)

if col1.button("Encrypt"):
    encrypted_text = caesar_cipher(text, shift)
    st.text_area("Encrypted Text:", encrypted_text, height=100)

if col2.button("Decrypt"):
    decrypted_text = caesar_cipher(text, shift, decrypt=True)
    st.text_area("Decrypted Text:", decrypted_text, height=100)
