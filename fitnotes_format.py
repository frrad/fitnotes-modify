#!/usr/bin/python

import csv


def summarize(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        accumulate = []

        for row in reader:

            [date, exercise, category, weight, reps, _, _, _] = row

            if accumulate == []:
                accumulate = [date, exercise, (weight, 1, reps)]
            elif accumulate[0] == date and accumulate[1] == exercise:
                if accumulate[-1][0] == weight and accumulate[-1][2] == reps:
                    accumulate[-1] = (weight, accumulate[-1][1] + 1, reps)
                else:
                    accumulate.append((weight, 1, reps))
            else:
                yield accumulate
                accumulate = [date, exercise, (weight, 1, reps)]
        yield accumulate


def display(generator):
    label = ''
    for line in generator:
        if line[0] != label:
            label = line[0]
            print "\n", label
        print ",".join([line[1]] + ["{0}".format(*triple) for triple in line[2:]])
        print ",".join([''] + ["{1}x{2}".format(*triple) for triple in line[2:]])

display(summarize('FitNotes_Export_2016_05_02_08_29_22.csv'))
