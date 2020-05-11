# smallest-circle
Solving smallest circle problem using Ritter's bounding sphere algorithm

## Ritter's bounding sphere:
    1. Pick a point x from P
    2. Search for a point y in P, which has the maximum distance from x
    3. Search for a point z in P, which has the maximum distance from y
    4. Set up an initial ball B, with its centre at the midpoint of y and z, 
        the radius as half of the distance between y and z
    5. If all points in P are within the ball B, then we get the bounding sphere
    5a. Otherwise, let p be the point outside the ball, which is at distance d rom the border of B. 
    6. Move the centre of B towards p and increase radius to get a new ball. 
Here I modified the algorithm a little bit: initially, the radius was supposed to be increased by d/2. However, in some cases this resulted in too big circles. So I increment it by d/alpha. At start alpha = 8, and is increased by 2 with every step.

## How to launch
 - If you want to run this in a virtual enviroment, run `create_venv.sh`;
 - Run `python start.py` to see the result;
###### Note: if nothing is displayed after running the command, delete the created virtual environment, uncomment lines in the `create_venv.sh` and run it again.
