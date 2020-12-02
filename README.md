# N9
N9 is a cipher I invented and implemented in Python

### I'll leave you the algorithm =)

The user is required to enter the text and the key that they want to encode their text with

We have a list of digits from 1 to 9. We multiply this list by the key length

Let's assume the key " test" -> [[1,2..9], [1,2..9], [1,2..9], [1,2..9]]

text = 'hello world'

Now we need to find the position of each character in the key in ASCII

That is, we should get the following -> [116, 101, 115, 116]. The length of a list with numbers from 1 to 9 is the same as the length of this list

Now we have to loop through the list with the numbers and our key

```python
nums = [[1,2..9], [1,2..9], [1,2..9], [1,2..9]]
key = 'test' #[116, 101, 115, 116]
new_nums = []
for i, value in enumerate(nums):
    nums2 = []
    for x in value:
        x *= ord(key[i])
        nums2.append(x)

    new_nums.append(nums2)
# new_nums = [[116, 232.., 1044], [101, 202.., 909]...]
```
The next stage is about the same. We iterate through lists and values in lists.

```python
multiplication_nums = []
for i, value in enumerate(new_nums):
    nums2 = []
    for x in value:
        x %= 256
        y = x ** 2 - i
        z = (y + x) % 256
        nums2.append(z)
    multiplication_nums.append(nums2)
```
The next step is to get the sum of each list and multiply the entire list by the length of the text

```python
nums = [sum(value) for value in multiplication_nums] * len(text)
nums = nums[0:len(text)]
```
Defining 2 constants:

```python
const1 = sum([ord(i) for i in key]) ^ len(key) * 2
const2 = len(text) * const1 ^ (len(key) * 3)
```
We already use this algorithm to encode characters in our text. 
I will not explain every action in the algorithm, everything is already clear there.

```python
for i, value in enumerate(text):

    x = nums[i-1] ^ (len(text)//len(key) ^ (len(key) ^ i*const2)) % 256
        
    lentext = len(text)
        
    shift = int(bin(lentext)[-1]) + int(bin(i)[-1])
        
    shift2 = (nums[i]//10) * (shift + 1)
    shift2 = oct(shift2)
    shift2 = int(shift2[2:])

    if shift < 1:
        value = (ord(value) + nums[i] ^ const1 ^ x) ^ shift2
    else:
        value = (ord(value) + nums[i] ^ const1 ^ x) ^ shift2 ^ i
```

Perhaps you will consider my algorithm as a made-up nonsense, but in fact it is =)
