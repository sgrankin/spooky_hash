from libc.stdint cimport *
from cython.operator import dereference
import binascii

cimport _SpookyV2

# Fast non-incremental hash functions

cpdef hash32(bytes message, uint32_t seed=0):
  return _SpookyV2.Hash32(message, len(message), seed)

cpdef hash64(bytes message, uint64_t seed=0):
  return _SpookyV2.Hash64(message, len(message), seed)

cpdef hash128(bytes message, uint64_t seed1=0, uint64_t seed2=0):
  cdef char digest[16]
  (<uint64_t*>&digest[0])[0] = seed1
  (<uint64_t*>&digest[8])[0] = seed2
  _SpookyV2.Hash128(message, len(message), <uint64_t*>(digest), <uint64_t*>(digest+8))
  return digest[:16]

cpdef hash128_long(bytes message, uint64_t seed1=0, uint64_t seed2=0):
  return long(binascii.hexlify(hash128(message, seed1, seed2)), 16)

# Incremental hashlib-style hash builders.  These bench almost 2x slower than the one-shot
# functions above.

cdef class _Hash:
  cdef _SpookyV2.SpookyHash __hash
  cdef int __digest_size

  def __cinit__(_Hash self, *args, **kwargs):
    pass # def needed so that __cinit__ dispatch is fast for derived classes

  cpdef update(_Hash self, bytes message):
    self.__hash.Update(message, len(message))
    return self

  cpdef bytes digest(_Hash self):
    cdef uint64_t digest[2]
    self.__hash.Final(&digest[0], &digest[1])
    return (<char*>digest)[:self.__digest_size]

  cpdef str hexdigest(_Hash self):
    return binascii.hexlify(self.digest())

  cpdef copy(_Hash self):
    raise NotImplementedError()

  property digest_size:
    def __get__(_Hash self):
      return self.__digest_size

  property block_size:
    def __get__(_Hash self):
      return 16

cdef class Hash32(_Hash):
  def __cinit__(Hash32 self, bytes message=None, uint32_t seed=0):
    self.__digest_size = 4
    self.__hash.Init(seed, seed)
    if message:
      self.__hash.Update(message, len(message))

  def __long__(Hash32 self):
    cdef uint64_t hash1, hash2
    self.__hash.Final(&hash1, &hash2)
    return <uint32_t>hash1

  cpdef copy(Hash32 self):
    copy = Hash32()
    copy.__hash = self.__hash
    return copy

cdef class Hash64(_Hash):
  def __cinit__(Hash64 self, bytes message=None, uint64_t seed=0):
    self.__digest_size = 8
    self.__hash.Init(seed, seed)
    if message:
      self.__hash.Update(message, len(message))

  def __long__(Hash64 self):
    cdef uint64_t hash1, hash2
    self.__hash.Final(&hash1, &hash2)
    return hash1

  cpdef copy(Hash64 self):
    copy = Hash64()
    copy.__hash = self.__hash
    return copy

cdef class Hash128(_Hash):
  def __cinit__(Hash128 self, bytes message=None, uint64_t seed1=0, uint64_t seed2=0):
    self.__digest_size = 16
    self.__hash.Init(seed1, seed2)
    if message:
      self.__hash.Update(message, len(message))

  def __long__(Hash128 self):
    return long(self.hexdigest(), 16)

  cpdef copy(Hash128 self):
    copy = Hash128()
    copy.__hash = self.__hash
    return copy


