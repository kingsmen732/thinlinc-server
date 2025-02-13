# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import select
import locale
import logging
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import subprocess
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from thinlinc . rpmvercmp import rpmVersionCompare
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
__all__ = [ "determine_upgrade" , "perform_upgrade" ]
if 98 - 98: I11iiIi11i1I % oOO
def i1ii1 ( fn ) :
 ooo0O0oO00 = subprocess . Popen ( [ "rpm" , "--query" , "--package" , fn ,
 "--queryformat" ,
 "%{NAME}\n%{EPOCH}\n%{VERSION}\n%{RELEASE}\n%{ARCH}\n[%{OBSOLETES},]\n" ] ,
 stdout = subprocess . PIPE , stderr = subprocess . PIPE ,
 universal_newlines = True )
 if 55 - 55: I11II1Ii % iIi
 ( ii , iiI ) = ooo0O0oO00 . communicate ( )
 if 10 - 10: ooOOO / IIiIIiIi11I1 * oOO / I11II1Ii / I11II1Ii
 if ooo0O0oO00 . returncode != 0 :
  logging . error ( "Failed to get information about package '%s':" % fn )
  if 61 - 61: Ooo0Ooo - I1I
  iIIIII1i111i = ii + iiI
  if iIIIII1i111i :
   for IIiiii1IiIiII in ( ii + iiI ) . splitlines ( ) :
    logging . error ( "    " + IIiiii1IiIiII )
    if 32 - 32: iI1iII1I1I1i
  return None
  if 71 - 71: Ii
 iiIII , IioOOOO000 , oOoo0 , Iio0 , i1i , I1i = ii . splitlines ( )
 if 75 - 75: iIi . Ooo0Ooo . I11II1Ii * I11iiIi11i1I % i1iiIII111
 I1i = I1i . split ( "," )
 if len ( I1i ) > 0 :
  I1i = I1i [ : - 1 ]
  if 34 - 34: i1iiIII111 * i1
 return { "name" : iiIII , "versions" : [ { "epoch" : IioOOOO000 , "version" : oOoo0 ,
 "release" : Iio0 , "arch" : i1i ,
 "obsoletes" : I1i } ] }
 if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
def ii1IiIiiII ( name ) :
 ooo0O0oO00 = subprocess . Popen ( [ "rpm" , "--query" , name ,
 "--queryformat" , "%{EPOCH} %{VERSION} %{RELEASE} %{ARCH}\n" ] ,
 stdout = subprocess . PIPE , stderr = subprocess . PIPE ,
 universal_newlines = True )
 if 21 - 21: oOo0O00 % I11iiIi11i1I % oOO . oOo0O00
 ( ii , iiI ) = ooo0O0oO00 . communicate ( )
 if 85 - 85: OooOoo
 if ooo0O0oO00 . returncode != 0 :
  if 34 - 34: Oo
  logging . debug ( "Failed to get information about package '%s':" % name )
  if 96 - 96: ooOOO / iIi + i1iiIII111 / ooOOO / I11iiIi11i1I
  iIIIII1i111i = ii + iiI
  if iIIIII1i111i :
   for IIiiii1IiIiII in ( ii + iiI ) . splitlines ( ) :
    logging . debug ( "    " + IIiiii1IiIiII )
    if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
  return { "name" : name , "versions" : [ ] }
  if 6 - 6: i1iiIII111
 I1I1 = [ ]
 if 91 - 91: Iii1i % i1i1i1111I . OooOoo * oOO
 for IIiiii1IiIiII in ii . splitlines ( ) :
  IioOOOO000 , oOoo0 , Iio0 , i1i = IIiiii1IiIiII . split ( )
  I1I1 . append ( { "epoch" : IioOOOO000 , "version" : oOoo0 ,
 "release" : Iio0 , "arch" : i1i } )
  if 5 - 5: oOO % Ooo0Ooo / OooOoo
 return { "name" : name , "versions" : I1I1 }
 if 6 - 6: Ii + I1I + i1
def II11iiiiIi ( pkgs , nodeps = False ) :
 if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
 if 29 - 29: IiIIii11Ii - oOo0O00
 i1IIiII11 = [ "rpm" , "--erase" , "--quiet" ]
 if nodeps :
  i1IIiII11 . append ( "--nodeps" )
 i1IIiII11 += pkgs
 if 52 - 52: i1iiIII111 % Oo . I1Ii1I1 + ooOOO % Oo . iIi
 logging . info ( "Removing installed package(s): %s" % ", " . join ( pkgs ) )
 if 56 - 56: i1iiIII111 * iIi - I11iiIi11i1I
 ooo0O0oO00 = subprocess . Popen ( i1IIiII11 , stdout = subprocess . PIPE , stderr = subprocess . PIPE ,
 universal_newlines = True )
 if 15 - 15: I1I % Ii + Ooo0Ooo * Iii1i
 ( ii , iiI ) = ooo0O0oO00 . communicate ( )
 if 67 - 67: I1I * Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
 if ooo0O0oO00 . returncode != 0 :
  logging . error ( "Removal of packages failed:" )
  if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
  iIIIII1i111i = ii + iiI
  if iIIIII1i111i :
   for IIiiii1IiIiII in ( ii + iiI ) . splitlines ( ) :
    logging . error ( "    " + IIiiii1IiIiII )
    if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * I11II1Ii % oOo0O00
  return False
  if 52 - 52: oOo0O00 . I1I + I11II1Ii - i1iiIII111 % iI1iII1I1I1i
 return True
 if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
def Oo0 ( pkgs , progress_cb = None ) :
 if 40 - 40: OooOoo / Iii1i
 if 6 - 6: iIi - i1i1i1111I
 i1IIiII11 = [ "rpm" , "--upgrade" , "--quiet" , "--hash" ]
 i1IIiII11 += pkgs
 if 59 - 59: I11II1Ii * ooo000 / ooo000 - i1
 logging . info ( "Installing package(s): %s" % ", " . join ( map ( os . path . basename , pkgs ) ) )
 if 19 - 19: Iii1i * Ooo0Ooo . I1Ii1I1 / I11iiIi11i1I * Ii - oOO
 with subprocess . Popen (
 i1IIiII11 , stdout = subprocess . PIPE , stderr = subprocess . PIPE ,
 ) as ooo0O0oO00 :
  if progress_cb is None :
   ( ii , iiI ) = ooo0O0oO00 . communicate ( )
  else :
   if 32 - 32: iI1iII1I1I1i
   I111II111I1I = len ( pkgs ) + 2
   IIi1I1I1i = 0
   O0O = 0
   if 31 - 31: i1iiIII111 + i1i1i1111I % OooOoo
   progress_cb ( 0 )
   if 20 - 20: OooOoo - I1I
   if 9 - 9: i1iiIII111 - iI1iII1I1I1i % Ii - I1I
   O0o0OOoOOOO = ooo0O0oO00 . stdout . fileno ( )
   IIIIi = ooo0O0oO00 . stderr . fileno ( )
   if 50 - 50: ooo000 * I1Ii1I1 * iI1iII1I1I1i
   ii = b""
   iiI = b""
   while True :
    try :
     ( i111ii1I , IiII , oOOOOOOoO ) = select . select ( [ O0o0OOoOOOO , IIIIi ] , [ ] , [ ] )
    except :
     break
     if 3 - 3: Ii % i1 + i1i1i1111I * Ii * i1 . I1I
    if O0o0OOoOOOO in i111ii1I :
     iiI1i = os . read ( O0o0OOoOOOO , 8192 )
     ii += iiI1i
     if 73 - 73: ooOOO - IiIIii11Ii
     for iIi1 in iiI1i :
      if 4 - 4: ooo000 % I1I - i1i1i1111I
      if 76 - 76: i1 * oOo0O00 . iIi * I11II1Ii . IiIIii11Ii . oOO
      if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
      iIi1 = bytes ( [ iIi1 ] )
      if 91 - 91: I1Ii1I1 - I11iiIi11i1I
      if iIi1 == b"#" :
       O0O += 1
      elif iIi1 == b"\n" :
       IIi1I1I1i += 1
       O0O = 0
       if 84 - 84: oOO % iI1iII1I1I1i - Ooo0Ooo
     progress_cb ( 100 * IIi1I1I1i // I111II111I1I + 100 * O0O // 50 // I111II111I1I )
     if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / I11II1Ii
    if IIIIi in i111ii1I :
     iiI += os . read ( IIIIi , 8192 )
     if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
    ooo0O0oO00 . poll ( )
    if ooo0O0oO00 . returncode is not None :
     break
     if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
   if ooo0O0oO00 . returncode is None :
    ooo0O0oO00 . wait ( )
    if 63 - 63: IIiIIiIi11I1 / IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
   progress_cb ( 100 )
   if 52 - 52: oOo0O00 / I11II1Ii * IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO
 if ooo0O0oO00 . returncode != 0 :
  logging . error ( "Installation of packages failed:" )
  if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
  iIIIII1i111i = ii + iiI
  if iIIIII1i111i :
   for IIiiii1IiIiII in ( ii + iiI ) . splitlines ( ) :
    IIiiii1IiIiII = IIiiii1IiIiII . decode ( locale . getpreferredencoding ( False ) ,
 errors = 'replace' )
    logging . error ( "    " + IIiiii1IiIiII )
    if 30 - 30: I1I
  return False
  if 41 - 41: oOO
 return True
 if 98 - 98: I1I / IIiIIiIi11I1 / I11II1Ii + iIi % Oo + I1I
def determine_upgrade ( fns ) :
 logging . info ( "Analyzing upgrade path..." )
 if 38 - 38: I1Ii1I1 + oOo0O00
 iii1I1 = [ ]
 Ii1 = [ ]
 OOOooOOoo = [ ]
 O00 = [ ]
 i1Ii = [ ]
 if 32 - 32: oOO
 for oOOOO0OO00 in fns :
  logging . debug ( "Checking '%s'..." % os . path . basename ( oOOOO0OO00 ) )
  if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
  iI = i1ii1 ( oOOOO0OO00 )
  if iI is None :
   return None
   if 58 - 58: IIiIIiIi11I1 % Ii + oOo0O00 / oOo0O00 * iI1iII1I1I1i * i1i1i1111I
  I11iIi1i1iIi = ii1IiIiiII ( iI [ "name" ] )
  if 10 - 10: I1Ii1I1
  OoO0O0OO0 = set ( iI [ "versions" ] [ 0 ] [ "obsoletes" ] )
  for O0o in OoO0O0OO0 :
   OOooo000o0O = ii1IiIiiII ( O0o )
   if len ( OOooo000o0O [ "versions" ] ) > 0 :
    i1Ii . append ( O0o )
    if 74 - 74: I1Ii1I1
    if 61 - 61: iI1iII1I1I1i * I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
  OOO0ooOO = "%s-%s.%s" % ( iI [ "versions" ] [ 0 ] [ "version" ] ,
 iI [ "versions" ] [ 0 ] [ "release" ] ,
 iI [ "versions" ] [ 0 ] [ "arch" ] )
  OO0oOoOOOoO0 = ""
  for Iii1I1I1 in I11iIi1i1iIi [ "versions" ] :
   OO0oOoOOOoO0 += "%s-%s.%s " % ( Iii1I1I1 [ "version" ] , Iii1I1I1 [ "release" ] , Iii1I1I1 [ "arch" ] )
   if 57 - 57: I1I
  logging . debug ( "Version to install: %s" % OOO0ooOO )
  logging . debug ( "Current version(s): %s" % OO0oOoOOOoO0 )
  if 35 - 35: oOo0O00 / IIiIIiIi11I1 - Iii1i . iIi * i1
  if len ( I11iIi1i1iIi [ "versions" ] ) == 0 :
   Ii1 . append ( oOOOO0OO00 )
  else :
   if 91 - 91: oOO + Iii1i
   if 71 - 71: i1 . iI1iII1I1I1i . OooOoo . IIiIIiIi11I1
   OOOoO0oO = ( iI [ "versions" ] [ 0 ] [ "epoch" ] ,
 iI [ "versions" ] [ 0 ] [ "version" ] ,
 iI [ "versions" ] [ 0 ] [ "release" ] )
   iII = ( I11iIi1i1iIi [ "versions" ] [ 0 ] [ "epoch" ] ,
 I11iIi1i1iIi [ "versions" ] [ 0 ] [ "version" ] ,
 I11iIi1i1iIi [ "versions" ] [ 0 ] [ "release" ] )
   if 44 - 44: Iii1i + oOo0O00 + I11II1Ii % IIiIIiIi11I1 * OooOoo
   OO00OOO = rpmVersionCompare ( OOOoO0oO , iII )
   if 25 - 25: I11II1Ii / i1 - Ii - IIiIIiIi11I1 + ooo000 * ooo000
   if OO00OOO <= 0 :
    O00 . append ( oOOOO0OO00 )
   else :
    if 85 - 85: IIiIIiIi11I1 / OooOoo . I11II1Ii % Oo + Oo - I11iiIi11i1I
    if 59 - 59: OooOoo
    if iI [ "versions" ] [ 0 ] [ "arch" ] != I11iIi1i1iIi [ "versions" ] [ 0 ] [ "arch" ] :
     if 53 - 53: i1i1i1111I / ooOOO - iIi + ooo000 * i1i1i1111I * i1iiIII111
     iii1I1 . append ( I11iIi1i1iIi [ "name" ] )
     Ii1 . append ( oOOOO0OO00 )
    else :
     OOOooOOoo . append ( oOOOO0OO00 )
     if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
 return { "remove" : iii1I1 , "install" : Ii1 ,
 "upgrade" : OOOooOOoo , "ignore" : O00 ,
 "obsolete" : i1Ii }
 if 81 - 81: i1 + i1i1i1111I * Oo - Oo * I1Ii1I1 - oOo0O00
def perform_upgrade ( actions , progress_cb = None , output_cb = None ) :
 iiIIIIi = 0
 iiIIIIi += len ( actions [ "remove" ] )
 iiIIIIi += len ( actions [ "install" ] )
 iiIIIIi += len ( actions [ "upgrade" ] )
 if 32 - 32: I11II1Ii - I1Ii1I1 * I1Ii1I1 / iIi . ooo000
 if progress_cb is not None :
  progress_cb ( 0 )
  if 80 - 80: IIiIIiIi11I1 / OooOoo % iI1iII1I1I1i / ooOOO * ooOOO - Iii1i
 O0ooOO0O0O0O = 0
 if 59 - 59: ooo000 / Oo - i1
 if 49 - 49: I11II1Ii + oOo0O00 + ooo000 . Iii1i + I11II1Ii
 if 88 - 88: iIi . IIiIIiIi11I1 * i1 + IiIIii11Ii % I1I / iIi
 if 33 - 33: OooOoo * Oo * Ii * iI1iII1I1I1i + I11II1Ii . IiIIii11Ii
 if 94 - 94: oOo0O00 . i1iiIII111
 if 96 - 96: I1I / oOO / I11iiIi11i1I + I11iiIi11i1I
 if 35 - 35: IIiIIiIi11I1 + oOo0O00
 if 96 - 96: iI1iII1I1I1i . OooOoo . i1
 if 87 - 87: ooo000 * IiIIii11Ii % ooo000 . ooOOO . Oo % iI1iII1I1I1i
 if 48 - 48: ooOOO * ooo000 % IiIIii11Ii * i1 . Iii1i - iIi
 if len ( actions [ "remove" ] ) > 0 :
  oo0O0O0Ooooo = II11iiiiIi ( actions [ "remove" ] , nodeps = True )
  if not oo0O0O0Ooooo :
   return False
   if 39 - 39: Oo . oOO / ooo000 / iI1iII1I1I1i
  O0ooOO0O0O0O += len ( actions [ "remove" ] )
  if progress_cb is not None :
   progress_cb ( 100 * O0ooOO0O0O0O / iiIIIIi )
   if 48 - 48: oOO * I11II1Ii - OooOoo * Oo - iIi - Ooo0Ooo
   if 36 - 36: IiIIii11Ii
 if progress_cb is not None :
  IiIi1I11I = lambda ooo0O0oO00 : progress_cb ( 100 * O0ooOO0O0O0O // iiIIIIi + ooo0O0oO00 * ( iiIIIIi - O0ooOO0O0O0O ) // iiIIIIi )
 else :
  IiIi1I11I = None
  if 8 - 8: I1I + iI1iII1I1I1i . I1I . iIi
 oo0O0O0Ooooo = Oo0 ( actions [ "install" ] + actions [ "upgrade" ] ,
 progress_cb = IiIi1I11I )
 if not oo0O0O0Ooooo :
  return False
  if 3 - 3: i1iiIII111
 if progress_cb is not None :
  progress_cb ( 100 )
  if 32 - 32: I1I % i1i1i1111I
 return True
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
