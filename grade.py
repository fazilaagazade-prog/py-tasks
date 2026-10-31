bal = int(input("İmtahan balinizi daxil edin (0-100): "))
if bal < 0 or bal > 100:
    print("Yanlış bal")
elif bal >= 91:
    print("A (Ela)") 
elif bal >= 81:
    print("B") 
elif bal >= 71:
    print("C")
elif bal >= 61:
    print("D")
elif bal >= 51:
    print("E")
else:
    print("F")                      