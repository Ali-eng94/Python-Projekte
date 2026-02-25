def Hello(**kwargs):
    #print( "Hello " + kwargs['First'] + kwargs['Milde'] + kwargs['Last'])
    #Hello(First="ALi ", Milde="Hassan ", Last="Haji")    #output: Hello ALi Hassan Haji

    for key ,value in kwargs.items():
        print(value, end="")

Hello(First="ALi ", Milde="Hassan ", Last="Haji ", Age="32")   #output ALi Hassan Haji 32