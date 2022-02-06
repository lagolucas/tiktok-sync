# tiktok-sync
 Sincronizador com banco de dados dos dados do tiktokscrapper

Ordem dos comandos:

- `curl -L -o tiktok-sync/tasks.txt "https://docs.google.com/spreadsheets/d/e/2PACX-1vQrVDas124s2bzOCBs9fN_hFKQWfvV_WL7BKRcifyELBVC84nBNhk1hstaD1BCYFY0AZYwcxBtSV9a9/pub?gid=0&single=true&output=csv"`

- `tiktok-scraper from-file tiktok-sync/tasks.txt 6 -n 0 -t csv --filepath tiktok-sync/`
  
- `python3 tiktok-sync/insert.py`

- `rm tiktok-sync/*.old`
