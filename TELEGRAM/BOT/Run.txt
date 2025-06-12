import subprocess

files = ["5B.py", "test.py"]
for file in files:
     subprocess.Popen(args=["start", "python", file], shell =True, stdout=subprocess.PIPE)