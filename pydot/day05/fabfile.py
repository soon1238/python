from fabric.api import local,lcd

def hello():
    print("EXECUTING HELLO....")
    local("python --version")

def startnb():
    print("Going to start Jupyter notebook")
    dirname ="/Users/tecksoon/ISS/pyCourse/pydot/day05"
    with lcd(dirname):
        local ("source activate pydot4")
        local ("jupyter notebook")
