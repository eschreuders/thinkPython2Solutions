##############################
# Chapter 17-2 kangaroo
##############################

class Kangaroo:
    """Represents an animal with a pouch list that can hold something else
    """
    
    def __init__(self, name = '', pouch = None):
        self.pouch_contents = []
        self.pouch_contents.append(pouch)
        self.name = name
    
    def __str__(self):
        return 'Object name: {}   and pouch contents: {}'.format(self.name, self.pouch_contents)    
        
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
        
def main():
    kanga = Kangaroo('kanga',34)
    roo = Kangaroo('roo','hello!')
    print(kanga)
    print(roo)
    
    kanga.put_in_pouch('keys')
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch(roo)
    
    print(kanga)
    print(roo)


if __name__ == "__main__":
    main()
     
