#! python3

def get_data():
    data = [6,5,1,1,1,3,1,1,1,9,1,1,7,1,9,1,1,1,6]
    return data

def get_peaks(data):
    peaks_list = []
    i = 1

    if data[0] > data[1]:
        peaks_list.append(data[0])

    for i in data:
        if data[i-1] < i and data[i+1] < i:
            peaks_list.append(i)
            i += 1
    return peaks_list

def get_valleys(data):
    valley_list = []
    i = 1

    if data[0] > data[1]:
        valley_list.append(data[0])

    for i in data:
        if data[i-1] > i and data[i+1] > i:
            valley_list.append(i)
            i += 1
    return valley_list
    

def main():
    peaks = get_peaks(get_data())
    valleys = get_valleys(get_data())
    peaks_and_valleys_list = []
    peaks_and_valleys_list.append(peaks)
    peaks_and_valleys_list.append(valleys)
    print(peaks_and_valleys_list)

main()

