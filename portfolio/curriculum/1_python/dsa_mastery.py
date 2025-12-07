"""
DSA MASTERY: Common Interview Algorithms
========================================
This file contains the most popular Data Structure & Algorithm problems
asked in QA / SDET Interviews.

CONCEPTS COVERED:
1. Strings & Slicing
2. Dictionaries (Hash Maps) for Counting
3. Lists & Two Pointers
4. Basic Math Logic
"""

# ==========================================
# 1. REVERSE A STRING (3 Ways)
# ==========================================
def reverse_string_v1(text):
    """The Pythonic Way (Slicing)"""
    return text[::-1]

def reverse_string_v2(text):
    """The Manual Way (Loop) - Interviewers ask for this"""
    result = ""
    for char in text:
        result = char + result
    return result

# ==========================================
# 2. PALINDROME CHECK
# ==========================================
def is_palindrome(text):
    """Checks if text reads the same forward and backward (e.g., 'madam')"""
    clean_text = text.lower()
    return clean_text == clean_text[::-1]

# ==========================================
# 3. FIZZBUZZ (The Classic)
# ==========================================
def fizz_buzz(n):
    """
    Print numbers 1 to n.
    If multiple of 3 -> Fizz.
    If multiple of 5 -> Buzz.
    If both -> FizzBuzz.
    """
    print(f"\n--- FIZZBUZZ (n={n}) ---")
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0: output += "Fizz"
        if i % 5 == 0: output += "Buzz"
        print(output if output else i)

# ==========================================
# 4. CHARACTER FREQUENCY (Hash Map)
# ==========================================
def count_chars(text):
    """
    Count how many times each character appears.
    Input: "banana"
    Output: {'b': 1, 'a': 3, 'n': 2}
    """
    freq_map = {}
    for char in text:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1
    return freq_map

# ==========================================
# 5. TWO SUM (The Google Question)
# ==========================================
def two_sum(nums, target):
    """
    Find two numbers in the list that add up to target.
    Returns their INDICES.
    Time Complexity: O(n) using a Dictionary.
    """
    seen = {}  # val : index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# ==========================================
# 6. FIND MAX NUMBER (Logic)
# ==========================================
def find_max_manual(nums):
    """Find largest number without using max()"""
    if not nums: return None
    current_max = nums[0]
    for n in nums:
        if n > current_max:
            current_max = n
    return current_max


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print(f"1. Reverse 'Python': {reverse_string_v1('Python')}")
    print(f"2. Is 'Racecar' palindrome? {is_palindrome('Racecar')}")
    
    fizz_buzz(15)
    
    print(f"\n4. Char Count 'mississippi': {count_chars('mississippi')}")
    
    nums = [2, 7, 11, 15]
    print(f"\n5. Two Sum ({nums}, target=9): Indices {two_sum(nums, 9)}")
    
    print(f"\n6. Max of [10, 50, 20]: {find_max_manual([10, 50, 20])}")
