# spooky_hash

> SpookyHash is a public domain noncryptographic hash function producing well-distributed 128-bit hash values for byte arrays of any length.[1]

[1]: http://burtleburtle.net/bob/hash/spooky.html

This python library is a Cython wrapper for the original C++ implementation.  There are both (fast) one-shot hash functions and (slower) hashlib-like hash objects.

## Usage

```python
>>> import spooky_hash
>>> print spooky_hash.hash32('hello world')
2617184861
>>> print long(spooky_hash.Hash32('hello ').update('world'))
2617184861

>>> print spooky_hash.hash64('hello world')
14865987102431973981
>>> print long(spooky_hash.Hash64('hello ').update('world'))
14865987102431973981
>>> print spooky_hash.Hash64('hello ').update('world').hexdigest()
5d12ff9b81984ece

>>> print spooky_hash.hash128_long('hello world')
123716849286372619103118623513034416523
>>> print long(spooky_hash.Hash128('hello ').update('world'))
123716849286372619103118623513034416523
>>> print spooky_hash.Hash128('hello ').update('world').hexdigest()
5d12ff9b81984ece25103f0dee88e18b
>>> import binascii
>>> print binascii.hexlify(spooky_hash.hash128('hello world'))
5d12ff9b81984ece25103f0dee88e18b

>>> print spooky_hash.hash32('hello world', seed=4)
4130951021
>>> print spooky_hash.Hash64('hello ', seed=8).update('world').hexdigest()
e54162c401e00c21
>>> print spooky_hash.Hash128('hello ', seed1=15, seed2=16).update('world').hexdigest()
1d46e376a416468b6c5c3a8f3798042b
```

## See also:

<http://burtleburtle.net/bob/hash/spooky.html>
