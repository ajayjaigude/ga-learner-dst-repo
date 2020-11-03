# --------------
class_1 = ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
print(class_1)
class_2 = ['Hilary Mason', 'Carla Gentry','Corinna Cortes']
print(class_2)
new_class = class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)

courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}
math=courses.get("Math")
english=courses.get("English")
history=courses.get("History")
french=courses.get("French")
science=courses.get("Science")
total=math+english+history+french+science
print(total)
percentage = total/len(courses)
print(percentage)

mathematics = {'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

topper = max(mathematics,key=mathematics.get)
print(topper)

splite_name = topper.split(" ")
first_name = splite_name[0]
last_name = splite_name[1]

cert = last_name + " " + first_name
certificate_name = cert.upper()
print(certificate_name)








