def main():
    print("hello")
    i = 20
    j = 30
    i, j = j, i
    print("i=%d; j=%d\n" % (i, j))
    pass


if __name__ == '__main__':
    main()
