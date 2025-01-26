# 🎸 DockNRoll

This project was created to test deployment using Docker, Nginx, and a Synology NAS, with domain configuration handled via DuckDNS. It consists of a frontend, a backend, and an Nginx configuration for reverse proxying. Service orchestration is managed with Docker Compose.

-> the goal is to create an app hosted on a VM (NAS) and deploy it

## Project Structure

- **backend/** (flask): receives the request and checks that the password is valid -> listens internally on port 5000 (flask)
- **frontend/** (html/js/css): displays a simple form and communicates with the backend -> runs on port 80 of the Nginx container (access via reverse proxy)
- **nginx/** (reverse proxy): intermediary between frontend and backend -> manages HTTP access by exposing a single port for the application
- **docker-compose.yml**: configuration file to orchestrate the Docker services

