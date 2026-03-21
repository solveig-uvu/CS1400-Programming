def quoteReader(file:str='quotes_data.txt') -> list:
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
    print(sortedQuotes)
    return sortedQuotes



def main():
    quotes = quoteReader('test.txt')
    lengthSorter(quotes)
    idSorter(quotes)

if __name__ == '__main__':
    main()