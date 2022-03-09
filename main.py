# Program for calculating digital root in Python by moonsidefan (v1.0.0)
import os


def main():
    # Editable values
    start = 0
    scale = 100
    inc = 3

    iteration = 0
    index = 0
    progress = 0
    progress_bar_steps = 25
    dr_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    value_validate(start, scale, inc)
    current = start
    print('Progress:                           0%')

    while current < scale:
        if current / scale >= progress + 0.01:
            progress += 0.01
            progress_bar(progress, progress_bar_steps)
        dr_count[digital_root_calculator(current)] += 1
        current += inc
        iteration += 1
    show_results(start, scale, inc, iteration, index, dr_count)


def value_validate(start, scale, inc):
    if start >= scale:
        print('Error: Start value (' + str(start) + ') must be smaller/equal the maximum value (' + str(scale) + ')')
        quit(1)
    elif inc <= 0:
        print('Error: Increment value cannot be smaller than 1')
        quit(1)


def digital_root_calculator(number):
    d_root = 0
    for figure in str(number):
        if not (figure == '.'):
            d_root += int(figure)
    if len(str(d_root)) > 1:
        d_root = digital_root_calculator(d_root)
    return d_root


def progress_bar(progress, steps):
    bar = ''
    for x in range(steps):
        if x < int(progress * steps):
            bar += '#'
        else:
            bar += ' '
    print('Progress: ' + bar + ' ' + str(int(progress * 100)) + '%')


def show_results(start, scale, inc, iteration, index, dr_count):
    print('Progress: ######################### 100%\n')
    print('+++ Results +++\n')
    print('Incremented by: ' + str(inc))
    print('From: ' + str(start) + ' (inclusive)')
    print('To: ' + str(scale) + ' (exclusive)')
    print('Iterations: ' + str(iteration) + '\n')
    for dr in dr_count:
        if dr == 1:
            print(str(index) + ': ' + str(round(dr / iteration * 100, 4)) + '%, (' + str(dr) + ' time)')
        else:
            print(str(index) + ': ' + str(round(dr / iteration * 100, 4)) + '%, (' + str(dr) + ' times)')
        index += 1
    quit(0)


if __name__ == '__main__':
    main()
