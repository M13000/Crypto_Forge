from cryptography.fernet import Fernet

decisão=input("Você quer criptografar ou descriptografar a mensagem? ")

key=Fernet.generate_key()

cipher_suite = Fernet(key)

if decisão == "criptografar":
    mensagem = input("Digite sua mensagem: ").encode()
    
    cipher_text = cipher_suite.encrypt(mensagem)
    print(f"Encrypted: {cipher_text}")
    print(f"Chave: {key.decode()}")
elif decisão == "descriptografar":
  cipher_text= input("Digite a mensagem criptografada: ").encode()
  key= input("Digite a chave: ").encode()
  cipher_suite = Fernet(key)
  plain_text = cipher_suite.decrypt(cipher_text)
  print(f"Decrypted: {plain_text.decode()}")


