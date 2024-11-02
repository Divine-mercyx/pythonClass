def nokia():
    print("""
Welcome to Nokia
1. Phonebook
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Settings
8. Call divert\n8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
""")
    choice = int(input(">>> "))

    match choice:
        case 1:
            print("""
Phonebook\n\n
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
""")
            phonebook_choice = int(input(">>> "))
            match phonebook_choice:
                case 1: print("search")
                case 2: print("Service Nos")
                case 3: print("Add name")
                case 4: print("Erase")
                case 5: print("Edit")
                case 6: print("Assign tone")
                case 7: print("Send b'card")
                case 8:
                    print("Options\n\n1. Type of view\n2. Memory status")
                    options_choice = int(input(">>> "))
                    match options_choice:
                        case 1:
                            print("Type of view")
                        case 2:
                            print("Memory status")
                        case _:
                            print("invalid input")
                case 9: print("Speed dials")
                case 10: print("Voice tags")
                case _: print("invalid input")


        case 2:
            print("""
Messages\n\n
1. Write messages
2. inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info Service
9. Voice mail number
10. Service command editor
""")
            messages_choice = int(input(">>> "))
            match messages_choice:
                case 1: print("write messages")
                case 2: print("inbox")
                case 3: print("Outbox")
                case 4: print("Picture messages")
                case 5: print("Templates")
                case 6: print("smileys")
                case 7:
                    print("Message settings\n\n1. Set 1\n2. Common")
                    message_settings_choice = int(input(">>> "))
                    match message_settings_choice:
                        case 1:
                            print("Set1\n\n1. Message\n2. Messages sent as\n3. Message validity")
                            set_choice = int(input(">>> "))
                            match set_choice:
                                case 1: print("Message")
                                case 2: print("Message sent as")
                                case 3: print("Message validity")
                                case _: print("invalid input")
                        case 2:
                            print("Common\n\n1. Delivery\n2. Reply via same centre\n3. Character support")
                        case _: print("invalid input")
                case 8: print("Info service")
                case 9: print("Voice mailbox number")
                case 10: print("Service command editor")

        case 3: print("Chat")
        case 4:
            print("""
Call register\n\n
1. missed calls
2. Recieved calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
            call_choice = int(input(">>> "))
            match call_choice:
                case 1: print("missed calls")
                case 2: print("recieved calls")
                case 3: print("Dialled numbers")
                case 4: print("Erase recent call lists")
                case 5:
                    print("Show call duration\n\n1. Last call duration\n2. All calls' duration\n3. Recieved calls' duration\n4. Dialled calls' duration\n5. Clear timers")
                    show_call_choice = int(input(">>> "))
                    match show_call_choice:
                        case 1: print("Last call duration")
                        case 2: print("All calls' duration")
                        case 3: print("Recieved calls' duration")
                        case 4: print("Dialled calls' duration")
                        case 5: print("Clear timers")
                        case _: print("invalid input")
                case 6:
                    print("show call costs\n\n1. Last call lost\n2. All calls' cost\n3. Clear counters")
                    show_choice = int(input(">>> "))
                    match show_choice:
                        case 1: print("Last call lost")
                        case 2: print("All calls' cost")
                        case 3: print("Clear counters")
                        case _: print("invalid input")
                case 7:
                        print("Call cost settings\n\n1. Call cost\n2. Show costs in")
                        call_cost_choice = int(input(">>> "))
                        match call_cost_choice:
                            case 1: print("Call cost")
                            case 2: print("Show costs in")
                            case _: print("invalid input")
                case 8: print("Prepaid credit")

        case 5:
            print("""
Tones\n\n
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
""")
            tones_choice = int(input(">>> "))
            match tones_choice:
                case 1: print("Ringing tone")
                case 2: print("Ringing volume")
                case 3: print("Incoming call alert")
                case 4: print("Composer")
                case 5: print("Message alert tone")
                case 6: print("Keypad tones")
                case 7: print("Warning and game tones")
                case 8: print("Vibrating alert")
                case 9: print("Screen saver")
                case _: print("invalid input")


        case 6:
            print("""
Settings\n\n
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
""")
            settings_choice = int(input(">>> "))
            match settings_choice:
                case 1:
                    print("Call settings\n\n1. Automatic redial\n2. Speed dialling\n3. Call waiting options\n4. Own number sending\n5. Phone line in use\n6. Automatic answer")
                    call_settings_choice = int(input(">>> "))
                    match call
                case 2: print("Phone settings")
                case 3: print("Security settings")
                case 4: print("Restore factory settings")
                case _: print("invalid input")
nokia()



