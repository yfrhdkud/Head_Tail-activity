list = [int(x) for x in input("Enter 3 numbers to be separated by spaces: ").split()]
guess = int(input(f"What is the head of the {list}?: "))
print(f"Head: {list[0]}, your guess: {guess}")

if guess == list[0]:
    print("Your guess was correct")
else:
    print("Your guess was wrong")