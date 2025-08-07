dict={"Alice":85,"John":75,"Avish":90,"Sanket":95,"Avi":65,"Neeru":80}
name=input("Enter your Student's name: ")

if name in dict:
    print(name+"'s marks:",dict[name])
else:
    print("Student not found.")
