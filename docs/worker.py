#open and read the file after the appending:
f = open("run.py", "a")
f.write("""
from app import app

if __name__='__main__':
    app.run
""")
f.close()
f=open('run.py', 'r')
print(f.read())