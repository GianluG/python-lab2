from sys import argv

def mySort(list):
    list.sort()

def showList(list):
    for element in list:
        print(element)
    print("")

filename = argv[1]
txt = open(filename)
tasks = txt.read().split("\n")
txt.close()
exit = 0
ordered=1
while exit==0:
    print("Scegli una delle seguenti opzioni:")
    print("1) Inserisci nuovo task")
    print("2) Rimuovi task")
    print("3) Mostra task esistenti")
    print("4) Elimina i task con una specifica sottostringa")
    print("5) Esci")

    cmd = int(input())
    if cmd == 1:
        print("Inserisci nome")
        new_task = input()
        tasks.append(new_task)
        ordered = 0
    elif cmd == 2:
        print("Quale task vuoi rimuovere?")
        rm_task=input()
        tasks.remove(rm_task)
    elif cmd == 3:
        if ordered == 0:
            mySort(tasks)
            ordered = 1
        print("")
        showList(tasks)
    elif cmd == 4:
        showList(tasks)
        print("Che sottostringa devo cercare?")
        substring = input()

        l = len(tasks)
        i=0
        while i < l:
            if tasks[i].find(substring) != -1:
                tasks.pop(i)
                l -= 1
            else:
                i += 1
        showList(tasks)
    elif cmd == 5:
        exit = 1
        out = open(filename, "w")
        if ordered == 0:
            mySort(tasks)
        l = len(tasks)
        for i in range(0, l):
            out.write(tasks[i])
            if i < l - 1:
                out.write("\n")
        out.close()
    else:
        print("Comando non riconosciuto")