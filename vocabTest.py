from vocabUnit import VocabUnit
import datetime
import pickle
import random

class VocabTest:
    """
    Class to store VocabUnits and process testing of Vocabulary 
    """
    def __init__(self, fname=None):
        self.fname =fname
        self.dateToday=datetime.date.today()
        #
        self.vocabUnitsList = None  # list of VocabUnits
        self.vocabTest_idx = []
        self.tested_count = 0
        
        # make list of VocabUnits
        if self.fname is not None:
            # load existing project w/ VocabUnits
            self.read_VocabUnitsList()
        else:
            self.fname =  f"VocabUnits{self.dateToday}"
            self.vocabUnitsList = []
        
        
        
    def read_VocabUnitsList(self):
        """
        read list of VocabUnits from pickle file
        """
        with open(self.fname, 'rb') as config_file:
            self.vocabUnitsList = pickle.load(config_file)
            
    def save_VocabUnitsList(self):
        """
        save list of VocabUnits to pickle file
        """
        with open(self.fname, 'wb') as config_file:
            pickle.dump(self.vocabUnitsList,config_file)
            print(f"The List of VocabUnits was saved to pickle file: {self.fname}")
    
    def add_VocabUnit(self,native,target,native_long=None,target_long=None):
        """
        add a new VocabUnit to the list
        """
        new_VU = VocabUnit(native,target,self.dateToday, counter=0, native_long=native_long,target_long=target_long)
        self.vocabList = self.vocabUnitsList.append(new_VU)
        
    # fill test idx for today
    def find_test_idxs(self):
        """
        find all indexes of VocabUnits in VocabUnits list which should be tested today
        """
        for idx,unit in enumerate(self.vocabUnitsList):
            to_test = unit.test_today(self.dateToday)
            if to_test:
                self.vocabTest_idx.append(idx)
    
    # randomize VocabUnits indexes to test
    def randomize_idx(self):
        """
        randomize the order of VocabUnits to be tested.
        """
        random.shuffle(self.vocabTest_idx)
    
    # pass VocabUnit to test
    def give_VocabUnit(self):
        """
        return VocabUnit to test.
        """
        test_idx_current = self.vocabTest_idx[self.tested_count]
        return self.vocabUnitsList[test_idx_current]
    
    # process input and VocabUnit in testing & return if correct/incorrect
    def process_test(self,inputString):
        """
        compare input with VocabUnit at specific index & change VocabUnit accordingly

        - return if correct or incorrect
        """
        test_idx_current = self.vocabTest_idx[self.tested_count]

        correct = self.vocabUnitsList[test_idx_current].compare_with_target(inputString)
    
        self.tested_count += 1   # here of in process_test function 
        
        return correct
    
    
    # smaller def to change VocabUnit properies under given index --> not needed anymore