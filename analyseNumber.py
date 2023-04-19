def analyse_num_input():
    postives = 0
    negatives = 0
    sum = 0
    count = 0

    while 1:
        num_input = int(input("Enter an int value (Program exits on 0): "))
        if num_input == 0:
            break
        sum += num_input
        count += 1

        if num_input > 0:
            postives += 1
        else:
            negatives += 1

    print("The number of positives is {}".format(postives))
    print("The number of negatives is {}".format(negatives))
    print("The total is {}".format(sum))
    print("The average is {}".format(sum/count))


analyse_num_input()
