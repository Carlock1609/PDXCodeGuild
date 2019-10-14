#! python3

# v1

# find solution for the first iteration and how to skip it on the for loop

def get_data():
    data = [9,5,1,1,1,3,1,1,1,9,1,1,7,1,9,1,1,1,]
    return data

def get_peaks(data):
    peaks_list = []

    if data[0] > data[1]:
        peaks_list.append(data[0])

    for i in data:
        if data[i-1] < i and data[i+1] < i:
            peaks_list.append(i)
    return peaks_list

def get_valleys(data):
    pass
    

def main():
    peaks = get_peaks(get_data())
    valleys = get_valleys(get_data())
    peaks_and_valleys_list = []
    peaks_and_valleys_list.append(peaks)
    peaks_and_valleys_list.append(valleys)
    print(peaks_and_valleys_list)


