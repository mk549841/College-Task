def makebold(fn):
    return lambda:"<b>" + fn() + "</b>"

def makeitalic(fn):
    return lambda:"<i>" + fn() + "</i>"

def makeunderline(fn):
    return lambda:"<u>" + fn() + "</u>"
@makebold
@makeitalic
@makeunderline
def hello():
    return "hello world"
print(hello())
