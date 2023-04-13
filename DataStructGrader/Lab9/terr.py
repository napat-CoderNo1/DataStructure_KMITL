def sortByAlphabetAZ(self):
        temp = self.head
        
        while temp.next != None:
            current = temp.next
            #equal = True
            
            while current.prev != None:
                equal = True
                bNode = current.title
                fNode = current.prev.title
                bNode = bNode.upper()
                fNode = fNode.upper()
                # print(bNode)
                
                if len(bNode) <= len(fNode):
                    for i in range(len(bNode)):
                        if ord(bNode[i]) < ord(fNode[i]):
                            self.swapDataInNode(current.prev, current)
                            equal = False
                            current = current.prev
                            break
                        elif ord(bNode[i]) > ord(fNode[i]):
                            equal = 'more than'
                            break

                    # จบ loop ก่อนค่อยเช็ค if นี้
                    if equal == 'more than':
                        break
                    elif equal == True:
                        self.swapDataInNode(current.prev, current)
                        current = current.prev
                else:
                    
                    for i in range(len(fNode)):
                        if ord(bNode[i]) < ord(fNode[i]):
                            self.swapDataInNode(current.prev, current)
                            equal = False
                            current = current.prev
                            break
                        elif ord(bNode[i]) > ord(fNode[i]):
                            equal = 'more than'
                            break
                    
                    # จบ loop ก่อนค่อยเช็ค if นี้
                    if equal == 'more than':
                        break
                    elif equal == True:
                        break

            temp = temp.next