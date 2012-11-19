"""autogenerated by genmsg_py from MakeTrajectoryActionResult.msg. Do not edit."""
import roslib.message
import struct

import roslib.rostime
import actionlib_msgs.msg
import geometry_msgs.msg
import seabee3_msgs.msg
import seabee3_actions.msg
import std_msgs.msg

class MakeTrajectoryActionResult(roslib.message.Message):
  _md5sum = "76799534ba0bf33c360ac23aa29ee38c"
  _type = "seabee3_actions/MakeTrajectoryActionResult"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
MakeTrajectoryResult result

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: seabee3_actions/MakeTrajectoryResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# result

# the resulting trajectory
seabee3_msgs/Trajectory trajectory

================================================================================
MSG: seabee3_msgs/Trajectory
Header header
# the discrete intervals that make up this trajectory
seabee3_msgs/TrajectoryInterval[] intervals

================================================================================
MSG: seabee3_msgs/TrajectoryInterval
duration length
seabee3_msgs/TrajectoryWaypoint initial_state
geometry_msgs/TwistWithCovariance acceleration

================================================================================
MSG: seabee3_msgs/TrajectoryWaypoint
# pose
geometry_msgs/PoseWithCovariance pose

# velocity
geometry_msgs/TwistWithCovariance velocity

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistWithCovariance
# This expresses velocity in free space with uncertianty.

Twist twist

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into it's linear and angular parts. 
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  __slots__ = ['header','status','result']
  _slot_types = ['Header','actionlib_msgs/GoalStatus','seabee3_actions/MakeTrajectoryResult']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       header,status,result
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(MakeTrajectoryActionResult, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = seabee3_actions.msg.MakeTrajectoryResult()
    else:
      self.header = std_msgs.msg._Header.Header()
      self.status = actionlib_msgs.msg.GoalStatus()
      self.result = seabee3_actions.msg.MakeTrajectoryResult()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.status.status))
      _x = self.status.text
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.result.trajectory.header.seq, _x.result.trajectory.header.stamp.secs, _x.result.trajectory.header.stamp.nsecs))
      _x = self.result.trajectory.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.result.trajectory.intervals)
      buff.write(_struct_I.pack(length))
      for val1 in self.result.trajectory.intervals:
        _v1 = val1.length
        _x = _v1
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
        _v2 = val1.initial_state
        _v3 = _v2.pose
        _v4 = _v3.pose
        _v5 = _v4.position
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = _v4.orientation
        _x = _v6
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_36d.pack(*_v3.covariance))
        _v7 = _v2.velocity
        _v8 = _v7.twist
        _v9 = _v8.linear
        _x = _v9
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v10 = _v8.angular
        _x = _v10
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        buff.write(_struct_36d.pack(*_v7.covariance))
        _v11 = val1.acceleration
        _v12 = _v11.twist
        _v13 = _v12.linear
        _x = _v13
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v14 = _v12.angular
        _x = _v14
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        buff.write(_struct_36d.pack(*_v11.covariance))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = seabee3_actions.msg.MakeTrajectoryResult()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.result.trajectory.header.seq, _x.result.trajectory.header.stamp.secs, _x.result.trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.result.trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.result.trajectory.intervals = []
      for i in range(0, length):
        val1 = seabee3_msgs.msg.TrajectoryInterval()
        _v15 = val1.length
        _x = _v15
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        _v16 = val1.initial_state
        _v17 = _v16.pose
        _v18 = _v17.pose
        _v19 = _v18.position
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v20 = _v18.orientation
        _x = _v20
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 288
        _v17.covariance = _struct_36d.unpack(str[start:end])
        _v21 = _v16.velocity
        _v22 = _v21.twist
        _v23 = _v22.linear
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v24 = _v22.angular
        _x = _v24
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        start = end
        end += 288
        _v21.covariance = _struct_36d.unpack(str[start:end])
        _v25 = val1.acceleration
        _v26 = _v25.twist
        _v27 = _v26.linear
        _x = _v27
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v28 = _v26.angular
        _x = _v28
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        start = end
        end += 288
        _v25.covariance = _struct_36d.unpack(str[start:end])
        self.result.trajectory.intervals.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs))
      _x = self.status.goal_id.id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.status.status))
      _x = self.status.text
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.result.trajectory.header.seq, _x.result.trajectory.header.stamp.secs, _x.result.trajectory.header.stamp.nsecs))
      _x = self.result.trajectory.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.result.trajectory.intervals)
      buff.write(_struct_I.pack(length))
      for val1 in self.result.trajectory.intervals:
        _v29 = val1.length
        _x = _v29
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
        _v30 = val1.initial_state
        _v31 = _v30.pose
        _v32 = _v31.pose
        _v33 = _v32.position
        _x = _v33
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v34 = _v32.orientation
        _x = _v34
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_v31.covariance.tostring())
        _v35 = _v30.velocity
        _v36 = _v35.twist
        _v37 = _v36.linear
        _x = _v37
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v38 = _v36.angular
        _x = _v38
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        buff.write(_v35.covariance.tostring())
        _v39 = val1.acceleration
        _v40 = _v39.twist
        _v41 = _v40.linear
        _x = _v41
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v42 = _v40.angular
        _x = _v42
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        buff.write(_v39.covariance.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg._Header.Header()
      if self.status is None:
        self.status = actionlib_msgs.msg.GoalStatus()
      if self.result is None:
        self.result = seabee3_actions.msg.MakeTrajectoryResult()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.status.goal_id.stamp.secs, _x.status.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.status.status,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.status.text = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.result.trajectory.header.seq, _x.result.trajectory.header.stamp.secs, _x.result.trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.result.trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.result.trajectory.intervals = []
      for i in range(0, length):
        val1 = seabee3_msgs.msg.TrajectoryInterval()
        _v43 = val1.length
        _x = _v43
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        _v44 = val1.initial_state
        _v45 = _v44.pose
        _v46 = _v45.pose
        _v47 = _v46.position
        _x = _v47
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v48 = _v46.orientation
        _x = _v48
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 288
        _v45.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        _v49 = _v44.velocity
        _v50 = _v49.twist
        _v51 = _v50.linear
        _x = _v51
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v52 = _v50.angular
        _x = _v52
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        start = end
        end += 288
        _v49.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        _v53 = val1.acceleration
        _v54 = _v53.twist
        _v55 = _v54.linear
        _x = _v55
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v56 = _v54.angular
        _x = _v56
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        start = end
        end += 288
        _v53.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        self.result.trajectory.intervals.append(val1)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_B = struct.Struct("<B")
_struct_36d = struct.Struct("<36d")
_struct_2i = struct.Struct("<2i")
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
