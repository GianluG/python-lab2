from sys import argv
filename = argv[1]
txt = open(filename)
tasks=txt.read().split("\n")
txt.close()
exit=0
ordered=0
while exit==0:
    print("Scegli una delle seguenti opzioni:")
    print("1) Inserisci nuovo task")
    print("2) Rimuovi task")
    print("3) Mostra task esistenti")
    print("4) Esci")

    cmd=int(input())
    if cmd == 1:
        print("Inserisci nome")
        new_task=input()
        tasks.append(new_task)
        ordered=0
    elif cmd == 2:
        print("Quale task vuoi rimuovere?")
        rm_task=input()
        tasks.remove(rm_task)
    elif cmd == 3:
        if ordered==0:
            tasks.sort()
            ordered=1
        print("")
        for element in tasks:
            print (element)
        print("")
    elif cmd == 4:
        exit=1
        out=open(filename,"w")
        for element in tasks:
            out.write(element + "\n")
        out.close()
    else:
        print("Comando non riconosciuto")