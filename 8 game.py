reward = 1000
print("your primery score is 1000")
print("p, jump to next level")
print("R, 1000 reward")
print("B, minus 10 from reward")
print("*, game over")

choose = input("Choose an option: ")

if (choose=="p" or choose=="P"):
    print("Jump to next level")
elif (choose == "R" or choose=="r"):
    name = input("Write your name: ")
    print(name,reward+1000)
elif (choose=="B" or choose=="b"):
    reward -= 10
    print("Minus 10 from reward, new reward is:", reward)
elif (choose == "*"):
    print("Game over")
else:
    print("None")