class FrequencyCounter:
    def Frequency(self, arr):
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
        maxFreq = 0
        minFreq = len(arr)
        maxEle = 0
        minEle = 0
        for element, count in freq_map.items():
            if count > maxFreq:
                maxFreq = count
                maxEle = element
            if count < minFreq:
                minFreq = count
                minEle = element
        print("The highest frequency element is:", maxEle)
        print("The lowest frequency element is:", minEle)
if __name__ == "__main__":
    fc = FrequencyCounter()
    arr = [10, 5, 10, 15, 10, 5]
    fc.Frequency(arr)