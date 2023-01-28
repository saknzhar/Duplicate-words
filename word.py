import sys
def print_words(file_name, word, count):
    file_obj = open(file_name, 'x')
    for _ in range(count):
        file_obj.write(word + "\n")
    file_obj.close()
    print("File Created")


def main():
    file_name = sys.argv[1]
    word = sys.argv[2]
    count = int(sys.argv[3])
    print_words(file_name, word, count)


if __name__ == "__main__":
    try:
        main()
    except:
        print("Error")
