# dict example program is :
D1 = {12:{"class":"b-tech","branch":"ece","percentage":62.10}
,13:{"class":"b-tech","branch":"ece","percentage":72.10}
,14:{"class":"b-tech","branch":"ece","percentage":82.10}
}
rollNumber = int(input('enter your roll number:'))
percentage = D1[rollNumber]["percentage"]
if (percentage > 45):
    print ("candidate is passed")
else:
    print("candidate is failed")
    