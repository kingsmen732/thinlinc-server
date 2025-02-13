# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2024 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import select
import logging
import locale
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import subprocess
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [ "determine_upgrade" , "perform_upgrade" ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
def iI111iiIi11i ( string ) :
 return [ s . strip ( ) for s in string . split ( "," ) if s . strip ( ) ]
 if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
 if 57 - 57: iiIi1 - i1 % i1 % i1i1i1111I . Ii
 if 30 - 30: Ii
def ooO0Oo0o00 ( fn ) :
 oOooo0OOO = subprocess . Popen ( [ "dpkg-deb" ,
 "--showformat" ,
 "${Package}\n${Version}\n${Architecture}\n${Conflicts}\n${Replaces}\n" ,
 "--show" , fn ] , universal_newlines = True ,
 stdout = subprocess . PIPE , stderr = subprocess . PIPE )
 if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
 ( ii1Ii , oOooO0 ) = oOooo0OOO . communicate ( )
 if 13 - 13: ooo0O0oO00
 if oOooo0OOO . returncode != 0 :
  logging . error ( "Failed to get information about package '%s':" % fn )
  if 2 - 2: i1
  IIiIiiIiI = ii1Ii + oOooO0
  if IIiIiiIiI :
   for OO0000 in ( ii1Ii + oOooO0 ) . splitlines ( ) :
    logging . error ( "    " + OO0000 )
    if 92 - 92: I1I / I1I + o00o0OO00O . ooo0O0oO00
  return None
  if 8 - 8: Ii + o00o0OO00O . iIiii1i - I1Ii1I1 % iIiii1i . i1i1i1111I
 ii1iIi1i11i , I111IIi11IiI , o0OOOooO00oo , IIii , OO00 = ii1Ii . splitlines ( )
 IIii = iI111iiIi11i ( IIii )
 OO00 = iI111iiIi11i ( OO00 )
 if 39 - 39: iIiii1i * ooo0O0oO00 . Oo + ooOOO / Oo
 return { "name" : ii1iIi1i11i , "versions" : [ { "version" : I111IIi11IiI ,
 "arch" : o0OOOooO00oo ,
 "conflicts" : IIii ,
 "replaces" : OO00 } ] }
 if 14 - 14: OooOoo % oOo0O00 + I1I % i1iiIII111 * ooOOO / iIiii1i
def OoOo ( name ) :
 oOooo0OOO = subprocess . Popen ( [ "dpkg-query" ,
 "--showformat" , "${Package}\n${Version}\n${Architecture}\n${Status}" ,
 "--show" , name ] , universal_newlines = True ,
 stdout = subprocess . PIPE , stderr = subprocess . PIPE )
 if 43 - 43: ooOOO * I1Ii1I1
 ( ii1Ii , oOooO0 ) = oOooo0OOO . communicate ( )
 if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
 if oOooo0OOO . returncode != 0 :
  if 70 - 70: IiIIii11Ii
  logging . debug ( "Failed to get information about package '%s'" % name )
  if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
  IIiIiiIiI = ii1Ii + oOooO0
  if IIiIiiIiI :
   for OO0000 in ( ii1Ii + oOooO0 ) . splitlines ( ) :
    logging . debug ( "    " + OO0000 )
    if 88 - 88: Oo * IiIIii11Ii
  return { "name" : name , "versions" : [ ] }
  if 100 - 100: iiIi1 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
 name , I111IIi11IiI , o0OOOooO00oo , I11iIi1i = ii1Ii . splitlines ( )
 if 49 - 49: IIiIIiIi11I1
 iIIiii1iI , OOO , I11iIi1i = I11iIi1i . split ( " " )
 if 83 - 83: ooo0O0oO00 - Iii1i + ooOOO . o00o0OO00O / ooOOO
 if 5 - 5: iiIi1
 if OOO != "ok" :
  logging . error ( "Existing package '%s' is in a broken state" % name )
  return None
  if 56 - 56: i1iiIII111 * iiIi1 - iIiii1i
  if 15 - 15: I1I % Ii + Ooo0Ooo * Iii1i
  if 67 - 67: I1I * Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
  if 52 - 52: ooo0O0oO00 + I1I / ooo000 - I1Ii1I1 * o00o0OO00O % oOo0O00
  if 52 - 52: oOo0O00 . I1I + o00o0OO00O - i1iiIII111 % iI1iII1I1I1i
  if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
  if 37 - 37: iiIi1 * i1i1i1111I + oOo0O00 / I1I / OooOoo
  if 4 - 4: i1
 if I11iIi1i == "not-installed" or I11iIi1i == "config-files" :
  return { "name" : name , "versions" : [ ] }
  if 61 - 61: iI1iII1I1I1i . o00o0OO00O - ooo000 / ooo000 - i1
  if 19 - 19: Iii1i * Ooo0Ooo . I1Ii1I1 / iIiii1i * Ii - ooo0O0oO00
 if I11iIi1i != "installed" :
  logging . error ( "Existing package '%s' is in an invalid state '%s'" % ( name , I11iIi1i ) )
  return None
  if 32 - 32: iI1iII1I1I1i
 return { "name" : name , "versions" : [ { "version" : I111IIi11IiI , "arch" : o0OOOooO00oo } ] }
 if 18 - 18: iIiii1i * iiIi1 % iI1iII1I1I1i + iiIi1
def O0OO ( pkgs ) :
 if 34 - 34: ooOOO * iIiii1i
 logging . error ( "Package removal not supported" )
 return False
 if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + ooo0O0oO00
def iiI1 ( pkgs , oldpkgs , progress_cb = None ) :
 logging . info ( "Installing package(s): %s" % ", " . join ( map ( os . path . basename , pkgs ) ) )
 if 20 - 20: i1i1i1111I / Ooo0Ooo - ooo0O0oO00 + Ooo0Ooo - I1I . Ooo0Ooo
 oOOoOOOO000 , IIIIi = os . pipe ( )
 if 50 - 50: ooo000 * I1Ii1I1 * iI1iII1I1I1i
 i111ii1I = [ "dpkg" , "--install" ]
 if 18 - 18: Ii / ooo000 + I1I + iI1iII1I1I1i
 if 42 - 42: ooOOO - ooOOO - i1i1i1111I
 if 61 - 61: ooo0O0oO00
 i111ii1I += [ "--force-confmiss" , "--force-confold" ]
 if 7 - 7: i1i1i1111I / Ii * Iii1i
 if 32 - 32: iiIi1 . OooOoo
 if 31 - 31: Oo - o00o0OO00O
 i111ii1I += [ "--force-overwrite" ]
 if 28 - 28: ooOOO * I1Ii1I1 + iiIi1 % Oo
 if 100 - 100: Oo + o00o0OO00O
 if 4 - 4: ooo000 % I1I - i1i1i1111I
 if 76 - 76: i1 * oOo0O00 . iiIi1 * o00o0OO00O . IiIIii11Ii . ooo0O0oO00
 if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
 if len ( oldpkgs ) > 0 :
  i111ii1I += [ "--ignore-depends=%s" % "," . join ( oldpkgs ) ]
  if 91 - 91: I1Ii1I1 - iIiii1i
 i111ii1I += [ "--status-fd" , str ( IIIIi ) ]
 i111ii1I += pkgs
 if 84 - 84: ooo0O0oO00 % iI1iII1I1I1i - Ooo0Ooo
 if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / o00o0OO00O
 with subprocess . Popen ( i111ii1I , stdin = subprocess . DEVNULL , stdout = subprocess . PIPE ,
 stderr = subprocess . PIPE , pass_fds = [ IIIIi ] ) as oOooo0OOO :
  if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
  if progress_cb is not None :
   progress_cb ( 0 )
   if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
   if 63 - 63: IIiIIiIi11I1 / IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
  o00OO0 = oOooo0OOO . stdout . fileno ( )
  O0OO0OOOOoo0o = oOooo0OOO . stderr . fileno ( )
  if 41 - 41: ooo0O0oO00
  if 98 - 98: I1I / IIiIIiIi11I1 / o00o0OO00O + iiIi1 % Oo + I1I
  ooOo00o = { }
  if 36 - 36: Ii
  ii1Ii = b""
  oOooO0 = b""
  oOoo0OOOOOoo = b""
  while True :
   try :
    ( OoO , o00ooo0Oooo , oOOOO0OO00 ) = select . select ( [ o00OO0 , O0OO0OOOOoo0o , oOOoOOOO000 ] , [ ] , [ ] )
   except :
    break
    if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
   if oOOoOOOO000 in OoO :
    oOoo0OOOOOoo += os . read ( oOOoOOOO000 , 8192 )
    if 71 - 71: I1Ii1I1
    while b"\n" in oOoo0OOOOOoo :
     ( OO0000 , oOoo0OOOOOoo ) = oOoo0OOOOOoo . split ( b"\n" , 1 )
     OO0000 = OO0000 . decode ( locale . getpreferredencoding ( False ) )
     if 1 - 1: iiIi1 - oOo0O00 - i1 . oOo0O00
     if OO0000 . startswith ( "processing:" ) :
      ( O0o , oo0o0oOo , ii1iIi1i11i ) = OO0000 . split ( ":" , 2 )
      oo0o0oOo = oo0o0oOo . strip ( )
      ii1iIi1i11i = ii1iIi1i11i . strip ( ": " )
      if 10 - 10: I1Ii1I1
      if oo0o0oOo == "install" or oo0o0oOo == "upgrade" :
       if 40 - 40: o00o0OO00O * iI1iII1I1I1i + iI1iII1I1I1i . oOo0O00 * ooo000
       if ii1iIi1i11i in ooOo00o :
        logging . warning ( "Warning: Package '%s' " "mentioned multiple times" % ii1iIi1i11i )
        if 35 - 35: IIiIIiIi11I1 % i1i1i1111I - Ii % i1iiIII111 - iiIi1
        if 33 - 33: i1i1i1111I
       ooOo00o [ ii1iIi1i11i ] = { "state" : "" , "mode" : oo0o0oOo }
     elif OO0000 . startswith ( "status:" ) :
      iI1iiI11IIi1 = OO0000 . split ( ":" , 3 )
      ii1iIi1i11i = iI1iiI11IIi1 [ 1 ] . strip ( )
      I11iIi1i = iI1iiI11IIi1 [ 2 ] . strip ( )
      if 56 - 56: i1i1i1111I - IiIIii11Ii - i1iiIII111 - Oo + i1iiIII111 / Ooo0Ooo
      if I11iIi1i == "error" :
       logging . warning ( "Warning during installation of" " '%s': %s" % ( ii1iIi1i11i , repr ( iI1iiI11IIi1 [ 3 ] ) ) )
       if 89 - 89: ooo000 + Ii % i1i1i1111I - i1iiIII111
      else :
       if ii1iIi1i11i in ooOo00o :
        ooOo00o [ ii1iIi1i11i ] [ "state" ] = I11iIi1i
        if 33 - 33: ooo000 . Iii1i % ooo0O0oO00
     OoOOooO0oOO0Oo = 0
     for I11iIi1i in ooOo00o . values ( ) :
      iiI1i1IiiiIi1 = 0
      if 20 - 20: oOo0O00 * ooOOO % IIiIIiIi11I1 - IIiIIiIi11I1
      if I11iIi1i [ "mode" ] == "install" :
       if I11iIi1i [ "state" ] == "half-installed" :
        iiI1i1IiiiIi1 = 25
       elif I11iIi1i [ "state" ] == "unpacked" :
        iiI1i1IiiiIi1 = 50
       elif I11iIi1i [ "state" ] == "half-configured" :
        iiI1i1IiiiIi1 = 75
       elif I11iIi1i [ "state" ] == "installed" :
        iiI1i1IiiiIi1 = 100
      elif I11iIi1i [ "mode" ] == "upgrade" :
       if I11iIi1i [ "state" ] == "half-configured" :
        iiI1i1IiiiIi1 = 17
       elif I11iIi1i [ "state" ] == "unpacked" :
        iiI1i1IiiiIi1 = 33
       elif I11iIi1i [ "state" ] == "half-installed" :
        iiI1i1IiiiIi1 = 50
        I11iIi1i [ "mode" ] = "replace"
      elif I11iIi1i [ "mode" ] == "replace" :
       if I11iIi1i [ "state" ] == "half-installed" :
        iiI1i1IiiiIi1 = 50
       elif I11iIi1i [ "state" ] == "unpacked" :
        iiI1i1IiiiIi1 = 67
       elif I11iIi1i [ "state" ] == "half-configured" :
        iiI1i1IiiiIi1 = 83
       elif I11iIi1i [ "state" ] == "installed" :
        iiI1i1IiiiIi1 = 100
        if 32 - 32: OooOoo % I1I - iIiii1i % OooOoo
      OoOOooO0oOO0Oo += iiI1i1IiiiIi1 / len ( pkgs )
      if 9 - 9: i1iiIII111 - ooOOO % Iii1i
     if progress_cb is not None :
      progress_cb ( OoOOooO0oOO0Oo )
      if 37 - 37: o00o0OO00O + IIiIIiIi11I1 % iI1iII1I1I1i / IIiIIiIi11I1 % i1iiIII111 + ooo0O0oO00
   if o00OO0 in OoO :
    ii1Ii += os . read ( o00OO0 , 8192 )
   if O0OO0OOOOoo0o in OoO :
    oOooO0 += os . read ( O0OO0OOOOoo0o , 8192 )
    if 98 - 98: iI1iII1I1I1i - I1I + i1 * ooo000 % i1
   oOooo0OOO . poll ( )
   if oOooo0OOO . returncode is not None :
    break
    if 100 - 100: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
 if progress_cb is not None :
  progress_cb ( 100 )
  if 85 - 85: IIiIIiIi11I1 / OooOoo . o00o0OO00O % Oo + Oo - iIiii1i
  if 59 - 59: OooOoo
  if 53 - 53: i1i1i1111I / ooOOO - iiIi1 + ooo000 * i1i1i1111I * i1iiIII111
  if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
  if 81 - 81: i1 + i1i1i1111I * Oo - Oo * I1Ii1I1 - oOo0O00
  if 4 - 4: i1iiIII111
  if 8 - 8: IiIIii11Ii + OooOoo - i1
 OOO = True
 if len ( ooOo00o ) != len ( pkgs ) :
  OOO = False
 else :
  for I11iIi1i in ooOo00o . values ( ) :
   if I11iIi1i [ "state" ] != "installed" :
    OOO = False
    break
    if 68 - 68: I1Ii1I1 % I1Ii1I1 / iiIi1 . ooo000
 if not OOO :
  logging . error ( "Installation of packages failed:" )
  if 80 - 80: IIiIIiIi11I1 / OooOoo % iI1iII1I1I1i / ooOOO * ooOOO - Iii1i
  IIiIiiIiI = ii1Ii + oOooO0
  if IIiIiiIiI :
   for OO0000 in ( ii1Ii + oOooO0 ) . splitlines ( ) :
    OO0000 = OO0000 . decode ( locale . getpreferredencoding ( False ) ,
 errors = 'replace' )
    logging . error ( "    " + OO0000 )
    if 60 - 60: ooo0O0oO00 * i1i1i1111I / iI1iII1I1I1i
  return False
  if 45 - 45: Ooo0Ooo + ooOOO * oOo0O00 - ooo000 / IIiIIiIi11I1
 return True
 if 14 - 14: o00o0OO00O - IiIIii11Ii
def O0 ( a , b ) :
 O0Ii1Ii1 = subprocess . call ( [ "dpkg" , "--compare-versions" , a , "lt" , b ] )
 if O0Ii1Ii1 == 0 :
  return - 1
  if 25 - 25: OooOoo + Oo * Ii * iI1iII1I1I1i + Ii
 oOO = subprocess . call ( [ "dpkg" , "--compare-versions" , a , "gt" , b ] )
 if oOO == 0 :
  return 1
  if 96 - 96: I1I / ooo0O0oO00 / iIiii1i + iIiii1i
 return 0
 if 35 - 35: IIiIIiIi11I1 + oOo0O00
def determine_upgrade ( fns ) :
 logging . info ( "Analyzing upgrade path..." )
 if 96 - 96: iI1iII1I1I1i . OooOoo . i1
 OOo = [ ]
 oO000O0O0 = [ ]
 ooOo00O0o0o0 = [ ]
 OOooooOOooo0 = [ ]
 II1111I11 = [ ]
 if 94 - 94: Oo - IIiIIiIi11I1
 for O0oOoOo0O00 in fns :
  logging . debug ( "Checking '%s'..." % os . path . basename ( O0oOoOo0O00 ) )
  if 46 - 46: ooo000
  oOo = ooO0Oo0o00 ( O0oOoOo0O00 )
  if oOo is None :
   return None
   if 85 - 85: iiIi1 * Iii1i
  Ii1ii = OoOo ( oOo [ "name" ] )
  if Ii1ii is None :
   return None
   if 98 - 98: o00o0OO00O / i1 / OooOoo + Iii1i % ooOOO
   if 19 - 19: ooOOO % I1Ii1I1
  IIii = oOo [ "versions" ] [ 0 ] [ "conflicts" ]
  IIii = set ( [ spec . split ( " " , 1 ) [ 0 ] for spec in IIii ] )
  OO00 = oOo [ "versions" ] [ 0 ] [ "replaces" ]
  OO00 = set ( [ spec . split ( " " , 1 ) [ 0 ] for spec in OO00 ] )
  if 15 - 15: OooOoo . IiIIii11Ii . o00o0OO00O / Iii1i + ooOOO / Ii
  Ii1iIII11i = IIii & OO00
  for oo000OO0ooO in Ii1iIII11i :
   OoO0OooO0ooo = OoOo ( oo000OO0ooO )
   if OoO0OooO0ooo is None :
    return None
   if len ( OoO0OooO0ooo [ "versions" ] ) > 0 :
    II1111I11 . append ( oo000OO0ooO )
    if 36 - 36: o00o0OO00O * i1iiIII111 % iiIi1 - oOo0O00 % iI1iII1I1I1i
  oo0000oOOoOOO = "%s_%s" % ( oOo [ "versions" ] [ 0 ] [ "version" ] ,
 oOo [ "versions" ] [ 0 ] [ "arch" ] )
  if len ( Ii1ii [ "versions" ] ) == 0 :
   OoOOO0OOo0Ooo = ""
  else :
   OoOOO0OOo0Ooo = "%s_%s" % ( Ii1ii [ "versions" ] [ 0 ] [ "version" ] ,
 Ii1ii [ "versions" ] [ 0 ] [ "arch" ] )
   if 11 - 11: Ooo0Ooo
  logging . debug ( "Version to install: %s" % oo0000oOOoOOO )
  logging . debug ( "Current version(s): %s" % OoOOO0OOo0Ooo )
  if 13 - 13: IiIIii11Ii * ooo0O0oO00 / o00o0OO00O . ooo0O0oO00 % Oo + Ooo0Ooo
  if len ( Ii1ii [ "versions" ] ) == 0 :
   oO000O0O0 . append ( O0oOoOo0O00 )
  else :
   OoO0OOo00oo0O = O0 ( oOo [ "versions" ] [ 0 ] [ "version" ] ,
 Ii1ii [ "versions" ] [ 0 ] [ "version" ] )
   if OoO0OOo00oo0O <= 0 :
    OOooooOOooo0 . append ( O0oOoOo0O00 )
   else :
    ooOo00O0o0o0 . append ( O0oOoOo0O00 )
    if 29 - 29: IiIIii11Ii
 return { "remove" : OOo , "install" : oO000O0O0 ,
 "upgrade" : ooOo00O0o0o0 , "ignore" : OOooooOOooo0 ,
 "obsolete" : II1111I11 }
 if 72 - 72: ooOOO . i1 % Ooo0Ooo
def perform_upgrade ( actions , progress_cb = None , output_cb = None ) :
 IiOOooo00 = 0
 IiOOooo00 += len ( actions [ "remove" ] )
 IiOOooo00 += len ( actions [ "install" ] )
 IiOOooo00 += len ( actions [ "upgrade" ] )
 if 52 - 52: OooOoo
 if progress_cb is not None :
  progress_cb ( 0 )
  if 95 - 95: i1i1i1111I . iIiii1i * ooo000 / iI1iII1I1I1i - I1Ii1I1 + IiIIii11Ii
 O0oooo0o0oO = 0
 if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - iIiii1i / IiIIii11Ii . Ooo0Ooo
 if 15 - 15: o00o0OO00O * iIiii1i - oOo0O00
 if len ( actions [ "remove" ] ) > 0 :
  if 6 - 6: iiIi1 - Ii
  logging . error ( "Package removal not supported" )
  return False
  if 1 - 1: I1I + OooOoo
  if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
 if progress_cb is not None :
  oO00 = lambda oOooo0OOO : progress_cb ( 100 * O0oooo0o0oO / IiOOooo00 + oOooo0OOO * ( IiOOooo00 - O0oooo0o0oO ) / IiOOooo00 )
 else :
  oO00 = None
  if 30 - 30: IiIIii11Ii % ooo000 . Ii * Iii1i - iI1iII1I1I1i
 OOO = iiI1 ( actions [ "install" ] + actions [ "upgrade" ] ,
 actions [ "remove" ] + actions [ "obsolete" ] ,
 progress_cb = oO00 )
 if not OOO :
  return False
  if 10 - 10: Ooo0Ooo % ooo000 % Ooo0Ooo
 if progress_cb is not None :
  progress_cb ( 100 )
  if 38 - 38: ooo000
 return True
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
