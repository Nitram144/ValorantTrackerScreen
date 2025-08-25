import requests ,os ,json

def tracker():

    os.system("cls")

    if os.path.exists("key.json"):
        with open("key.json", "r") as read:
            key_data = json.load(read)
            key = key_data["key"] 

    else:

        print("\033[31mGet your key here > https://discord.gg/EUCyQwxGUM\033[0m")
        key = str(input("\033[35mKey > \033[0m"))
        with open("key.json", "w") as write:
            json.dump({"key": key}, write)

    player_name = str(input("Player name > "))
    player_tag = str(input("Player tag > "))

    player_region = "eu" #Possible values: 'eu' 'na' 'latam' 'br' 'ap' 'kr'

    headers = {"Authorization": key}

    player_acc_url = f"https://api.henrikdev.xyz/valorant/v1/account/{player_name}/{player_tag}"

    try:

        player_acc = requests.get(player_acc_url, headers=headers)
        acc_data = player_acc.json()
        player_puuid = acc_data["data"]["puuid"]
        player_level = acc_data["data"]["account_level"]
        player_last_update = acc_data["data"]["last_update"]
        player_card = acc_data["data"]["card"]
    
    except Exception as err:

        print("\033[31mKey ,Player name or Player tag is incorrect...\033[0m")
        input("\033[33mPress enter to return to the menu...\033[0m")

        menu()

    player_mmr_url = f"https://api.henrikdev.xyz/valorant/v2/mmr/{player_region}/{player_name}/{player_tag}"
    player_mmr = requests.get(player_mmr_url, headers=headers)
    mmr_data = player_mmr.json()
    player_peak_rank = mmr_data["data"]["highest_rank"]["patched_tier"]
    player_current_rank = mmr_data["data"]["current_data"]["currenttierpatched"]

    print("\033[37m{--------------Account Info--------------}\033")

    print(f"\033[94mPlayer Name > \033[0m{player_name}#{player_tag}")
    print(f"\033[94mPlayer Level > \033[0m{player_level}")
    print(f"\033[94mPlayer Highest Rank > \033[0m{player_peak_rank}")
    print(f"\033[94mPlayer Rank > \033[0m{player_current_rank}")
    print(f"\033[93mLast Update > \033[0m{player_last_update}")
    input("\033[33mPress enter to return to the menu...\033[0m")

    menu()

def help():
     
     os.system("cls")

     print("\033[33mVTS GitHub > https://github.com/Nitram144/ValoTrackScreen/\033[0m")
     print("\033[33mHenrikDev GitHub > https://github.com/Henrik-3\033[0m")

     menu()    

def menu():

    os.system("cls")

    print("\033[33mVTS GitHub > https://github.com/Nitram144/ValoTrackScreen/\033[0m")
    print("\033[91mV\033[97mTS\033[0m v.0.0.1")

    try:
         
        print("\033[35m(1) Track a player\033[0m")
        print("(2) Help")
        print("(3) Reset your key")
        choice = int(input("> "))
        while choice not in [1 ,2 ,3 ,4]:
                os.system("cls")
                print("\033[35m(1) Track a player\033[0m")
                print("(2) Help")
                print("(3) Reset your key")
                choice = int(input("> "))

    except Exception as err:
         
         menu()
         
    if choice == 1:
         tracker()
    elif choice == 2:
         help()  
    elif choice == 3:
         reset_key()         

def reset_key():

    os.system("cls")
    
    if os.path.exists("key.json"):
        os.remove("key.json")
        print("\033[32mKey has been reset\033[0m")
    else:
         print("\033[31mYou dont have a key\033[0m")    

    menu() 

menu()
