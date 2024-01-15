def draw():
    blocks = int(input())
    for n in range(blocks + 1):
        print(" " * n * 2 + "+-+")
        print(" " * n * 2 + "  " + "| |")
        print(" " * n * 2 + "    " + "+-", end="")

def main():
    draw()

if __name__ == "__main__":
    main()