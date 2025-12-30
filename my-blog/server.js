const express = require('express');
const path = require('path');
const app = express();
const PORT = 8080;

// 静的ファイル配信（HTML / CSS / JS）
app.use(express.static(path.join(__dirname, 'public')));

// ホーム
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// 記事ページ
app.get('/post1', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'post1.html'));
});

app.get('/post2', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'post2.html'));
});

app.listen(PORT, () => {
  console.log(`Site running at http://localhost:${PORT}`);
});
