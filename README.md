# Crypto Forge
Ferramenta que criptografa e descriptografa mensagens.

## Sobre
Um programa pra quem quer enviar mensagens com segurança real — não só "esconder" texto, mas criptografar de verdade.

## Como usar

```bash
python3 crypto.py
```

Rode o script, escolha entre criptografar ou descriptografar. Caso seja a opção "criptografar" - escreva a mensagem, o programa retorna o texto criptografado e a chave. Guarde a chave, sem ela é impossível descriptografar. 

Caso seja a opção "descriptografar" - cole a mensagem criptografada e a chave.

## Por que usar essa ferramenta?
Essa ferramenta usa criptografia simétrica real com o algoritmo Fernet, o mesmo usado em aplicações profissionais. Sem a chave correta, é matematicamente impossível descriptografar a mensagem.

## Contexto
Projetei esse código do zero, testando, errando e acertando. O que me trouxe até a cibersegurança foi exatamente isso, querer ser anônimo de verdade, protegido contra qualquer coisa externa. Esse projeto é um reflexo disso.
