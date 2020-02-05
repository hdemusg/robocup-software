import play
import behavior
import robocup
import constants

from forces import force_visualizer
from forces import force
from forces import constant_force
from forces import test_robot_force

##
# A demo/base test play for visualizing forces using the force
# visualizer
#
#
#
class ForceVisualize(play.Play):
    

    ##This point will be the bottom left corner of the field
    corner = robocup.Point(0, constants.Field.Length / 2)
   
    ##Set how you want the points drawn here
    x_size = 2.0
    y_size = 2.0
    interval = 0.5

    ##There is a default scale factor, but you can also set it here
    scaleFactor = 0.3

    ##You can swap out the force you want to visualize here
    #force = constant_force.ConstantForce(robocup.Point(1.2,1.3))
    force = test_robot_force.TestRobotForce(scale=5)

    def __init__(self):
        super().__init__(continuous=False)

        #Create the visualizer object
        self.visualizer = force_visualizer.ForceVisualizer(self.force, scaleFactor=self.scaleFactor)

        self.add_transition(behavior.Behavior.State.start,
                            behavior.Behavior.State.running, lambda: True,
                            'immediately')


    def execute_running(self):
        #self.visualizer.pointVisualize(self.center)
        self.visualizer.fieldVisualize(self.corner, self.x_size, self.y_size, 0.5)