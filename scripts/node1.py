#! /usr/bin/env python
import rospy
from beginner_tutorials.msg import NameandAge

def talker():
	pub=rospy.Publisher('data1',NameandAge,queue_size=10)			
	rospy.init_node('node1',anonymous=True)	
	rate=rospy.Rate(10)
	x= NameandAge()
	while not rospy.is_shutdown():
		x.name= raw_input("Name: ")
		x.age=int(raw_input("Age: "))
		rospy.loginfo(x)
		pub.publish(x)
		rate.sleep()

if __name__=='__main__':
	try:
	    talker()
	except rospy.ROSInterruptException:
	    pass


