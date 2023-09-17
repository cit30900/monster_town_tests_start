import unittest
from monstertown import Town, Mutant, Vampire

class TestMonsterTown(unittest.TestCase):

    def setUp(self):
        # TODO: Create THREE Town objects
        # TODO: Create TWO Mutant objects
        # TODO: Create TWO Vampire objects
        pass

    def testTownInitializer(self):
        # TODO: Test all three of the Town objects you created in the setUp() method. 
        pass

    def testMutantTerrorizeTown(self):
        # TODO: Write tests that validate that the values for population, buildings, and stoplights will never go below zero no matter how many times the town is terrorized. 
        pass

    def testVampireTerrorizeTown(self):
        # TODO: Write tests that validate that the values for population will never go below zero no matter how many times the town is terrorized.
        # TODO: Write tests to ensure that the values for buildings and stoplights never change after terrorizing. 
        pass

    def testMutantMMI(self):
        # TODO: Write tests that validate the calculated value of a Mutant’s mmi property. 
        # A Mutant with a height of 10 and weight of 6000 should have an mmi of 30.  
        # A Mutant with a height of 2 and weight of 200 should have an mmi of 5.
        pass

    def testVampireMMI(self):
        # TODO: Write tests that validate the calculated value of a Vampire’s mmi property. 
        # A Vampire with a height of 3 and weight of 170 should have an mmi of 25.5. 
        # A Vampire with a height of 1.5 and weight of 90 should have an mmi of 27. 
        pass

if __name__ == '__main__':
    unittest.main()