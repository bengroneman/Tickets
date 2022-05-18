# Tickets
Ticketing application concept

# Deployment
[![Netlify Status](https://api.netlify.com/api/v1/badges/2beb0727-f5a1-4f80-a53c-cd03b47b96cf/deploy-status)](https://app.netlify.com/sites/brave-newton-e914b3/deploys)

> [Client](https://brave-newton-e914b3.netlify.app)

## Running locally

```bash
git clone https://github.com/bengroneman/Tickets.git
```
```bash
cd Tickets/tickets_client
```
```bash
npm install
```
```bash
npm install nuxt
```
```bash
npm run dev
```
## Server setup

```bash
cd ../tickets_server
```
```bash
python3 -m venv venv
```
```bash
source env/bin/activate
```
```bash
pip install django django-allauth django-filter django-cors-headers
```
```bash
python manage.py migrate
```
```bash
python manage.py makemigrations
```
```bash
python manage.py runserver
```

