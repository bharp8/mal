from inspect import EndOfBlock


def READ[T](readIn: T) -> T:
    return readIn

def EVAL[T](evalIn: T) -> T:
    return evalIn

def PRINT[T](printIn: T) -> T:
    return printIn

def rep[T](funcIn: T) -> T:
    return PRINT(EVAL(READ(funcIn))) 

def main():
    while(True):
        try:
            print(rep(input("user> ")))
        except EOFError:
            break

if __name__ == "__main__":
    main()

