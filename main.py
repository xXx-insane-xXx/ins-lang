f = open("test.ins")
code = f.read()
# print(list(code))

int_holder = []
result = 0

def add(li):
    global result
    for i in li:
        result += i

for word in code:
    try:
        if int(word):
            int_holder.append(int(word))
    except:
        pass
    if word == "+":
        add(int_holder)
        
    if word == ".":
        print(result)
