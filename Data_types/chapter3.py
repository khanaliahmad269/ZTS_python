#Strings
#core 
First_Name= "Ali"
Last_Name= "Ahmad"
print(First_Name)
print(Last_Name)
print(First_Name + Last_Name)
full_name = First_Name + Last_Name
print(full_name)




#indexing 
photo= "Photography"
print(photo[::1])
print(photo[::-1])


#encoding

encoded_photo = photo.encode("utf-8")
print(encoded_photo)


decoded_photo = encoded_photo.decode("utf-8")
print(decoded_photo)
