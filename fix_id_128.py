import json
import os

def generate_test_cases():
    def longestConsecutive(nums):
        if not nums: return 0
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                longest = max(longest, curr_streak)
        return longest

    cases = [
        {"input": "[100,4,200,1,3,2]", "expected_output": "4", "is_sample": True},
        {"input": "[0,3,7,2,5,8,4,6,0,1]", "expected_output": "9", "is_sample": True},
        {"input": "[]", "expected_output": "0", "is_sample": False},
        {"input": "[1]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3]", "expected_output": "3", "is_sample": False},
        {"input": "[1,3,5,7,9]", "expected_output": "1", "is_sample": False},
        {"input": "[1,2,3,10,11,12,13]", "expected_output": "4", "is_sample": False},
    ]

    # Case 8: 1000 nodes, sequential
    cases.append({"input": json.dumps(list(range(1, 1001))), "expected_output": "1000", "is_sample": False})

    # Case 9: 10000 nodes, reverse
    cases.append({"input": json.dumps(list(range(10000, 0, -1))), "expected_output": "10000", "is_sample": False})

    # Case 10: 100000 nodes (Peak Constraint)
    cases.append({"input": json.dumps(list(range(1, 100001))), "expected_output": "100000", "is_sample": False})

    return cases

target_path = "d:/College Projects/MNC_based/companyWiseQuestions/Bloomberg/128_Longest_Consecutive_Sequence.json"

if not os.path.exists(target_path):
    print(f"Error: {target_path} not found.")
else:
    with open(target_path, "r", encoding="utf-8") as f: d = json.load(f)

    d["question_text"] = "<h3>128 Longest Consecutive Sequence</h3><p>Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest consecutive elements sequence.</em></p><p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time.</p>"
    d["difficulty"] = "MEDIUM"
    d["marks"] = 15
    d["input_format"] = "An integer array nums."
    d["output_format"] = "Integer representing the length of the longest consecutive sequence."
    
    d["metadata"] = {
        "time_limit_ms": 1000,
        "memory_limit_mb": 256,
        "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
    }

    d["answer"] = """class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                longest = max(longest, curr_streak)
        return longest"""

    d["boilerplate"]["python"] = """import sys, json

def solve(nums):
    if not nums: return 0
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_streak = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_streak += 1
            longest = max(longest, curr_streak)
    return longest

if __name__ == '__main__':
    line = sys.stdin.read().strip()
    if line:
        try:
            nums = json.loads(line)
            print(solve(nums))
        except:
            print(0)
    else:
        print(0)"""

    d["test_cases"] = generate_test_cases()
    
    with open(target_path, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4)
    print("Standardized ID 128 in Bloomberg")
