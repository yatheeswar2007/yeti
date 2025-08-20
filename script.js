fetch('/api/yeti')
  .then(r => r.json())
  .then(data => {
    const el = document.getElementById('data');
    el.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  })
  .catch(() => {
    document.getElementById('data').textContent = 'Could not load data.';
  });
