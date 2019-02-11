#!/usr/bin/env python
import struct
from optparse import OptionParser

def decode_cookie(ip,port):
    (a,b,c,d) = [i for i in struct.pack("<I",int(ip))]
    p = [i for i in struct.pack("<H",int(port))]
    port = "0x%02X%02X"%(p[0],p[1])
    return ('.'.join(map(str,[a,b,c,d,]))), int(port,16)

def decode_cookie_rd(ip):
    (a, b, c, d) = [i for i in struct.pack(">I", int(ip,16))]
    return '.'.join(map(str,[a,b,c,d,]))


def main():
    parser = OptionParser("usage : %prog [options]  -h for help")
    parser.add_option('-c',dest ='cookie',type='string',help ='Example: Cookie value should be in the format of "1677787402.36895.0000" for default and "rd5o00000000000000000000ffffc0000201o80" for route domains')
    (options,args) = parser.parse_args()

    if(options.cookie == None):
        print (parser.usage)
        exit(0)
    else:
        print ("\n[*] Cookie Value String to decode: %s\n"%options.cookie)

# Set cookie  with (key:value) pair  for pools in Non default Route Domains is as  BIGipServer<pool_name>:rd5o00000000000000000000ffffc0000201o80

        if ((options.cookie).startswith('rd')):
            (Routedomain,encodedIp,port) = (options.cookie).split("o")
            ip = encodedIp.split('ffff')[1]
            decodedip = decode_cookie_rd(ip)
            print ("[*] Decocded IP and port from the  cookie with RouteDomain ID is  : %s%%%s:%s"%(decodedip,(Routedomain.split('d')[1]),port))

# Default set cookie  with (key:value) pair is as   BIGipServer<pool_name>:1677787402.36895.0000
        else:
            (ip,port,end) = (options.cookie).split(".")
            print ("[*] Decocded  IP and port  value from the cookie is :  %s:%s\n"%(decode_cookie(ip,port)))

if __name__ =="__main__":
    main()

