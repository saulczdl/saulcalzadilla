print("Please chose your option fron the list below: ")
list = ["1. Eat", "2. Drank", "3. Sleep", "4. Study", "5. Read a book",
        "6. Listen music", "7. Watch the news", "8. Walk whith your dog",
        "9. Pratice exercises", "0. Exit"]
# incluir while para gerar o menu select e exibir o menu até uma escolha,
# copiar do adventure e do hiLo.
option_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
option = ""
choice = "You choice was: {}. ".format(option)
#while option not in option_list:
while option != "0":
    for todomenu in list:
        print(todomenu)
    option = input("Choose a option number(1-9): ")
    choice = "You choice was: {} - ".format(option)
    if option == "1":
        print(choice + "Eat something healthy!!!")
    elif option == "2":
        print(choice + "Drank water!:")
    elif option == "3":
        print(choice + "Have you brushed your teeth yet?")
    elif option == "4":
        print(choice + "Check if your ambient have suitable conditions for a better concentration.")
    elif option == "5":
        print(choice + "Read something with content for your career!")
    elif option == "6":
        print(choice + "Use your phones!")
    elif option == "7":
        print(choice + "Don't forget to watch JovemPan channel on YouTube!")
    elif option == "8":
        print(choice + "Don't forget to bring a bag to pickup your dog's poop. ")
    elif option == "9":
        print(choice + "Remember, run is very important for your health, just don't make only bodybuilding.")
    elif option == "0":
        print(choice + "Bye bye!!!")
else:
    exit()