# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2019 Pierre Ossman for Cendio AB.
# Copyright 2021, Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import re
import shlex
import subprocess
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from shutil import which
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [ "CPU_ARCH" , "X86_64" ,
 "PACKAGE_FORMAT" , "RPM" , "DEB" ,
 "DISTRIBUTION" , "RHEL" , "FEDORA" ,
 "SLED" , "SLES" ,
 "UBUNTU" , "DEBIAN" ,
 "DISTRIBUTION_FAMILY" , "SLE" ,
 "DISTRIBUTION_VERSION" ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
CPU_ARCH = None
X86_64 = "x86_64"
if 31 - 31: i1I
PACKAGE_FORMAT = None
RPM = "rpm"
DEB = "deb"
if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
DISTRIBUTION = None
DISTRIBUTION_FAMILY = None
RHEL = "RHEL"
FEDORA = "Fedora"
SLE = "SLE"
SLED = "SLED"
SLES = "SLES"
UBUNTU = "Ubuntu"
DEBIAN = "Debian"
if 16 - 16: i1i1i1111I / i1iiIII111
DISTRIBUTION_VERSION = None
if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
if 9 - 9: i1iiIII111
if 10 - 10: ooOOO / IIiIIiIi11I1 * oOO / i1I / i1I
def oOooo0OOO ( fn ) :
 try :
  with open ( fn , "rt" ) as Oo000ooO0Oooo :
   IIiI = Oo000ooO0Oooo . readline ( ) . strip ( "\n" )
 except OSError :
  return None
  if 60 - 60: iI1iII1I1I1i . oOO
 return IIiI
 if 13 - 13: oOO
def iiIII ( ) :
 try :
  with open ( "/etc/os-release" , "rt" ) as Oo000ooO0Oooo :
   IioOOOO000 = Oo000ooO0Oooo . read ( ) . splitlines ( )
 except OSError :
  return None
  if 85 - 85: OooOoo - oOo0O00 / Ii / oOO % i1iiIII111 . Ii
 I1ii1iii1i = { }
 for IIiI in IioOOOO000 :
  try :
   I1i = shlex . split ( IIiI , comments = True )
  except ValueError :
   if 75 - 75: IiI11Ii111 . Ooo0Ooo . i1I * I11iiIi11i1I % i1iiIII111
   continue
   if 34 - 34: i1iiIII111 * i1
   if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
  if len ( I1i ) != 1 :
   continue
   if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
  try :
   ( IiI11I , IiiIii11iII1 ) = I1i [ 0 ] . split ( "=" , 1 )
  except ValueError :
   continue
   if 27 - 27: I1I + ooOOO * IIiIIiIi11I1 % Ii + Ooo0Ooo . ooOOO
  I1ii1iii1i [ IiI11I ] = IiiIii11iII1
  if 6 - 6: i1iiIII111
 return ( I1ii1iii1i . get ( "ID" , "linux" ) , I1ii1iii1i . get ( "VERSION_ID" , None ) ,
 I1ii1iii1i . get ( "ID_LIKE" , "" ) . split ( " " ) )
 if 99 - 99: ooOOO * I1Ii1I1
def Oooo0o0oO0 ( ) :
 IIiI = oOooo0OOO ( "/etc/system-release-cpe" )
 if IIiI is None :
  return None
  if 71 - 71: OooOoo - Ii
 if not IIiI . startswith ( "cpe:/" ) :
  return None
  if 40 - 40: IiIIii11Ii . i1 / Oo
 I1i = IIiI [ 5 : ] . split ( ":" )
 if 46 - 46: IiI11Ii111 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
 if len ( I1i ) < 7 :
  I1i += [ "" ] * ( 7 - len ( I1i ) )
  if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
 if I1i [ 0 ] != "o" :
  return None
  if 29 - 29: IiIIii11Ii - oOo0O00
 return I1i
 if 30 - 30: I1I . ooo000
def OOO ( ) :
 try :
  with subprocess . Popen ( [ "lsb_release" , "--id" , "--release" ] ,
 stdout = subprocess . PIPE , universal_newlines = True ) as OooOoo0OO0OO0 :
   IiIi1Ii1111 = OooOoo0OO0OO0 . stdout . read ( )
 except OSError :
  return None
  if 95 - 95: I1I * Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo * oOo0O00
 id = None
 OO0O0oo = None
 if 54 - 54: I1Ii1I1 - i1I % ooo000 + Iii1i % oOo0O00 + I1I
 for IIiI in IiIi1Ii1111 . splitlines ( ) :
  if IIiI . startswith ( "Distributor ID:" ) :
   id = IIiI . split ( ":" , 1 ) [ 1 ] . strip ( )
  if IIiI . startswith ( "Release:" ) :
   OO0O0oo = IIiI . split ( ":" , 1 ) [ 1 ] . strip ( )
   if 56 - 56: i1iiIII111 % iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
 if ( id is None ) or ( OO0O0oo is None ) :
  return None
  if 85 - 85: oOo0O00
 return ( id , OO0O0oo )
 if 66 - 66: IiI11Ii111 * i1i1i1111I + oOo0O00 / I1I / Iii1i / Ii
def IiII11i11II ( ) :
 global DISTRIBUTION , DISTRIBUTION_FAMILY , DISTRIBUTION_VERSION
 if 52 - 52: Iii1i / Oo
 if 100 - 100: I1Ii1I1 / I11iiIi11i1I * Ii - oOO
 iiI1111II = iiIII ( )
 if iiI1111II is not None :
  ( O0OO , oO0O0oOOo0Oo , O0ooooO ) = iiI1111II
  if 89 - 89: I1I * i1i1i1111I
  if 54 - 54: oOO + Ooo0Ooo - I1I . Ooo0Ooo
  if O0OO == 'rhel' :
   DISTRIBUTION = RHEL
  elif O0OO == 'fedora' :
   DISTRIBUTION = FEDORA
  elif O0OO == 'sles' :
   DISTRIBUTION = SLES
  elif O0OO == 'sled' :
   DISTRIBUTION = SLED
  elif O0OO == 'ubuntu' :
   DISTRIBUTION = UBUNTU
  elif O0OO == 'debian' :
   DISTRIBUTION = DEBIAN
   if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
   if 54 - 54: oOO * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
   if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - IiI11Ii111
   if 69 - 69: ooo000
   if 76 - 76: Iii1i * Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
  DISTRIBUTION_VERSION = oO0O0oOOo0Oo
  if 49 - 49: iI1iII1I1I1i / i1iiIII111 + ooo000
  if 36 - 36: i1i1i1111I + Iii1i - oOO * Ii
  for id in [ O0OO ] + O0ooooO :
   if id == 'rhel' :
    DISTRIBUTION_FAMILY = RHEL
   elif id == 'fedora' :
    DISTRIBUTION_FAMILY = FEDORA
   elif id == 'sles' :
    DISTRIBUTION_FAMILY = SLE
   elif id == 'sled' :
    DISTRIBUTION_FAMILY = SLE
   elif id == 'ubuntu' :
    DISTRIBUTION_FAMILY = UBUNTU
   elif id == 'debian' :
    DISTRIBUTION_FAMILY = DEBIAN
    if 45 - 45: i1i1i1111I * Ii
   if DISTRIBUTION_FAMILY is not None :
    break
    if 97 - 97: i1
 if DISTRIBUTION_FAMILY is not None :
  return
  if 26 - 26: IiI11Ii111
  if 20 - 20: IIiIIiIi11I1 / Oo
 IIIi1111iiIi1 = Oooo0o0oO0 ( )
 if IIIi1111iiIi1 is not None :
  if IIIi1111iiIi1 [ 1 ] == "redhat" :
   if IIIi1111iiIi1 [ 2 ] == "enterprise_linux" :
    DISTRIBUTION_FAMILY = RHEL
    DISTRIBUTION = RHEL
    DISTRIBUTION_VERSION = IIIi1111iiIi1 [ 3 ]
  elif IIIi1111iiIi1 [ 1 ] == "centos" :
   DISTRIBUTION_FAMILY = RHEL
   DISTRIBUTION_VERSION = IIIi1111iiIi1 [ 3 ]
   if 4 - 4: ooo000 % I1I - i1i1i1111I
 if DISTRIBUTION_FAMILY is not None :
  return
  if 76 - 76: i1 * oOo0O00 . IiI11Ii111 * i1I . IiIIii11Ii . oOO
  if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
 if os . path . exists ( "/etc/fedora-release" ) :
  DISTRIBUTION_FAMILY = FEDORA
  if 91 - 91: I1Ii1I1 - I11iiIi11i1I
  IIiI = oOooo0OOO ( "/etc/fedora-release" )
  if IIiI is not None :
   OO00OOooO = re . match ( "Fedora release (?P<ver>[0-9]+) .*" , IIiI )
   if OO00OOooO :
    DISTRIBUTION = FEDORA
    DISTRIBUTION_VERSION = OO00OOooO . group ( "ver" )
    if 58 - 58: i1I - IiI11Ii111
 if DISTRIBUTION_FAMILY is not None :
  return
  if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
  if 46 - 46: ooOOO + ooOOO % oOO
 if os . path . exists ( "/etc/redhat-release" ) :
  if 2 - 2: i1i1i1111I / Ooo0Ooo / oOO - IIiIIiIi11I1 / IIiIIiIi11I1
  DISTRIBUTION_FAMILY = RHEL
  if 58 - 58: i1i1i1111I
  IIiI = oOooo0OOO ( "/etc/redhat-release" )
  if IIiI is not None :
   OO00OOooO = re . match ( "Red Hat Enterprise Linux[ ]?(?P<type>.*) release (?P<ver>[0-9.]+) .*" ,
 IIiI )
   if OO00OOooO :
    DISTRIBUTION = RHEL
    DISTRIBUTION_VERSION = "%s%s" % ( OO00OOooO . group ( "ver" ) , OO00OOooO . group ( "type" ) )
    if 38 - 38: i1 - oOo0O00
 if DISTRIBUTION_FAMILY is not None :
  return
  if 85 - 85: IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO * i1iiIII111
  if 46 - 46: ooOOO - ooOOO + Oo / I1I * Oo + oOO
 if os . path . exists ( "/etc/novell-release" ) or os . path . exists ( "/etc/SuSE-release" ) :
  DISTRIBUTION_FAMILY = SLE
  if 98 - 98: I1I / IIiIIiIi11I1 / i1I + IiI11Ii111 % Oo + I1I
  if os . path . exists ( "/etc/novell-release" ) :
   IIiI = oOooo0OOO ( "/etc/novell-release" )
  else :
   IIiI = oOooo0OOO ( "/etc/SuSE-release" )
   if 38 - 38: I1Ii1I1 + oOo0O00
  if IIiI is not None :
   OO00OOooO = re . match ( "SUSE Linux Enterprise (?P<type>.+) (?P<ver>[0-9]+)" ,
 IIiI )
   if OO00OOooO :
    if OO00OOooO . group ( "type" ) == "Desktop" :
     DISTRIBUTION = SLED
     DISTRIBUTION_VERSION = OO00OOooO . group ( "ver" )
    elif OO00OOooO . group ( "type" ) == "Server" :
     DISTRIBUTION = SLES
     DISTRIBUTION_VERSION = OO00OOooO . group ( "ver" )
     if 2 - 2: OooOoo % Ii + oOO . OooOoo + IIiIIiIi11I1 * Oo
 if DISTRIBUTION_FAMILY is not None :
  return
  if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
 iIi111ii = OOO ( )
 if iIi111ii is not None :
  if 20 - 20: i1i1i1111I + Oo / Ooo0Ooo % IiI11Ii111 % IiI11Ii111
  if iIi111ii [ 0 ] == "Ubuntu" :
   DISTRIBUTION_FAMILY = UBUNTU
   DISTRIBUTION = UBUNTU
   DISTRIBUTION_VERSION = iIi111ii [ 1 ]
   if 29 - 29: iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % i1I + IiI11Ii111
   if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
   if 71 - 71: I1Ii1I1
 if DISTRIBUTION_FAMILY is not None :
  return
  if 1 - 1: IiI11Ii111 - oOo0O00 - i1 . oOo0O00
  if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
  if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
 if os . path . exists ( "/etc/debian_version" ) :
  DISTRIBUTION_FAMILY = DEBIAN
  if 19 - 19: Ii
  if 22 - 22: i1I % iI1iII1I1I1i + Oo
  if 60 - 60: ooo000 + I11iiIi11i1I + IIiIIiIi11I1 % i1i1i1111I - Ii % Ooo0Ooo
  if 95 - 95: ooOOO % i1i1i1111I . i1
 if DISTRIBUTION_FAMILY is not None :
  return
  if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
  if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
  if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
def OOO0O0oOoOOOo ( ) :
 global CPU_ARCH
 global PACKAGE_FORMAT
 global DISTRIBUTION , DISTRIBUTION_FAMILY , DISTRIBUTION_VERSION
 if 99 - 99: Iii1i % oOO * Ooo0Ooo - Ii
 II1IiiI1iII = os . uname ( ) [ 4 ]
 if II1IiiI1iII == "x86_64" :
  CPU_ARCH = X86_64
  if 90 - 90: Iii1i . IiI11Ii111 * I1Ii1I1 / oOo0O00
 Iii = False
 ooO0O00OOOOo = False
 if 59 - 59: ooo000 / IiI11Ii111 / OooOoo % ooOOO . Ooo0Ooo
 if which ( "rpm" ) is not None :
  Iii = True
 if which ( "dpkg" ) is not None :
  ooO0O00OOOOo = True
  if 44 - 44: Iii1i + oOo0O00 + i1I % IIiIIiIi11I1 * OooOoo
  if 58 - 58: IiIIii11Ii - oOO + ooo000 % i1iiIII111 - I1I
  if 90 - 90: ooo000 % i1
 if Iii and ooO0O00OOOOo :
  if 100 - 100: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
  if 85 - 85: IIiIIiIi11I1 / OooOoo . i1I % Oo + Oo - I11iiIi11i1I
  if 59 - 59: OooOoo
  oOOOoO00OO00O0o = "/var/lib/rpm/"
  i1Ii1iIi11iI = ""
  if 22 - 22: Iii1i + i1iiIII111 . oOo0O00 . IiIIii11Ii + OooOoo - i1
  if 68 - 68: I1Ii1I1 % I1Ii1I1 / IiI11Ii111 . ooo000
  if os . path . isfile ( oOOOoO00OO00O0o + "rpmdb.sqlite" ) :
   i1Ii1iIi11iI = oOOOoO00OO00O0o + "rpmdb.sqlite"
  elif os . path . isfile ( oOOOoO00OO00O0o + "Packages.db" ) :
   i1Ii1iIi11iI = oOOOoO00OO00O0o + "Packages.db"
  elif os . path . isfile ( oOOOoO00OO00O0o + "Packages" ) :
   i1Ii1iIi11iI = oOOOoO00OO00O0o + "Packages"
  else :
   Iii = False
   if 80 - 80: IIiIIiIi11I1 / OooOoo % iI1iII1I1I1i / ooOOO * ooOOO - Iii1i
  if i1Ii1iIi11iI != "" :
   try :
    O0ooOO0O0O0O = os . stat ( i1Ii1iIi11iI )
    if 59 - 59: ooo000 / Oo - i1
    if 49 - 49: i1I + oOo0O00 + ooo000 . Iii1i + i1I
    if 88 - 88: IiI11Ii111 . IIiIIiIi11I1 * i1 + IiIIii11Ii % I1I / IiI11Ii111
    if 33 - 33: OooOoo * Oo * Ii * iI1iII1I1I1i + i1I . IiIIii11Ii
    if 94 - 94: oOo0O00 . i1iiIII111
    if 96 - 96: I1I / oOO / I11iiIi11i1I + I11iiIi11i1I
    if 35 - 35: IIiIIiIi11I1 + oOo0O00
    if 96 - 96: iI1iII1I1I1i . OooOoo . i1
    if 87 - 87: ooo000 * IiIIii11Ii % ooo000 . ooOOO . Oo % iI1iII1I1I1i
    if 48 - 48: ooOOO * ooo000 % IiIIii11Ii * i1 . Iii1i - IiI11Ii111
    if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
    if 90 - 90: Ooo0Ooo * OooOoo . Ii
    if 5 - 5: Oo - i1 . oOO
    if O0ooOO0O0O0O . st_size < 1048576 :
     Iii = False
     if 18 - 18: IiIIii11Ii - oOO * i1I - OooOoo
   except FileNotFoundError :
    Iii = False
    if 54 - 54: IIiIIiIi11I1 . Ooo0Ooo % Ii + IiIIii11Ii * iI1iII1I1I1i / iI1iII1I1I1i
    if 31 - 31: IiIIii11Ii . IiIIii11Ii % Ii
    if 51 - 51: Oo / i1i1i1111I - I1I
    if 83 - 83: Iii1i % i1iiIII111 . OooOoo / I1I % oOO . I1I
    if 76 - 76: i1iiIII111 / OooOoo
  try :
   O0ooOO0O0O0O = os . stat ( '/var/lib/dpkg/status' )
   if O0ooOO0O0O0O . st_size < 1024 :
    ooO0O00OOOOo = False
  except FileNotFoundError :
   ooO0O00OOOOo = False
   if 77 - 77: ooOOO
   if 19 - 19: ooOOO % I1Ii1I1
 if Iii and ooO0O00OOOOo :
  PACKAGE_FORMAT = None
 else :
  if Iii :
   PACKAGE_FORMAT = RPM
  elif ooO0O00OOOOo :
   PACKAGE_FORMAT = DEB
   if 15 - 15: OooOoo . IiIIii11Ii . i1I / Iii1i + ooOOO / Ii
 IiII11i11II ( )
 if 17 - 17: I11iiIi11i1I - i1i1i1111I . iI1iII1I1I1i - I11iiIi11i1I + Oo % iI1iII1I1I1i
OOO0O0oOoOOOo ( )
if 65 - 65: Ii % I11iiIi11i1I
if 39 - 39: Iii1i * IIiIIiIi11I1 . Ooo0Ooo - Oo
if DISTRIBUTION_VERSION is not None :
 DISTRIBUTION_VERSION = DISTRIBUTION_VERSION . lower ( )
 if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . IiI11Ii111 + i1I
if __name__ == "__main__" :
 print ( "CPU architecture: %s" % CPU_ARCH )
 print ( "Package format: %s" % PACKAGE_FORMAT )
 print ( "Distribution: %s" % DISTRIBUTION )
 print ( "Distribution family: %s" % DISTRIBUTION_FAMILY )
 print ( "Distribution version: %s" % DISTRIBUTION_VERSION )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
