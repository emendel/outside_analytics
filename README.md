# outside_analytics
1. Provide code that simulates an elevator. You are free to use any language.
2. Upload the completed project to GitHub for discussion during interview.
3. Document all assumptions and any features that weren’t implemented.
4. The result should be an executable, or script, that can be run with the following inputs and generate the following outputs..

Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
Program Constants: Single floor travel time: 10

Assumptions:
1. Does not include negative floor numbers

Features not included:
1. Retry if given bad input instead of exitting the application
2. Include negative floor numbers

Potential Bugs:
1. If a user does not read the instructions closely they might think they can input the floors with a space in between. This could cause a problem because of the .replace(" ", ""). If someone wanted to visit floors 1 & 2 and they typed in "1 2" the program would remove the whitespace and send them to floor 12.
