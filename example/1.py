import os

def w(x):
    print(x)
    global y
    y = x**2



def main():
    x=5
    w(x)
    print(y)
    os.system('2.py')

if __name__ == "__main__":
    main()