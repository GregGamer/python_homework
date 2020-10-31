def fizzbuzz() :
    print("\n".join( "Fizz" * (i%3==0) + "Buzz" * (i%5==0) or str(i) for i in range(1,101) ))

def changeVariables() :
    x = 100
    y = 200
    x, y = y, x
    print(x, y)


def main() :
    # fizzbuzz()
    changeVariables()


if __name__ == "__main__":
    main()