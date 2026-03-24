const fs = require('fs');
const path = require('path');

const outDir = path.join(__dirname, 'companyWiseQuestions', 'Quora');

// 755 Pour Water
const p755 = path.join(outDir, '755_Pour_Water.json');
if (fs.existsSync(p755)) {
  const d755 = JSON.parse(fs.readFileSync(p755, 'utf8'));
  d755.question_text = `<h3>Pour Water</h3><p>We are given an elevation map, <code>heights</code> represented by an array of non-negative integers where <code>heights[i]</code> is the height of the terrain at index <code>i</code>. Given a quantity of water <code>volume</code> and a location <code>k</code>, return the final state of the terrain after <code>volume</code> units of water have been poured at <code>k</code>.</p><p>Water behaves according to these rules:</p><ul><li>First, the water attempts to move to the left. If there is a position to the left that is lower than the current position, the water will move to the leftmost such position that is the lowest.</li><li>If the water cannot move to the left, it then attempts to move to the right. If there is a position to the right that is lower than the current position, the water will move to the rightmost such position that is the lowest.</li><li>If the water cannot move to the left or right, it stays at its current position.</li></ul>`;
  fs.writeFileSync(p755, JSON.stringify(d755, null, 2));
  console.log('Patched 755');
}

// 253 Meeting Rooms II (already handled in previous companies, but let's be sure)
const p253 = path.join(outDir, '253_Meeting_Rooms_II.json');
if (fs.existsSync(p253)) {
  const d253 = JSON.parse(fs.readFileSync(p253, 'utf8'));
  if (d253.question_text.length < 50) {
    d253.question_text = `<h3>Meeting Rooms II</h3><p>Given an array of meeting time intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of conference rooms required</em>.</p>`;
    fs.writeFileSync(p253, JSON.stringify(d253, null, 2));
    console.log('Patched 253');
  }
}

// 1256 Encode Number
const p1256 = path.join(outDir, '1256_Encode_Number.json');
if (fs.existsSync(p1256)) {
  const d1256 = JSON.parse(fs.readFileSync(p1256, 'utf8'));
  if (d1256.question_text.length < 50) {
      d1256.question_text = `<h3>Encode Number</h3><p>Given a non-negative integer <code>num</code>, return its encoding which is done by converting <code>num + 1</code> to binary and removing the leading <code>1</code>.</p>`;
      fs.writeFileSync(p1256, JSON.stringify(d1256, null, 2));
      console.log('Patched 1256');
  }
}
