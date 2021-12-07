"""Classes used throughout project"""
class NewZooBorn():
    '''
    A class for a new Zoo that only houses lions, elephants, zebras, and polar bears.
    Methods within will allow for a list ofnewborns from a certain season, brief bios, favorite food, and determination of relocation based     on new born condition. 
    
   __init__
   self.n_born : int 
   counts number of new born animals in the zoo 
   
   self.born : list
   list where new born info will be stored, by use of 'add_newborn' method
   
   self.n_relocated : int
   counts number of relocate animals
   
   self.relocated : list
   list of info of new born animals that need to be relocated 
   
   '''
    def __init__(self):
        
        self.n_born = 0
        self.born = []
        self.n_relocated = 0
        self.relocated = []
        
    def add_newborn(self, name, species, extinction, habitat):
        '''
        creates a dictionray of new born animals, returns a list that contains the dictionary, 
        as well as an int that counts how many new borns. 
        
        Parameters
        -------
        name : str
        Stores the name of the new born animal
        
        species : str
        Stores the species of the new born animal 
        
        extinction : str
        Stores the extinction status of the new born animal, if in extinction input "is", if not, input "is not"
        
        habitat : str
        Stores habitat of new born animal 
        
        Returns 
        -------
        self.born : list
        list of animal info in a dictionary 
        
        self.n_born : int
        count of newborn animals 
        
        '''
        
        #born_dict stores info of animal into a dictionary
        born_dict = {'Name' : name, 'Species' : species, 'Extinction' : extinction, 'Habitat' : habitat}
        #self.born is a list that stores the born_dict
        self.born.append(born_dict)
        #self.n_born stores the int of how many newborn animals there are
        self.n_born+=1
        
        return self.born , self.n_born
    
    def newborn_bio(self, name, species, extinction, habitat):
        '''
        Concatenates strings of new born animal info
        
        Parameters
        -------
        name : str
        Stores the name of the new born animal
        
        species : str
        Stores the species of the new born animal 
        
        extinction : str
        Stores the extinction status of the new born animal, if in extinction input "is", if not, input "is not"
        
        habitat : str
        Stores habitat of new born animal 
        
        Returns
        -------
        String concatenation of parameters and other strings 
        
        '''
        #will return concatenation of strings 
        return name + ' ' + 'is a' + ' ' + species + ' ' + 'who' + ' ' + extinction + ' ' + 'in extinction' + ' ' + 'and lives in the ' + habitat + '.'
    
    def newborn_fav_food(self, name, species):
        '''
        Creates a dictionray on behalf of newborn species
        
        Parameters
        -------
        name : str
        Stores the name of the new born animal
        
        species : str
        Stores the species of the new born animal 
        
        Returns
        -------
        fav_food_dict : dict
        stores species of newborn in 'key' and the corresponding favorite food in the 'value'
        
        '''
        
        #blank dictionary that will store speices and favorite food  
        fav_food_dict = {}
        #conditional that regards a specific string 
        if species == 'lion':
                #string stored into variable
                food = 'meat'
                #dictionary that stores species and food, key and value
                fav_food_dict[species] = food
        #conditional that regards a specific string
        elif species == 'elephant':
                #string stored into a variable
                food = 'greens'
                #dictionary that stores species and food,key and value
                fav_food_dict[species] = food
        #conditional that regards a specific string
        elif species == 'zebra':
                #variable that stores string
                food = 'greens'
                #dictionary that stores species and food, key and fod
                fav_food_dict[species] = food
        #conditional that regards a specific string
        elif species == 'polar bear':
                #variable that stores string
                food = 'fish'
                #dictionary that stores species and food, key and value
                fav_food_dict[species] = food
        #conditional that regards all other inputs
        else:
                #dictionary that stores species and corresponding info, key and value
                fav_food_dict[species] = 'unknown'
        
        return fav_food_dict
            
    def newborn_relocation(self, name, species, extinction, habitat, intensive_care):
        '''
       Determines whether a newborn needs to be in intensive care, creates a dictionary of that stores animals info
       and counts number of newborns in intnesive care
       
       Parameters
       -------
        name : str
        Stores the name of the new born animal
        
        species : str
        Stores the species of the new born animal 
        
        extinction : str
        Stores the extinction status of the new born animal, if in extinction input "is", if not, input "is not"
        
        habitat : str
        Stores habitat of new born animal 
        
        intensive_care : str
        Stores 'yes' if newborn needs to be in ICU, stores 'no' if it does not need to be in ICU
        
        Returns
        -------
        if intensive_care is 'yes'
        self.n_relocated : int
        counts number of relocate animals
   
       self.relocated : list
       list of info of new born animals that need to be relocated 
   
       if intensive_care is 'no'
       returns corresponding string
       
       if other input for intensiv_care
       returns corresponding string
       
       ''' 
        #conditional regarding a specific string
        if intensive_care == 'yes':
            #dictionary that stores animal info 
            potential_ICU = {'name' : name, 'species' : species, 'extinction' : extinction, 'habitat' : habitat, 'intensive_care' : intensive_care}
            #dictionary that gets appended onto list
            self.relocated.append(potential_ICU)
            #int that stores all the animals that need to be relocated
            self.n_relocated+=1
            
            return self.relocated, self.n_relocated
        #conditional that regards a specific string
        elif intensive_care == 'no':
            
            return 'Not in critical condition!'
        #conditional for all other inputs
        else:
            
            return 'Need more infomation to determine appropriate location'     
