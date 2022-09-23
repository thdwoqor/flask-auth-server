# Getting Started  

## SET SSL 

```sh
docker run -it --rm --name certbot \
  -v '/etc/letsencrypt:/etc/letsencrypt' \
  -v '/var/lib/letsencrypt:/var/lib/letsencrypt' \
  certbot/certbot certonly -d '{MY DOMAIN}' --manual --preferred-challenges dns --server https://acme-v02.api.letsencrypt.org/directory

  # SET DNS TTX
```

```sh
cp /etc/letsencrypt/live/legonft.n-e.kr/fullchain.pem ./server.crt
cp /etc/letsencrypt/live/legonft.n-e.kr/privkey.pem ./server.key
chmod 755 server.crt
chmod 755 server.key
```

