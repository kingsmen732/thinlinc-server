# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2002-2014 Cendio AB.
# For more information, see http://www.cendio.com
import os
import sys
if 82 - 82: Iii1i
__all__ = [ "get_tl_prefix" , "get_tl_var_prefix" ,
 "get_tl_sessions_root" , "get_tl_user_dir" , "assert_in_session" , "get_tl_session_dir" ,
 "get_other_tl_session_dir" , "get_tl_session_dev_dir" , "get_tl_session_drives_dir" ,
 "get_tl_run_prefix" , "get_tl_socket_dir" , "get_tl_sessnum" ]
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
def get_tl_prefix ( ) :
 if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
 OOoOoo000O00 = os . path . realpath ( __file__ )
 if 55 - 55: o0Oo - ii1I1iII1I1I . i1I1IiIIiIi1 % oo0O000ooO * iIIiiIIiii1
 for iIi1ii1I1iI11 in range ( 3 ) :
  OOoOoo000O00 = os . path . dirname ( OOoOoo000O00 )
 return OOoOoo000O00
 if 55 - 55: I11II1Ii % iIi
def get_tl_var_prefix ( ) :
 return "/var/opt/thinlinc"
 if 76 - 76: i11 / i1 . Ii . i1i1i1111I + iIIiiIIiii1
def get_tl_sessions_root ( ) :
 return os . path . join ( get_tl_var_prefix ( ) , "sessions" )
 if 31 - 31: oo0O000ooO * I11II1Ii / OooOoo
 if 93 - 93: oo0O000ooO % oo0O000ooO / I1I - Oo . ii1I1iII1I1I
def get_tl_user_dir ( username ) :
 return os . path . join ( get_tl_sessions_root ( ) , username )
 if 46 - 46: i1I1IiIIiIi1 - Ii * Oo * Ii
 if 52 - 52: Oo + I1I / I11II1Ii / OooOoo - I1Ii1I1 - ooOOO
def assert_in_session ( ) :
 oO0 = get_tl_session_dir ( )
 if 13 - 13: I11II1Ii
 if 2 - 2: i1
 if oO0 is None :
  sys . exit ( "TLSESSIONDATA is not set. Are you in a proper ThinLinc session?" )
 if get_tl_sessnum ( oO0 ) is None :
  sys . exit ( "Unable to retrieve session number. Are you in a proper ThinLinc session?" )
  if 22 - 22: oo0O000ooO - o0Oo / I1Ii1I1 . o0Oo
def get_tl_session_dir ( ) :
 return os . getenv ( "TLSESSIONDATA" )
 if 1 - 1: i1I1IiIIiIi1 + ii1I1iII1I1I + I11II1Ii * oo0O000ooO
 if 20 - 20: I1I + Ii
 if 75 - 75: Ii % i1iiIII111 * Ii . oo0O000ooO % iIIiiIIiii1 % I1Ii1I1
def get_other_tl_session_dir ( username , display ) :
 if isinstance ( "" , type ( display ) ) and ":" in display :
  if 8 - 8: I1Ii1I1 . i11 . i1 . Oo - iIi
  if 32 - 32: Ii % i1i1i1111I % iIi - iIIiiIIiii1 % i1iiIII111
  display = display . split ( ":" ) [ 1 ] . split ( "." ) [ 0 ]
 elif isinstance ( 1 , type ( display ) ) :
  display = str ( display )
 return os . path . join ( get_tl_user_dir ( username ) , display )
 if 34 - 34: i1iiIII111 * i1
def get_tl_session_dev_dir ( sessiondata ) :
 return os . path . join ( sessiondata , "dev" )
 if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . i1I1IiIIiIi1
 if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
def get_tl_session_drives_dir ( sessiondata ) :
 return os . path . join ( sessiondata , "drives" )
 if 32 - 32: I1Ii1I1 + I11II1Ii - oOo0O00
 if 79 - 79: Iii1i % I11II1Ii * Oo + ooOOO / Oo . I11II1Ii
def get_tl_run_prefix ( ) :
 return "/var/run/thinlinc"
 if 20 - 20: i11 + i1iiIII111 / I1I
def get_tl_socket_dir ( ) :
 return os . path . join ( get_tl_run_prefix ( ) , "master" )
 if 88 - 88: iIIiiIIiii1 + ooOOO - i1i1i1111I . ii1I1iII1I1I * Ii + Iii1i
def get_tl_sessnum ( sessiondata ) :
 oOo0O00O0ooo = os . path . join ( sessiondata , "sessnum" )
 if 89 - 89: Ii % IiIIii11Ii
 try :
  with open ( oOo0O00O0ooo ) as IiII :
   I1i1i = IiII . read ( )
 except OSError :
  print ( "Warning: Missing session number file" , file = sys . stderr )
  return None
 try :
  I1i1i = int ( I1i1i )
 except ValueError :
  print ( "Warning: Corrupt session number file" , file = sys . stderr )
  return None
 return I1i1i
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
