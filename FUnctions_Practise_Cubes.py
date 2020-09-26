

def main():      #define function for main
    result1 = cubeVolume(2)    # store resut from CubeVolume function in result 1
    result2 = cubeVolume(10)
    print('A cube with side length 2 has volume ', result1)
    print('A cube with side length 10 has volume ', result2)

def cubeVolume(sidelenght):   # define function cubeVolume
    volume = sidelenght ** 3
    return volume   #return value to parent function

main()


def boxString(content):
    n = len(content)
    if n == 0 :
        return 0
    print("-" * (n+4))
    print("!", content, "!")
    print("-" * (n+4))

boxString(input("Enter any string: "))
