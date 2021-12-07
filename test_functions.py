"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

#from classes import NewZooBorn
from my_module.classes import NewZooBorn 


def test_add_newborn():
    assert add_newborn('Bill', 'lion', 'is', 'desert') != np.nan
    assert add_newborn('Leo', 'lion', 'is', 'desert') == ([{'Name': 'Leo', 'Species': 'lion', 'Extinction': 'is', 'Habitat': 'desert'}],
 1)
    assert add_newborn('Rich', 'elephant', 'is', 'sahara') == ([{'Name': 'Rich',
   'Species': 'elephant',
   'Extinction': 'is',
   'Habitat': 'sahara'}],
 1)
    
    
def test_newborn_bio():
    assert newborn_bio('Bill', 'lion', 'is', 'desert') != np.nan
    assert newborn_bio('Bill', 'lion', 'is', 'desert') == 'Bill is a lion who is in extinction and lives in the desert.'
    assert newborn_bio('Shill', 'zebra', 'is', 'sahara') == 'Shill is a zebra who is in extinction and lives in the sahara.'

def test_newborn_fav_food():
    assert newborn_fav_food('Bill', 'lion') != np.nan
    assert newborn_fav_food('Bill', 'lion') == {'lion': 'meat'}
    assert newborn_fav_food('Stew', 'elephant') == {'elephant': 'greens'}
    assert newborn_fav_food('Sam', 'zebra') == {'zebra': 'greens'}
    assert newborn_fav_food('Edurme', 'polar bear') == {'polar bear': 'fish'}
                            

def test_newborn_relocation():
    assert newborn_relocation('Bill', 'lion', 'is', 'desert', 'no') != np.nan
    assert newborn_relocation('Bill', 'lion', 'is', 'desert', 'no') == 'Not in critical condition!'
    assert newborn_relocation('Bill', 'lion', 'is', 'desert', 'maybe') == 'Need more infomation to determine appropriate location'
    
    
