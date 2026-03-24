const fs = require('fs');
const path = require('path');

const missingData = [
    {
        qid: "1095",
        title: "Find in Mountain Array",
        difficulty: "Hard",
        topic: "Binary Search",
        content: `<h3>1095. Find in Mountain Array</h3>
<p><em>(This problem is an <strong>interactive problem</strong>.)</em></p>
<p>You may recall that an array <code>arr</code> is a <strong>mountain array</strong> if and only if:</p>
<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with <code>0 &lt; i &lt; arr.length - 1</code> such that:
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>
<p>Given a mountain array <code>mountainArr</code>, return the <strong>minimum</strong> <code>index</code> such that <code>mountainArr.get(index) == target</code>. If such an <code>index</code> does not exist, return <code>-1</code>.</p>
<p><strong>You cannot access the mountain array directly.</strong> You may only access the array using a <code>MountainArray</code> interface:</p>
<ul>
	<li><code>MountainArray.get(k)</code> returns the element of the array at index <code>k</code> (0-indexed).</li>
	<li><code>MountainArray.length()</code> returns the length of the array.</li>
</ul>
<p>Submissions making more than <code>100</code> calls to <code>MountainArray.get</code> will be judged <em>Wrong Answer</em>. Also, any solutions that attempt to circumvent the judge will result in disqualification.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> array = [1,2,3,4,5,3,1], target = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 exists in the array at index 2 and index 5. Return the minimum index, which is 2.</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> array = [0,1,2,4,2,1], target = 3
<strong>Output:</strong> -1
<strong>Explanation:</strong> 3 does not exist in the array.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>3 &lt;= mountainArr.length() &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= mountainArr.get(index) &lt;= 10<sup>9</sup></code></li>
</ul>`,
        tcs: [
            { input: "[1,2,3,4,5,3,1]\n3", output: "2", is_sample: true },
            { input: "[0,1,2,4,2,1]\n3", output: "-1", is_sample: true },
            { input: "[1,5,2]\n2", output: "2", is_sample: false },
            { input: "[1,5,2]\n5", output: "1", is_sample: false },
            { input: "[1,5,2]\n1", output: "0", is_sample: false },
            { input: "[1,5,2]\n0", output: "-1", is_sample: false },
            { input: "[1,2,3,4,5,6,7,8,9,10,9,8,7]\n9", output: "8", is_sample: false },
            { input: "[1,2,3,4,5,6,7,8,9,10,9,8,7]\n1", output: "0", is_sample: false },
            { input: "[1,2,3,4,5,6,7,8,9,10,9,8,7]\n7", output: "6", is_sample: false },
            { input: "[1,2,3,4,5,6,7,8,9,10,9,8,7]\n11", output: "-1", is_sample: false }
        ]
    },
    {
        qid: "479",
        title: "Largest Palindrome Product",
        difficulty: "Hard",
        topic: "Math",
        content: `<h3>479. Largest Palindrome Product</h3>
<p>Given an integer n, return <em>the <strong>largest palindromic integer</strong> that can be represented as the product of two n-digit integers.</em> Since the answer can be very large, return it <strong>modulo</strong> <code>1337</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 987
<strong>Explanation:</strong> 99 x 91 = 9009, 9009 % 1337 = 987
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>`,
        tcs: [
            { input: "2", output: "987", is_sample: true },
            { input: "1", output: "9", is_sample: true },
            { input: "3", output: "123", is_sample: false },
            { input: "4", output: "597", is_sample: false },
            { input: "5", output: "677", is_sample: false },
            { input: "6", output: "1218", is_sample: false },
            { input: "7", output: "877", is_sample: false },
            { input: "8", output: "475", is_sample: false },
            { input: "1", output: "9", is_sample: false },
            { input: "2", output: "987", is_sample: false }
        ]
    },
    {
        qid: "311",
        title: "Sparse Matrix Multiplication",
        difficulty: "Medium",
        topic: "Matrix",
        content: `<h3>311. Sparse Matrix Multiplication</h3>
<p>Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> <code>mat1</code> of size <code>m x k</code> and <code>mat2</code> of size <code>k x n</code>, return the result of <code>mat1 x mat2</code>. You may assume that multiplication is always possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/mw1.jpg" style="width: 500px; height: 142px;" />
<pre><strong>Input:</strong> mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
<strong>Output:</strong> [[7,0,0],[-7,0,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> mat1 = [[0]], mat2 = [[0]]
<strong>Output:</strong> [[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li><code>m == mat1.length</code></li>
	<li><code>k == mat1[i].length == mat2.length</code></li>
	<li><code>n == mat2[i].length</code></li>
	<li><code>1 &lt;= m, n, k &lt;= 100</code></li>
	<li><code>-100 &lt;= mat1[i][j], mat2[i][j] &lt;= 100</code></li>
</ul>`,
        tcs: [
            { input: "[[1,0,0],[-1,0,3]]\n[[7,0,0],[0,0,0],[0,0,1]]", output: "[[7,0,0],[-7,0,3]]", is_sample: true },
            { input: "[[0]]\n[[0]]", output: "[[0]]", is_sample: true },
            { input: "[[1,1]]\n[[1],[1]]", output: "[[2]]", is_sample: false },
            { input: "[[1,2],[3,4]]\n[[0,0],[0,0]]", output: "[[0,0],[0,0]]", is_sample: false },
            { input: "[[0,0],[0,0]]\n[[1,2],[3,4]]", output: "[[0,0],[0,0]]", is_sample: false },
            { input: "[[1,0],[0,1]]\n[[5,6],[7,8]]", output: "[[5,6],[7,8]]", is_sample: false },
            { input: "[[2,0],[0,2]]\n[[1,2],[3,4]]", output: "[[2,4],[6,8]]", is_sample: false },
            { input: "[[1,2,3]]\n[[4],[5],[6]]", output: "[[32]]", is_sample: false },
            { input: "[[4],[5],[6]]\n[[1,2,3]]", output: "[[4,8,12],[5,10,15],[6,12,18]]", is_sample: false },
            { input: "[[1,0,1],[0,1,0],[1,0,1]]\n[[1,1,1],[1,1,1],[1,1,1]]", output: "[[2,2,2],[1,1,1],[2,2,2]]", is_sample: false }
        ]
    }
];

const cDir = 'companyWiseQuestions/Apple';
if (!fs.existsSync(cDir)) fs.mkdirSync(cDir, { recursive: true });

missingData.forEach(q => {
    const filename = `${q.qid}_${q.title.replace(/ /g, '_').replace(/[^-a-zA-Z0-9_]/g, '')}.json`;
    const fpath = path.join(cDir, filename);
    const data = {
        title: q.title,
        problem_id: q.qid,
        difficulty: q.difficulty,
        topic: q.topic,
        companyIndex: 3,
        question_text: q.content,
        test_cases: q.tcs
    };
    fs.writeFileSync(fpath, JSON.stringify(data, null, 4));
    console.log(`Generated: ${filename}`);
});
