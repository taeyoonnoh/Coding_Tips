# 통과는 했지만 조금 비효율적..

from collections import deque

roman_to_num_dict = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

class RomanNumerals : 
    def to_roman(num) : 
        a = str(num)
        answer = ''
        index = 0
        for i in range(len(a)-1,-1,-1) : 
            b = a[i]
            if b == '0' : 
                index+=1
                continue
            elif '0' < b < '4' : 
                if index==0 :
                    multiplier = int(b) * 'I'
                elif index == 1 :
                    multiplier = int(b) * 'X'
                elif index == 2 :
                    multiplier = int(b) * 'C'
                else :
                    multiplier = int(b) * 'M'
                answer = multiplier + answer 
            elif '5' < b < '9' : 
                if index == 0 :
                    multiplier = (int(b) - 5) * 'I'
                    adder = 'V' + multiplier
                elif index == 1 :
                    multiplier = (int(b) - 5) * 'X'
                    adder = 'L' + multiplier
                elif index == 2 :
                    multiplier = (int(b)-5) * 'C'
                    adder = 'D' +multiplier
                answer = adder + answer
            elif b == '5' : 
                if index == 0 :
                    answer = 'V' + answer
                elif index == 1 :
                    answer = 'L' + answer
                else :
                    answer = 'D' + answer
            else :
                if b == '4' : 
                    if index == 0 :
                        answer = 'IV' + answer
                    elif index == 1 :
                        answer = 'XL' + answer
                    else :
                        answer = 'CD' + answer
                else :
                    if index == 0 :
                        answer = 'IX' + answer
                    elif index == 1 :
                        answer = 'XC' + answer
                    else :
                        answer = 'CM' + answer
            index+=1

        return answer

    def from_roman(letter) : 
        queue = deque(letter)
        prev = roman_to_num_dict[queue.pop()]
        summed = prev
        while queue : 
            curr = roman_to_num_dict[queue.pop()]
            if curr >= prev :
                summed +=curr
            else :
                summed-=curr
            prev = curr
        return summed
