def quoteReader(file:str) -> list:
    reader = open(file, 'r')
    quotes = []
    for line in reader:
        quoteText, authorID = line.strip('\n').split('|')
        readQuote = quoteText, authorID
        quotes.append(readQuote)
    return quotes

# Helper functions for sorting by length and ID number, as well as figuring out average quote lengths.
def lengthSorter(quotes:list) -> list:
    baseQuotes = []
    for line in quotes:
        baseQuotes.append(line[0])    
    sortedQuotes = sorted(baseQuotes, key=len)
    return sortedQuotes

def idSorter(quotes:list) -> list:
    sortedQuotes = sorted(quotes, key=lambda quotes: quotes[1])
    return sortedQuotes

# Helper functions for statistics
def quoteTotal(quotes:list) -> int:
    total = 0
    for i in quotes:
        total += 1
    return total

def averageLength(quotes:list) -> int:
    avgLength = sum(len(q) for q in quotes) / len(quotes)
    return round(avgLength)

def longestQuote(quotes:list) -> str:
    sortQuotes = lengthSorter(quotes)
    return sortQuotes[-1]

# Creating a function to do all of this for the user with ANY specified text.

def quotesStats(file:str='quotes_data.txt') -> None:
    writer = open('sortedQuotes.txt', 'w')
    if file.endswith('.txt'):
        quotes = quoteReader(file)
    else:
        quotes = quoteReader(f'{file}.txt')

    lengthSorted = lengthSorter(quotes)
    idSorted = idSorter(quotes)
    total = quoteTotal(quotes)
    avg = averageLength(quotes)
    longest = longestQuote(quotes)

    writer.write('Sorted Quotes\n===========================\n')
    for line in range(len(quotes)):
        writer.write(f'{lengthSorted[line]}\n')
    writer.write('\n')
    for line in range(len(quotes)-1):
        writer.write(f'{idSorted[line][0]} | {idSorted[line][1]}\n')
    writer.write(f'{idSorted[line][0]} | {idSorted[-1][1]}\n \n \n')
    writer.write('Statistics\n===========================\n')
    writer.write(f'Total quotes: {total}\nAverage quote length: {avg}\nQuote with most words: {longest}')

def main():
    quotesStats()

if __name__ == '__main__':
    main()