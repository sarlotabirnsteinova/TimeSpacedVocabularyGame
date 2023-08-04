import datetime

class VocabUnit:
    """
    Class for one VocabUnit as a representation of one word, with translation into a target language
    and arbitrary example sentence using a given word.
    """
    def __init__(self, native, target, timeInfo, counter=0, native_long=None, target_long=None):
        self.native = native
        self.target = target
        self.timeInfo = timeInfo
        self.counter = counter
        self.native_long = None
        self.target_long = None
        
        self.noun, self.noun_core = self.is_noun()
        
        
    def test_today(self,dateToday):
        """
        Figure out if the VocabUnit should be tested at dateToday, depending on learning status 
        stored in counter
        
        - returns True if test today. False if not its time to be tested
        """
        dt = dateToday - self.timeInfo
        ddays = dt.days
        if ddays >= 1 and self.counter==0:
            # to be tested at dateToday
            return True
        elif ddays >= 14 and self.counter<=1:
            return True
        elif ddays >= 30 and self.counter<=2:
            return True
        elif ddays >= 60 and self.counter<=3:
            return True
        else:
            # return False
            return True   # only for testing
    
    # change dateInfo & counter if tested
    def change_after_testing(self,newTimeInfo,newCounter):
        """
        Change info when last tested and learning status - counter. 
        """
        self.timeInfo = newTimeInfo
        self.counter = newCounter       
        
    def is_noun(self):
        """
        Checks if VocabUnit is a noun.
        """
        parts = self.target.split()
        if len(parts) == 2 and parts[1][0].isupper():
            return True, parts[1]
        else:
            return False, None
        
    # compare input with VocabUnit target strings:
    def compare_with_target(self,inputString):
        """
        Compare inputString with target translation.
        
        - return if input correct or not 
        """
        translation = False
        new_counter = 0
        
        if self.target_long is None:
            if inputString == self.target:
                translation, new_counter = True, 1
            elif self.noun and inputString.split()[1] == self.noun_core:
                translation, new_counter = True, 0
            else:
                translation, new_counter = False, None
        else:
            if inputString == self.target_long:
                translation, new_counter = True, 1
            elif inputString in self.target_long:
                translation, new_counter = True, 0
            elif inputString == self.target_long:
                translation, new_counter = True, 1 
            elif self.noun and inputString.split()[1] == self.noun_core:
                translation, new_counter = True, 0
            else:
                translation, new_counter = False, 0
                
        self.change_after_testing(datetime.date.today(), new_counter)
        return translation

