"""
a simple python script to parse json format grades inputs into GPA into csv format
"""

import os
import json


def load_config(file_path):
    with open(file_path) as data_sets:
        return json.load(data_sets)


def main():
    gpa_input_path = os.path.join(os.getcwd(), "gpa.json")
    if not os.path.exists(gpa_input_path):
        Exception('{} does not exist!'.format(gpa_input_path))
    data_sets = load_config(gpa_input_path)
    scores = data_sets['scores']
    grades_to_points = data_sets['grades_to_points']
    semester_list = [score['year'] for score in scores]
    semester_dict = {key: semester_list.count(key) for key in semester_list}
    terms = semester_dict.keys()

    line = '{}, {}, {}, {}, {}, {}'.format("term".capitalize(), "course".capitalize(), "credit".capitalize(),
                                           "grade".capitalize(), "term gpa".upper(), "cum gpa".upper())
    with open("gpa.csv", "w+") as csv:
        csv.write('{}\n'.format(line))
        print(line)
        cum_points = 0
        cum_credits = 0
        for term in terms:
            term_points = 0
            term_credits = 0
            for score in scores:
                course = score['course'].upper()
                credit = score['credit']
                grade = score['grade']
                points = grades_to_points.get(grade)
                year = score['year']
                if term == year:
                    term_points = float(term_points) + float(credit) * float(points)
                    term_credits = float(term_credits) + float(credit)
                    line = '{}, {}, {}, {}, {}, {}'.format(term.upper(), course, credit, grade, "", "")
                    csv.write('{}\n'.format(line))
                    print(line)
            term_average = term_points / term_credits
            line = '{}, {}, {}, {}, {}, {}'.format(term.upper(), "", "", "", float("{0:.2f}".format(term_average)), "")
            csv.write('{}\n'.format(line))
            print(line)
            cum_credits = float(cum_credits) + term_credits
            cum_points = float(cum_points) + term_points
            cum_average = cum_points / cum_credits
            line = '{}, {}, {}, {}, {}, {}'.format("", "", "", "", "", float("{0:.2f}".format(cum_average)))
            csv.write('{}\n'.format(line))
            print(line)
        csv.close()


if __name__ == '__main__':
    main()
