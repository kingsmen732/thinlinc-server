# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2024 Emelie Eriksson and Samuel Mannehed for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import sys
import pwd
import subprocess
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from gi . repository import Gtk
from gi . repository import Gdk
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [
 "Label" ,
 ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
class Label ( Gtk . Label ) :
 def __init__ ( self , * args , ** kwargs ) :
  if 98 - 98: I11iiIi11i1I % oOO
  if 31 - 31: i1I
  if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
  if 16 - 16: i1i1i1111I / i1iiIII111
  if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
  if 9 - 9: i1iiIII111
  if 10 - 10: ooOOO / IIiIIiIi11I1 * oOO / i1I / i1I
  super ( ) . __init__ ( * args , ** kwargs )
  self . connect ( "activate-link" , self . _open )
  if 61 - 61: Ooo0Ooo - I1I
 def _open ( self , widget , uri ) :
  if 'SUDO_UID' not in os . environ :
   if 13 - 13: Ooo0Ooo
   return False
   if 46 - 46: iI1iII1I1I1i - Ii * Oo * Ii
  Ooo = Gtk . Clipboard . get ( Gdk . SELECTION_CLIPBOARD )
  Ooo . set_text ( uri , - 1 )
  widget . get_toplevel ( ) . show_notification ( "Copied link to clipboard" , 3.0 )
  return True
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
