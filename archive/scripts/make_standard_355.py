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
        "python": (
            "import sys\n"
            "import heapq\n"
            "from collections import defaultdict\n\n"
            "class Twitter:\n"
            "    def __init__(self):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def postTweet(self, userId, tweetId):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def getNewsFeed(self, userId):\n"
            "        # User logic here\n"
            "        return []\n\n"
            "    def follow(self, followerId, followeeId):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "    def unfollow(self, followerId, followeeId):\n"
            "        # User logic here\n"
            "        pass\n\n"
            "if __name__ == '__main__':\n"
            "    lines = sys.stdin.read().splitlines()\n"
            "    obj = Twitter()\n"
            "    for line in lines:\n"
            "        parts = line.split()\n"
            "        if not parts: continue\n"
            "        if parts[0] == 'post' and len(parts) >= 3:\n"
            "            obj.postTweet(int(parts[1]), int(parts[2]))\n"
            "        elif parts[0] == 'feed' and len(parts) >= 2:\n"
            "            feed = obj.getNewsFeed(int(parts[1]))\n"
            "            print('[' + ','.join(map(str, feed)) + ']')\n"
            "        elif parts[0] == 'follow' and len(parts) >= 3:\n"
            "            obj.follow(int(parts[1]), int(parts[2]))\n"
            "        elif parts[0] == 'unfollow' and len(parts) >= 3:\n"
            "            obj.unfollow(int(parts[1]), int(parts[2]))"
        ),
        "cpp": (
            "#include <iostream>\n"
            "#include <vector>\n"
            "#include <queue>\n"
            "#include <unordered_map>\n"
            "#include <unordered_set>\n"
            "#include <string>\n"
            "using namespace std;\n\n"
            "class Twitter {\n"
            "public:\n"
            "    Twitter() {\n"
            "        // User logic here\n"
            "    }\n"
            "    void postTweet(int userId, int tweetId) {\n"
            "        // User logic here\n"
            "    }\n"
            "    vector<int> getNewsFeed(int userId) {\n"
            "        // User logic here\n"
            "        return {};\n"
            "    }\n"
            "    void follow(int followerId, int followeeId) {\n"
            "        // User logic here\n"
            "    }\n"
            "    void unfollow(int followerId, int followeeId) {\n"
            "        // User logic here\n"
            "    }\n"
            "};\n\n"
            "int main() {\n"
            "    Twitter obj;\n"
            "    string op;\n"
            "    while (cin >> op) {\n"
            "        if (op == \"post\") {\n"
            "            int u, t; cin >> u >> t;\n"
            "            obj.postTweet(u, t);\n"
            "        } else if (op == \"feed\") {\n"
            "            int u; cin >> u;\n"
            "            auto feed = obj.getNewsFeed(u);\n"
            "            cout << '[';\n"
            "            for (size_t i = 0; i < feed.size(); i++) {\n"
            "                cout << feed[i];\n"
            "                if (i + 1 < feed.size()) cout << ',';\n"
            "            }\n"
            "            cout << \"]\\n\";\n"
            "        } else if (op == \"follow\") {\n"
            "            int a, b; cin >> a >> b;\n"
            "            obj.follow(a, b);\n"
            "        } else if (op == \"unfollow\") {\n"
            "            int a, b; cin >> a >> b;\n"
            "            obj.unfollow(a, b);\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        ),
        "java": (
            "import java.util.*;\n\n"
            "public class Main {\n"
            "    static class Twitter {\n"
            "        public Twitter() { /* User logic here */ }\n"
            "        public void postTweet(int userId, int tweetId) { /* User logic here */ }\n"
            "        public List<Integer> getNewsFeed(int userId) { return new ArrayList<>(); /* User logic here */ }\n"
            "        public void follow(int followerId, int followeeId) { /* User logic here */ }\n"
            "        public void unfollow(int followerId, int followeeId) { /* User logic here */ }\n"
            "    }\n\n"
            "    public static void main(String[] args) {\n"
            "        Scanner sc = new Scanner(System.in);\n"
            "        Twitter obj = new Twitter();\n"
            "        while (sc.hasNext()) {\n"
            "            String op = sc.next();\n"
            "            if (op.equals(\"post\") && sc.hasNextInt()) {\n"
            "                int u = sc.nextInt();\n"
            "                if (sc.hasNextInt()) obj.postTweet(u, sc.nextInt());\n"
            "            } else if (op.equals(\"feed\") && sc.hasNextInt()) {\n"
            "                List<Integer> feed = obj.getNewsFeed(sc.nextInt());\n"
            "                StringBuilder sb = new StringBuilder(\"[\");\n"
            "                for (int i = 0; i < feed.size(); i++) {\n"
            "                    sb.append(feed.get(i));\n"
            "                    if (i + 1 < feed.size()) sb.append(',');\n"
            "                }\n"
            "                sb.append(']');\n"
            "                System.out.println(sb);\n"
            "            } else if (op.equals(\"follow\") && sc.hasNextInt()) {\n"
            "                int a = sc.nextInt();\n"
            "                if (sc.hasNextInt()) obj.follow(a, sc.nextInt());\n"
            "            } else if (op.equals(\"unfollow\") && sc.hasNextInt()) {\n"
            "                int a = sc.nextInt();\n"
            "                if (sc.hasNextInt()) obj.unfollow(a, sc.nextInt());\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}"
        ),
        "javascript": (
            "const fs = require('fs');\n\n"
            "class Twitter {\n"
            "    constructor() {\n"
            "        // User logic here\n"
            "    }\n"
            "    postTweet(userId, tweetId) { /* User logic here */ }\n"
            "    getNewsFeed(userId) { return []; /* User logic here */ }\n"
            "    follow(followerId, followeeId) { /* User logic here */ }\n"
            "    unfollow(followerId, followeeId) { /* User logic here */ }\n"
            "}\n\n"
            "function main() {\n"
            "    const input = fs.readFileSync(0, 'utf8').split(/\\s+/);\n"
            "    let idx = 0;\n"
            "    const obj = new Twitter();\n"
            "    while (idx < input.length) {\n"
            "        if (input[idx] === '') { idx++; continue; }\n"
            "        if (input[idx] === 'post') {\n"
            "            idx++;\n"
            "            if (idx + 1 < input.length) obj.postTweet(parseInt(input[idx]), parseInt(input[idx+1]));\n"
            "            idx++;\n"
            "        } else if (input[idx] === 'feed') {\n"
            "            idx++;\n"
            "            if (idx < input.length) {\n"
            "                const f = obj.getNewsFeed(parseInt(input[idx]));\n"
            "                console.log('[' + f.join(',') + ']');\n"
            "            }\n"
            "        } else if (input[idx] === 'follow') {\n"
            "            idx++;\n"
            "            if (idx + 1 < input.length) obj.follow(parseInt(input[idx]), parseInt(input[idx+1]));\n"
            "            idx++;\n"
            "        } else if (input[idx] === 'unfollow') {\n"
            "            idx++;\n"
            "            if (idx + 1 < input.length) obj.unfollow(parseInt(input[idx]), parseInt(input[idx+1]));\n"
            "            idx++;\n"
            "        }\n"
            "        idx++;\n"
            "    }\n"
            "}\n"
            "main();"
        ),
        "c": (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "#include <stdlib.h>\n\n"
            "void postTweet(int userId, int tweetId) {\n"
            "    // User logic here\n"
            "}\n\n"
            "void getNewsFeed(int userId) {\n"
            "    // User logic here — print [id1,id2,...]\n"
            "    printf(\"[]\\n\");\n"
            "}\n\n"
            "void follow(int followerId, int followeeId) {\n"
            "    // User logic here\n"
            "}\n\n"
            "void unfollow(int followerId, int followeeId) {\n"
            "    // User logic here\n"
            "}\n\n"
            "int main() {\n"
            "    char op[20];\n"
            "    while (scanf(\"%19s\", op) == 1) {\n"
            "        if (!strcmp(op, \"post\")) {\n"
            "            int u, t; \n"
            "            if (scanf(\"%d %d\", &u, &t) == 2) postTweet(u, t);\n"
            "        } else if (!strcmp(op, \"feed\")) {\n"
            "            int u; \n"
            "            if (scanf(\"%d\", &u) == 1) getNewsFeed(u);\n"
            "        } else if (!strcmp(op, \"follow\")) {\n"
            "            int a, b; \n"
            "            if (scanf(\"%d %d\", &a, &b) == 2) follow(a, b);\n"
            "        } else if (!strcmp(op, \"unfollow\")) {\n"
            "            int a, b; \n"
            "            if (scanf(\"%d %d\", &a, &b) == 2) unfollow(a, b);\n"
            "        }\n"
            "    }\n"
            "    return 0;\n"
            "}"
        )
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
