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
  


newfun2ction()
original = r'***************************'
target = r'************************'
copyfiles(original, target)