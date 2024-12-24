class MRO_Algorithm:
    ''' Method Resolution Object (MRO) is ued to find out the order in whihc Python looks for methods in a hierarchy of classes. The order will be as follows: first Depth , i.e the  child node will be looked up first for the method, next if it inherits from multiple parents, the order will be from left to right of the inherited classes.'''


# Inheritance Flowchart E.g:
# 
#    A       B      C
#     \     / \    /| 
#      \   /   \  / |
#       X        Y  |
#        \     /    |   
#         \   /     |
#          \ /      |
#           P _ _ _ |

class A: pass
class B: pass
class C: pass
class X(A,B): pass
class Y(B,C): pass
class P(X,Y,C): pass

print(MRO_Algorithm.__doc__)
print("MRO of A: ",A.mro())
print("MRO of B: ",B.mro())
print("MRO of C: ",C.mro())
print("MRO of X: ",X.mro())
print("MRO of Y: ",Y.mro())
print("The assumed MRO of P would be P,X,Y,C,A,B,Object. But it's wrong.")
print("The actual MRO of P: ",P.mro())
print("The reason is, The depth-first + left-to-right rule (DLR) algorithm we're referring to is actually how Python used to handle method resolution in older versions (Python 2.1 and earlier). This was called old-style classes(those that do not explicitly inherit from the object class and thus have some limitations in terms of functionality and performance.). In modern Python (2.2 and later), ALL multiple inheritance uses the C3 Linearization algorithm. The simple depth-first + left-to-right rule was abandoned because it could lead to inconsistencies and ambiguities in complex multiple inheritance hierarchies.\n C3 ALgoithm focuses on these 3 Key Principles. They are: \n 1. Local precedence: It just preserves the order specified in EACH class definition separately. This is about maintaining the left-to-right order of direct parents as written in each class declaration.\n E.g., P(X,Y,C),X(A,B),Y(B,C) IN our case, the specified inheritance order shoudl be maintained always. i.e Y should come before B, B shoudl come before C. A should come before C. \n 2. Monotonicity: It requires a class to appear before ALL its parent classes. This is about the global relationship between a class and its ancestors. It is about  maintaining consistent ordering throughout the entire inheritance chain e.,g If X appears before Y in the MRO And X contains A and B in its ancestry. Then A must appear before B in the ENTIRE MRO, even in places where we're resolving Y's methods.\n 3. Consistency: It is about maintaining the same relative order between any two classes e.g., if we decide A comes before B at any point, this ordering must be maintained everywhere in the MRO.\n Why our expected MRO ORder don't work. Here, P, X, Y, C, A, B, Object violates the local precendence order of Y, whihc is Y(B,C),leading to ambiguous or contradictory inheritance scenarios. To avoid, it ,we'll use C3 algorithm, which wil ensure all 3 key princeiples. \n Here's how C3 works: To manually impemetn it, first we will write all the MRO orders of all the parent classes, our child class inherits, tehn finally alos have the list of parent class names alone we inherited in the same order. Then first element fo each roder is HEad, reamingin all terms are referred as Tail. for e.g,  YBCO Y-head, BCO -tail. We'll iteratei each term and check if teh head of the current order, is elsewhere cmae as tail in any other order terms. IF nowhere it is there, as tail, that term is our correct order lookup, include that in the final orde, adnhten remove that elmetn , frmoa ll teh order terms, then again tierate from first term, IF u find the head of first term,to be present soemwher as tail, then iterate to the nedxt term, and check its' head, it wille nsreu we follwo all the principles, and our final MRO order wodulbe correct \n MRO(P) = P + Merge(MRO(X), MRO(Y), MRO(C), XYC)\n MRO(P) = P + Merge(XABO, YBCO, CO, XYC)\n MRO(P) = P + X + Merge(ABO, YBCO, CO, YC)\n MRO(P) = P + X + A + Merge(BO, YBCO, CO, YC)\n Here, the next lookup is B, but B is in the tail part of YBCO, i.e Y should come before B in order, butif u write B now itself, in this order then Y woudl come after B, YBCO order wodul be violated, so next we won't check O of BO, as O shoudl come before B in this local order, but we did not include B as of now , so we wdoul check the enxt term YBCO. Here, Y is not been in the tail part of any order terms, so it satisifes all the principles, and we use that\n MRO(P) = P + X + A + Y + Merge(BO, BCO, CO, C)\n MRO(P) = P + X + A + Y + B + Merge(O, CO, CO, C)\n O can't be used here. MRO(P) = P + X + A + Y + B + Merge(O, CO, CO, C) \n MRO(P) = P + X + A + Y + B + C +  Merge(O, O, O, ) \n MRO(P) = P + X + A + Y + B + C + O Merge(, , , ). \n MRO(P) = P + X + A + Y + B + C + O. \n It matches the exact MRO Order",P.mro())





