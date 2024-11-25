print("salam be in bazi khosh amadid dar in bazi shoma yek adad vared mikonid va in barname be shoma mi gooyad ke adad balatar ast ya paiin tar omidvaram az in bazi khoshet biad\n karbar gerami shoma kolan 15 bar forsat entekhab doros ra darid\nmovafagh bashid.")

my_number = 56

for i in range(15):
    if(i == 14):
        print("karbar gerami shoma say khod ra kardid va be natije naresidid lotfan befarmaiid biroon!")
        break
    user_number = int(input("lotfan adadi bein1, 100 antekhab bokonid:"))

    if( my_number == user_number ):
        print("tabrik migam shoma barande shodid!!!")
        break

    elif( my_number > user_number ):
        print("adad mosha khas shode balatar ast!")

    elif( my_number < user_number):
        print("adad moshakhas shodeh paien tar ast!")

    else:
        print("moteasefam shoma bakhtid!")        