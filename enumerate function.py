#  if we want to buy odd numbers from list
l=["pizza","gulabjamun","kfc","mirchi"]
# i=1
# for item in l:
#     if i%2 is not 0:
#         print(f"jarvis please bring {item}")
#     i+=1
# **using enumerate function***

for index,item in enumerate (l):
    if index%2 == 0:
        print(f"jarvis please buy {item}")
