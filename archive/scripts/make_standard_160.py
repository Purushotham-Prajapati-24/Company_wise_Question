import json
import os

def generate_json():
    problem_id = 160
    title = "Intersection of Two Linked Lists"
    difficulty = "Easy"
    marks = 10
    
    html_description = """<h3>160. Intersection of Two Linked Lists</h3>
<p>Given the heads of two singly linked-lists <code>headA</code> and <code>headB</code>, return <em>the node at which the two lists intersect</em>. If the two linked lists have no intersection at all, return <code>null</code>.</p>

<p>For example, the following two linked lists begin to intersect at node c1:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png" style="width: 500px; height: 162px;" />
<p>The test cases are generated such that there are no cycles anywhere in the entire linked structure.</p>

<p><strong>Note</strong> that the linked lists must <strong>retain their original structure</strong> after the function returns.</p>

<p><strong>Custom Judge:</strong></p>
<p>The inputs to the <strong>judge</strong> are given as follows (your program is <strong>not</strong> given these inputs):</p>
<ul>
	<li><code>intersectVal</code> - The value of the node where the intersection occurs. This is <code>0</code> if there is no intersection node.</li>
	<li><code>listA</code> - The first linked list.</li>
	<li><code>listB</code> - The second linked list.</li>
	<li><code>skipA</code> - The number of nodes to skip ahead in <code>listA</code> (starting from the head) to get to the intersected node.</li>
	<li><code>skipB</code> - The number of nodes to skip ahead in <code>listB</code> (starting from the head) to get to the intersected node.</li>
</ul>
<p>The judge will then create the linked structure based on these inputs and pass the two heads, <code>headA</code> and <code>headB</code> to your program. If you correctly return the intersected node, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="width: 500px; height: 162px;" />
<pre><strong>Input:</strong> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
<strong>Output:</strong> Intersected at '8'
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="width: 500px; height: 194px;" />
<pre><strong>Input:</strong> intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong>Output:</strong> Intersected at '2'
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>
<ul>
	<li>The number of nodes of <code>listA</code> is in the <code>m</code>.</li>
	<li>The number of nodes of <code>listB</code> is in the <code>n</code>.</li>
	<li><code>1 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= skipA &lt;= m</code></li>
	<li><code>0 &lt;= skipB &lt;= n</code></li>
	<li><code>intersectVal</code> is <code>0</code> if <code>listA</code> and <code>listB</code> do not intersect.</li>
	<li><code>intersectVal == listA[skipA] == listB[skipB]</code> if <code>listA</code> and <code>listB</code> intersect.</li>
</ul>

<p>&nbsp;</p>
<b>Follow up:</b> Could you write a solution that runs in <code>O(m + n)</code> time and use only <code>O(1)</code> memory?"""

    input_format = "5 lines. 1: intersectVal. 2: listA (space-separated). 3: listB (space-separated). 4: skipA. 5: skipB."
    output_format = "An integer (value of the intersecting node or 0)."
    
    constraints = [
        "1 <= m, n <= 3 * 10^4",
        "O(m + n) time, O(1) memory."
    ]
    
    explanation = """To find the intersection of two linked lists in O(1) space:
1. **Two Pointers Approach**:
   - Initialize two pointers `ptrA = headA` and `ptrB = headB`.
   - Traverse through the lists. When a pointer reaches the end of a list, redirect it to the head of the **other** list.
2. **Logic**:
   - If they intersect, the two pointers will meet at the intersection point after at most `m + n` steps.
   - Why? Let `a` be the length of the non-overlapping part of listA, `b` be the length of non-overlapping part of listB, and `c` be the overlapping part.
   - Pointer A travels `a + c + b`. Pointer B travels `b + c + a`.
   - Both travel exactly `a + b + c` distance before meeting at the start of `c`.
   - If they don't intersect, they will both reach `null` at the same time and loop terminates.
3. **Complexity**:
   - Time Complexity: O(M + N).
   - Space Complexity: O(1)."""
    
    answer = """class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
        
    pA = headA
    pB = headB
    
    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
        
    return pA"""

    boilerplate = {
        "python": "import sys\n\nclass ListNode:\n    def __init__(self, x):\n        self.val = x\n        self.next = None\n\ndef getIntersectionNode(headA, headB):\n    # User logic here\n    pass\n\ndef build_lists(intersectVal, listA, listB, skipA, skipB):\n    if not listA and not listB: return None, None\n    nodesA = [ListNode(int(x)) for x in listA]\n    nodesB = [ListNode(int(x)) for x in listB]\n    if intersectVal != 0:\n        for i in range(skipB, len(nodesB)):\n            nodesB[i] = nodesA[skipA + (i - skipB)]\n    for i in range(len(nodesA) - 1): nodesA[i].next = nodesA[i+1]\n    for i in range(len(nodesB) - 1): nodesB[i].next = nodesB[i+1]\n    return nodesA[0] if nodesA else None, nodesB[0] if nodesB else None\n\nif __name__ == '__main__':\n    lines = sys.stdin.read().splitlines()\n    if len(lines) >= 5:\n        iv = int(lines[0])\n        lA = lines[1].split()\n        lB = lines[2].split()\n        sA = int(lines[3])\n        sB = int(lines[4])\n        hA, hB = build_lists(iv, lA, lB, sA, sB)\n        res = getIntersectionNode(hA, hB)\n        print(res.val if res else 0)",
        "cpp": "#include <iostream>\n#include <vector>\n#include <string>\n#include <sstream>\nusing namespace std;\nstruct ListNode{int val;ListNode*next;ListNode(int x):val(x),next(NULL){}};\nclass Solution {\npublic:\n    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {\n        // User logic\n        return NULL;\n    }\n};\nint main(){\n    string ivS,laS,lbS,saS,sbS; if(getline(cin,ivS)&&getline(cin,laS)&&getline(cin,lbS)&&getline(cin,saS)&&getline(cin,sbS)){\n        int iv=stoi(ivS), sa=stoi(saS), sb=stoi(sbS);\n        vector<ListNode*> nA, nB; istringstream ssa(laS), ssb(lbS); int x;\n        while(ssa>>x) nA.push_back(new ListNode(x));\n        while(ssb>>x) nB.push_back(new ListNode(x));\n        if(iv!=0) for(size_t i=sb; i<nB.size(); i++){ delete nB[i]; nB[i]=nA[sa+(i-sb)]; }\n        for(size_t i=1;i<nA.size();i++) nA[i-1]->next=nA[i];\n        for(size_t i=1;i<nB.size();i++) nB[i-1]->next=nB[i];\n        Solution sol; ListNode* res=sol.getIntersectionNode(nA.empty()?NULL:nA[0], nB.empty()?NULL:nB[0]);\n        cout<<(res?res->val:0)<<endl;\n    }\n    return 0;\n}",
        "java": "import java.util.*;\nimport java.io.*;\nclass ListNode {int val; ListNode next; ListNode(int x){val=x;}}\npublic class Main {\n    static class Solution {\n        public ListNode getIntersectionNode(ListNode headA, ListNode headB) {\n            // User logic\n            return null;\n        }\n    }\n    public static void main(String[] args) throws Exception{\n        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));\n        String l0=br.readLine(); if(l0==null)return;\n        int iv=Integer.parseInt(l0.trim());\n        String[] laS=br.readLine().trim().split(\"\\\\s+\"), lbS=br.readLine().trim().split(\"\\\\s+\");\n        int sA=Integer.parseInt(br.readLine().trim()), sB=Integer.parseInt(br.readLine().trim());\n        List<ListNode> nA=new ArrayList<>(), nB=new ArrayList<>();\n        for(String s:laS) if(!s.isEmpty()) nA.add(new ListNode(Integer.parseInt(s)));\n        for(String s:lbS) if(!s.isEmpty()) nB.add(new ListNode(Integer.parseInt(s)));\n        if(iv!=0) for(int i=sB; i<nB.size(); i++) nB.set(i, nA.get(sA+(i-sB)));\n        for(int i=1;i<nA.size();i++) nA.get(i-1).next=nA.get(i);\n        for(int i=1;i<nB.size();i++) nB.get(i-1).next=nB.get(i);\n        Solution sol=new Solution(); ListNode res=sol.getIntersectionNode(nA.isEmpty()?null:nA.get(0), nB.isEmpty()?null:nB.get(0));\n        System.out.println(res!=null?res.val:0);\n    }\n}",
        "javascript": "const fs=require('fs');\nfunction ListNode(val){this.val=val;this.next=null;}\nfunction getIntersectionNode(headA, headB){\n    // User logic\n    return null;\n}\nconst lines=fs.readFileSync(0,'utf8').trim().split('\\n');\nif(lines.length>=5){\n    const iv=parseInt(lines[0]), sa=parseInt(lines[3]), sb=parseInt(lines[4]);\n    const nA=lines[1].trim()?lines[1].trim().split(/\\s+/).map(x=>new ListNode(parseInt(x))):[];\n    const nB=lines[2].trim()?lines[2].trim().split(/\\s+/).map(x=>new ListNode(parseInt(x))):[];\n    if(iv!==0) for(let i=sb;i<nB.length;i++) nB[i]=nA[sa+(i-sb)];\n    for(let i=1;i<nA.length;i++) nA[i-1].next=nA[i];\n    for(let i=1;i<nB.length;i++) nB[i-1].next=nB[i];\n    const res=getIntersectionNode(nA.length?nA[0]:null, nB.length?nB[0]:null);\n    console.log(res?res.val:0);\n}",
        "c": "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\nstruct ListNode{int val;struct ListNode*next;};\nstruct ListNode* getIntersectionNode(struct ListNode* headA, struct ListNode* headB){\n    // User logic\n    return NULL;\n}\nint main(){\n    char l0[100],l1[50000],l2[50000],l3[100],l4[100];\n    if(fgets(l0,sizeof(l0),stdin)&&fgets(l1,sizeof(l1),stdin)&&fgets(l2,sizeof(l2),stdin)&&fgets(l3,sizeof(l3),stdin)&&fgets(l4,sizeof(l4),stdin)){\n        int iv=atoi(l0), sa=atoi(l3), sb=atoi(l4);\n        struct ListNode* nA[30005]; struct ListNode* nB[30005]; int sA=0, sB=0;\n        char* tok=strtok(l1,\" \\t\\r\\n\"); while(tok){nA[sA]=(struct ListNode*)malloc(sizeof(struct ListNode));nA[sA]->val=atoi(tok);nA[sA]->next=NULL;sA++;tok=strtok(NULL,\" \\t\\r\\n\");}\n        tok=strtok(l2,\" \\t\\r\\n\"); while(tok){nB[sB]=(struct ListNode*)malloc(sizeof(struct ListNode));nB[sB]->val=atoi(tok);nB[sB]->next=NULL;sB++;tok=strtok(NULL,\" \\t\\r\\n\");}\n        if(iv!=0) for(int i=sb; i<sB; i++){free(nB[i]); nB[i]=nA[sa+(i-sb)];}\n        for(int i=1;i<sA;i++) nA[i-1]->next=nA[i];\n        for(int i=1;i<sB;i++) nB[i-1]->next=nB[i];\n        struct ListNode* res=getIntersectionNode(sA?nA[0]:NULL, sB?nB[0]:NULL);\n        printf(\"%d\\n\",res?res->val:0);\n    }\n    return 0;\n}"
    }

    test_cases = [
        {"input": "8\\n4 1 8 4 5\\n5 6 1 8 4 5\\n2\\n3", "expected_output": "8", "is_sample": True},
        {"input": "2\\n1 9 1 2 4\\n3 2 4\\n3\\n1", "expected_output": "2", "is_sample": True},
        {"input": "0\\n2 6 4\\n1 5\\n3\\n2", "expected_output": "0", "is_sample": True},
        {"input": "1\\n1\\n1\\n0\\n0", "expected_output": "1", "is_sample": False},
        {"input": "0\\n1 2\\n3 4\\n2\\n2", "expected_output": "0", "is_sample": False},
        {"input": "3\\n1 2 3 4\\n5 3 4\\n2\\n1", "expected_output": "3", "is_sample": False},
        {"input": "5\\n5\\n5\\n0\\n0", "expected_output": "5", "is_sample": False},
        # Stress cases
        {"input": "1\\n" + " ".join(["2"]*20000 + ["1"]) + "\\n" + " ".join(["3"]*10000 + ["1"]) + "\\n20000\\n10000", "expected_output": "1", "is_sample": False},
        {"input": "0\\n" + " ".join(["2"]*20000) + "\\n" + " ".join(["3"]*20000) + "\\n20000\\n20000", "expected_output": "0", "is_sample": False},
        {"input": "100\\n" + " ".join(["1"]*15000 + ["100"]) + "\\n" + " ".join(["2"]*15000 + ["100"]) + "\\n15000\\n15000", "expected_output": "100", "is_sample": False}
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
            "time_limit_ms": 1000,
            "memory_limit_mb": 256,
            "allowed_languages": ["python", "cpp", "java", "javascript", "c"]
        },
        "topics": ["Hash Table", "Linked List", "Two Pointers"],
        "companyIndex": 0
    }

    output_path = "1-200/160_Intersection_of_Two_Linked_Lists.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    generate_json()
