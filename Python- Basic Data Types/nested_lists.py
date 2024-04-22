if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
records.sort(key= lambda col: (col[1], col[0]))
           
print(records)