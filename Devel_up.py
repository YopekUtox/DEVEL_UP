import sys, os                  
import time
import json

if sys.platform == "win32":
    os.system("cls")

if sys.platform == "linux":
    os.system("clear")

if sys.platform == "darwin":
    print("[ERROR] This OS is not supported !")    
    sys.exit(1)

def menu():

    print("""\033[94m
    .:::::    .::::::::.::         .::.::::::::.::            .::     .::.:::::::  
    .::   .:: .::       .::       .:: .::      .::            .::     .::.::    .::
    .::    .::.::        .::     .::  .::      .::            .::     .::.::    .::
    .::    .::.::::::     .::   .::   .::::::  .::            .::     .::.:::::::  
    .::    .::.::          .:: .::    .::      .::            .::     .::.::       
    .::   .:: .::           .::::     .::      .::            .::     .::.::       
    .:::::    .::::::::      .::      .::::::::.::::::::        .:::::   .::       
                                                        .:::::                                                           
    """)
    print("                                                              \033[34mBy: \033[0mYopekUtox")
    print("\n\n")
    print("                             \033[94m>>\033[0m MENU \033[94m<<\n")
    print("                          \033[94m[\033[0m1\033[94m]\033[0m Start exp'ing")
    print("                          \033[94m[\033[0m2\033[94m]\033[0m Check config")
    print("                          \033[94m[\033[0m3\033[94m]\033[0m Set config")
    print("                          \033[94m[\033[0m4\033[94m]\033[0m Install libary")
    print("                          \033[94m[\033[0m5\033[94m]\033[0m Exit")
    print("\n")
    choice = input("                          \033[94m>>\033[0m ")

    if choice == "4":
        print("\n\033[33m[\033[0mINFO\033[33m]\033[0m Install modules please wait ...")
        time.sleep(3)
        try:
            os.system("pip install discord.py")
        except:
            os.system("pip3 install discord.py")

        input("\033[33m[\033[0mINFO\033[33m]\033[0m Installation was successful, press ENTER to back")
        if sys.platform == "win32":
            os.system("cls")
        if sys.platform == "linux":
            os.system("clear")
        menu()

    if choice == "3":
        with open("config.json") as f: 
            print("\n")
            token = input("Your token\033[94m->> \033[0m ")
            delay = input("The time \033[94m(\033[0min second\033[94m)\033[0m which the message giving exp will be sent\033[94m->> \033[0m ")
            word = input("A message that will be sent to earn exp\033[94m->> \033[0m ")
            data = json.load(f)
            data["token"] = token
            data["delay"] = delay
            data["word"] = word
            json.dump(data, open("config.json", "w"), indent = 4)
            print("\n\033[33m[\033[0mINFO\033[33m]\033[0m Config is set now ...")
            time.sleep(3)
            if sys.platform == "win32":
                os.system("cls")
            if sys.platform == "linux":
                os.system("clear")
            menu()    

    if choice == "2":     
        with open("config.json", "r") as read_config:  
            print("\n\033[94mCONFIG: \033[00m")
            print(json.dumps(json.load(read_config), indent=4))
            input("\n\033[33m[\033[0mINFO\033[33m]\033[0m Press enter to back")
            if sys.platform == "win32":
                os.system("cls")
            if sys.platform == "linux":
                os.system("clear")
            menu()    

    if choice == "1":    
        print("\n")
        print("\n\033[91m[\033[0mWARN\033[91m]\033[0m Remember, for this you can get a ban \033[91m!!!\033[00m\n")
        print("\n")
        print("                          \033[94m[\033[0m1\033[94m]\033[0m Use .json config")
        print("                          \033[94m[\033[0m2\033[94m]\033[0m Set all without .json config")
        print("                          \033[94m[\033[0m3\033[94m]\033[0m Back")
        print("\n")
        choice_start = input("                          \033[94m>>\033[0m ")

        if choice_start == "1": 
            import discord
            
            with open("config.json", "r") as read_config:  
                read_object = json.load(read_config)

                token = read_object["token"]
                delay = read_object["delay"]
                word = read_object["word"]

                chat_id = input("Channel ID where message for exp is sending and deleting\033[94m->> \033[0m ")
                cout = input("How many messages you want to send for exp \033[94m->> \033[0m ")

                intents = discord.Intents.default()
                intents.members = True
                exp = discord.Client()
                @exp.event
                async def on_ready():
                    print(f"\033[33m[\033[0mINFO\033[33m]\033[0m {exp.user} is connected")
                    channel = exp.get_channel(int(chat_id))
                    up_cout = 0
                    while True:
                        try:
                            if up_cout <= int(cout):
                                exp_msg = await channel.send(word)
                                await exp_msg.delete()
                                time.sleep(int(delay))
                                print(f"\033[33m[\033[0mINFO\033[33m]\033[0m {exp.user} message is sended and deleted")
                                up_cout = up_cout + 1
                            if up_cout == int(cout):  
                                print(f"\033[33m[\033[0mINFO\033[33m]\033[0m Grind exp is completed, successively sended {cout} messages")
                                input("\n\033[33m[\033[0mINFO\033[33m]\033[0m Press enter to back")
                                if sys.platform == "win32":
                                    os.system("cls")
                                if sys.platform == "linux":
                                    os.system("clear")
                                menu()   

                            
                        except Exception as e:
                            print("\n\033[91m[\033[0mWARN\033[91m]\033[0m Someting is wrong. Please check this in discord \033[91m!!!\033[00m\n")
                            input("\n\033[33m[\033[0mINFO\033[33m]\033[0m Press enter to back")
                            menu()

                exp.run(token, bot=False)

        if choice_start == "2":     
            import discord

            token = input("Your token\033[94m->> \033[0m ")
            delay = input("The time \033[94m(\033[0min second\033[94m)\033[0m which the message giving exp will be sent\033[94m->> \033[0m ")
            word = input("A message that will be sent to earn exp\033[94m->> \033[0m ")

            chat_id = input("Channel ID where message for exp is sending and deleting\033[94m->> \033[0m ")
            cout = input("How many messages you want to send for exp \033[94m->> \033[0m ")

            intents = discord.Intents.default()
            intents.members = True
            exp = discord.Client()
            @exp.event
            async def on_ready():
                print(f"\033[33m[\033[0mINFO\033[33m]\033[0m {exp.user} is connected")
                channel = exp.get_channel(int(chat_id))
                up_cout = 0
                while True:
                    try:
                        if up_cout <= int(cout):
                            exp_msg = await channel.send(word)
                            await exp_msg.delete()
                            time.sleep(int(delay))
                            print(f"\033[33m[\033[0mINFO\033[33m]\033[0m {exp.user} message is sended and deleted")
                            up_cout = up_cout + 1
                        if up_cout == int(cout):  
                            print(f"\033[33m[\033[0mINFO\033[33m]\033[0m Grind exp is completed, successively sended {cout} messages")
                            input("\n\033[33m[\033[0mINFO\033[33m]\033[0m Press enter to back")
                            if sys.platform == "win32":
                                os.system("cls")
                            if sys.platform == "linux":
                                os.system("clear")
                            menu()   

                    except Exception as e:
                        print("\n\033[91m[\033[0mWARN\033[91m]\033[0m Someting is wrong. Please check this in discord \033[91m!!!\033[00m\n")
                        input("\n\033[33m[\033[0mINFO\033[33m]\033[0m Press enter to back")
                        menu()

            exp.run(token, bot=False)    

        if choice_start == "3": 
            if sys.platform == "win32":
                os.system("cls")
            if sys.platform == "linux":
                os.system("clear")    
            menu()  
    else:
        print("\n\033[91m[\033[0mWARN\033[91m]\033[0m Does not exist\033[91m !!!\033[00m\n")
        time.sleep(3)
        if sys.platform == "win32":
            os.system("cls")
        if sys.platform == "linux":
            os.system("clear")
        menu()

menu()