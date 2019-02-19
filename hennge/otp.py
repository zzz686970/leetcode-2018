import hmac
import hashlib
import time
import sys
import struct

userid = "ninja@example.com"
secret_suffix = "HDECHALLENGE003"
shared_secret = userid+secret_suffix

timestep = 30
T0 = 0

def HOTP(K, C, digits=10):
    """HTOP:
    K is the shared key
    C is the counter value
    digits control the response length
    """
    K_bytes = K.encode()
    C_bytes = struct.pack(">Q", C)
    hmac_sha512 = hmac.new(key = K_bytes, msg=C_bytes, digestmod=hashlib.sha512).hexdigest()
    return Truncate(hmac_sha512)[-digits:]

def Truncate(hmac_sha512):
    """truncate sha512 value"""
    offset = int(hmac_sha512[-1], 16)
    binary = int(hmac_sha512[(offset *2):((offset*2)+8)], 16) & 0x7FFFFFFF
    return str(binary)

def TOTP(K, digits=10, timeref = 0):
    """TOTP, time-based variant of HOTP
    digits control the response length
    the C in HOTP is replaced by ( (currentTime - timeref) / timestep )
    """
    C = int ( 1395069651 - timeref ) // timestep
    return HOTP(K, C, digits = digits)

passwd = TOTP(shared_secret+shared_secret, 10, T0).zfill(10)
print (passwd)

# """
# OATH HOTP + TOTP Implementation in python.
# Based on http://tools.ietf.org/html/rfc4226
#          http://tools.ietf.org/html/rfc6238
# Parameter and function names kept inline with the RFC
# (e.g. HOTP, Truncate, K, C etc)
# """

# import hmac
# import hashlib
# import struct
# import time
# import unittest

# __version__ = "1.0.5"


# def HOTP(K, C, digits=6, digestmod=hashlib.sha1):
#     """
#     HOTP accepts key K and counter C
#     optional digits parameter can control the response length
#     returns the OATH integer code with {digits} length
#     """
#     C_bytes = struct.pack(b"!Q", C)
#     hmac_digest = hmac.new(key=K, msg=C_bytes,
#                            digestmod=digestmod).hexdigest()
#     print("original hamc:", hmac_digest)
#     return Truncate(hmac_digest)[-digits:]


# def TOTP(K, digits=6, window=30, clock=None, digestmod=hashlib.sha1):
#     """
#     TOTP is a time-based variant of HOTP.
#     It accepts only key K, since the counter is derived from the current time
#     optional digits parameter can control the response length
#     optional window parameter controls the time window in seconds
#     returns the OATH integer code with {digits} length
#     """
#     if clock is None:
#         clock = time.time()
#     C = int(clock / window)
#     return HOTP(K, C, digits=digits, digestmod=digestmod)


# def Truncate(hmac_digest):
#     """
#     Truncate represents the function that converts an HMAC
#     value into an HOTP value as defined in Section 5.3.
#     http://tools.ietf.org/html/rfc4226#section-5.3
#     """
#     print("trauncate hmac:", hmac_digest)

#     offset = int(hmac_digest[-1], 16)
#     binary = int(hmac_digest[(offset * 2):((offset * 2) + 8)], 16) & 0x7fffffff
#     print('**********test**********')
#     # last_digit = eval('0x'+passwd[-1])
#     # print(timestamp2)
#     return str(binary)


# class HotpTest(unittest.TestCase):
#     """
#     a very simple test case for HOTP.
#     Based on test vectors from http://www.ietf.org/rfc/rfc4226.txt
#                           and  http://tools.ietf.org/html/rfc6238
#     """
#     def setUp(self):
#         self.key_string = b'12345678901234567890'
#         self.key_string_256 = b'12345678901234567890123456789012'
#         # self.key_string_512 = b'1234567890123456789012345678901234567890123456789012345678901234'
#         ## ''.join(str(ord(c)) for c in 'E0146282@u.nus.eduHDECHALLENGE003')
#         self.key_string_512 = b'6948495254505650641174611011711546101100117726869677265767669787169484851'

#         # self.key_string_512 = b'6948495254505650641174611011711546101100117726869677265767669787'

#     def test_hotp_vectors(self):
#         hotp_result_vector = ['755224', '287082', '359152',
#                               '969429', '338314', '254676',
#                               '287922', '162583', '399871',
#                               '520489']
#         for i, r in enumerate(hotp_result_vector):
#             self.assertEqual(HOTP(self.key_string, i), r)

#     def test_totp_vectors_rfc6238(self):
#         totp_result_vector = [
#             (self.key_string, 59, '94287082', hashlib.sha1),
#             (self.key_string_256, 59, '46119246', hashlib.sha256),
#             (self.key_string_512, 59, '90693936', hashlib.sha512),
#             (self.key_string, 1111111109, '07081804', hashlib.sha1),
#             (self.key_string_256, 1111111109, '68084774', hashlib.sha256),
#             (self.key_string_512, 1111111109, '25091201', hashlib.sha512),
#             (self.key_string, 1111111111, '14050471', hashlib.sha1),
#             (self.key_string_256, 1111111111, '67062674', hashlib.sha256),
#             (self.key_string_512, 1111111111, '99943326', hashlib.sha512),
#             (self.key_string, 1234567890, '89005924', hashlib.sha1),
#             (self.key_string_256, 1234567890, '91819424', hashlib.sha256),
#             (self.key_string_512, 1234567890, '93441116', hashlib.sha512),
#             (self.key_string, 2000000000, '69279037', hashlib.sha1),
#             (self.key_string_256, 2000000000, '90698825', hashlib.sha256),
#             (self.key_string_512, 2000000000, '38618901', hashlib.sha512),
#             (self.key_string, 20000000000, '65353130', hashlib.sha1),
#             (self.key_string_256, 20000000000, '77737706', hashlib.sha256),
#             (self.key_string_512, 20000000000, '47863826', hashlib.sha512),
#         ]
#         for (key, clock, result, digestmod) in totp_result_vector:
#             self.assertEqual(result, TOTP(key,
#                                           digits=8,
#                                           window=30,
#                                           clock=clock,
#                                           digestmod=digestmod))

# if __name__ == '__main__':
#     # unittest.main()
#     print(TOTP(b'12345678901234567890', digits=8, clock = 59, digestmod=hashlib.sha1,))