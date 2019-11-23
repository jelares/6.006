from Binary_Tree_Set import BST_Node, Binary_Tree_Set
# ----------------------------------- #
# DO NOT REMOVE THIS IMPORT STATEMENT # 
# DO NOT MODIFY IMPORTED CODE         #
# ----------------------------------- #


class Temperature_DB_Node(BST_Node):
    def subtree_update(A):
        super().subtree_update()
        # ------------------------------------ #
        # YOUR CODE IMPLEMENTING PART (A) HERE #
        # ------------------------------------ #
        if A.left is None and A.right is None:
            A.max_temp = A.item.temp
            A.min_date = A.item.key
            A.max_date = A.item.key

        elif A.left is None:
            rightmax = A.right.max_temp
            temp = A.item.temp

            if rightmax > temp:
                A.max_temp = rightmax
            else:
                A.max_temp = temp

            A.min_date = A.item.key
            A.max_date = A.right.max_date

        elif A.right is None:
            leftmax = A.left.max_temp
            temp = A.item.temp

            if leftmax > temp:
                A.max_temp = leftmax
            else:
                A.max_temp = temp

            A.min_date = A.left.min_date
            A.max_date = A.item.key

        else:
            leftmax = A.left.max_temp
            rightmax = A.right.max_temp
            temp = A.item.temp

            A.max_date = A.right.max_date
            A.min_date = A.left.min_date

            maxset = set()
            maxset.add(leftmax)
            maxset.add(rightmax)
            maxset.add(temp)

            A.max_temp = max(maxset)

    def subtree_max_in_range(A, d1, d2):
        # ------------------------------------ #
        # YOUR CODE IMPLEMENTING PART (C) HERE #
        # ------------------------------------ #

        if A.min_date >= d1 and A.max_date <= d2:
            return A.max_temp

        elif A.min_date > d2 or A.max_date < d1:
            return None

        else:
            maxset = set()

            if A.left is not None:
                leftmax = A.left.subtree_max_in_range(d1, d2)
                if leftmax == None:
                    leftmax = float("-inf")
                maxset.add(leftmax)

            if A.right is not None:
                rightmax = A.right.subtree_max_in_range(d1, d2)
                if rightmax == None:
                    rightmax = float("-inf")
                maxset.add(rightmax)

            if A.item.key in range(d1, d2+1):
                maxset.add(A.item.temp)

            if maxset == set():
                return None
            else:
                maxtemp = max(maxset)
                if maxtemp == float("-inf"):
                    return None
                else:
                    return maxtemp




# ----------------------------------- #
# DO NOT MODIFY CODE BELOW HERE       # 
# ----------------------------------- #
class Measurement:
    def __init__(self, temp, date):
        self.key  = date
        self.temp = temp

    def __str__(self): 
        return "%s,%s" % (self.key, self.temp)

class Temperature_DB(Binary_Tree_Set):
    def __init__(self): 
        super().__init__(Temperature_DB_Node)

    def record_temp(self, t, d):
        try:
            m = self.delete(d)
            t = max(t, m.temp)
        except: pass
        self.insert(Measurement(t, d))

    def max_in_range(self, d1, d2):
        return self.root.subtree_max_in_range(d1, d2)
