#!/usr/bin/env python3
import subprocess, webbrowser, time, urllib.request, pathlib, sys

PROJECT = pathlib.Path("/Users/hlibpakhomov/PycharmProjects/personal-website")


if not PROJECT.exists():
    print("ERROR: hlib-portfolio folder not found in Downloads.")
    sys.exit(1)

# Kill anything already on port 3000
subprocess.run("lsof -ti:3000 | xargs kill -9 2>/dev/null; true", shell=True)
time.sleep(1)

print("Starting portfolio...")

proc = subprocess.Popen(
    ["npm", "run", "dev"],
      cwd=PROJECT,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)

# Wait for server to be ready (up to 30s)
ready = False
for i in range(30):
    time.sleep(1)
    try:
        urllib.request.urlopen("http://localhost:3000", timeout=2)
        ready = True
        break
    except Exception:
        print(f"  starting... {i+1}s")

if not ready:
    print("Server took too long. Try opening http://localhost:3000 manually.")
else:
    print("Ready! Opening http://localhost:3000")
    webbrowser.open("http://localhost:3000")

print("Press Ctrl+C to stop the server.\n")

try:
    proc.wait()
except KeyboardInterrupt:
    proc.terminate()
    print("Server stopped.")