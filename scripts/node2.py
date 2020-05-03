#! /usr/bin/env python
import rospy
from beginner_tutorials.msg import NameandAge
from beginner_tutorials.msg import Eligibility

rospy.init_node("node2",anonymous=True)
pub=rospy.Publisher('data2',Eligibility,queue_size=10)
rate=rospy.Rate(10)
y=Eligibility()
	
def callback(data):
	if (data.age)>=18:
		y.criteria="Eligible"
	else:
		y.criteria="Not Eligible"
	#rospy.loginfo(y)	
	pub.publish(y)
	rate.sleep()
				

def listener():	
	rospy.Subscriber("data1",NameandAge,callback)
	rospy.spin()

if __name__=='__main__':
	listener()
