import json
import os
import heapq

def generate_json():
    problem_id = 355
    title = "Design Twitter"
    difficulty = "Medium"
    marks = 10

    html_description = """<h3>355. Design Twitter</h3>
<p>Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user's news feed.</p>
<p>Implement the <code>Twitter</code> class:</p>
<ul>
\t<li><code>Twitter()</code> Initializes your twitter object.</li>
\t<li><code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.</li>
\t<li><code>List&lt;Integer&gt; getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themselves. Tweets must be ordered from most recent to least recent.</li>
\t<li><code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> starts following the user with ID <code>followeeId</code>.</li>
\t<li><code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> starts unfollowing the user with ID <code>followeeId</code>.</li>
</ul>
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
<strong>Output</strong>
[null,null,[5],null,null,[6,5],null,[5]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
\t<li><code>1 &lt;= userId, followerId, followeeId &lt;= 500</code></li>
\t<li><code>0 &lt;= tweetId &lt;= 10<sup>4</sup></code></li>
\t<li>All the tweets have <strong>unique</strong> IDs.</li>
\t<li>At most <code>3 * 10<sup>4</sup></code> calls will be made.</li>
</ul>"""

    input_format = (
        "Each line is one of:\n"
        "  `post userId tweetId`\n"
        "  `feed userId`\n"
        "  `follow followerId followeeId`\n"
        "  `unfollow followerId followeeId`\n"
        "Output only for `feed` operations."
    )
    output_format = "For each `feed` operation: comma-separated tweetIds in `[id1,id2,...]` format (up to 10, most recent first)."

    constraints = [
        "1 <= userId, followerId, followeeId <= 500",
        "0 <= tweetId <= 10^4",
        "All tweet IDs are unique",
        "At most 3 * 10^4 calls"
    ]

    explanation = """Use a **heap merge** for getNewsFeed.

### Data Structures:
- `tweets[userId]`: list of `(timestamp, tweetId)` in reverse-chronological order.
- `following[userId]`: set of users this user follows.

### getNewsFeed(userId):
1. Collect the latest tweet from each followed user (and self) into a max-heap.
2. Pop up to 10 tweets, refilling from each user's tweet list.

### Complexity:
- `postTweet`: O(1)
- `getNewsFeed`: O(F log F + 10 log F) where F = number of followees
- `follow/unfollow`: O(1)"""

    answer = """import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((-self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            tweets = self.tweets[u]
            if tweets:
                idx = len(tweets) - 1
                t, tid = tweets[idx]
                heapq.heappush(heap, (t, tid, u, idx - 1))
        res = []
        while heap and len(res) < 10:
            t, tid, u, idx = heapq.heappop(heap)
            res.append(tid)
            if idx >= 0:
                nt, ntid = self.tweets[u][idx]
                heapq.heappush(heap, (nt, ntid, u, idx - 1))
        return res

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)"""

    boilerplate = {
        "python": "import sys\nimport re\nfrom collections import defaultdict\nimport heapq\n\nclass Twitter:\n    def __init__(self):\n        # User logic here\n        pass\n    def postTweet(self, userId, tweetId):\n        # User logic here\n        pass\n    def getNewsFeed(self, userId):\n        # User logic here\n        return []\n    def follow(self, followerId, followeeId):\n        # User logic here\n        pass\n    def unfollow(self, followerId, followeeId):\n        # User logic here\n        pass\n\nif __name__ == '__main__':\n    obj = Twitter()\n    for line in sys.stdin.read().splitlines():\n        parts = re.findall(r'\\w+', line)\n        if not parts: continue\n        cmd = parts[0]\n        ids = [int(x) for x in parts[1:]]\n        if cmd == 'post': obj.postTweet(ids[0], ids[1])\n        elif cmd == 'feed': print('[' + ','.join(map(str, obj.getNewsFeed(ids[0]))) + ']')\n        elif cmd == 'follow': obj.follow(ids[0], ids[1])\n        elif cmd == 'unfollow': obj.unfollow(ids[0], ids[1])",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\n#include <regex>\nusing namespace std;\n\nclass Twitter {\npublic:\n    Twitter() {}\n    void postTweet(int userId, int tweetId) {}\n    vector<int> getNewsFeed(int userId) { return {}; }\n    void follow(int followerId, int followeeId) {}\n    void unfollow(int followerId, int followeeId) {}\n};\n\nint main() {\n    Twitter obj;\n    string line, cmd;\n    while (getline(cin, line)) {\n        stringstream ss(line);\n        if (!(ss >> cmd)) continue;\n        int id1, id2;\n        if (cmd == \"post\") { ss >> id1 >> id2; obj.postTweet(id1, id2); }\n        else if (cmd == \"feed\") {\n            ss >> id1;\n            vector<int> f = obj.getNewsFeed(id1);\n            cout << '[';\n            for (int i = 0; i < (int)f.size(); ++i) cout << f[i] << (i == (int)f.size() - 1 ? \"\" : \",\");\n            cout << \"]\\n\";\n        } else if (cmd == \"follow\") { ss >> id1 >> id2; obj.follow(id1, id2); }\n        else if (cmd == \"unfollow\") { ss >> id1 >> id2; obj.unfollow(id1, id2); }\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.util.regex.*;\n\npublic class Solution {\n    static class Twitter {\n        public Twitter() {}\n        public void postTweet(int userId, int tweetId) {}\n        public List<Integer> getNewsFeed(int userId) { return new ArrayList<>(); }\n        public void follow(int followerId, int followeeId) {}\n        public void unfollow(int followerId, int followeeId) {}\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Twitter obj = new Twitter();\n        while (sc.hasNextLine()) {\n            String line = sc.nextLine();\n            String[] p = line.trim().split(\"\\\\s+\");\n            if (p.length == 0 || p[0].isEmpty()) continue;\n            if (p[0].equals(\"post\")) obj.postTweet(Integer.parseInt(p[1]), Integer.parseInt(p[2]));\n            else if (p[0].equals(\"feed\")) {\n                List<Integer> f = obj.getNewsFeed(Integer.parseInt(p[1]));\n                System.out.print(\"[\");\n                for (int i = 0; i < f.size(); i++) System.out.print(f.get(i) + (i == f.size() - 1 ? \"\" : \",\"));\n                System.out.println(\"]\");\n            } else if (p[0].equals(\"follow\")) obj.follow(Integer.parseInt(p[1]), Integer.parseInt(p[2]));\n            else if (p[0].equals(\"unfollow\")) obj.unfollow(Integer.parseInt(p[1]), Integer.parseInt(p[2]));\n        }\n    }\n}",
        "javascript": "\"use strict\";\nconst fs = require('fs');\nclass Twitter {\n    constructor() {}\n    postTweet(userId, tweetId) {}\n    getNewsFeed(userId) { return []; }\n    follow(followerId, followeeId) {}\n    unfollow(followerId, followeeId) {}\n}\nfunction main() {\n    const obj = new Twitter();\n    const lines = fs.readFileSync(0, 'utf8').split('\\n');\n    for (let line of lines) {\n        const p = line.trim().split(/\\s+/);\n        if (!p[0]) continue;\n        if (p[0] === 'post') obj.postTweet(Number(p[1]), Number(p[2]));\n        else if (p[0] === 'feed') console.log('[' + obj.getNewsFeed(Number(p[1])).join(',') + ']');\n        else if (p[0] === 'follow') obj.follow(Number(p[1]), Number(p[2]));\n        else if (p[0] === 'unfollow') obj.unfollow(Number(p[1]), Number(p[2]));\n    }\n}\nmain();",
        "c": "#include <stdio.h>\n#include <string.h>\n#include <stdlib.h>\n\nvoid postTweet(int userId, int tweetId) {}\nvoid getNewsFeed(int userId) { printf(\"[]\\n\"); }\nvoid follow(int followerId, int followeeId) {}\nvoid unfollow(int followerId, int followeeId) {}\n\nint main() {\n    char cmd[20]; int id1, id2;\n    while (scanf(\"%s\", cmd) != EOF) {\n        if (!strcmp(cmd, \"post\")) { scanf(\"%d %d\", &id1, &id2); postTweet(id1, id2); }\n        else if (!strcmp(cmd, \"feed\")) { scanf(\"%d\", &id1); getNewsFeed(id1); }\n        else if (!strcmp(cmd, \"follow\")) { scanf(\"%d %d\", &id1, &id2); follow(id1, id2); }\n        else if (!strcmp(cmd, \"unfollow\")) { scanf(\"%d %d\", &id1, &id2); unfollow(id1, id2); }\n    }\n    return 0;\n}"
    }


    test_cases = [
        # 2 sample cases
        {
            "input": "post 1 5\nfeed 1\nfollow 1 2\npost 2 6\nfeed 1\nunfollow 1 2\nfeed 1",
            "expected_output": "[5]\n[6,5]\n[5]",
            "is_sample": True
        },
        {
            "input": "post 1 1\npost 2 2\npost 3 3\nfollow 1 2\nfollow 1 3\nfeed 1",
            "expected_output": "[3,2,1]",
            "is_sample": True
        },
        # 5 diverse cases
        {
            "input": "feed 1",
            "expected_output": "[]",
            "is_sample": False
        },
        {
            "input": "post 1 10\npost 1 20\npost 1 30\nfeed 1",
            "expected_output": "[30,20,10]",
            "is_sample": False
        },
        {
            "input": "post 1 1\nfollow 1 1\nfeed 1",
            "expected_output": "[1]",
            "is_sample": False
        },
        {
            "input": "follow 1 2\npost 2 99\nfeed 1\nunfollow 1 2\nfeed 1",
            "expected_output": "[99]\n[]",
            "is_sample": False
        },
        {
            "input": "post 1 1\npost 1 2\npost 1 3\npost 1 4\npost 1 5\npost 1 6\npost 1 7\npost 1 8\npost 1 9\npost 1 10\npost 1 11\nfeed 1",
            "expected_output": "[11,10,9,8,7,6,5,4,3,2]",
            "is_sample": False
        },
        # 3 stress cases
        {
            "input": "\n".join(f"post 1 {i}" for i in range(1, 201)) + "\nfeed 1",
            "expected_output": "[200,199,198,197,196,195,194,193,192,191]",
            "is_sample": False
        },
        {
            "input": (
                "\n".join(f"post {u} {u}" for u in range(1, 101)) +
                "\n" + "\n".join(f"follow 1 {u}" for u in range(2, 101)) +
                "\nfeed 1"
            ),
            "expected_output": "[100,99,98,97,96,95,94,93,92,91]",
            "is_sample": False
        },
        {
            "input": (
                "\n".join(f"post 1 {i}" for i in range(1, 51)) +
                "\n" + "\n".join(f"post 2 {i}" for i in range(51, 101)) +
                "\nfollow 1 2\nfeed 1"
            ),
            "expected_output": "[100,99,98,97,96,95,94,93,92,91]",
            "is_sample": False
        },
    ]

    data = {
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
        "metadata": {
            "time_limit_ms": 2000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Hash Table", "Linked List", "Design", "Heap (Priority Queue)"],
        "companyIndex": 1
    }

    output_path = "301-500/355_Design_Twitter.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
