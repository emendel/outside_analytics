from main import *


def time_to_floor(origin, destination):
  return(abs(origin - destination) * VELOCITY)
  
def test_time_to_floor_same_floor_returns_0():
  assert time_to_floor(8,8) == 0, "time to floor should be 0"

def test_time_to_floor_returns_10():
  assert time_to_floor(8, 9) == 10, "time to floor should be 10"

def test_time_to_floor_returns_20():
  assert time_to_floor(8, 6) == 20, "time to floor should be 20"

def test_given_example_returns_560():
  assert driver(12, [2,9,1,32]) == [560,12,2,9,1,32], "given examples returns 560,12,2,9,1,32"
