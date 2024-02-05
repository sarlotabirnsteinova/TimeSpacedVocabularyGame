# TimeSpacedVocabularyGame
Game for testing vocabulary in your target language.

It is a flashcard type of testing, with an extra feature of flashcards appearing with decreasing frequency (see https://en.wikipedia.org/wiki/Forgetting_curve).

There are two different versions of this game, one is meant for learning and the other for testing vocabulary.
## Learning vocabulary
It is meant for adding new vocabulary to your flashcard deck.

## Testing vocabulary
It will test vocabulary from your deck according to your previous performance and the time passed since the last testing. 
In the case of correct answers while testing, given flashcard appears the day of testing, the next day, after two weeks, after a month, and the last time after three months, after which the expression is considered learned.

## How does it work (detailed)
Here I will add more detailed description on how to use this game. A simple schema shows purpose of some of the files included in this project.  
![plot](tsvg_intro_img.jpg)


### Creating a flash card deck:
1. One need to run 'learnVocabulary.py', pick file name for and press 'loadVocabTest' to either loading existing deck or creating new one.
2. Next steps are writing prompts in native and target language. Native language fields will be later used as prompts for your answers in target language. both native and target group cponsist of two fields. Top one can be single word, or an expression. This will need to be a perfectly mach with an answer in order to be correct. Native and target 'example sentence', is not a mandatory field, and as label suggest can be the given expression used in a sentence. 
3. Step 2. is repeated for however many expressions one wants. After adding of new vocabulary is finnished 'Save Game' button has to be pressed to save it all. 
4. to Exit this window one can press 'Exit Game'  
### For testing from flash cards:
5. Run 'testVocab.py' file. Write the filename of deck you want to be tested on and press 'Load VocabTest' button. In terminal information about number of flashcards will be displayed. 
6. To start press 'Next' to show first expression. If  given expression contains both short and example sentence version, they will be displayed. 
7. Next step is to wite the answer. Preffered is the example sentence, but also short expression is compared with the answer.
8. After answer field is filled  'Submitt answer' should be pressed. AFter that, the correct answers for both short and long target are displayed under the answer field. 
9. For testing the next expression press 'Next'.
10. After the testing is finnished: either the deck is empty or one wants to close test, press 'Save Game' for saving the progress and answers to update tested vocabulary in the deck. 
11. To close the game window and extit game press 'Exit Game'.   

### Logic for points and when the expression is considered learned 
The idea here is to use point system to track learning of every expression. Newly added expression has value 0 and with each correct translation it will increase its value with one point increments. If an expression is translated incorrectly, its value falls to zero. Time spaced part controlls when the given expression will appear in testing.  

#### Time-spaced feature
Point system shows how many times an expression has been traslated correctly. Testing of expressions is possible at any moment of test taking place for expressions with value 0 (newly added or previously incorrectly translated expression). At least one day since last testing period is required for expressions with value=1 to appear in another test. One month and three months for expression with values 2, 3. Reaching value 4 means that expression is considered learned and will not appear in following tests.

#### When a translation is correct?
This can of course depend on the language and since this project has been written focusing on German translations it leads to several features.  
There is a slight difference in expressions containing an example sentence and those not. If there is not example sentence, expression will be considered correclty translated only if is the same as target expression. One of the features is a special treatment for nouns. If the noun is tested, in order to be awarded a point also article has to be correct, in other case, points will stay the same. If expression has a example sentence, one can translate either short expression of the example sentence and if translated correctly they will be both awarded a point. Special feature for nouns hold the same here for short target expression. In the case translation is only partially correct with respect to the example sentence points will stay the same. 
