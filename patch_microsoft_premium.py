import json, os

premium_content = {
    "186": """<h3>186. Reverse Words in a String II</h3>
<p>Given a character array <code>s</code>, reverse the order of the <strong>words</strong>.</p>
<p>A <strong>word</strong> is defined as a sequence of non-space characters. The <strong>words</strong> in <code>s</code> will be separated by a single space.</p>
<p>Your code must solve the problem&nbsp;<strong>in-place,</strong> meaning you must modify the input character array without allocating extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
<strong>Output:</strong> ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["a"]
<strong>Output:</strong> ["a"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is an English letter (uppercase or lowercase), a digit, or a space <code>' '</code>.</li>
	<li>There is <strong>at least one</strong> word in <code>s</code>.</li>
	<li><code>s</code> does not contain leading or trailing spaces.</li>
	<li>All the words in <code>s</code> are guaranteed to be separated by a single space.</li>
</ul>""",

    "253": """<h3>253. Meeting Rooms II</h3>
<p>Given an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of conference rooms required</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[0,30],[5,10],[15,20]]
<strong>Output:</strong> 2
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[7,10],[2,4]]
<strong>Output:</strong> 1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;=&nbsp;intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>""",

    "277": """<h3>277. Find the Celebrity</h3>
<p>Suppose you are at a party with <code>n</code> people labeled from <code>0</code> to <code>n - 1</code>. A celebrity is defined as one person who is known by all the other <code>n - 1</code> people, but does not know any of them.</p>

<p>You are given a helper function <code>bool knows(a, b)</code> that tells you whether <code>a</code> knows <code>b</code>. Implement a function <code>int findCelebrity(n)</code> to find the celebrity. If there is no celebrity, return <code>-1</code>.</p>

<p>There will be exactly one celebrity if they are at the party. The <code>knows</code> function will be called at most <code>3 * n</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g1.jpg" style="width: 224px; height: 145px;" />
<pre><strong>Input:</strong> graph = [[1,1,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are 3 people labeled 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0. The celebrity is the person labeled 1 because everyone knows him and he does not know anyone.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/19/g2.jpg" style="width: 224px; height: 145px;" />
<pre><strong>Input:</strong> graph = [[1,0,1],[1,1,0],[0,1,1]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no celebrity.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>n == graph.length == graph[i].length</code></li>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li><code>graph[i][j]</code> is <code>0</code> or <code>1</code>.</li>
	<li><code>graph[i][i] == 1</code></li>
</ul>""",

    "348": """<h3>348. Design Tic-Tac-Toe</h3>
<p>Design a Tic-Tac-Toe game that is played on an <code>n x n</code> grid. Two players alternatingly place their marks on the grid.</p>

<p>Implement the <code>TicTacToe</code> class:</p>
<ul>
	<li><code>TicTacToe(int n)</code> Initializes the object the size of the board <code>n</code>.</li>
	<li><code>int move(int row, int col, int player)</code> Indicates that the player <code>player</code> (either 1 or 2) places their mark at the cell <code>(row, col)</code>. The move is guaranteed to be a valid move. At each step, a winner is decided. Returns:
	<ul>
		<li>0: No one wins.</li>
		<li>1: Player 1 wins.</li>
		<li>2: Player 2 wins.</li>
	</ul>
	</li>
</ul>

<p>A winner is decided if a player has <code>n</code> consecutive marks in a horizontal, vertical, or diagonal row.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input</strong>
["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
<strong>Output</strong>
[null, 0, 0, 0, 0, 0, 0, 1]

<strong>Explanation</strong>
TicTacToe ticTacToe = new TicTacToe(3);
Assume player 1 is X and player 2 is O in the board.
ticTacToe.move(0, 0, 1); // return 0 (no one wins)
ticTacToe.move(0, 2, 2); // return 0 (no one wins)
ticTacToe.move(2, 2, 1); // return 0 (no one wins)
ticTacToe.move(1, 1, 2); // return 0 (no one wins)
ticTacToe.move(2, 0, 1); // return 0 (no one wins)
ticTacToe.move(1, 0, 2); // return 0 (no one wins)
ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>2 &lt;= n &lt;= 100</code></li>
	<li>player is <code>1</code> or <code>2</code>.</li>
	<li><code>0 &lt;= row, col &lt; n</code></li>
	<li>Every move will be to an empty cell.</li>
	<li>At most <code>n<sup>2</sup></code> calls will be made to <code>move</code>.</li>
</ul>"""
}

odir = 'companyWiseQuestions/Microsoft'
files = os.listdir(odir)

patched = 0
for qid, content in premium_content.items():
    # Find matching file
    for f in files:
        if f.startswith(qid + '_'):
            fpath = os.path.join(odir, f)
            data = json.load(open(fpath))
            data['question_text'] = content
            with open(fpath, 'w') as out:
                json.dump(data, out, indent=4)
            patched += 1
            break

print(f'Total premium Microsoft questions patched manually with <h3>: {patched}')
