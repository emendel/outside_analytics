STARTING_FLOOR = 12
INPUT = [2,9,1,32]
VELOCITY = 10

def generate_inputs():
  print("Starting Floor? (Defaults to 0 if invalid data is given)")
  start = input()
  print("Comma separated value of floors to travel to. Example: 2,9,1,32 - if given data is invalid will default to example")
  floors = input()
  start = validate_start(start):    
  floors = validate_floors(floors):
  driver(start, floors)

def validate_start(start):
  if not isinstance(int, start) or start < 0:
    return 0

def valid_floors(floors):
  valid_input = "1234567890, "
  for char in floors:
    if char not in valid_input:
      return [2,9,1,32]
  floors = floors.replace(" ", "")
  floors = floors.split(",")
  res = [eval(i) for i in floors]
  print("Modified list is: ", res)
  return res


def driver(start, floors):
  total_time = 0
  current_floor = start
  for next_floor in INPUT:
    total_time += time_to_floor(current_floor, next_floor)
    current_floor = next_floor
  output = [total_time] + [start] + floors
  return(output)
   
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
