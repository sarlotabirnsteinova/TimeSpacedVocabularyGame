from vocabUnit import VocabUnit
import datetime
import pickle
import random
import os

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
        self.tested_count = 0 # make as currentVocabUnit
        
        # make list of VocabUnits
        if self.fname is not None:
            # make new if does not exist
            if not os.path.isfile(self.fname):
                self.vocabUnitsList = []
                print(f"New filename for VocabTest ")
            else:
                # load existing project w/ VocabUnits
                self.read_VocabUnitsList()
                print(f"VocabTest read from previously saved file: {self.fname}, number of words {len(self.vocabUnitsList)}")
        else:
            self.fname =  f"VocabUnits{self.dateToday}"
            self.vocabUnitsList = []
        # prepare to make test
        self.find_test_idxs()
        self.randomize_idx()
        # set firts expression to be tested
        self.currentVocabUnit = None
        if len(self.vocabTest_idx) > 0:
            self.currentVocabUnit = self.vocabUnitsList[ self.vocabTest_idx.pop() ]
            print(f"Test {self.fname} is ready!")
        else:
            print(f"No expressions to be tested in {self.fname}.")

        
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
            print(f"The List of VocabUnits was saved to pickle file: {self.fname}, number of words {len(self.vocabUnitsList)}")
    
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
    def give_correct_answer(self):
        """
        return correct translation of VocabUnit to be currently tested
        """
        if len(self.vocabTest_idx) > 0:
            str_target = self.currentVocabUnit.target
            str_target_long = self.currentVocabUnit.target_long
            if str_target_long is not None:
                return f"<{str_target}>\n<{str_target_long}>"
            return f"{str_target}"
        else:
            return "Out of expressions to test. Try new VocabTest."

    # process input and VocabUnit in testing & return if correct/incorrect
    def process_test(self,inputString):
        """
        compare input with VocabUnit at specific index & change VocabUnit accordingly

        - return if correct or incorrect
        """
        if len(self.vocabTest_idx) > 0:
            # check translation
            translation_status = self.currentVocabUnit.compare_with_target(inputString)    
            # set a new current test expression
            self.currentVocabUnit = self.vocabUnitsList[ self.vocabTest_idx.pop() ]
            return translation_status
        else:
            self.currentVocabUnit = None
            return None
