import json
import os

def generate_json():
    problem_id = 1242
    title = "Web Crawler Multithreaded"
    difficulty = "MEDIUM"
    marks = 10

    html_description = """<h3>1242. Web Crawler Multithreaded</h3>
<p>Given a URL <code>startUrl</code> and an interface <code>HtmlParser</code>, implement a multi-threaded web crawler to collect all links that are under the <strong>same hostname</strong> as <code>startUrl</code>. </p>

<p>Return all URLs obtained by your web crawler in <strong>any order</strong>.</p>

<p>Your crawler should:</p>
<ul>
	<li>Start from the page: <code>startUrl</code></li>
	<li>Call <code>HtmlParser.getUrls(url)</code> to get all URLs from a webpage of a given URL.</li>
	<li>Do not crawl the same page twice.</li>
	<li>Only crawl the URLs that are under the <strong>same hostname</strong> as <code>startUrl</code>.</li>
</ul>

<p>Note: <code>hostname</code> is the string after <code>"http://"</code> until the first <code>"/"</code>. For example, the hostname of <code>"http://leetcode.com/problems"</code> is <code>"leetcode.com"</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://raw.githubusercontent.com/doocs/leetcode/main/solution/1200-1299/1242.Web%20Crawler%20Multithreaded/images/sample_2_1497.png" style="width: 610px; height: 300px;">
<pre><strong>Input:</strong>
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com",
  "http://news.yahoo.com/us"
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = "http://news.yahoo.com/news/topics/"
<strong>Output:</strong> [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.yahoo.com/us"
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= urls.length &lt;= 1000</code></li>
	<li><code>1 &lt;= urls[i].length &lt;= 300</code></li>
	<li><code>startUrl</code> is one of the <code>urls</code>.</li>
	<li>Hostname label must be from 1 to 63 characters long, containing only letters, numbers, hyphens.</li>
	<li>Edges are given as source-destination indices.</li>
</ul>"""

    input_format = "A list of all URLs, a list of edges (idx pairs), and the `startUrl` provided as `[urls, edges, startUrl]` in JSON."
    output_format = "A JSON array of URLs found."

    constraints = [
        "1 <= urls.length <= 1000",
        "1 <= url.length <= 300",
        "Only crawl same hostname"
    ]

    explanation = """To implement a multi-threaded web crawler:
1. Extract the hostname from `startUrl`.
2. Use a thread-safe data structure (e.g., `ConcurrentHashMap`, `Set` with Lock) to keep track of visited URLs.
3. Use a thread pool (e.g., `ThreadPoolExecutor`) to manage crawling tasks.
4. Each task:
   - Fetches URLs from the current page using `HtmlParser.getUrls(url)`.
   - Filters the URLs to keep only those with the same hostname.
   - For each new URL, if it hasn't been visited, add it to visited and submit a new task.
5. Wait for all tasks to complete and return the visited list."""

    answer = """import threading
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        hostname = startUrl.split('//')[1].split('/')[0]
        visited = {startUrl}
        lock = threading.Lock()
        
        def process(url):
            new_urls = htmlParser.getUrls(url)
            for next_url in new_urls:
                if next_url.split('//')[1].split('/')[0] == hostname:
                    with lock:
                        if next_url not in visited:
                            visited.add(next_url)
                            executor.submit(process, next_url)
                            
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.submit(process, startUrl)
            
        return list(visited)"""

    boilerplate = {
        "python": """import sys
import json
import threading
from concurrent.futures import ThreadPoolExecutor

class HtmlParser(object):
    def getUrls(self, url):
        return []

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        # User logic here
        return []

if __name__ == '__main__':
    # Simulator logic here
    pass""",
        "cpp": """#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

class HtmlParser {
public:
    vector<string> getUrls(string url);
};

class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        // User logic here
        return {};
    }
};

int main() {
    return 0;
}""",
        "java": """import java.util.*;
import java.util.concurrent.*;

interface HtmlParser {
    public List<String> getUrls(String url);
}

class Solution {
    public List<String> crawl(String startUrl, HtmlParser htmlParser) {
        // User logic here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {}
}""",
        "javascript": """/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * function HtmlParser() {
 *
 *     /**
 *      * @param {string} url
 *      * @return {string[]}
 *      */
 *     this.getUrls = function(url) {
 *      ...
 *     };
 * };
 */

/**
 * @param {string} startUrl
 * @param {HtmlParser} htmlParser
 * @return {string[]}
 */
var crawl = function(startUrl, htmlParser) {
    
};""",
        "c": """#include <stdio.h>
#include <stdlib.h>

char** crawl(char* startUrl, void* htmlParser, int* returnSize){
    // User logic here
    return NULL;
}

int main() {
    return 0;
}"""
    }

    def solve(urls, edges, startUrl):
        hostname = startUrl.split('//')[1].split('/')[0]
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[urls[u]].append(urls[v])
        
        visited = {startUrl}
        queue = collections.deque([startUrl])
        while queue:
            curr = queue.popleft()
            for next_url in adj[curr]:
                if next_url.split('//')[1].split('/')[0] == hostname:
                    if next_url not in visited:
                        visited.add(next_url)
                        queue.append(next_url)
        return sorted(list(visited))

    import collections
    test_cases_data = [
        [
            ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"],
            [[2,0],[2,1],[3,2],[3,1],[0,4]],
            "http://news.yahoo.com/news/topics/"
        ], # Sample 1
        [
            ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"],
            [[2,0],[2,1],[3,2],[3,1],[0,4]],
            "http://news.yahoo.com"
        ], # Different start
        [
            ["http://site.com", "http://site.com/a", "http://site.com/b"],
            [[0,1],[1,2],[2,0]],
            "http://site.com"
        ], # Circle
        [
            ["http://a.com", "http://b.com"],
            [[0,1]],
            "http://a.com"
        ], # Different host
        [
            ["http://a.com/1", "http://a.com/2", "http://a.com/3"],
            [[0,1],[1,2]],
            "http://a.com/1"
        ], # Path
        # Stress tests
        [
            ["http://host.com/" + str(i) for i in range(100)],
            [[i, i+1] for i in range(99)],
            "http://host.com/0"
        ],
        [
            ["http://host.com/" + str(i) for i in range(100)],
            [[0, i] for i in range(1, 100)],
            "http://host.com/0"
        ],
        [
            ["http://sub.a.com", "http://a.com"],
            [[1,0]],
            "http://a.com"
        ], # Subdomain is different hostname
        [
            ["http://a.com", "http://a.com/p"],
            [[0,1]],
            "http://a.com"
        ],
        [
            ["http://site.org", "http://site.org/1"],
            [[0,1]],
            "http://site.org"
        ]
    ]

    test_cases = []
    for i, t in enumerate(test_cases_data):
        inp = json.dumps(t).replace(" ", "")
        out = json.dumps(solve(t[0], t[1], t[2])).replace(" ", "")
        test_cases.append({"input": inp, "expected_output": out, "is_sample": i < 1})

    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "input_format": input_format, "output_format": output_format, "constraints": constraints,
        "explanation": explanation, "answer": answer, "boilerplate": boilerplate, "test_cases": test_cases,
        "metadata": {"time_limit_ms": 2000, "memory_limit_mb": 256, "allowed_languages": ["python", "cpp", "java", "javascript", "c"]},
        "topics": ["DFS", "BFS", "Concurrency"], "companyIndex": 0
    }

    output_path = f"1201-1400/{problem_id}_{title.replace(' ', '_')}.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
