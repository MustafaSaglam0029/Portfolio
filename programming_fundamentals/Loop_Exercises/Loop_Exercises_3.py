side= input("Enter the side of the dna: ").upper()
def dna(string):
    dna_pairs={"A":"T","T":"A","G":"C","C":"G"}
    other_side=[]
    for char in side:
        other_side.append(dna_pairs[char])
    return "".join(other_side)
print(dna(side))
#do it with dict
















