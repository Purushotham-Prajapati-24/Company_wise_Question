import json

def minimumTotal(triangle):
    if not triangle: return 0
    dp = triangle[-1][:]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    return dp[0]

specs = [
    {"arr": [[2],[3,4],[6,5,7],[4,1,8,3]], "is_sample": True},
    {"arr": [[-10]], "is_sample": True},
    {"arr": [[0], [0,1], [0,1,2]], "is_sample": False},
    {"arr": [[1], [2,3], [4,5,6], [7,8,9,10]], "is_sample": False},
    {"arr": [[10]], "is_sample": False},
    {"arr": [[-1], [-2,-3], [-4,-5,-6]], "is_sample": False},
    {"arr": [[1], [1,1], [1,1,1], [1,1,1,1], [1,1,1,1,1]], "is_sample": False},
    {"arr": [[5], [2,8], [1,9,3]], "is_sample": False},
    {"arr": [[v for v in range(i+1)] for i in range(20)], "is_sample": False},
    {"arr": [[1]*(i+1) for i in range(200)], "is_sample": False}
]

final_tcs = []
for spec in specs:
    arr = spec["arr"]
    result = minimumTotal(arr)
    final_tcs.append({
        "input": json.dumps(arr).replace(" ", ""),
        "expected_output": str(result),
        "is_sample": spec["is_sample"]
    })

file_path = 'd:/College Projects/MNC_based/companyWiseQuestions/Visa/120_Triangle.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data['test_cases'] = final_tcs

if "<h3>120 " in data['question_text']:
     data['question_text'] = data['question_text'].replace("<h3>120 ", "<h3>120. ")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updated 120 in Visa")
