def getDataPoint(line):
    elements = line.strip().split(',')
    return (elements[0], elements[1], elements[2], (float(elements[1]) + float(elements[2]))/2)

def getRatio(a, b):
    if (b[3] == 0):
        return None
    return a[3]/b[3]

def main():
    lines = [
        "A,0.05,0.05",
        "B,0.05,0.06",
        "A,0.06,0.07",
        "B,0.06,0.08"
    ]

    data = []
    for line in lines:
        data.append(getDataPoint(line))

    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            a = data[i]
            b = data[j]
            if (a[0] != b[0]):
                ratio = getRatio(a, b)
                if (ratio != None):
                    print("%s/%s = %f" % (a[0], b[0], ratio))

if __name__ == "__main__":
    main()

input("Press Enter to Exit")