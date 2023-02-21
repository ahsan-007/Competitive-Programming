# https://leetcode.com/problems/encode-and-decode-tinyurl/

import random


class Codec:
    def __init__(self):
        self.urls = {}
        self.valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX0123456789"

    def get_random_string(self, length):
        random_string = ''
        for i in range(length):
            random_string = random_string + \
                self.valid_chars[random.randint(0, len(self.valid_chars))-1]
        return random_string

    def encode(self, longUrl: str) -> str:
        # Before encoding, it can be checked whether a url is already shortened i.e. it has already been encoded
        # and an entry exists for it in urls, if yes then that shortened url can be returned
        # Advantage is that storage will be saved as in case same URL is encoded multiple times there will not be multiple entries
        # Disadvantage is that time complexity will increase as all the encoded URLs need to be checked before encoding any URL
        # time-space trade off
        random_string = self.get_random_string(8)
        while random_string in self.urls:
            random_string = self.get_random_string(8)
        self.urls[random_string] = longUrl
        return f'http://tinyurl.com/{random_string}'

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl.split('/')[3]]


codec = Codec()
enc = codec.encode('https://leetcode.com/problems/design-tinyurl')
print(enc)
print(codec.decode(enc))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
