class N9:

    @classmethod
    def encode(self, text, key, deep=False):
        nums = [self._get_nums()] * len(key)
        nums = self._get_new_nums(nums, key, deep)
        nums = self._get_multiplication_nums(nums)

        encode_text = self._get_encoded_text(text, nums, key, deep)

        return encode_text

    @classmethod
    def decode(self, text, key, deep=False):
        nums = [self._get_nums()] * len(key)
        nums = self._get_new_nums(nums, key, deep)
        nums = self._get_multiplication_nums(nums)

        decoded_text = self._get_decoded_text(text, nums, key, deep)

        return decoded_text

    @staticmethod
    def _get_nums():
        return [i for i in range(1, 10)]

    @staticmethod
    def _get_new_nums(nums, key, deep=False):
        new_nums = []
        for i, value in enumerate(nums):
            nums2 = []
            for x in value:
                x = x * ord(key[i])
                if deep: x = x * deep
                nums2.append(x)
            new_nums.append(nums2)

        return new_nums

    @staticmethod
    def _get_multiplication_nums(nums):
        multiplication_nums = []
        for i, value in enumerate(nums):
            nums2 = []
            for x in value:
                x %= 256
                y = x ** 2 - i
                z = (y + x) % 256
                nums2.append(z)
            multiplication_nums.append(nums2)

        return multiplication_nums

    @staticmethod
    def _get_encoded_text(text, nums, key, deep):
        lentext = len(text)
        if deep:
            lentext *= deep

        nums = [sum(value) for value in nums] * lentext
        nums = nums[0:lentext]

        const1 = sum([ord(i) for i in key]) ^ len(key) * 2
        const2 = lentext * const1 ^ (len(key) * 3)

        encoded_text = ''
        for i, value in enumerate(text):

            x = nums[i-1] ^ (lentext//len(key) ^ (len(key) ^ i*const2)) % 256
            shift = int(bin(lentext)[-1]) + int(bin(i)[-1])
            shift2 = (nums[i]//10) * (shift + 1)
            shift2 = oct(shift2)
            shift2 = int(shift2[2:])

            if shift < 1:
                value = (ord(value) + nums[i] ^ const1 ^ x) ^ shift2
            else:
                value = (ord(value) + nums[i] ^ const1 ^ x) ^ shift2 ^ i

            encoded_text += str(value) + ' '

        return encoded_text.strip()

    @staticmethod
    def _get_decoded_text(text, nums, key, deep):
        text = text.split()

        lentext = len(text)
        if deep:
            lentext *= deep

        nums = [sum(value) for value in nums] * lentext
        nums = nums[0:lentext]

        const1 = sum([ord(i) for i in key]) ^ len(key) * 2
        const2 = lentext * const1 ^ (len(key) * 3)

        decoded_text = ''

        for i, value in enumerate(text):
            x = nums[i - 1] ^ (len(text) // len(key) ^ (len(key) ^ i * const2)) % 256

            x = nums[i - 1] ^ (lentext // len(key) ^ (len(key) ^ i * const2)) % 256
            shift = int(bin(lentext)[-1]) + int(bin(i)[-1])
            shift2 = (nums[i] // 10) * (shift + 1)
            shift2 = oct(shift2)
            shift2 = int(shift2[2:])

            if shift < 1:
                # value = (ord(value) + nums[i] ^ const1 ^ const) ^ shift2
                value = int(value) ^ shift2
                value = value ^ x
                value = value ^ const1
                value -= nums[i]
            else:
                # value = (ord(value) + nums[i] ^ const1 ^ const) ^ shift2 ^ i
                value = int(value) ^ i
                value = value ^ shift2
                value = value ^ x
                value = value ^ const1
                value -= nums[i]

            decoded_text += chr(value)

        return decoded_text.strip()

#print(N9.encode('111111111111111111111111111'*20, '1'))
