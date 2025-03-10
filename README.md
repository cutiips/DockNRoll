# 🎸 DockNRoll

This project was created to test deployment using Docker, Nginx, and a Synology NAS, with domain configuration handled via DuckDNS. It consists of a frontend, a backend, and an Nginx configuration for reverse proxying. Service orchestration is managed with Docker Compose.

-> the goal is to create an app hosted on a VM (NAS) and deploy it

## Project Structure

- **backend/** (flask): receives the request and checks that the password is valid -> listens internally on port 5000 (flask)
- **frontend/** (html/js/css): displays a simple form and communicates with the backend -> runs on port 80 of the Nginx container (access via reverse proxy)
- **nginx/** (reverse proxy): intermediary between frontend and backend -> manages HTTP access by exposing a single port for the application
- **docker-compose.yml**: configuration file to orchestrate the Docker services

----
# Security things

## Monitor logs
Nginx : /var/log/nginx/access.log et /var/log/nginx/error.log (or in your Docker containers : docker logs nginx_proxy).

SSH : /var/log/auth.log (to view SSH connections).

Fail2ban : /var/log/fail2ban.log.

## UFW
```bash
sudo ufw default deny incoming # disable incoming connections by default
sudo ufw default allow outgoing # allow outgoing connections

sudo ufw enable # enable ufw

sudo ufw status verbose # status

sudo ufw status
```

## fail2ban
```bash
sudo fail2ban-client status

sudo fail2ban-client status sshd
```

## nginx proxy and container
```bash
docker logs nginx_proxy

docker logs frontend

docker logs backend

docker logs duckdns
```

## journals
Sur la VM Ubuntu :
```bash
sudo tail -f /var/log/auth.log (SSH)
docker logs -f nginx_proxy (Nginx)
sudo tail -f /var/log/fail2ban.log (Fail2ban)
```

Sur le NAS :
```bash
DSM interface > Control Panel > Logs # Interface DSM > Panneau de configuration > Journal.
```

Sur Windows :
```bash
Event Observer (eventvwr.exe).
```

## docker
```bash
docker-compose up -d #enable

docker-compose down #disable
```
