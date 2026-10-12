import sys

if len(sys.argv) != 2:
    print("Error. Use: python main.py program.bf")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8") as f: #with Per evitare che read se solleva eccezione non chiude la stream
    testo = f.read()    #Torna una stringa
    print(f"Source File:{testo}")

COMMANDS = ['>', '<', '+', '-', '.', ',', '[', ']']

def exec (testo):
    memory = [0] * 30000
    pointer = 0 #Puntatore alla cella di memoria
    code = [c for c in testo if c in COMMANDS] #List comprehension
    programCounter = 0  #Registra a quale istruzione siamo
    stack = []
    while(programCounter < len(code)):
        match code[programCounter]:
            case '+':
                memory[pointer] = (memory[pointer] + 1) % 256
                programCounter += 1 
            case '-':
                memory[pointer] = (memory[pointer] - 1) % 256
                programCounter += 1
            case '>':
                pointer = (pointer + 1) % len(memory)
                programCounter += 1
            case '<':
                pointer = (pointer - 1) % len(memory)
                programCounter += 1 
            case '[':
                if(memory[pointer]) == 0:
                    try:
                        programCounter = code.index(']', programCounter)
                    except ValueError:
                        print("Error: Missing end square bracket")
                else:
                    stack.append(programCounter)
                    programCounter += 1
            case ']':
                if(len(stack) == 0):
                    print("Error: Missing begin square bracket")
                    programCounter += 1
                else:
                    tmp = stack.pop()
                    if(memory[pointer]> 0):
                        programCounter = tmp
                    else:#ci sta la [, ma ciclo terminato
                        programCounter += 1
            case '.':
                print(chr(memory[pointer]), end = '')
                programCounter += 1

exec(testo)

                            


        

