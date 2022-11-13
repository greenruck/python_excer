def freq_count(combo):
    
    Frequency = {}
   
    for i in combo:
        Frequency[i] = Frequency.get(i, 0)+1
    
    return Frequency


def same_frequency(num1, num2):
    
    return freq_count(str(num1))==freq_count(str(num2))

