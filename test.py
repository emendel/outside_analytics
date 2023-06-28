import unittest
from main import Elevator

class ElevatorTest(unittest.TestCase):
  elevator = Elevator()

  def test_validate_floors_with_empty_floors_returns_default(self):
    assert self.elevator.validate_floors("2,9") == [2,9], "valid floors should return [2,9]"

  def test_validate_floors_with_empty_floors_returns_default(self):
    assert self.elevator.validate_floors("") == [2,9,1,32], "empty floors should return default"

  def test_validate_floors_with_letters_returns_default(self):
    assert self.elevator.validate_floors("23,9,mm,09") == [2,9,1,32], "letters in floors should return default"

  def test_time_to_floor_same_floor_returns_0(self):
    assert self.elevator.time_to_floor(8,8) == 0, "time to floor should be 0"

  def test_time_to_floor_returns_10(self):
    assert self.elevator.time_to_floor(8, 9) == 10, "time to floor should be 10"

  def test_time_to_floor_returns_20(self):
    assert self.elevator.time_to_floor(8, 6) == 20, "time to floor should be 20"

  def test_given_example_returns_560(self):
    assert self.elevator.calculate_output(12, [2,9,1,32]) == [560,12,2,9,1,32], "given examples returns 560,12,2,9,1,32"

if __name__ == '__main__':
  unittest.main()
