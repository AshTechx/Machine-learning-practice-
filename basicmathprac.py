# student marks analysis 
marks = [45, 56, 78, 90, 67, 78, 56, 89, 45, 78]
a =0
for i in (marks):
  a = a + i
  n = len(marks)
mean = a/n
print(mean)



#median 
mid = round(len(marks)/2)

if (mid %2==0):
  median = (marks[mid-1]+marks[mid])/2
else:
 median = marks[mid]

print("the median is ",median)

#mode 

num1 = marks.count(marks[0])
num2 = marks.count(marks[1])
num3= marks.count(marks[2])
num4= marks.count(marks[3])
num5= marks.count(marks[4])
num6= marks.count(marks[5])
num7= marks.count(marks[6])
num8= marks.count(marks[7])
num9= marks.count(marks[8])

print(marks[0],num1)
print(marks[1],num2)
print(marks[2],num3)
print(marks[3],num4)
print(marks[4],num5)
print(marks[5],num6)
print(marks[6],num7)
print(marks[7],num8)
print(marks[8],num9)

counts = [num1,num2,num3,num4,num5,num6,num7,num8]
maximum = max(counts)
max_index = counts.index(maximum)
print("the mode is",marks[max_index])


# percentage problem 
scores = [78, 45, 92, 60, 33]
l1=[]
for i in range (len(scores)):
  percent = (scores[i]/100)*100
  l1.append(percent)
  print (f" the percentage of each student is as follows {percent}%")
print(l1)
total = 0
for i in range (len(scores)):
  total = scores[i]+total
print(total)
avg = total/len(scores)
avg_percent = (avg)/100*100
print(f" the average percentage of the clas is {avg_percent} %")
for i in range (len(l1)):
  if (l1[i]>50):
   print(f"smart student the percentage is higher than 50 the index is {i}")

