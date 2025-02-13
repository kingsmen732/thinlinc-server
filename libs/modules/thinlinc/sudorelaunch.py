# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Peter Åstrand for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
__all__ = [ "sudo_question" , "relaunch_via_sudo" ]
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import os
import sys
import gettext
import locale
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from thinlinc import prefix
from thinlinc import tlgtk
from thinlinc import wizard
import subprocess
import tempfile
import shutil
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
if 31 - 31: i1I
def i1I1 ( title , text , secondary_text ) :
 if tlgtk . has_gtk :
  I1Ii111i1I = tlgtk . SimpleMessageDialog (
 title = title ,
 text = text ,
 secondary_text = secondary_text ,
 message_type = tlgtk . Gtk . MessageType . ERROR )
  if 52 - 52: OOooooOo00 * i1I / Iii1i / Ii . i1i1i1111I / Ii
  I1Ii111i1I . run ( )
  I1Ii111i1I . destroy ( )
 else :
  wizard . text_print_wrapped ( text )
  wizard . text_print_wrapped ( secondary_text )
  if 43 - 43: I11iiIi11i1I
  if 31 - 31: IIiIIiIi11I1 * oOO / OooOoo
def sudo_question ( title , program ) :
 oOooo0OOO = gettext . translation ( "tl-misc" ,
 os . path . join ( prefix . get_tl_prefix ( ) ,
 "share/locale" ) ,
 fallback = True )
 Oo000ooO0Oooo = oOooo0OOO . gettext
 if 25 - 25: OooOoo - I1Ii1I1 - iI1iII1I1I1i + i1i1i1111I / iI1iII1I1I1i
 try :
  i1iiiiIIIiIi = "Authorization required"
  II = "Do you want to relaunch %s with 'sudo'?" % ( program , )
  if 34 - 34: Ooo0Ooo + oOO * IIiIIiIi11I1 * OooOoo
  if tlgtk . has_gtk :
   I1Ii111i1I = tlgtk . SimpleMessageDialog (
 title = title ,
 text = i1iiiiIIIiIi ,
 secondary_text = II ,
 cancel_button = True ,
 ok_button_label = Oo000ooO0Oooo ( "_Proceed" ) ,
 message_type = tlgtk . Gtk . MessageType . QUESTION )
   if 25 - 25: Ii / oOO % Ii
   o0 = I1Ii111i1I . run ( )
   I1Ii111i1I . destroy ( )
   if 62 - 62: I1Ii1I1 % I11iiIi11i1I . I1Ii1I1 . OOooooOo00 . i1i1i1111I
   while tlgtk . Gtk . events_pending ( ) :
    tlgtk . Gtk . main_iteration ( )
   if o0 == tlgtk . Gtk . ResponseType . OK :
    relaunch_via_sudo ( title )
    if 87 - 87: Oo - i1I
  else :
   wizard . text_print_wrapped ( i1iiiiIIIiIi )
   iiI1111IIi1 = II
   oOo00O = wizard . text_prompt ( iiI1111IIi1 , [ "Yes" , "no" ] )
   if oOo00O == "yes" :
    relaunch_via_sudo ( title )
    if 59 - 59: Iii1i . OOooooOo00 - i1I
 except KeyboardInterrupt :
  pass
  if 13 - 13: oOO
  if 28 - 28: OooOoo + i1i1i1111I + IiIIii11Ii / I1Ii1I1 + iI1iII1I1I1i
def o0O0ooOoo00o ( ) :
 os . setsid ( )
 if 35 - 35: I1I % i1iiIII111 * I1I
 Ooo0OO = os . open ( os . ttyname ( 0 ) , os . O_RDWR )
 os . close ( Ooo0OO )
 if 6 - 6: i1iiIII111
 if 99 - 99: ooOOO * I1Ii1I1
def relaunch_via_sudo ( title ) :
 if os . getenv ( "DISPLAY" ) :
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  with tempfile . NamedTemporaryFile ( delete = False ) as I1iIiiIIiIi :
   i1I11ii = os . getenv ( "XAUTHORITY" )
   if not i1I11ii :
    i1I11ii = os . path . expanduser ( "~/.Xauthority" )
   try :
    with open ( i1I11ii , 'rb' ) as iii1II11 :
     shutil . copyfileobj ( iii1II11 , I1iIiiIIiIi )
    I1iIiiIIiIi . flush ( )
    os . environ [ "XAUTHORITY" ] = I1iIiiIIiIi . name
   except OSError as I1iI :
    print ( "warning: failed to copy %s to %s:" % ( i1I11ii , I1iIiiIIiIi . name ) ,
 file = sys . stderr )
    print ( I1iI , file = sys . stderr )
    if 5 - 5: I1I / IiIIii11Ii - i1 + i1
    if 4 - 4: ooo000 / ooOOO + ooOOO . I11iiIi11i1I + oOO - i1iiIII111
 ii1Iii = [ "sudo" , "-E" ]
 if tlgtk . has_gtk :
  os . environ [ "SUDO_ASKPASS" ] = os . path . join ( prefix . get_tl_prefix ( ) , "libexec/tl-ssh-askpass" )
  if 77 - 77: i1iiIII111 + OOooooOo00 - Oo % ooo000
  if 74 - 74: Ii + Ooo0Ooo
  if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
  os . environ [ "TLSSOIGNORE" ] = "1"
  ii1Iii . append ( "-A" )
  if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * i1I % oOo0O00
  if 52 - 52: oOo0O00 . I1I + i1I - i1iiIII111 % iI1iII1I1I1i
  if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
  if 37 - 37: OOooooOo00 * i1i1i1111I + oOo0O00 / I1I / OooOoo
  if 4 - 4: i1
 ii1Iii . append ( sys . executable )
 ii1Iii . extend ( sys . argv )
 if 61 - 61: iI1iII1I1I1i . i1I - ooo000 / ooo000 - i1
 try :
  if 19 - 19: Iii1i * Ooo0Ooo . I1Ii1I1 / I11iiIi11i1I * Ii - oOO
  if 32 - 32: iI1iII1I1I1i
  if 18 - 18: I11iiIi11i1I * OOooooOo00 % iI1iII1I1I1i + OOooooOo00
  if tlgtk . has_gtk :
   if 93 - 93: oOO - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
   if 82 - 82: IIiIIiIi11I1 % i1 * ooOOO
   if 57 - 57: oOo0O00
   if 31 - 31: i1iiIII111 + i1i1i1111I % OooOoo
   if 20 - 20: OooOoo - I1I
   II1IIiiI , oOOoOOOO000 = os . openpty ( )
   IIIIi = subprocess . Popen (
 ii1Iii , preexec_fn = o0O0ooOoo00o , universal_newlines = True ,
 pass_fds = [ II1IIiiI ] , stdin = oOOoOOOO000 ,
 stdout = subprocess . PIPE , stderr = subprocess . STDOUT ,
 )
  else :
   os . execvp ( ii1Iii [ 0 ] , ii1Iii )
 except OSError as I1iI :
  i1I1 ( title , "Failed 'sudo' execution" , str ( I1iI ) )
  sys . exit ( 1 )
  if 50 - 50: ooo000 * I1Ii1I1 * iI1iII1I1I1i
  if 17 - 17: Iii1i % i1I - Iii1i % Ooo0Ooo . OooOoo
 oO = ""
 while True :
  if 49 - 49: iI1iII1I1I1i / i1iiIII111 + ooo000
  if 36 - 36: i1i1i1111I + Iii1i - oOO * Ii
  try :
   oo0ooooo0ooo = IIIIi . stdout . readline ( )
   if oo0ooooo0ooo == "" :
    break
   sys . stdout . write ( oo0ooooo0ooo )
   oO += oo0ooooo0ooo
  except KeyboardInterrupt :
   if 61 - 61: i1I . iI1iII1I1I1i / ooOOO * I1Ii1I1 + OOooooOo00 % Oo
   if 100 - 100: Oo + i1I
   if 4 - 4: ooo000 % I1I - i1i1i1111I
   if 76 - 76: i1 * oOo0O00 . OOooooOo00 * i1I . IiIIii11Ii . oOO
   os . write ( II1IIiiI , b'\x03' )
   if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
   if 91 - 91: I1Ii1I1 - I11iiIi11i1I
 OO00OOooO = IIIIi . wait ( )
 IIIIi . stdout . close ( )
 if OO00OOooO == 1 :
  if 58 - 58: i1I - OOooooOo00
  i1I1 ( title , "Failed 'sudo' relaunch" , oO )
 else :
  if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
  if 46 - 46: ooOOO + ooOOO % oOO
  if 2 - 2: i1i1i1111I / Ooo0Ooo / oOO - IIiIIiIi11I1 / IIiIIiIi11I1
  if 58 - 58: i1i1i1111I
  if 38 - 38: i1 - oOo0O00
  if 85 - 85: IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO * i1iiIII111
  if 46 - 46: ooOOO - ooOOO + Oo / I1I * Oo + oOO
  if 98 - 98: I1I / IIiIIiIi11I1 / i1I + OOooooOo00 % Oo + I1I
  if 38 - 38: I1Ii1I1 + oOo0O00
  if 2 - 2: OooOoo % Ii + oOO . OooOoo + IIiIIiIi11I1 * Oo
  os . _exit ( OO00OOooO )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
