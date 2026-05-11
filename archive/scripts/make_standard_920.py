import json
import os

def generate_json():
    problem_id = 920
    title = "Number of Music Playlists"
    difficulty = "HARD"
    marks = 10

    html_description = """<h3>920. Number of Music Playlists</h3>
<p>Your music player has <code>n</code> different songs. You want to listen to <code>goal</code> songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:</p>

<ul>
    <li>Every song is played <strong>at least once</strong>.</li>
    <li>A song can only be played again only if <strong>at least</strong> <code>k</code> other songs have been played.</li>
</ul>

<p>Given <code>n</code>, <code>goal</code>, and <code>k</code>, return <em>the number of possible playlists that you can create</em>. Since the answer can be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3, goal = 3, k = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2, goal = 3, k = 0
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> n = 2, goal = 3, k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
    <li><code>0 &lt;= k &lt; n &lt;= goal &lt;= 100</code></li>
</ul>"""

    input_format = "Three integers n, goal, and k separated by spaces or on new lines."
    output_format = "An integer representing the number of valid playlists modulo 10^9 + 7."

    constraints = [
        "0 <= k < n <= goal <= 100"
    ]

    explanation = """This is a dynamic programming problem. Let `dp[i][j]` be the number of playlists of length `i` using exactly `j` unique songs.
To form a playlist of length `i` with `j` unique songs:
1. We can append a new song that hasn't been used yet. There are `n - (j - 1)` choices for this.
   `dp[i][j] += dp[i-1][j-1] * (n - (j - 1))`
2. We can append a song that has already been used. This is only possible if the number of unique songs `j` is greater than `k`. There are `j - k` choices for this.
   `dp[i][j] += dp[i-1][j] * (j - k)`
Base case: `dp[0][0] = 1`.
Result: `dp[goal][n]`."""

    answer = """class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # Add a new song
                dp[i][j] = (dp[i-1][j-1] * (n - j + 1)) % MOD
                # Add an old song
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD
        return dp[goal][n]"""

    boilerplate = {
        "python": """import sys

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # User logic here
        return 0

if __name__ == '__main__':
    raw = sys.stdin.read().split()
    if len(raw) >= 3:
        n = int(raw[0])
        goal = int(raw[1])
        k = int(raw[2])
        sol = Solution()
        print(sol.numMusicPlaylists(n, goal, k))""",
        "cpp": """#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numMusicPlaylists(int n, int goal, int k) {
        // User logic here
        return 0;
    }
};

int main() {
    int n, goal, k;
    if (cin >> n >> goal >> k) {
        Solution sol;
        cout << sol.numMusicPlaylists(n, goal, k) << endl;
    }
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public int numMusicPlaylists(int n, int goal, int k) {
        // User logic here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            int goal = sc.nextInt();
            int k = sc.nextInt();
            Solution sol = new Solution();
            System.out.println(sol.numMusicPlaylists(n, goal, k));
        }
    }
}""",
        "javascript": """/**
 * @param {number} n
 * @param {number} goal
 * @param {number} k
 * @return {number}
 */
var numMusicPlaylists = function(n, goal, k) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\\s+/);
if (input.length >= 3) {
    console.log(numMusicPlaylists(parseInt(input[0]), parseInt(input[1]), parseInt(input[2])));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int numMusicPlaylists(int n, int goal, int k) {
    // User logic here
    return 0;
}

int main() {
    int n, goal, k;
    if (scanf("%d %d %d", &n, &goal, &k) == 3) {
        printf("%d\\n", numMusicPlaylists(n, goal, k));
    }
    return 0;
}"""
    }

    def solve(n, goal, k):
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                dp[i][j] = (dp[i-1][j-1] * (n - j + 1)) % MOD
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD
        return dp[goal][n]

    test_cases_data = [
        (3, 3, 1),
        (2, 3, 0),
        (2, 3, 1),
        (4, 5, 2),
        (5, 5, 3),
        (10, 20, 5),
        (100, 100, 50),
        (2, 2, 0),
        (10, 15, 2),
        (50, 100, 25)
    ]

    test_cases = []
    for i, (n, goal, k) in enumerate(test_cases_data):
        inp = f"{n} {goal} {k}"
        out = str(solve(n, goal, k))
        is_sample = i < 3
        test_cases.append({"input": inp, "expected_output": out, "is_sample": is_sample})

    data = {
        "question_id": problem_id,
        "question_text": html_description,
        "difficulty": difficulty,
        "marks": marks,
        "input_format": input_format,
        "output_format": output_format,
        "constraints": constraints,
        "explanation": explanation,
        "answer": answer,
        "boilerplate": boilerplate,
        "test_cases": test_cases,
        "metadata": {"time_limit_ms": 1000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["Math", "Dynamic Programming", "Combinatorics"],
        "companyIndex": 0
    }

    output_path = f"801-1000/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
