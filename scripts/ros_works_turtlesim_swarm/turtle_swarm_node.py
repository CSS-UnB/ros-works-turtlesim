#!/usr/bin/env python
import rospy
from turtle_swarm import TurtleSwarm

def main():
    rospy.init_node('turtle_swarm_node')

    turtle_swarm = TurtleSwarm()

    while not rospy.is_shutdown():
        try:
            turtle_swarm.run()

        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    main()
