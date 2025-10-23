import random

# 23人の名前
people = [f"Person{i}" for i in range(1, 24)]

# 8テーブル
tables = {f"Table{i}": [] for i in range(1, 9)}

# シャッフル
random.shuffle(people)

# 割り振り
table_keys = list(tables.keys())
table_index = 0

for person in people:
    # 各テーブル3人まで
    while len(tables[table_keys[table_index]]) >= 3:
        table_index += 1
        if table_index >= len(table_keys):
            table_index = 0
    tables[table_keys[table_index]].append(person)

# HTML生成
html = """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>席割りシステム</title>
<style>
  body {
    font-family: 'Segoe UI', Roboto, sans-serif;
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: #333;
    margin: 0;
    padding: 20px;
  }
  h1 {
    text-align: center;
    color: white;
    margin-bottom: 40px;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
  }
  .tables {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 20px;
  }
  .table {
    background: white;
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .table:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
  }
  .table h2 {
    text-align: center;
    margin-bottom: 12px;
    color: #444;
  }
  .table ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .table li {
    padding: 8px 10px;
    margin-bottom: 6px;
    background: #f5f5f5;
    border-radius: 6px;
    text-align: center;
    font-weight: 500;
    color: #222;
    transition: background 0.2s;
  }
  .table li:hover {
    background: #e0e7ff;
  }
</style>
</head>
<body>
<h1>席割り結果</h1>
<div class="tables">
"""

for table, members in tables.items():
    html += f'<div class="table">\n<h2>{table}</h2>\n<ul>\n'
    for member in members:
        html += f'<li>{member}</li>\n'
    html += '</ul>\n</div>\n'

html += """
</div>
</body>
</html>
"""

# ファイルに保存
with open("seating.html", "w", encoding="utf-8") as f:
    f.write(html)

print("seating.html が生成されました。")
