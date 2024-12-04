# == TEST FUNCTION: Return parameters in a string ==
# Run function on flask endpoint, test for some return value
def returnNodes(startNode, endNode):
    return("Nodes: " + startNode + ", " + endNode)

# == TEST FUNCTION: Return a list of items ==
# Run function on flask endpoint, test for ability to return a list of list items
def returnSomeList():
    tempList = [["coord1", "coord2"], ["coord3", "coord4"]]
    return(tempList)

# == Test CLASS: Return the same previous functions, but in a class ==
# Run class on flask endpoint, test for ability to get return values from classes
class Test():
    def __init__():
        # self.tempList = []
        pass
    
    def returnClassValue():
        return("classValue")
    
    # def returnClassList():
    #     return(tempList)