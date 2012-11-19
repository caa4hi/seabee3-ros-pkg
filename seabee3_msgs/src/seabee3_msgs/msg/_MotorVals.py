"""autogenerated by genmsg_py from MotorVals.msg. Do not edit."""
import roslib.message
import struct


class MotorVals(roslib.message.Message):
  _md5sum = "206324076e37080a4aa9d397c298278e"
  _type = "seabee3_msgs/MotorVals"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8[9] mask
int8[9] motors
"""
  __slots__ = ['mask','motors']
  _slot_types = ['int8[9]','int8[9]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       mask,motors
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(MotorVals, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.mask is None:
        self.mask = [0,0,0,0,0,0,0,0,0]
      if self.motors is None:
        self.motors = [0,0,0,0,0,0,0,0,0]
    else:
      self.mask = [0,0,0,0,0,0,0,0,0]
      self.motors = [0,0,0,0,0,0,0,0,0]

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
      buff.write(_struct_9b.pack(*self.mask))
      buff.write(_struct_9b.pack(*self.motors))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      start = end
      end += 9
      self.mask = _struct_9b.unpack(str[start:end])
      start = end
      end += 9
      self.motors = _struct_9b.unpack(str[start:end])
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
      buff.write(self.mask.tostring())
      buff.write(self.motors.tostring())
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
      end = 0
      start = end
      end += 9
      self.mask = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=9)
      start = end
      end += 9
      self.motors = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=9)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_9b = struct.Struct("<9b")
