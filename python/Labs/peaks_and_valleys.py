#! python3

# v1

# find solution for the first iteration and how to skip it on the for loop
# and the last

def get_data():
    data = [6,5,1,1,1,3,1,1,1,9,1,1,7,1,9,1,1,1,8,]
    return data

def get_peaks(data):
    peaks_list = []

    for i in data:
        if i == data[0] and data[i+1] < i:
            peaks_list.append(i)
        else:
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

print(get_peaks(get_data()))

