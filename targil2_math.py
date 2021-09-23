num = 4567

# To print each digit number 4567

print("Alafim digit is: " + str(num//1000))
print("Meot digit is: " + str((num%1000)//100))
print("Asarot digit is: " + str(((num%1000)%100)//10))
print("Ahadot digit is: " + str(((num%1000)%100)%10))
