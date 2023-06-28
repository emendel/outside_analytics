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
      floors = input("Comma separated value of floors to travel to. Example: 2,9,1,32 - if given data is invalid will default to example: ")
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
    
if __name__ == "__main__":
    elevator = Elevator()
    print(elevator.driver())
