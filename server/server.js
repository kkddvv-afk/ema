const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.get('/api/hello', (req, res) => {
  const name = (req.query.name || 'мир').toString();
  res.json({ message: `Привет, ${name}!` });
});

const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server listening on http://localhost:${port}`);
});

