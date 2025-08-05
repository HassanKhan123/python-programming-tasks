def is_even(num):
    return True if num % 2 == 0 else False


# res = is_even(2)


def count_vowels(str: str):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for s in str:
        if s.lower() in vowels:
            count += 1

    return count


# res = count_vowels("I am Hassan")


def find_max(lst: list):
    max = lst[0]

    for l in lst:
        if l > max:
            max = l

    return max


# res = find_max([5, 2, 13, 4, 1])


def fizz_buzz(n: int):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", i)
        elif i % 3 == 0:
            print("Fizz", i)
        elif i % 5 == 0:
            print("Buzz", i)
        else:
            print(i)


# res = fizz_buzz(15)


def reverse_string(s: str):
    return s[::-1]
    # chars = []

    # for i in range(len(s)-1, -1, -1):
    #     chars.append(s[i])

    # return "".join(chars)


# res = reverse_string("Hassan")


def word_frequencies(text: str) -> dict:
    arr = text.split(" ")
    word_dict = {}

    for word in arr:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word]+1

    return word_dict


# res = word_frequencies("My name is Hassan and My age is 26")


def find_duplicates(lst: list) -> list:
    seen = set()
    duplicates = set()

    for i in lst:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)

    return list(duplicates)


# res = find_duplicates([1, 2, 3, 2, 1, 5, 6])


def is_anagram(s1: str, s2: str) -> bool:
    if (len(s1) != len(s2)):
        return False

    count1 = {}
    count2 = {}

    for ch in s1:
        count1[ch] = count1.get(ch, 0) + 1
    for ch in s2:
        count2[ch] = count2.get(ch, 0) + 1

    return count1 == count2


# res = is_anagram("hello", "world")
# res = is_anagram("listen", "silent")


def sum_of_evens(lst: list):
    return sum(x for x in lst if x % 2 == 0)
    # evens = []
    # sum = 0

    # for l in lst:
    #     if l % 2 == 0:
    #         evens.append(l)

    # for n in evens:
    #     sum += n

    # return sum


# res = sum_of_evens([1, 2, 3, 4,  5, 6, 7, 8, 9, 10])


def fibonacci(n: int):
    if n == 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])

    return fib


# res = fibonacci(5)


def is_palindrome(s: str) -> bool:
    updated_str = s.replace(" ", "").lower()
    reverse_str = updated_str[::-1]

    return updated_str == reverse_str


# res = is_palindrome("Was it a car or a cat I saw")

def remove_duplicates(lst: list) -> list:
    dup = []

    for l in lst:
        if l not in dup:
            dup.append(l)

    return dup


# res = remove_duplicates([1, 2, 2, 5, 5, 4, 2, 3, 1])


def char_count(s: str) -> dict:
    counts = {}
    s = s.replace(" ", "").lower()

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    return counts


# res = char_count("Hello world")

def find_missing_number(nums: list, n: int) -> int:
    missing = None

    for i in range(n+1):

        if i not in nums:
            missing = i

    return missing


# res = find_missing_number([1, 2, 4, 5, 3, 7, 6], 8)

# def two_sum(nums: list, target: int) -> tuple:
#     indices = ()
#     for i in range(len(nums)):

#         if nums[i] != nums[-1] and (nums[i] + nums[i+1]) == target:
#             indices = (nums[i], nums[i+1])

#     return indices if indices else None

def two_sum(nums, target):
    seen = {}  # maps number -> index
    for i, num in enumerate(nums):
        complement = target - num
        print(complement)
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


# res = two_sum([2, 7, 11, 15], 9)


def is_substring(s1: str, s2: str) -> bool:
    return s1.lower() in s2.lower()


# res = is_substring("dog", "catalogue")

def second_largest(lst: list) -> int:
    largest = lst[0]
    for l in lst:
        if l > largest:
            largest = l
    lst.remove(largest)

    secondLg = lst[0]
    for l in lst:
        if l > secondLg:
            secondLg = l

    return secondLg


# res = second_largest([10, 20, 40, 30])


def flatten_list(nestedList: list) -> list:
    flat_list = []

    for lst in nestedList:
        for l in lst:
            flat_list.append(l)

    return flat_list


# res = flatten_list([[1, 2], [3, 4], [5]])


def longest_word(word: str) -> str:
    words_arr = word.split(" ")
    max_len = len(words_arr[0])
    long_word = words_arr[0]

    for word in words_arr:
        if len(word) > max_len:
            max_len = len(word)
            long_word = word
    return long_word


# res = longest_word("I love programming in Python")


def rotate_list(lst: list, steps: int) -> list:
    rotated_list = [lst[-steps:], lst[:-steps]]

    return flatten_list(rotated_list)


res = rotate_list([1, 2, 3, 4, 5], 2)
print(res)
