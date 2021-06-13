class Calculator(object):
    def evaluate(self, string):
        a = string.split(" ")
        
        pri_dict = {
            '(' : 3,
            '*' : 2,
            '/' : 2,
            '+' : 1,
            '-' : 1
        }

        num_stack_list = []
        oper_stack_list = []

        for i in a :
            if i.isnumeric() : # int 형이거나
                num_stack_list.append(i)

            elif '.' in i: # float 형이면 해당 문자 append
                num_stack_list.append(i)
            
            elif i == '(' : 
                oper_stack_list.append(i)

            elif i == ')' : 
                while oper_stack_list and oper_stack_list[-1] !='(' : # '(' 전까지 계속 pop
                    num_stack_list.append(oper_stack_list.pop())
                oper_stack_list.pop() # 마지막은 '(' 로 되어 있으니까 pop

            else : 
                while oper_stack_list and oper_stack_list[-1]!='(' and pri_dict[i]<=pri_dict[oper_stack_list[-1]] : # 더하기나 빼기 나올때까지 pop
                    num_stack_list.append(oper_stack_list.pop())
                oper_stack_list.append(i) # 이 이외에는 그냥 append

        while oper_stack_list : 
            num_stack_list.append(oper_stack_list.pop()) # 마지막에 남아 있는 operator 는 그냥 pop 시키기
        
        stack = []
        for i in num_stack_list : # 왼쪽부터 오른쪽으로 연산하기
            if i.isnumeric() : 
                stack.append(int(i))

            elif '.' in i :
                stack.append(float(i))
                
            else :
                b = stack.pop()
                a = stack.pop()
                if i == '+' : 
                    stack.append(a+b)
                elif i == '-' : 
                    stack.append(a-b)
                elif i == '*' : 
                    stack.append(a*b)
                elif i == '/' : 
                    stack.append(a//b)
        
        return stack[0]
