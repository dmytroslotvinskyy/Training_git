import shutil
print("Hello, World!")
print("Hello, dear Dmytro!")
def newfun2ction():
    print ('f')
    print ('u')
    print ('c')
    print ('k')


def copyfiles(original, target):
   # shutil.copyfile(original, target)
    shutil.copy2(original, target)
    print("Hello, " + name + ". Good morning!")


newfun2ction()
original = r'C:\Users\Ирина\Downloads\Cossacks European Wars'
target = r'D:\new'
copyfiles(original, target)