import student
import time

def insert(SL):
    start = time.time()
    frank = open('/home/valencia/Documents/Python Assignments/InsertNames.txt','r')
    for line in frank:
        check = True 
        words = line.split()
        S = student.student(words[0],words[1],words[2],words[3],words[4])
        for i in SL:
            if i == S:
                print 'duplicate student error'
                print S.Fname+' '+S.Lname
                check = False
        if check:
            SL.append(S)
    print 'done'
    print time.time()- start
                
                
    
def delete(SL):
    start = time.time()
    Delete = open('/home/valencia/Documents/Python Assignments/DeleteNames.txt','r')
    for line in Delete:
        ssn = line.strip()
        fail =True
        other = student.student('','',ssn,'',0)
        for i in range(len(SL)):
            if SL[i] == other:
                fail = False
                SL.pop(i)
                break
        if fail:
            print 'no student at '+other.ssn
            
    print time.time()- start

def retrieve(SL):
    start = time.time()
    select = open('/home/valencia/Documents/Python Assignments/RetrieveNames.txt','r')
    totalage = 0
    numofstudents = 0
    for line in select:
        ssn = line.strip()
        check =True
        other = student.student('','',ssn,'',0) 
        for S in SL:
            if S == other:
                totalage += S.age
                numofstudents += 1
                check = False
                break
        if check:
            print 'no student at '+other.ssn
    print round(float(totalage)/float(numofstudents),4)
    print time.time()- start
    
def travers(SL):
    start = time.time()
    totalage = 0
    numofstudents = 0
    for s in SL:
        totalage += s.age
        numofstudents += 1
    print round(float(totalage)/float(numofstudents),4)
    print time.time()- start
    
def main():
    
    SL = []
    print'insert'
    insert(SL)
    print 'travers'
    travers(SL)
    print'delete'
    delete(SL)
    print'retrieve'
    retrieve(SL)
    
    
    

main()
    
