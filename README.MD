1. Buat venv dengan nama folder env
2. Kemudian install dari requirement dengan pip3
3. Masuk ke venv dan activate
4. Kemudian mulai app "python3 main.py"
5. Atau jalankan production "python3 -m gunicorn -w 4 -b 0.0.0.0:8000 main:app"