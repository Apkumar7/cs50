def main():
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")


def value(x):
    x = x.lower()
    if x.startswith("hello ") or x.startswith(" hello ") or x.startswith("hello"):
        return(0)

    elif x.startswith("h"):
        return(20)

    else:
        return(100)

if __name__ == "__main__":
    main()