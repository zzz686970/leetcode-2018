import hmac
import hashlib
import time
import sys
import struct
# """
# OATH HOTP + TOTP Implementation in python.
# Based on http://tools.ietf.org/html/rfc4226
#          http://tools.ietf.org/html/rfc6238
# Parameter and function names kept inline with the RFC
# (e.g. HOTP, Truncate, K, C etc)
# """

timestep = 30
T0 = 0

def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    HOTP accepts key K and counter C
    optional digits parameter can control the response length
    returns the OATH integer code with {digits} length
    """
    K_bytes = K.encode()
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value
    Truncate represents the function that converts an HMAC
    value into an HOTP value as defined in Section 5.3.
    http://tools.ietf.org/html/rfc4226#section-5.3
    """
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K, digits, each_time,  timeref = 0):
    """TOTP, time-based variant of HOTP
    digits control the response length
    the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
    TOTP is a time-based variant of HOTP.
    It accepts only key K, since the counter is derived from the current time
    optional digits parameter can control the response length
    optional window parameter controls the time window in seconds
    returns the OATH integer code with {digits} length
    """
    C = int ( each_time - timeref ) // timestep
    return HOTP(K, C, digits = digits)

# key_string_512 = '1234567890123456789012345678901234567890123456789012345678901234'
key_string_512 = 'tianyh96@link.cuhk.edu.hkHDECHALLENGE003'
for each_time in [59, 1111111109, 1111111111 ,  1234567890, 2000000000 , 20000000000 , 1550903233, int(time.time()) ]:
    #转换成localtime
    time_local = time.localtime(each_time)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    passwd = TOTP(key_string_512, 10, each_time).zfill(10)
    print (each_time, dt,  passwd)

# 1550905207 2019-02-23 15:00:07 0869021512

"""
+---------------+-----------------------+------------------+--------+--------+
|  Time(sec)    |   Time (UTC format)   | Value of T(Hex)  |  TOTP  | Mode   |
+---------------+-----------------------+------------------+--------+--------+
|  59           |  1970-01-01 00:00:59  | 0000000000000001 |0490693936| SHA512 |
+---------------+-----------------------+------------------+--------+--------+
|  1111111109   |  2005-03-18 01:58:29  | 00000000023523EC |0225091201| SHA512 |
+---------------+-----------------------+------------------+--------+--------+
|  1111111111   |  2005-03-18 01:58:31  | 00000000023523ED |1899943326| SHA512 |
+---------------+-----------------------+------------------+--------+--------+
|  1234567890   |  2009-02-13 23:31:30  | 000000000273EF07 |1493441116| SHA512 |
+---------------+-----------------------+------------------+--------+--------+
|  2000000000   |  2033-05-18 03:33:20  | 0000000003F940AA |1938618901| SHA512 |
+---------------+-----------------------+------------------+--------+--------+
|  20000000000  |  2603-10-11 11:33:20  | 0000000027BC86AA |1047863826| SHA512 |
+---------------+-----------------------+------------------+--------+--------+
|  1550903233   |  2019-02-23 06:27:13  | 000000000314D486 |0810289621| SHA512 |
+---------------+-----------------------+------------------+--------+--------+

"""
