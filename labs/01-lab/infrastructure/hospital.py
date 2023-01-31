def draw_hospital():
    print("[Hospital]:")
    
    print(" "*13, "|")
    print(" "*10, "-"*7)
    print(" "*13, "|")
    print("-"*29)
    for i in range(15):
        print("|", " "*5, "[ ]", " "*5,"[ ]"," "*5,"|")
        
    print("|", " "*9, "_____", " "*9, "|")
    for i in range (3):
        print("|", " "*9, "|   |", " "*9, "|")
