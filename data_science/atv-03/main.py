
def main():

    rows, test_row = map(int, input().split(' '))
    data_1 = map(int, input().split(' '))
    data_2 = map(int, input().split(' '))
    data_3 = map(int, input().split(' '))

    data_1 = list(data_1)
    data_2 = list(data_2)
    data_3 = list(data_3)

    def start_process(data_1: list, data_2: list) -> float:
        result = float((data_1[-1] + data_2[-1]) / 2)

        return result


    print(start_process(data_1, data_2))

if __name__ == "__main__":
    main()
