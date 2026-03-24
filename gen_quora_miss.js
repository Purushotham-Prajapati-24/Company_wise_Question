const fs = require('fs');
const path = require('path');
const raw = JSON.parse(fs.readFileSync(path.join(__dirname, 'quora_raw_data.json'), 'utf8'));

const outDir = path.join(__dirname, 'companyWiseQuestions', 'Quora');
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

const meta = { time_limit_ms: 2000, memory_limit_mb: 512, allowed_languages: ["python", "cpp", "java", "javascript", "c"] };
const bp = (t) => ({
  python: `import sys\nimport json\n\ndef solve(*args):\n    # Implement ${t} here\n    pass\n\nif __name__ == '__main__':\n    data = sys.stdin.read().strip().split('\\n')\n    if not data or data == ['']:\n        sys.exit(0)\n    args = [json.loads(line) for line in data]\n    print(json.dumps(solve(*args)))`,
  cpp: `#include <iostream>\n#include <vector>\n#include <string>\n#include <algorithm>\nusing namespace std;\nint main() {\n    string line;\n    while (getline(cin, line)) {}\n    return 0;\n}`,
  java: `import java.util.*;\nimport java.io.*;\npublic class Main {\n    public static void main(String[] args) throws IOException {\n        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));\n        String line;\n        while ((line = br.readLine()) != null) {}\n    }\n}`,
  javascript: `const fs = require('fs');\nfunction solve(...args) { return 0; }\nconst lines = fs.readFileSync(0, 'utf8').trim().split('\\n');\nif (lines.length) {\n    console.log(JSON.stringify(solve(...lines.map(l => JSON.parse(l)))));\n}\nmodule.exports = solve;`,
  c: `#include <stdio.h>\n#include <stdlib.h>\nint main() { return 0; }`
});

function writeJson(filename, data) {
  const obj = {
    question_text: data.qt,
    difficulty: data.diff,
    marks: 10,
    input_format: data.inf,
    output_format: data.outf,
    constraints: data.cons,
    explanation: data.expl,
    answer: data.ans,
    boilerplate: bp(filename.replace('.json', '').replace(/_/g, ' ')),
    metadata: meta,
    test_cases: data.tc,
    topics: data.topics,
    companyIndex: 26
  };
  fs.writeFileSync(path.join(outDir, filename), JSON.stringify(obj, null, 2));
  console.log('Written:', filename);
}

function qt(id, fallback) {
  return (raw[id] && raw[id].content) ? raw[id].content : fallback;
}

// ─── 1. 525 Contiguous Array ──────────────────────────────────────────────────
writeJson('525_Contiguous_Array.json', {
  qt: qt('525', `<h3>Contiguous Array</h3><p>Given a binary array <code>nums</code>, return <em>the maximum length of a contiguous subarray with an equal number of <code>0</code> and <code>1</code></em>.</p>`),
  diff: 'MEDIUM', inf: 'nums.', outf: 'Int.',
  cons: ['1 <= nums.length <= 10^5', 'nums[i] is either 0 or 1.'],
  expl: 'Transform 0 to -1. Now the problem is to find the longest subarray with sum 0. Use a hash map to store the first occurrence of each prefix sum. If a prefix sum repeats, the subarray between the two occurrences has sum 0.',
  ans: `def findMaxLength(nums):\n    count = 0\n    max_len = 0\n    table = {0: -1}\n    for i, n in enumerate(nums):\n        count += (1 if n == 1 else -1)\n        if count in table: max_len = max(max_len, i - table[count])\n        else: table[count] = i\n    return max_len`,
  tc: [
    { input: `[0,1]`, expected_output: `2`, is_sample: true },
    { input: `[0,1,0]`, expected_output: `2`, is_sample: true },
    { input: `[0,0,0,1,1,1]`, expected_output: `6`, is_sample: false },
    { input: `[1,1,1]`, expected_output: `0`, is_sample: false },
    { input: `[0,0]`, expected_output: `0`, is_sample: false },
    { input: `[0,1,0,1,0,1]`, expected_output: `6`, is_sample: false },
    { input: `[${new Array(50000).fill(0).concat(new Array(50000).fill(1)).join(',')}]`, expected_output: `100000`, is_sample: false },
    { input: `[${new Array(100000).fill(1).join(',')}]`, expected_output: `0`, is_sample: false },
    { input: `[1,0,1,0,1,0,1,0,1]`, expected_output: `8`, is_sample: false },
    { input: `[0,0,0,0,1,1,1,1,0]`, expected_output: `8`, is_sample: false }
  ],
  topics: ['Array', 'Hash Table', 'Prefix Sum']
});

// ─── 2. 437 Path Sum III ──────────────────────────────────────────────────────
writeJson('437_Path_Sum_III.json', {
  qt: qt('437', `<h3>Path Sum III</h3><p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>the number of paths where the sum of the values along the path equals </em><code>targetSum</code>.</p>\n<p>The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).</p>`),
  diff: 'MEDIUM', inf: 'Serialized binary tree, targetSum.', outf: 'Int.',
  cons: ['The number of nodes in the tree is in the range [0, 1000].', '-10^9 <= Node.val <= 10^9', '-1000 <= targetSum <= 1000'],
  expl: 'Use prefix sum on paths from root. At each node, current prefix sum `currSum` is checked against `currSum - targetSum` in a hash map. This tells us how many paths ending at the current node have the target sum.',
  ans: `def pathSum(root, targetSum):\n    self.count = 0\n    preSum = {0: 1}\n    def dfs(node, currSum):\n        if not node: return\n        currSum += node.val\n        self.count += preSum.get(currSum - targetSum, 0)\n        preSum[currSum] = preSum.get(currSum, 0) + 1\n        dfs(node.left, currSum)\n        dfs(node.right, currSum)\n        preSum[currSum] -= 1\n    dfs(root, 0)\n    return self.count`,
  tc: [
    { input: `[10,5,-3,3,2,null,11,3,-2,null,1]\n8`, expected_output: `3`, is_sample: true },
    { input: `[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22`, expected_output: `3`, is_sample: true },
    { input: `[]\n0`, expected_output: `0`, is_sample: false },
    { input: `[1]\n1`, expected_output: `1`, is_sample: false },
    { input: `[1,2]\n3`, expected_output: `1`, is_sample: false },
    { input: `[1,2]\n2`, expected_output: `1`, is_sample: false },
    { input: `[1000000000]\n1000000000`, expected_output: `1`, is_sample: false },
    { input: `[1,1,1,1,1]\n2`, expected_output: `4`, is_sample: false },
    { input: `[1,null,2,null,3,null,4,null,5]\n3`, expected_output: `2`, is_sample: false },
    { input: `[1,-2,-3,1,3,-2,null,-1]\n-1`, expected_output: `4`, is_sample: false }
  ],
  topics: ['Tree', 'Depth-First Search', 'Binary Tree']
});

// ─── 3. 452 Minimum Number of Arrows to Burst Balloons ────────────────────────
writeJson('452_Minimum_Number_of_Arrows_to_Burst_Balloons.json', {
  qt: qt('452', `<h3>Minimum Number of Arrows to Burst Balloons</h3><p>There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code>points</code> where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code> denotes a balloon whose <strong>horizontal diameter</strong> stretches between <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code>. You do not know the exact y-coordinates of the balloons.</p>\n<p>Arrows can be shot up <strong>directly vertically</strong> (in the positive y-direction) from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> is <strong>burst</strong> by an arrow shot at <code>x</code> if <code>x<sub>start</sub> <= x <= x<sub>end</sub></code>. There is <strong>no limit</strong> to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.</p>\n<p>Given the array <code>points</code>, return <em>the minimum number of arrows that must be shot to burst all balloons</em>.</p>`),
  diff: 'MEDIUM', inf: '2D int array points.', outf: 'Int.',
  cons: ['1 <= points.length <= 10^5', 'points[i].length == 2', '-2^31 <= x_start < x_end <= 2^31 - 1'],
  expl: 'Sort balloons by their end coordinates. Shoot an arrow at the end of the first balloon. Skip all balloons that start before or at the arrow position. Repeat for the next un-burst balloon.',
  ans: `def findMinArrowShots(points):\n    if not points: return 0\n    points.sort(key=lambda x: x[1])\n    arrows = 1\n    end = points[0][1]\n    for i in range(1, len(points)):\n        if points[i][0] > end:\n            arrows += 1\n            end = points[i][1]\n    return arrows`,
  tc: [
    { input: `[[10,16],[2,8],[1,6],[7,12]]`, expected_output: `2`, is_sample: true },
    { input: `[[1,2],[3,4],[5,6],[7,8]]`, expected_output: `4`, is_sample: true },
    { input: `[[1,2],[2,3],[3,4],[4,5]]`, expected_output: `2`, is_sample: true },
    { input: `[[1,10],[2,5],[6,8]]`, expected_output: `2`, is_sample: false },
    { input: `[[1,2]]`, expected_output: `1`, is_sample: false },
    { input: `[[-2147483648,2147483647]]`, expected_output: `1`, is_sample: false },
    { input: `[[-10,-5],[-8,-3],[-2,1]]`, expected_output: `2`, is_sample: false },
    { input: `[[1,5],[5,8],[8,12]]`, expected_output: `2`, is_sample: false },
    { input: `[[1,2],[1,2],[1,2]]`, expected_output: `1`, is_sample: false },
    { input: `[${new Array(50000).fill('[1,2]').join(',')},${new Array(50000).fill('[3,4]').join(',')}]`, expected_output: `2`, is_sample: false }
  ],
  topics: ['Array', 'Greedy', 'Sorting']
});

// ─── 4. 390 Elimination Game ──────────────────────────────────────────────────
writeJson('390_Elimination_Game.json', {
  qt: qt('390', `<h3>Elimination Game</h3><p>You have a list of sorted integers from <code>1</code> to <code>n</code>. Starting from left to right, remove the first number and every other number after that until you reach the end of the list.</p>\n<p>Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.</p>\n<p>We keep repeating the steps again, alternating left to right and right to left, until a single number remains.</p>\n<p>Given the integer <code>n</code>, return <em>the last remaining number</em>.</p>`),
  diff: 'MEDIUM', inf: 'Int n.', outf: 'Int.',
  cons: ['1 <= n <= 10^9'],
  expl: 'The head (first element) changes only when shifting from left to right, OR from right to left with an odd count of remaining elements. Track the step size (doubles each turn) and the count (halves each turn).',
  ans: `def lastRemaining(n):\n    head = 1\n    step = 1\n    left = True\n    while n > 1:\n        if left or n % 2 == 1:\n            head += step\n        step *= 2\n        n //= 2\n        left = not left\n    return head`,
  tc: [
    { input: `9`, expected_output: `6`, is_sample: true },
    { input: `1`, expected_output: `1`, is_sample: true },
    { input: `2`, expected_output: `2`, is_sample: false },
    { input: `3`, expected_output: `2`, is_sample: false },
    { input: `4`, expected_output: `2`, is_sample: false },
    { input: `10`, expected_output: `8`, is_sample: false },
    { input: `100`, expected_output: `54`, is_sample: false },
    { input: `1000`, expected_output: `510`, is_sample: false },
    { input: `1000000000`, expected_output: `536870912`, is_sample: false },
    { input: `6`, expected_output: `4`, is_sample: false }
  ],
  topics: ['Math', 'Recursion']
});

// ─── 5. 717 1-bit and 2-bit Characters ────────────────────────────────────────
writeJson('717_1-bit_and_2-bit_Characters.json', {
  qt: qt('717', `<h3>1-bit and 2-bit Characters</h3><p>We have two special characters. The first character can be represented by one bit <code>0</code>. The second character can be represented by two bits (<code>10</code> or <code>11</code>).</p>\n<p>Now given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.</p>`),
  diff: 'EASY', inf: 'Binary array bits.', outf: 'bool.',
  cons: ['1 <= bits.length <= 1000', 'bits[i] is either 0 or 1.'],
  expl: 'Scan the array from left to right. If `bits[i] == 1`, jump two steps (it is a 2-bit character). If `bits[i] == 0`, jump one step (it is a 1-bit character). At the end, if we land exactly at `n-1`, the last character must have been a single 0.',
  ans: `def isOneBitCharacter(bits):\n    i = 0\n    n = len(bits)\n    while i < n - 1:\n        if bits[i] == 1: i += 2\n        else: i += 1\n    return i == n - 1`,
  tc: [
    { input: `[1,0,0]`, expected_output: `true`, is_sample: true },
    { input: `[1,1,1,0]`, expected_output: `false`, is_sample: true },
    { input: `[0]`, expected_output: `true`, is_sample: false },
    { input: `[1,1,0]`, expected_output: `true`, is_sample: false },
    { input: `[1,0,1,0]`, expected_output: `false`, is_sample: false },
    { input: `[1,1,1,1,0]`, expected_output: `true`, is_sample: false },
    { input: `[1,0,1,1,1,1,0]`, expected_output: `false`, is_sample: false },
    { input: `[${new Array(500).fill('1,1').join(',')},0]`, expected_output: `true`, is_sample: false },
    { input: `[${new Array(500).fill('1,1').join(',')},1,0]`, expected_output: `false`, is_sample: false },
    { input: `[0,0,0,0,0]`, expected_output: `true`, is_sample: false }
  ],
  topics: ['Array']
});

console.log('All 5 Quora missing questions generated.');
