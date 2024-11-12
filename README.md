# playwright_vnc

HEADED=true docker-compose up --build

Running your tests in headed mode:
docker-compose exec playwright-python pytest tests/test_example.py --headed -v
Start record new test by doing things in browser in VNC window
docker-compose exec playwright-python python -m playwright codegen --target python -o tests/my_test.py

docker-compose exec playwright-python python -m playwright --version

Linux:
sudo apt-get install tigervnc-viewer

vncviewer localhost:5900


Windows?

https://www.tightvnc.com/download.php