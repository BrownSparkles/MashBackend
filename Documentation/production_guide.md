# Running the MASH Game Service in Low-Traffic Production

---

## 1. Use a Production WSGI Server

Use `gunicorn` to serve your Flask app.

```bash
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:8000 app:app
```

---

## 2. Secure Your Environment Variables

Use a `.env` file or set environment variables manually. Never commit your API key to source control.

---

## 3. Optional: Use Nginx as a Reverse Proxy

```nginx
server {
  listen 80;
  server_name yourdomain.com;

  location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
  }
}
```

---

## 4. Run as a Background Process

Use `systemd`, `supervisord`, or similar tools to keep your app alive:

```ini
[program:mashgame]
command=/path/to/venv/bin/gunicorn app:app -b 0.0.0.0:8000
directory=/path/to/app
autostart=true
autorestart=true
```

---

## 5. Improve Performance

- Add caching for common themes
- Compress responses using `Flask-Compress`

---

## 6. Security Tips

- Disable debug mode in production: `app.run(debug=False)`
- Add rate limiting (e.g., Flask-Limiter)

---
