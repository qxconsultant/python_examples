"""
a simple python script to parse json format grades inputs into GPA into csv format
"""
grades_to_points = {
    'A': '4.0',
    'A-': '3.7',
    'B+': '3.3',
    'B': '3.0',
    'B-': '2.7',
    'C+': '2.3',
    'C': '2.0',
    'D': '1.0',
    'F': '0'
}
scores = [
    {'course': 'biol200', 'credit': '3', 'grade': 'B+', 'year': 'fall 2017'},
    {'course': 'math203', 'credit': '3', 'grade': 'B+', 'year': 'fall 2017'},
    {'course': 'mimm211', 'credit': '3', 'grade': 'B', 'year': 'fall 2017'},
    {'course': 'mimm212', 'credit': '3', 'grade': 'A', 'year': 'fall 2017'},
    {'course': 'chem181', 'credit': '3', 'grade': 'A', 'year': 'winter 2018'},
    {'course': 'biol300', 'credit': '3', 'grade': 'B', 'year': 'fall 2018'},
    {'course': 'biol306', 'credit': '3', 'grade': 'B', 'year': 'fall 2018'},
    {'course': 'esat204d1', 'credit': '4.5', 'grade': 'A-', 'year': 'fall 2018'},
    {'course': 'biol201', 'credit': '3', 'grade': 'B+', 'year': 'winter 2019'},
    {'course': 'biol303', 'credit': '3', 'grade': 'B-', 'year': 'winter 2019'},
    {'course': 'biol313', 'credit': '3', 'grade': 'B+', 'year': 'winter 2019'},
    {'course': 'esat204d2', 'credit': '4.5', 'grade': 'A-', 'year': 'winter 2019'},
    {'course': 'biol202', 'credit': '3', 'grade': 'C+', 'year': 'summer 2019'}
]


def main():
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
