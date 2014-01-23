from nose.tools import *

import spooky_hash
import binascii

def test_Hash32():
   h = spooky_hash.Hash32('hello', seed=0)
   copy = h.copy()
   h.update('world')
   eq_(4, h.digest_size)
   eq_('f47d8a47', h.hexdigest())
   eq_(binascii.unhexlify('f47d8a47'), h.digest())
   eq_(0x478a7df4, long(h))

   assert_not_equal(0x478a7df4, long(copy))
   copy.update('world')
   eq_(0x478a7df4, long(copy))

def test_Hash64():
   h = spooky_hash.Hash64('hello', seed=0)
   copy = h.copy()
   h.update('world')
   eq_(8, h.digest_size)
   eq_('f47d8a477ddd6b4f', h.hexdigest())
   eq_(binascii.unhexlify('f47d8a477ddd6b4f'), h.digest())
   eq_(0x4f6bdd7d478a7df4, long(h))

   assert_not_equal(0x4f6bdd7d478a7df4, long(copy))
   copy.update('world')
   eq_(0x4f6bdd7d478a7df4, long(copy))

def test_Hash128():
   h = spooky_hash.Hash128('hello', seed1=0, seed2=0)
   copy = h.copy()
   h.update('world')
   eq_(16, h.digest_size)
   eq_('f47d8a477ddd6b4fbf3b493f8396830d', h.hexdigest())
   eq_(binascii.unhexlify('f47d8a477ddd6b4fbf3b493f8396830d'), h.digest())
   eq_(0xf47d8a477ddd6b4fbf3b493f8396830d, long(h))

   assert_not_equal('f47d8a477ddd6b4fbf3b493f8396830d', copy.hexdigest())
   copy.update('world')
   eq_(0xf47d8a477ddd6b4fbf3b493f8396830d, long(copy))

def test_hash32():
   h = spooky_hash.hash32('hi', seed=0)
   eq_(0x9aa6d50f, h)

   h = spooky_hash.hash32('helloworld', seed=0)
   eq_(0x478a7df4, h)

def test_hash64():
   h = spooky_hash.hash64('helloworld', seed=0)
   eq_(0x4f6bdd7d478a7df4, h)

def test_hash128():
   h = spooky_hash.hash128('hi', seed1=0, seed2=0)
   eq_('\x0f\xd5\xa6\x9a\x2a\x77\x5a\xcd\x50\xed\xd1\xb6\xdc\xa8\x63\x1d', h)
   h = spooky_hash.hash128('helloworld')
   eq_(binascii.unhexlify('f47d8a477ddd6b4fbf3b493f8396830d'), h)

def test_hash128_long():
   eq_(0xf47d8a477ddd6b4fbf3b493f8396830d, spooky_hash.hash128_long('helloworld'))

