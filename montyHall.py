import sys,random

rounds = 100000
wins = 0


random.seed()                                                       #rastgele sayı üretecini başlatmak için kullanılır

print("Do you want to change your choice? Choose 1 if you do")
answer = input()                                         

for i in range(rounds):
    doors = ["Car", "Goat", "Goat"]
    random.shuffle(doors)                                            #array'in elemanlarını karıştır

    playerPick = random.randint(0,2)
    managerPick = random.randint(0,2)                         

    while managerPick == playerPick or doors[managerPick] != "Goat": #goat olan ve seçimin dışında kalan kapılardan birini alıyoruz
        managerPick = random.randint(0,2)                         

    goatDoor = managerPick

    if answer =='1':                                                   #playerPick değişim işlemi
        playerPick = 3 - (playerPick + goatDoor)

    if doors[playerPick] == "Car":
        wins +=1

print("You played", rounds, "rounds, and won", wins, "of them!")