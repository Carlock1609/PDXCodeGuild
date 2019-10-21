#! python3

# v1

# figured out how to get last digit, now just get the first digit
# I dont think data[i-1] will work because it still doesnt know the index
# try using index to check for it in the list to compare
# use two tables? -> one with the index list and one with the data list. and compare over eachother
# Top is data, bottom is index. check data retain the index. 

def get_data():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    return data

def get_peaks(data):
    peaks = []
    index_list = list(range(len(data)))

    for i in index_list:
        if (i-1) in index_list and (i+1) in index_list: # makes the index start at 1 so the indexing is not out of range?
            if data[i] >= data[i-1] and data[i] >= data[i+1]:
                peaks.append(i)
    return peaks

def get_valleys(data):
    valleys = []
    index_list = list(range(len(data)))

    for i in index_list:
        if (i-1) in index_list and (i+1) in index_list: # makes the index start at 1 so the indexing is not out of range?
            if data[i] <= data[i-1] and data[i] <= data[i+1]:
                valleys.append(i)
    return valleys

def peaks_and_valleys(peaks, valleys):
    return peaks+valleys

def main():
    peaks = get_peaks(get_data())
    valleys = get_valleys(get_data())
    print(peaks_and_valleys(peaks, valleys))
main()
