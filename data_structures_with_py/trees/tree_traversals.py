class Dugum:
    def __init__(self, veri):
        self.veri = veri
        self.sol = None
        self.sag = None

def pre_order(dugum):
    if dugum:
        print(dugum.veri, end=" ") 
        pre_order(dugum.sol)       
        pre_order(dugum.sag)       

def in_order(dugum):
    if dugum:
        in_order(dugum.sol)        
        print(dugum.veri, end=" ") 
        in_order(dugum.sag)        

def post_order(dugum):
    if dugum:
        post_order(dugum.sol)      
        post_order(dugum.sag)      
        print(dugum.veri, end=" ") 

root = Dugum(1)
root.sol = Dugum(2)
root.sag = Dugum(3)
root.sol.sol = Dugum(4)
root.sol.sag = Dugum(5)

print("Pre-Order (Kök-Sol-Sağ):")
pre_order(root)
print("\n") 

print("In-Order (Sol-Kök-Sağ):")
in_order(root)
print("\n")

print("Post-Order (Sol-Sağ-Kök):")
post_order(root)
print("\n")