#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import Eligibility

def callback(data):
    rospy.loginfo(" %s" % (data.criteria))

def listener():
    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber("data2", Eligibility, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
