def print_chart(chart):
    print(chart_to_string(chart))

def chart_to_string(chart):
    string = ""
    num_rows = len(chart)
    num_cols = len(chart[0])
    for col in range(num_cols):
        for row in range(num_rows):
            string += chart[row][col]
        string += "\n"
    string += "\n"
    return string


def sort_chart(chart):
    def greater(a, b):
        # A > B ?
        for i in range(len(a)):
            if a[i] == "*":
                return True
            if b[i] == "*":
                return False
        return False
    for i in range(len(chart) - 1):
        for j in range(0, len(chart) - i - 1):
            if greater(chart[j], chart[j + 1]):
                chart[j], chart[j + 1] = chart[j + 1], chart[j]


def process(data):

    chart = convert(data)
    sort_chart(chart)
    return chart_to_string(chart)

def convert(data):
    # of data
    num_rows = len(data)
    num_cols = len(data[0])

    chart = [[None for _ in range(num_rows)] for _ in range(num_cols)]
    for row in range(num_rows):
        for col in range(num_cols):
            chart[col][row] = data[row][col]
    return chart


result = ""
try:
    while True:
        data = []
        while True:
            line = input()
            if line == "":
                result += process(data)
                break
            data.append(line)
except:
    pass
print(result[:-2])
