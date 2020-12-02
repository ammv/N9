class N9:

    @classmethod
    def encode(self, text, key):
        nums = [self._get_nums()] * len(key)
        nums = self._get_new_nums(nums, key)
        nums = self._get_multiplication_nums(nums)

        encode_text = self._get_encoded_text(text, nums, key)

        return encode_text

    @classmethod
    def decode(self, text, key):
        text = text.split()

        nums = [self._get_nums()] * len(key)
        nums = self._get_new_nums(nums, key)
        nums = self._get_multiplication_nums(nums)
        nums = [sum(value) for value in nums] * len(text)
        nums = nums[0:len(text)]

        const1 = sum([ord(i) for i in key]) ^ len(key) * 2
        const2 = len(text) * const1 ^ (len(key) * 3)

        decoded_text = ''

        for i, value in enumerate(text):
            const = nums[i - 1] ^ (len(text) // len(key) ^ (len(key) ^ i * const2)) % 256

            lentext = len(text)
            shift = int(bin(lentext)[-1]) + int(bin(i)[-1])
            shift2 = (nums[i] // 10) * (shift + 1)
            shift2 = oct(shift2)
            shift2 = int(shift2[2:])

            if shift < 1:
                #value = (ord(value) + nums[i] ^ const1 ^ const) ^ shift2
                value = int(value) ^ shift2
                value = value ^ const
                value = value ^ const1
                value -= nums[i]
            else:
                #value = (ord(value) + nums[i] ^ const1 ^ const) ^ shift2 ^ i
                value = int(value) ^ i
                value = value ^ shift2
                value = value ^ const
                value = value ^ const1
                value -= nums[i]

            decoded_text += chr(value)

        return decoded_text

    @staticmethod
    def _get_nums():
        return [i for i in range(1, 10)]

    @staticmethod
    def _get_new_nums(nums, key):
        new_nums = []
        for i, value in enumerate(nums):
            nums2 = []
            for x in value:
                x = x * ord(key[i])
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
    def _get_encoded_text(text, nums, key):
        nums = [sum(value) for value in nums] * len(text)
        nums = nums[0:len(text)]

        const1 = sum([ord(i) for i in key]) ^ len(key) * 2
        const2 = len(text) * const1 ^ (len(key) * 3)

        encoded_text = ''
        for i, value in enumerate(text):

            const = nums[i-1] ^ (len(text)//len(key) ^ (len(key) ^ i*const2)) % 256
            lentext = len(text)
            shift = int(bin(lentext)[-1]) + int(bin(i)[-1])
            shift2 = (nums[i]//10) * (shift + 1)
            shift2 = oct(shift2)
            shift2 = int(shift2[2:])

            if shift < 1:
                value = (ord(value) + nums[i] ^ const1 ^ const) ^ shift2
            else:
                value = (ord(value) + nums[i] ^ const1 ^ const) ^ shift2 ^ i

            encoded_text += str(value) + ' '

        return encoded_text.strip()

#print(N9.encode('111111111111111111111111111'*20, '1'))
