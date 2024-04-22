print("homework:dictionary")
D1={"age":25,"time":17.19,"id":2741585993}
print(D1)
print(len(D1))
if"name"in D1:print("name exists")
#output is noting
D2={ "name":"mohammadreza",
    "dars":"pishrafte",
    "day":"wensday"}
D2.update(D1)
print(D2)
if"name"in D2:print("name exists")
#output is name exists
print(D2.pop("id"))
#حذف میکنه ولی مقدار رو برمیگردونه
print(D2)