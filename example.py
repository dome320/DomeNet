from Network import network

def main():

    n: network = network([2, 3, 1])
    print(n) 
    n.forward([1.0, 0.5])
    print(n)

if __name__ == "__main__":
    main()