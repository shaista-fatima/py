# class=template
# object=instance of class
# DRY   = Do not repeat urself

class students:
    pass
harry=students()
larry=students()
harry.name="harry" #variable
harry.std=5
harry.roll_no=2356
larry.name="larry" #variable
larry.std=50
larry.roll_no=23
larry.subjects=["hindi","english"]
print(harry.name,larry.subjects)