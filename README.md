# TagesDjump

git clone https://github.com/StaryiDed/TagesDjump.git

cd TagesDjump

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

uvicorn app.main:app --host 0.0.0.0 --port 8000

pytest -v app/tests/test_fibonacci.py

pytest -v app/tests/test_ping.py
