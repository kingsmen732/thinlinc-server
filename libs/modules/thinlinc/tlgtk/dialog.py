# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import gettext
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from gi . repository import Gtk
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from thinlinc import prefix
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
__all__ = [ "SimpleMessageDialog" , "EntryDialog" ]
if 98 - 98: I11iiIi11i1I % oOO
i1ii1 = None
if 63 - 63: iI1iI11Ii111
def I11II1Ii ( ) :
 global i1ii1
 if i1ii1 is None :
  iIi = os . path . join ( prefix . get_tl_prefix ( ) , "share" , "locale" )
  ii = gettext . translation ( "tl-misc" , iIi , fallback = True )
  i1ii1 = ii . gettext
  if 91 - 91: iI . I11iiIi11i1I . ooOOO / IIiIIiIi11I1 * oOO / OooOoo
class SimpleMessageDialog ( Gtk . MessageDialog ) :
 def __init__ ( self ,
 title = None ,
 text = None ,
 secondary_text = None ,
 cancel_button = False ,
 ok_button = True ,
 cancel_button_label = None ,
 ok_button_label = None ,
 default_response = Gtk . ResponseType . OK ,
 transient_for = None ,
 modal = False ,
 message_type = Gtk . MessageType . INFO ,
 ) :
  if 93 - 93: IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo . Ooo0Ooo
  if 46 - 46: iI1iII1I1I1i - Ii * Oo * Ii
  Gtk . MessageDialog . __init__ ( self ,
 title = title ,
 text = text ,
 secondary_text = secondary_text ,
 transient_for = transient_for ,
 modal = modal ,
 message_type = message_type ,
 buttons = Gtk . ButtonsType . NONE ,
 )
  if 52 - 52: Oo + I1I / oOO / OooOoo - I1Ii1I1 - ooOOO
  if 60 - 60: iI1iII1I1I1i . oOO
  I11II1Ii ( )
  if 13 - 13: oOO
  if 2 - 2: i1
  if cancel_button :
   if cancel_button_label is None :
    cancel_button_label = i1ii1 ( "_Cancel" )
   self . add_button ( cancel_button_label , Gtk . ResponseType . CANCEL )
  if ok_button :
   if ok_button_label is None :
    ok_button_label = i1ii1 ( "_OK" )
   self . add_button ( ok_button_label , Gtk . ResponseType . OK )
   if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
   if 1 - 1: iI1iII1I1I1i + Ooo0Ooo + oOO * IIiIIiIi11I1
  self . set_default_response ( default_response )
  if 20 - 20: I1I + Ii
  if 75 - 75: Ii % i1iiIII111 * Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
  if 8 - 8: I1Ii1I1 . iI . i1 . Oo - iI1iI11Ii111
  if self . get_titlebar ( ) is not None :
   self . get_titlebar ( ) . get_children ( ) [ 0 ] . hide ( )
   if 32 - 32: Ii % i1i1i1111I % iI1iI11Ii111 - I11iiIi11i1I % i1iiIII111
  self . set_skip_taskbar_hint ( False )
  if 34 - 34: i1iiIII111 * i1
class EntryDialog ( SimpleMessageDialog ) :
 def __init__ ( self ,
 title = None ,
 message_format = None ,
 secondary_text = None ,
 cancel_button = True ,
 ok_button = True ,
 cancel_button_label = None ,
 ok_button_label = None ,
 default_response = Gtk . ResponseType . OK ,
 transient_for = None ,
 modal = False ,
 message_type = Gtk . MessageType . QUESTION ,
 visibility = True ,
 ) :
  if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
  if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
  SimpleMessageDialog . __init__ ( self ,
 title = title ,
 text = message_format ,
 secondary_text = secondary_text ,
 cancel_button = cancel_button ,
 ok_button = ok_button ,
 cancel_button_label = cancel_button_label ,
 ok_button_label = ok_button_label ,
 default_response = default_response ,
 transient_for = transient_for ,
 modal = modal ,
 message_type = message_type ,
 )
  if 32 - 32: I1Ii1I1 + oOO - oOo0O00
  if 79 - 79: Iii1i % oOO * Oo + ooOOO / Oo . oOO
  self . entry = Gtk . Entry ( )
  self . entry . set_visibility ( visibility )
  self . entry . set_width_chars ( 40 )
  self . entry . set_margin_start ( 30 )
  self . entry . set_margin_end ( 30 )
  self . entry . set_margin_bottom ( 12 )
  if 20 - 20: iI + i1iiIII111 / I1I
  if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
  if 43 - 43: ooOOO * I1Ii1I1
  self . entry . set_activates_default ( True )
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  self . vbox . pack_start ( self . entry , expand = False , fill = False , padding = 0 )
  self . entry . show ( )
  if 70 - 70: IiIIii11Ii
  if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
  if 88 - 88: Oo * IiIIii11Ii
  self . entry . grab_focus ( )
  if 100 - 100: iI - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
 def run ( self ) :
  id = Gtk . MessageDialog . run ( self )
  if id != Gtk . ResponseType . OK :
   return None
   if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
  return self . entry . get_text ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
