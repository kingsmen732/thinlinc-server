# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import math
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from gi . repository import Gdk
from gi . repository import Gtk
from gi . repository import GdkPixbuf
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from thinlinc import tlgtk
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
__all__ = [
 "boxed_list" , "check_list" , "radio_list" , "spinner_text" , "scrolled_view" ,
 "switch_list" , "boxed_label_list" , "scale_aware_surface_from_pixbuf" ,
 ]
if 98 - 98: I11iiIi11i1I % oOO
def scrolled_view ( widget , hsb_policy = Gtk . PolicyType . AUTOMATIC ,
 vsb_policy = Gtk . PolicyType . AUTOMATIC ) :
 i1ii1 = Gtk . ScrolledWindow ( )
 i1ii1 . set_policy ( hsb_policy , vsb_policy )
 i1ii1 . set_shadow_type ( Gtk . ShadowType . NONE )
 if 63 - 63: iI1iI11Ii111
 I11II1Ii = Gtk . Viewport ( )
 I11II1Ii . set_shadow_type ( Gtk . ShadowType . NONE )
 I11II1Ii . add ( widget )
 if 32 - 32: o0o0ooo00oo . i1i1i1111I
 i1ii1 . add ( I11II1Ii )
 if 5 - 5: I11iiIi11i1I . ooOOO / IIiIIiIi11I1
 return i1ii1
 if 28 - 28: iI1iI11Ii111 / IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo
def check_list ( choices , title = None , subtitle = None ) :
 IIII1i1 = [ Gtk . CheckButton ( label = choice , can_focus = False )
 for choice in choices ]
 if 84 - 84: Ii . i1iiIII111 - i1 . I1I / iI1iII1I1I1i % OooOoo
 def oOooO0 ( list , row ) :
  i1iiiiIIIiIi = IIII1i1 [ row . get_index ( ) ]
  i1iiiiIIIiIi . emit ( 'activate' )
  if 22 - 22: ooo000 . iI1iII1I1I1i + Ooo0Ooo + oOO
 oOoo0 = boxed_list ( IIII1i1 , title , subtitle , oOooO0 )
 return ( oOoo0 , IIII1i1 )
 if 95 - 95: i1iiIII111 . Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
def boxed_list ( widgets , title = None , subtitle = None ,
 row_activated_cb = None , activatable = True ) :
 oOoo0 = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL , spacing = 6 )
 if 8 - 8: I1Ii1I1 . o0o0ooo00oo . i1 . Oo - iI1iI11Ii111
 if title :
  iiI1111IIi1 = tlgtk . Label ( halign = Gtk . Align . FILL , xalign = 0 )
  iiI1111IIi1 . set_markup ( "<b>%s</b>" % ( title , ) )
  oOoo0 . pack_start ( iiI1111IIi1 , expand = False , fill = False , padding = 0 )
  if 92 - 92: ooOOO / OooOoo - oOo0O00
 if subtitle :
  OoO = tlgtk . Label (
 label = subtitle ,
 halign = Gtk . Align . FILL ,
 xalign = 0 ,
 wrap = True , max_width_chars = 0 ,
 use_markup = True ,
 )
  oOoo0 . pack_start ( OoO , expand = False , fill = False , padding = 0 )
  if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
 if not widgets :
  oOoo0 . show_all ( )
  return oOoo0
  if 32 - 32: I1Ii1I1 + oOO - oOo0O00
 IiiIii11iII1 = Gtk . Frame ( )
 oOoo0 . pack_start ( IiiIii11iII1 , expand = False , fill = False , padding = 6 )
 if 27 - 27: I1I + ooOOO * IIiIIiIi11I1 % Ii + Ooo0Ooo . ooOOO
 ii1Ii1I = Gtk . ListBox ( activate_on_single_click = True ,
 selection_mode = Gtk . SelectionMode . NONE )
 IiiIii11iII1 . add ( ii1Ii1I )
 if 71 - 71: oOO - Oo . OooOoo . Ii % iI1iI11Ii111 + oOO
 if row_activated_cb :
  ii1Ii1I . connect ( 'row-activated' , row_activated_cb )
  if 19 - 19: Ii / IiIIii11Ii + IiIIii11Ii . I1I
 for i1I11ii in widgets :
  iii1II11 = Gtk . ListBoxRow (
 selectable = False ,
 activatable = activatable ,
 )
  if 32 - 32: Oo / Ii - IIiIIiIi11I1
  iIIiii1iI = 12
  OOO = 12
  if 83 - 83: oOO - Iii1i + ooOOO . iI1iI11Ii111 / ooOOO
  iII1II11iI1 = Gtk . Box ( orientation = Gtk . Orientation . HORIZONTAL )
  iII1II11iI1 . set_margin_top ( iIIiii1iI )
  iII1II11iI1 . set_margin_bottom ( iIIiii1iI )
  iII1II11iI1 . pack_start ( i1I11ii , expand = True , fill = True , padding = OOO )
  iii1II11 . add ( iII1II11iI1 )
  if 25 - 25: Ooo0Ooo . I11iiIi11i1I . oOO
  ii1Ii1I . add ( iii1II11 )
  if 88 - 88: I1I * Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo * oOo0O00
 oOoo0 . show_all ( )
 return oOoo0
 if 65 - 65: Ooo0Ooo * ooo000 + oOo0O00
def boxed_label_list ( labels , title = None , subtitle = None ) :
 IIII1i1 = [ tlgtk . Label ( label = label ) for label in labels ]
 return boxed_list ( IIII1i1 , title , subtitle , activatable = False )
 if 71 - 71: Ooo0Ooo / ooo000
def radio_list ( choices , title = None , subtitle = None ) :
 if 87 - 87: o0o0ooo00oo / oOo0O00 % oOO - oOo0O00 . I1I + Ooo0Ooo
 if 75 - 75: i1iiIII111 * iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
 if 85 - 85: oOo0O00
 if 66 - 66: o0o0ooo00oo * i1i1i1111I + oOo0O00 / I1I / Iii1i / Ii
 if 32 - 32: i1i1i1111I % Ooo0Ooo - iI1iI11Ii111 * I1I
 if 92 - 92: IIiIIiIi11I1 - i1 - Iii1i / Ooo0Ooo . I1Ii1I1 / I11iiIi11i1I
 IIII1i1 = [ Gtk . RadioButton ( label = choice ) for choice in choices ]
 for i1I11ii in IIII1i1 [ 1 : ] :
  i1I11ii . join_group ( IIII1i1 [ 0 ] )
  if 60 - 60: oOO
 def oOooO0 ( list , row ) :
  i1iiiiIIIiIi = IIII1i1 [ row . get_index ( ) ]
  i1iiiiIIIiIi . emit ( 'activate' )
  if 32 - 32: iI1iII1I1I1i
 oOoo0 = boxed_list ( IIII1i1 , title , subtitle , oOooO0 )
 return ( oOoo0 , IIII1i1 )
 if 18 - 18: I11iiIi11i1I * o0o0ooo00oo % iI1iII1I1I1i + o0o0ooo00oo
def switch_list ( choices , title = None , subtitle = None ) :
 IIII1i1 = [ ]
 O0OO = [ ]
 if 34 - 34: ooOOO * I11iiIi11i1I
 for oOo0Oo in choices :
  if 35 - 35: oOO + OooOoo . OooOoo
  Ii1iiIII1IIii = Gtk . Box ( orientation = Gtk . Orientation . HORIZONTAL )
  if 54 - 54: Iii1i % ooo000 % Iii1i - IiIIii11Ii
  O00000oO = tlgtk . Label ( label = oOo0Oo )
  Ii1iiIII1IIii . pack_start ( O00000oO , expand = False , fill = False , padding = 12 )
  if 29 - 29: IIiIIiIi11I1 - ooo000 . i1iiIII111
  oo00oO000 = Gtk . Switch ( )
  oo00oO000 . set_can_focus ( False )
  Ii1iiIII1IIii . pack_end ( oo00oO000 , expand = False , fill = False , padding = 0 )
  IIII1i1 . append ( oo00oO000 )
  if 4 - 4: Ooo0Ooo
  O0OO . append ( Ii1iiIII1IIii )
  if 18 - 18: Ii / ooo000 + I1I + iI1iII1I1I1i
 def oOooO0 ( list , row ) :
  i1iiiiIIIiIi = IIII1i1 [ row . get_index ( ) ]
  i1iiiiIIIiIi . emit ( 'activate' )
  if 42 - 42: ooOOO - ooOOO - i1i1i1111I
 oOoo0 = boxed_list ( O0OO , title , subtitle , oOooO0 )
 return oOoo0 , IIII1i1
 if 61 - 61: oOO
def spinner_text ( text ) :
 oOoo0 = Gtk . Box ( orientation = Gtk . Orientation . HORIZONTAL ,
 halign = Gtk . Align . CENTER , valign = Gtk . Align . CENTER )
 oOoo0 . set_spacing ( 6 )
 if 7 - 7: i1i1i1111I / Ii * Iii1i
 i1iI1i = Gtk . Spinner ( active = True )
 oOoo0 . pack_start ( i1iI1i , expand = True , fill = True , padding = 0 )
 if 73 - 73: ooOOO - IiIIii11Ii
 iIi1 = tlgtk . Label ( label = text )
 oOoo0 . pack_end ( iIi1 , expand = True , fill = True , padding = 0 )
 if 4 - 4: ooo000 % I1I - i1i1i1111I
 return oOoo0
 if 76 - 76: i1 * oOo0O00 . o0o0ooo00oo * iI1iI11Ii111 . IiIIii11Ii . oOO
def scale_aware_surface_from_pixbuf (
 pixbuf , width , height , preserve_aspect_ratio = False ,
 ) :
 if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
 if 91 - 91: I1Ii1I1 - I11iiIi11i1I
 if 84 - 84: oOO % iI1iII1I1I1i - Ooo0Ooo
 if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / iI1iI11Ii111
 if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
 if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
 if 63 - 63: IIiIIiIi11I1 / IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
 if 52 - 52: oOo0O00 / iI1iI11Ii111 * IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO
 if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
 if 30 - 30: I1I
 if 41 - 41: oOO
 if 98 - 98: I1I / IIiIIiIi11I1 / iI1iI11Ii111 + o0o0ooo00oo % Oo + I1I
 if 38 - 38: I1Ii1I1 + oOo0O00
 if 2 - 2: OooOoo % Ii + oOO . OooOoo + IIiIIiIi11I1 * Oo
 if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
 if 15 - 15: ooo000
 if preserve_aspect_ratio :
  if 63 - 63: iI1iI11Ii111
  if 81 - 81: OooOoo . iI1iI11Ii111 / i1i1i1111I + Oo / Ooo0Ooo % o0o0ooo00oo
  if 77 - 77: I11iiIi11i1I / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  if width == - 1 and height == - 1 :
   width = pixbuf . get_width ( )
   height = pixbuf . get_height ( )
   if 73 - 73: o0o0ooo00oo . Oo * I1I / i1i1i1111I + I1Ii1I1
  elif width == - 1 and height != - 1 :
   width = ( height / pixbuf . get_height ( ) ) * pixbuf . get_width ( )
   if 31 - 31: i1i1i1111I % I1Ii1I1
  elif width != - 1 and height == - 1 :
   height = ( width / pixbuf . get_width ( ) * pixbuf . get_height ( ) )
   if 1 - 1: o0o0ooo00oo - oOo0O00 - i1 . oOo0O00
 else :
  if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
  I1i = ( pixbuf . get_width ( ) / width , pixbuf . get_height ( ) / height )
  if 83 - 83: OooOoo + i1i1i1111I
  i111II = (
 max ( 1 , I1i [ 1 ] / I1i [ 0 ] ) , max ( 1 , I1i [ 0 ] / I1i [ 1 ] )
 )
  II1II11IIi1iI = pixbuf . get_width ( ) * i111II [ 0 ]
  OoiI1iiI11IIi1 = pixbuf . get_height ( ) * i111II [ 1 ]
  if 56 - 56: i1i1i1111I - IiIIii11Ii - i1iiIII111 - Oo + i1iiIII111 / Ooo0Ooo
  pixbuf = pixbuf . scale_simple ( II1II11IIi1iI , OoiI1iiI11IIi1 ,
 GdkPixbuf . InterpType . TILES )
  if 89 - 89: ooo000 + Ii % i1i1i1111I - i1iiIII111
  if 33 - 33: ooo000 . Iii1i % oOO
  if 60 - 60: I1I . IiIIii11Ii % IIiIIiIi11I1 % iI1iII1I1I1i
 I1i = ( pixbuf . get_width ( ) / width , pixbuf . get_height ( ) / height )
 if I1i != ( int ( I1i [ 0 ] ) , int ( I1i [ 1 ] ) ) :
  I1i = ( math . ceil ( I1i [ 0 ] ) , math . ceil ( I1i [ 1 ] ) )
  if 98 - 98: I1I
  oO0Ooo = I1i [ 0 ] * width
  i1i1Ii = I1i [ 1 ] * height
  pixbuf = pixbuf . scale_simple ( oO0Ooo , i1i1Ii ,
 GdkPixbuf . InterpType . TILES )
  if 29 - 29: iI1iII1I1I1i
 return Gdk . cairo_surface_create_from_pixbuf (
 pixbuf , max ( I1i ) , for_window = None
 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
