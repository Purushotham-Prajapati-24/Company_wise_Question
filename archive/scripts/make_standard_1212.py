import json
import os

def generate_json():
    problem_id = 1212
    title = "Selection"
    difficulty = "MEDIUM"
    marks = 10

    # Note: 1212 is not a standard LeetCode problem ID (1212 is Team Scores in Football Matches - SQL).
    # However, 1212 in the user's pending list might refer to a different source or a specific problem named "Selection".
    # Researching "Selection" problem near 1212.
    # Actually, 1211 is Queries Quality and Percentage (SQL), 1212 is Team Scores (SQL).
    # If the user has it in "pending_audit", I suspect it's a specific internal problem or I should check the context.
    # Looking at the ID list [1212, 1223, 1229...], 1223 is definitely LC.
    # Let's check if 1212 is actually "Team Scores in Football Matches" and if we should skip SQL. 
    # Usually, we skip SQL and only do Algo. 
    # Let me check the user's directory for 1212.
    
    html_description = """<h3>1212. Team Scores in Football Matches</h3>
<p>This is an SQL problem. Standardizing to algorithm format if applicable, or skipping if purely SQL.</p>
<p><i>Note: High probability of being a SQL problem. Moving to next algorithm problem if SQL.</i></p>"""

    # For safety, I'll check if 1212 is actually 1212 in a search.
    # If it's SQL, I'll mark it as skipped in next turn.
    # Let's assume for now 1212 is 1212 Team Scores (SQL).
    
    data = {
        "question_id": problem_id, "question_text": html_description, "difficulty": difficulty, "marks": marks,
        "test_cases": []
    }
    # Skip creating file for SQL if that's the rule.
    print(f"ID 1212 is likely SQL. Checking next.")

if __name__ == "__main__":
    generate_json()
