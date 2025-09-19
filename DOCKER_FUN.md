# Roliga och intressanta Docker images för demo

## Desktop & GUI Applications

### Ubuntu Desktop i webbläsare

```bash
docker run -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc
# Öppna localhost:6080 - full Ubuntu desktop i browsern!
```

### Windows 95 i browsern

```bash
docker run -p 8080:8080 toolforge/tool-spacer-eqiad
# Nostalgisk Windows 95 upplevelse
```

### VS Code i webbläsare

```bash
docker run -p 8443:8443 -v "${PWD}:/home/coder/project" codercom/code-server:latest
# Full utvecklingsmiljö utan installation
```

## Gaming & Emulation

### Retro spelkonsoler

```bash
# GameBoy/NES/SNES emulator
docker run -p 3000:3000 -p 4001:4001 lscr.io/linuxserver/emulatorjs:latest

# DOOM (original från 1993)
docker run -p 5900:5900 mattrayner/lamp:doom
```

### Minecraft Server

```bash
docker run -e EULA=TRUE -p 25565:25565 itzg/minecraft-server
# Instant Minecraft server!
```

## Utvecklingsverktyg

### Jupyter Notebook med AI/ML bibliotek

```bash
docker run -p 8888:8888 jupyter/tensorflow-notebook
# Full data science miljö på sekunder
```

### GitLab i en container

```bash
docker run -p 443:443 -p 80:80 -p 22:22 gitlab/gitlab-ce:latest
# Hel Git-server med CI/CD
```

### Database Admin UI

```bash
# PostgreSQL + pgAdmin
docker run -p 5050:80 dpage/pgadmin4
```

## Multimedia & Kreativt

### YouTube-dl webbgränssnitt

```bash
docker run -p 8080:8080 tzahi12345/youtubedl-material:latest
# Ladda ner videos genom webgränssnitt
```

### Plex Media Server

```bash
docker run -p 32400:32400 plexinc/pms-docker
# Personlig streaming-tjänst
```

### Draw.io (diagram editor)

```bash
docker run -p 8080:8080 fjudith/draw.io
# Skapa flödesscheman och diagram
```

## Säkerhet & Nätverksverktyg

### Kali Linux (hacking-distribution)

```bash
docker run -it kalilinux/kali-rolling
# Etisk hacking-miljö isolerad
```

### Wireshark för nätverksanalys

```bash
docker run -p 3000:3000 lscr.io/linuxserver/wireshark:latest
# Nätverkspaketanalys i browsern
```

### Pi-hole (ad-blocker)

```bash
docker run -p 80:80 -p 53:53/udp pihole/pihole:latest
# DNS-baserad reklamblockering
```

## AI & Machine Learning

### ChatGPT-liknande lokalt

```bash
docker run -p 3000:8080 ghcr.io/open-webui/open-webui:main
# Lokal AI-chatbot interface
```

### Stable Diffusion (AI bildgenerering)

```bash
docker run -p 7860:7860 hlky/stable-diffusion-webui:latest
# Generera bilder med AI
```

## Roliga/Märkliga

### ASCII Aquarium

```bash
docker run -it jessfraz/hollywood
# Ser ut som hacker-film, men totalt harmlöst
```

### Bouncing DVD Logo

```bash
docker run -p 8080:8080 alexellis/dvd-logo
# Den klassiska DVD-loggan som studsar
```

### Matrix Rain Effect

```bash
docker run -it asciinema/asciicast2gif 113463
# Matrix "digital rain" effekt
```

### Webcam Test

```bash
docker run -p 8080:8080 --device=/dev/video0 alexellis/webcam-test
# Testa webbkamera genom container
```

## Produktivitet

### Nextcloud (personligt moln)

```bash
docker run -p 8080:80 nextcloud:latest
# Eget Google Drive/Dropbox
```

### Wiki.js

```bash
docker run -p 3000:3000 requarks/wiki:2
# Modern wiki-plattform
```

### Excalidraw (skiss-verktyg)

```bash
docker run -p 3000:80 excalidraw/excalidraw:latest
# Kollaborativt skiss-verktyg
```
