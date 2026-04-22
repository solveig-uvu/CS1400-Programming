# Reader function that returns a list of the text and each time a severity level occurs.
def logReader(file:str="server_logs.txt") -> list:
    reader = open(file, 'r')
    logs = []
    data = {}
    for line in reader:
        logLevel, logText = line.strip('\n').split('|')
        logs.append(logText)
        if logLevel not in data:
            data[logLevel] = 1
        else:
            data[logLevel] += 1
    compiledLogs = [data, logs]
    return compiledLogs

def longestMessage(logs:list) -> str:
    sortedLogs = sorted(logs, key=len)
    return sortedLogs[-1]

# Main file output function.
def outputToFile(logs:list, file:str="outputSummary.txt") -> None:
    if file.endswith('.txt'):
        writer = open(file, 'w')
    else:
        writer = open(f'{file}.txt', 'w')
    data = dict(logs[0])
    longest = longestMessage(logs[1])
    writer.write('Log Summary\n\n')
    for key in data:
        value = data[key]
        writer.write(f'{key}: {value}\n')
    writer.write(f"\nLongest message: {longest}")

def main():
    logs = logReader()
    outputToFile(logs)

if __name__ == '__main__':
    main()