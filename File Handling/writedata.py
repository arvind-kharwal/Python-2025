import pickle
def writedata():
    with open('db.dat','wb') as f:
        records = []
        while True:
            r = input()
            name = input()
            mark = int(input())
            data = [r,name,mark]
            records.append(data)
            ch = input('Press y and n')
            if ch == 'n':
                break
        pickle.dump(records,f)
writedata()
