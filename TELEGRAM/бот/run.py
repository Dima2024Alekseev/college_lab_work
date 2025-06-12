import subprocess

files = ["bot.py", "parser.py"]
for file in files:
     subprocess.Popen(args=["start", "python", file], shell =True, stdout=subprocess.PIPE)