#!/opt/thinlinc/libexec/python3
# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2002-2014 Cendio AB.
# For more information, see http://www.cendio.com
# Author: Peter Åstrand <astrand@cendio.se>
if 82 - 82: Iii1i
import sys
import gettext
import locale
import os
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from thinlinc import prefix
from thinlinc import tlgtk
try :
 from thinlinc import sso
except ImportError :
 sso = None
 if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
def OOoOoo000O00 ( ) :
 locale . setlocale ( locale . LC_ALL , "" )
 Ooo0Ooo = gettext . translation ( "tl-misc" ,
 os . path . join ( prefix . get_tl_prefix ( ) ,
 "share/locale" ) ,
 fallback = True )
 ii1I1iII1I1I = Ooo0Ooo . gettext
 if 71 - 71: IIiIIiIi11I1
 iI111iiIi11i = ""
 if len ( sys . argv ) > 1 :
  iI111iiIi11i = sys . argv [ 1 ]
  if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
 if sso is not None and "assword:" in iI111iiIi11i :
  Ooo = sso . get_password ( )
  if Ooo is not None :
   print ( Ooo )
   sys . exit ( 0 )
   if 9 - 9: ii . iiI * i1Ii1i
 tlgtk . init ( wmclass = "Credentials" )
 if 93 - 93: oOooo0OOO % ooo0O0oO00 - Ii * Oo * Ii
 OooIIiI = " " . join ( sys . argv [ 1 : ] ) . strip ( )
 if 60 - 60: ooo0O0oO00 . iiI
 if 13 - 13: iiI
 if len ( OooIIiI ) > 0 and OooIIiI [ - 1 ] == ':' :
  OooIIiI = OooIIiI [ : - 1 ]
  if 2 - 2: i1
 IIiIiiIiI = tlgtk . EntryDialog ( title = "Credentials" ,
 message_format = "Authentication required" ,
 secondary_text = OooIIiI ,
 ok_button_label = ii1I1iII1I1I ( "_Authenticate" ) ,
 visibility = False )
 if 34 - 34: iIiii1i + iiI * o00o0OO00O * OooOoo
 Ii111 = IIiIiiIiI . run ( )
 IIiIiiIiI . destroy ( )
 if Ii111 is None :
  sys . exit ( 255 )
 print ( Ii111 )
 if 8 - 8: Ii + i1Ii1i . ii - I1Ii1I1 % ii . i1i1i1111I
if __name__ == "__main__" :
 OOoOoo000O00 ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
