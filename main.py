VELOCITY = 10

class Elevator:
    
    def __init__(self):
        return
    
    def driver(self):
      start, floors = self.generate_inputs()
      return self.calculate_output(start,floors)
      
    def calculate_output(self, start, floors):
      total_time = 0
      current_floor = start
      for next_floor in floors:
        total_time += self.time_to_floor(current_floor, next_floor)
        current_floor = next_floor
      output = [total_time] + [start] + floors
      return output
    
    def generate_inputs(self):
      start = int(input("Enter starting Floor : "))
      floors = input("Comma separated value of floors to travel to. Example: 2,9,1,32 - if given data is invalid will default to example")
      floors = self.validate_floors(floors)
      return start, floors
    
    
    def validate_floors(self, floors):
      valid_input = "1234567890, "
      if len(floors) < 1:
          return [2,9,1,32]
      for char in floors:
        if char not in valid_input:
          return [2,9,1,32]
      floors = floors.replace(" ", "")
      floors = floors.split(",")
      res = [eval(i) for i in floors]
      return res
       
    def time_to_floor(self, origin, destination):
      return(abs(origin - destination) * VELOCITY)
    
    def test_validate_floors_with_empty_floors_returns_default():
      assert validate_floors("2,9") == [2,9], "valid floors should return [2,9]"
    
    def test_validate_floors_with_empty_floors_returns_default():
      assert validate_floors("") == [2,9,1,32], "empty floors should return default"
    
    def test_validate_floors_with_letters_returns_default():
      assert validate_floors("23,9,mm,09") == [2,9,1,32], "letters in floors should return default" 
    
    def test_time_to_floor_same_floor_returns_0():
      assert time_to_floor(8,8) == 0, "time to floor should be 0"
    
    def test_time_to_floor_returns_10():
      assert time_to_floor(8, 9) == 10, "time to floor should be 10"
    
    def test_time_to_floor_returns_20():
      assert time_to_floor(8, 6) == 20, "time to floor should be 20"
    
    def test_given_example_returns_560():
      assert calculate_output(12, [2,9,1,32]) == [560,12,2,9,1,32], "given examples returns 560,12,2,9,1,32"
      
    
if __name__ == "__main__":
    elevator = Elevator()
    print(elevator.driver())
    
    
    
    
    


# test_validate_floors_with_empty_floors_returns_default()
# test_validate_floors_with_empty_floors_returns_default()
# test_validate_floors_with_letters_returns_default()
# test_time_to_floor_same_floor_returns_0()
# test_time_to_floor_returns_10()
# test_time_to_floor_returns_20()
# test_given_example_returns_560()
# print(driver())
