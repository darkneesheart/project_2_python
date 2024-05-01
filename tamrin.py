reward = 1000

print("p, jump to next level")
print("R, 1000 reward")
print("B, minus 10 from reward")
print("×, game over")

choose = input("Choose an option: ")

if choose == "p":
    print("Jump to next level")
elif choose == "R":
    name = input("Write your name: ")
    print(name + ", 1000 reward")
elif choose == "B":
    reward -= 10
    print("Minus 10 from reward, new reward is:", reward)
elif choose == "×":
    print("Game over")
else:
    print("None")