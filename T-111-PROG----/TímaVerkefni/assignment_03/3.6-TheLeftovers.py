number_of_players =int(input())
while number_of_players < 2:
    number_of_players =int(input())

sum = 0

counter = 0
while counter < number_of_players:

    fingers =  int(input())
    sum= sum+fingers
    counter +=1

remainder = sum % number_of_players

print(f"The sum of all contributions is {sum}")
print (f"When {sum} is divided by {number_of_players}, the remainder is {remainder}")
print (f"Player {remainder} is the winner!")
    




 