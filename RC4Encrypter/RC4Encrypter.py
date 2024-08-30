from Cryptodome.Cipher import ARC4

class RC4Encrypter:
    def __init__(self):
        self.key = b'fhsd6f86f67rt8fw78fw789we78r9789wer6re'
        self.nonce = b'nonce'
        self.RC4_Stream = ARC4.new(self.key + self.nonce)
        self.RC4_Stream.encrypt(self.key + self.nonce)
        self.RC4_Stream2 = ARC4.new(self.key + self.nonce)
        self.RC4_Stream2.encrypt(self.key + self.nonce)

    def decrypt(self, data):
        decryptedData = self.RC4_Stream.encrypt(data)
        return decryptedData

    def encrypt(self, encEncodingBytes):
        encryptedData = self.RC4_Stream2.encrypt(encEncodingBytes)
        return encryptedData