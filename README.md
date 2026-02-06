# random-word-api
simple api for returning a random word. replacing http://randomword.saasbook.info/RandomWord

# Quick start

Install the necessary packages and run `app.py`. You may want to replace the `VALID_KEY`.

For production, you can use `gunicorn -b 127.0.0.1:12345 app:app`, e.g.

```
/var/www/html/random-word-api/
├── app.py
```

`cd /var/www/html/random-word-api && gunicorn -b 127.0.0.1:12345 app:app`

**It is recommended that you use a reverse proxy to serve this app**

# Security

There is basically no security. The key is plain-text (not hashed). There is no rate limit. There is also no HTTPS.

HTTPS and rate limits are expected to be handled by reverse proxies, e.g. Caddy / nginx.

Do not rely on this for mission-critical purposes.

