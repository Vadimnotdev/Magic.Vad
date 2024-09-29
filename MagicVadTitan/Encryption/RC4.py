class RC4:
    def __init__(self, key: bytes):
        self.S = list(range(256))  # Инициализация массива S
        self.i = 0  # Индексы для генерации псевдослучайного ключевого потока
        self.j = 0
        self.key_schedule(key)

    def key_schedule(self, key: bytes):
        key_length = len(key)
        j = 0
        for i in range(256):
            j = (j + self.S[i] + key[i % key_length]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]  # Меняем местами значения

    def process(self, data: bytes) -> bytes:
        output = bytearray()
        for byte in data:
            self.i = (self.i + 1) % 256
            self.j = (self.j + self.S[self.i]) % 256
            self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
            K = self.S[(self.S[self.i] + self.S[self.j]) % 256]
            output.append(byte ^ K)
        return bytes(output)
