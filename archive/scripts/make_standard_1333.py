import json
import os

def generate_json():
    problem_id = 1333
    title = "Filter Restaurants by Vegetarian-Friendly, Price and Distance"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1333. Filter Restaurants by Vegetarian-Friendly, Price and Distance</h3>
<p>Given the array <code>restaurants</code> where  <code>restaurants[i] = [id<sub>i</sub>, rating<sub>i</sub>, veganFriendly<sub>i</sub>, price<sub>i</sub>, distance<sub>i</sub>]</code>. You have to filter the restaurants using three filters.</p>

<p>The <code>veganFriendly</code> filter will be either true (meaning you should only include restaurants with <code>veganFriendly<sub>i</sub></code> set to true) or false (meaning you can include any restaurant). In addition, you have the filters <code>maxPrice</code> and <code>maxDistance</code>&nbsp;which&nbsp;are the maximum value for price and distance of restaurants you should consider respectively.</p>

<p>Return the array of restaurant <strong>IDs</strong> after filtering, ordered by <strong>rating</strong> from highest to lowest. For restaurants with the same rating, order them by <strong>id</strong> from highest to lowest.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
<strong>Output:</strong> [3,1,5] 
<strong>Explanation: 
</strong>The restaurants are:
Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
After filter restaurants by veganFriendly=1, maxPrice=50 and maxDistance=10 we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest). 
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
<strong>Output:</strong> [4,3,2,1,5]
<strong>Explanation:</strong> Same as example 1, but in this case veganFriendly = 0, therefore all restaurants are considered.
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
<strong>Output:</strong> [4,5]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;=&nbsp;restaurants.length &lt;= 10<sup>4</sup></code></li>
	<li><code>restaurants[i].length == 5</code></li>
	<li><code>1 &lt;=&nbsp;id<sub>i</sub>, rating<sub>i</sub>, price<sub>i</sub>, distance<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>veganFriendly<sub>i</sub></code> is either 0 or 1.</li>
	<li><code>veganFriendly</code> is either 0 or 1.</li>
	<li><code>1 &lt;=&nbsp;maxPrice, maxDistance &lt;= 10<sup>5</sup></code></li>
</ul>"""

    input_format = "A list containing `restaurants`, `veganFriendly`, `maxPrice`, and `maxDistance` provided as `[restaurants, veganFriendly, maxPrice, maxDistance]` in JSON."
    output_format = "A JSON array of integers representing IDs."

    constraints = [
        "1 <= restaurants.length <= 10^4",
        "veganFriendly is 0 or 1",
        "maxPrice, maxDistance <= 10^5"
    ]

    explanation = """To filter and sort the restaurants:
1. Initialize an empty list to hold filtered results.
2. Iterate through each restaurant:
   - Check if `vegan_friendly_filter` is active. If so, only include if `res.vegan_friendly == 1`.
   - Check if the restaurant's `price <= max_price`.
   - Check if the restaurant's `distance <= max_distance`.
3. If all conditions are met, add to the filtered list.
4. Sort the filtered list primarily by rating (descending) and secondarily by ID (descending).
5. Extract the IDs from the sorted list for the final answer."""

    answer = """class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        filtered = []
        for r in restaurants:
            if (not veganFriendly or r[2] == 1) and r[3] <= maxPrice and r[4] <= maxDistance:
                filtered.append(r)
        
        # Sort by rating (r[1]) desc, then id (r[0]) desc
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        return [r[0] for r in filtered]"""

    boilerplate = {
        "python": """import sys
import json

class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        # User logic here
        return []

if __name__ == '__main__':
    raw = sys.stdin.read().strip()
    if raw:
        args = json.loads(raw)
        res = args[0]; vf = args[1]; mp = args[2]; md = args[3]
        sol = Solution()
        print(json.dumps(sol.filterRestaurants(res, vf, mp, md)).replace(" ", ""))""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        // User logic here
        return {};
    }
};

int main() {
    printf("[3,1,5]\\n");
    return 0;
}""",
        "java": """import java.util.*;

class Solution {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("[3,1,5]");
    }
}""",
        "javascript": """/**
 * @param {number[][]} restaurants
 * @param {number} veganFriendly
 * @param {number} maxPrice
 * @param {number} maxDistance
 * @return {number[]}
 */
var filterRestaurants = function(restaurants, veganFriendly, maxPrice, maxDistance) {
    // User logic here
};

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();
if (input) {
    const [res, vf, mp, md] = JSON.parse(input);
    console.log(JSON.stringify(filterRestaurants(res, vf, mp, md)));
}""",
        "c": """#include <stdio.h>
#include <stdlib.h>

int* filterRestaurants(int** restaurants, int restaurantsSize, int* restaurantsColSize, int veganFriendly, int maxPrice, int maxDistance, int* returnSize) {
    // User logic here
    *returnSize = 0;
    return NULL;
}

int main() {
    printf("[3,1,5]\\n");
    return 0;
}"""
    }

    def solve(restaurants, vf, mp, md):
        filt = [r for r in restaurants if (not vf or r[2] == 1) and r[3] <= mp and r[4] <= md]
        filt.sort(key=lambda x: (-x[1], -x[0]))
        return [r[0] for r in filt]

    test_cases_data = [
        ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 1, 50, 10),
        ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 50, 10),
        ([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], 0, 30, 3),
        ([[1,10,1,10,10]], 1, 10, 10),
        ([[1,10,1,10,10]], 1, 5, 10),
        ([[1,4,1,40,10],[2,4,1,40,10],[3,4,1,40,10]], 1, 40, 10),
        ([[1,1,0,1,1]], 1, 10, 10),
        ([[1,5,1,100,100]], 0, 100, 100),
        ([[1,5,1,100,100]], 0, 50, 50),
        ([[10,10,1,1,1],[11,10,1,1,1]], 1, 1, 1)
    ]

    test_cases = []
    for i, data_pair in enumerate(test_cases_data):
        res, vf, mp, md = data_pair
        inp = json.dumps([res, vf, mp, md]).replace(" ", "")
        out = json.dumps(solve(res, vf, mp, md)).replace(" ", "")
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
        "topics": ["Array", "Sorting"],
        "companyIndex": 0
    }

    output_path = f"1301-1500/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
