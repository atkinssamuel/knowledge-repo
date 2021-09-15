import rsa

"""
Fernet encrypts and decrypts using AES in CBC mode with a 128-bit key for encryption using PKCS7 padding. For 
authentication, it uses HMAC and SHA256. The initialization vectors are generated using os.urandom().
"""

"""
Asymmetric encryption explained:

In asymmetric encryption, there is a public key and a private key. The public key is available to everyone while the 
private key is kept private. When two parties wish to exchange encrypted information, they each have separate public
and private keys. If they wish to send information to each other, they do so by encrypting their messages with their
own public keys and then sending the encrypted messages to each other.

Alice:
- Alice_pub
- Alice_priv

Bob:
- Bob_pub
- Bob_priv

To exchange their private keys, Alice encrypts her private key using Bob's public key and sends the encrypted message
to Bob. Bob then decrypts the encrypted message to discover Alice's private key. Now, when Alice sends Bob encrypted
messages using her public key, Bob can decrypt these messages because he has Alice's private key. 

Bob can send Alice his private key as well in the same way. This process is illustrated in the script below. Note that
this script utilizes 4 pre-generated keys: Alice_pub, Alice_priv, Bob_pub, and Bob_priv. Note that a third party 
eavesdropper, Eve, only ever sees encrypted messages passed from Alice to Bob and vice-versa. There is no opportunity
for a third party to uncover the private keys or the content of the encrypted messages. 
"""

