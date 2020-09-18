#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def concatenator(data):
	#publishing to topic 'y_axis'
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		#remap yaxis to variables
		left_y = 100*data.axes[1]
		right_y = 100*data.axes[4]
		output_str = "Left Y:"+str(left_y)+" Right y:"+str(right_y)
		rospy.loginfo(output_str)
		pub.publish(output_str)
		rate.sleep()

def start():
	rospy.Subscriber("joy", Joy, concatenator)
	pub = rospy.Publisher('y_axis', String, queue_size=10)
	rospy.init_node('joy_pa_node')
	rospy.spin()


if __name__ == '__main__':
	try:
		start()
	except rospy.ROSInterruptException:
		pass

		

		
		

