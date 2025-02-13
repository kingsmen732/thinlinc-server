# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# Copyright 2024 Samuel Mannehed for Cendio AB.
# For more information, see http://www.cendio.com
import os
import gettext
import threading
if 82 - 82: Iii1i
from gi . repository import Gtk
from gi . repository import Gdk
from gi . repository import GObject
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from thinlinc import prefix
from thinlinc import tlgtk
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
__all__ = [ "Wizard" , "centered_view" , "centered_label" ]
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
iI111iiIi11i = None
if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
Ooo = 30
I1 = 150
if 71 - 71: i11 % Ii
def iI ( ) :
 global iI111iiIi11i
 if iI111iiIi11i is None :
  i1Ii1i = os . path . join ( prefix . get_tl_prefix ( ) , "share" , "locale" )
  oOooo0OOO = gettext . translation ( "tl-misc" , i1Ii1i , fallback = True )
  iI111iiIi11i = oOooo0OOO . gettext
  if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
def centered_view ( scrollable = False , orientation = Gtk . Orientation . VERTICAL ,
 spacing = 30 , ** kwargs ) :
 ii1Ii = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL ,
 halign = Gtk . Align . FILL , valign = Gtk . Align . START )
 ii1Ii . set_margin_top ( Ooo )
 ii1Ii . set_margin_bottom ( Ooo )
 ii1Ii . set_margin_start ( I1 )
 ii1Ii . set_margin_end ( I1 )
 if 55 - 55: iI1iII1I1I1i + i1
 Iii11iiiiI = Gtk . Box ( orientation = orientation , spacing = spacing , ** kwargs )
 ii1Ii . pack_start ( Iii11iiiiI , expand = True , fill = True , padding = 0 )
 if 63 - 63: ooo000 / I1Ii1I1 . Iii1i - ooo000
 if scrollable :
  ii1Ii = tlgtk . factory . scrolled_view ( ii1Ii )
  if 34 - 34: Ooo0Ooo + ooo0O0oO00 * IIiIIiIi11I1 * OooOoo
 return ii1Ii , Iii11iiiiI
 if 25 - 25: Ii / ooo0O0oO00 % Ii
 if 96 - 96: Ii . IIiIIiIi11I1 % iIiii1i
 if 68 - 68: iIiii1i . i1i1i1111I
 if 24 - 24: i11
 if 9 - 9: ooo000 / o00o0OO00O . o00o0OO00O / Ii % i1i1i1111I % Ooo0Ooo
 if 85 - 85: iIiii1i % ooOOO + i1iiIII111 / ooOOO / ooo000
def centered_label ( label , use_markup = True ,
 max_width_chars = 0 , wrap = True ,
 xalign = 0.5 ,
 valign = Gtk . Align . CENTER ,
 ** label_kwargs ) :
 IIiiI11ii = tlgtk . Label (
 label = label , use_markup = use_markup ,
 max_width_chars = max_width_chars , wrap = wrap ,
 xalign = xalign , valign = valign ,
 margin_start = I1 , margin_end = I1 ,
 ** label_kwargs
 )
 if 69 - 69: ooOOO % OooOoo
 def oOOoO ( widget , * args ) :
  if 70 - 70: i11 + iIiii1i * ooo0O0oO00 . Oo + ooOOO / Oo
  iI1i1I = widget . get_layout ( ) . get_line_count ( )
  if 27 - 27: ooOOO * IIiIIiIi11I1 % Ii + Ooo0Ooo . Ii + Iii1i
  if 43 - 43: ooOOO * I1Ii1I1
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  if 70 - 70: IiIIii11Ii
  if iI1i1I > 2 :
   widget . set_justify ( Gtk . Justification . LEFT )
  else :
   widget . set_justify ( Gtk . Justification . CENTER )
   if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
 IIiiI11ii . connect ( 'map' , oOOoO )
 IIiiI11ii . connect ( 'notify::label' , oOOoO )
 if 88 - 88: Oo * IiIIii11Ii
 return IIiiI11ii
 if 100 - 100: i11 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
class Wizard ( Gtk . Window ) :
 __gsignals__ = {
 'close' : ( GObject . SignalFlags . RUN_LAST | GObject . SignalFlags . ACTION ,
 GObject . TYPE_NONE ,
 ( ) )
 }
 if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
 def __init__ ( self ) :
  Gtk . Window . __init__ ( self )
  if 29 - 29: IiIIii11Ii - oOo0O00
  iI ( )
  if 30 - 30: I1I . ooo000
  self . connect ( "delete-event" , self . _on_delete )
  self . connect ( "key-press-event" , self . _on_key_press )
  self . set_resizable ( False )
  if 43 - 43: ooOOO . iIiii1i + ooo000
  self . _history = [ ]
  self . _notification_timer = None
  if 87 - 87: Iii1i + ooOOO . o00o0OO00O / Ii + Oo
  self . _build_ui ( )
  if 77 - 77: i1iiIII111 + i11 - Oo % ooo000
 def run ( self ) :
  self . _finished = False
  if 74 - 74: Ii + Ooo0Ooo
  self . connect ( "destroy" , Gtk . main_quit )
  if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if self . forward_button . get_property ( "visible" ) :
   self . forward_button . grab_focus ( )
  elif self . close_button . get_property ( "visible" ) :
   self . close_button . grab_focus ( )
   if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
  self . show ( )
  Gtk . main ( )
  if 52 - 52: ooo0O0oO00 + I1I / ooo000 - I1Ii1I1 * o00o0OO00O % oOo0O00
  return self . _finished
  if 52 - 52: oOo0O00 . I1I + o00o0OO00O - i1iiIII111 % iI1iII1I1I1i
 def _add_intro_or_finish ( self , title , text , intro_forward_button = None ,
 banner_path = None , width = - 1 , height = - 1 ) :
  Oo0O0o0oO000 = Gtk . EventBox ( valign = Gtk . Align . CENTER )
  ii1Ii , o0Ooo = centered_view ( spacing = 0 )
  Oo0O0o0oO000 . add ( ii1Ii )
  if 19 - 19: Ii
  if banner_path is not None :
   if 32 - 32: i1i1i1111I % Ooo0Ooo - o00o0OO00O * I1I
   Ooo00ooO = 480
   i1Ii1iiIiI111 = 144
   if 77 - 77: i11 - iIiii1i * Ooo0Ooo
   if ( width , height ) == ( - 1 , - 1 ) :
    width = Ooo00ooO
    height = i1Ii1iiIiI111
    if 71 - 71: IIiIIiIi11I1 / ooOOO - ooOOO / iIiii1i
    if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + ooo0O0oO00
   iiI1 = 1
   iII = 1
   if width > Ooo00ooO :
    iiI1 = Ooo00ooO / width
   if height > i1Ii1iiIiI111 :
    iII = i1Ii1iiIiI111 / height
   width = width * min ( iiI1 , iII )
   height = height * min ( iiI1 , iII )
   if 43 - 43: Ooo0Ooo - I1I . ooo000 - Iii1i % o00o0OO00O
   if 49 - 49: IiIIii11Ii . ooo000 + ooo0O0oO00 - ooo0O0oO00
   if 78 - 78: i1 - ooOOO
   if 56 - 56: ooo000 . ooo000 + I1Ii1I1 * iI1iII1I1I1i
   if 17 - 17: Iii1i % o00o0OO00O - Iii1i % Ooo0Ooo . OooOoo
   if os . path . splitext ( banner_path ) [ 1 ] == '.svg' :
    if 60 - 60: ooOOO . ooo000
    oOOOOOOoO = ( 1 , 1 )
    if width != - 1 and height != - 1 :
     oOOOOOOoO = ( width * 4 , height * 4 )
    elif width == - 1 and height != - 1 :
     oOOOOOOoO = ( - 1 , height * 4 )
    elif width != - 1 and height == - 1 :
     oOOOOOOoO = ( width * 4 , - 1 )
     if 3 - 3: Ii % i1 + i1i1i1111I * Ii * i1 . I1I
    iiI1i = tlgtk . GdkPixbuf . Pixbuf . new_from_file_at_scale (
 banner_path ,
 width = oOOOOOOoO [ 0 ] ,
 height = oOOOOOOoO [ 1 ] ,
 preserve_aspect_ratio = True ,
 )
    if 73 - 73: ooOOO - IiIIii11Ii
   else :
    iiI1i = tlgtk . GdkPixbuf . Pixbuf . new_from_file ( banner_path )
    if 22 - 22: Oo % oOo0O00 / o00o0OO00O . oOo0O00 . o00o0OO00O
    if 87 - 87: I1I - o00o0OO00O . i1 * Oo
    if 90 - 90: i11 * o00o0OO00O . Ii
    if 45 - 45: IiIIii11Ii - iIiii1i . i1iiIII111 * Ooo0Ooo . IIiIIiIi11I1
    if 14 - 14: iI1iII1I1I1i + OooOoo * I1Ii1I1 - iIiii1i
    if 84 - 84: ooo0O0oO00 % iI1iII1I1I1i - Ooo0Ooo
    if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / o00o0OO00O
   if width != - 1 and height != - 1 :
    iiI1 = iiI1i . get_width ( ) / width
    iII = iiI1i . get_height ( ) / height
    if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
    if iiI1 < iII :
     width = width * ( iiI1 / iII )
    elif iiI1 > iII :
     height = height * ( iII / iiI1 )
     if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
   oO00OOooOoO0o = tlgtk . factory . scale_aware_surface_from_pixbuf (
 iiI1i ,
 width = width ,
 height = height ,
 preserve_aspect_ratio = True ,
 )
   if 40 - 40: IiIIii11Ii % ooo0O0oO00 - IiIIii11Ii % ooo0O0oO00 - IiIIii11Ii + iI1iII1I1I1i
   Ooo0oO = tlgtk . Gtk . Image . new_from_surface ( oO00OOooOoO0o )
   Ooo0oO . set_margin_bottom ( 60 )
   o0Ooo . pack_start ( Ooo0oO , expand = False , fill = False , padding = 0 )
   if 16 - 16: I1Ii1I1 % I1I / IIiIIiIi11I1 * o00o0OO00O + i11 % oOo0O00
  iiIiIi = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL , vexpand = True ,
 halign = Gtk . Align . FILL , valign = Gtk . Align . CENTER ,
 spacing = 18 )
  o0Ooo . pack_start ( iiIiIi , expand = False , fill = False , padding = 0 )
  if 91 - 91: ooOOO / Ii . oOo0O00 % OooOoo * IIiIIiIi11I1
  iIIIIIiiIIi = tlgtk . Label (
 label = title , max_width_chars = 35 , wrap = True ,
 xalign = 0.5 , justify = Gtk . Justification . CENTER ,
 )
  iIIIIIiiIIi . get_style_context ( ) . add_class ( 'title-1' )
  iiIiIi . pack_start ( iIIIIIiiIIi , expand = False , fill = True , padding = 0 )
  if 9 - 9: i1i1i1111I - Ii % OooOoo / o00o0OO00O
  if text is not None :
   oo0O0 = tlgtk . Label (
 label = text , halign = Gtk . Align . FILL , valign = Gtk . Align . START ,
 max_width_chars = 35 ,
 xalign = 0.5 , justify = Gtk . Justification . CENTER ,
 )
   oo0O0 . set_use_markup ( True )
   oo0O0 . set_line_wrap ( True )
   iiIiIi . pack_start ( oo0O0 , expand = True , fill = True , padding = 0 )
   if 77 - 77: iIiii1i / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  i1iI1 = intro_forward_button is not None
  if 11 - 11: I1Ii1I1 / ooo0O0oO00
  iIOooO0O = ooO000oOo0o0 ( self , '' , halign = Gtk . Align . FILL , valign = Gtk . Align . FILL )
  iIOooO0O . connect ( "notify::page-backable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-forwardable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-intro" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-busy" , self . _on_page_notify )
  if 20 - 20: i1i1i1111I / I1Ii1I1 . oOo0O00
  iIOooO0O . set_page_intro ( i1iI1 )
  iiIiIi . pack_end ( iIOooO0O , expand = True , fill = True , padding = 0 )
  if 77 - 77: oOo0O00 % Oo - oOo0O00 - ooo000 * iIiii1i + ooo0O0oO00
  if i1iI1 :
   intro_forward_button . connect ( "clicked" , self . _on_forward )
   iiIiIi . pack_start ( intro_forward_button ,
 expand = False , fill = False , padding = 0 )
   iiIiIi . set_focus_child ( intro_forward_button )
   if 64 - 64: i11 . Ooo0Ooo . i1iiIII111 * i11
  Oo0O0o0oO000 . show_all ( )
  if 33 - 33: i1i1i1111I
  Oo0O0o0oO000 . page = iIOooO0O
  self . notebook . append_page ( Oo0O0o0oO000 )
  if 30 - 30: o00o0OO00O % ooOOO . Ii % IIiIIiIi11I1 / iI1iII1I1I1i % ooOOO
  return iIOooO0O
  if 24 - 24: IIiIIiIi11I1 - IIiIIiIi11I1 . Ooo0Ooo + i1iiIII111 + Oo
 def add_intro ( self , title , text , button_label ,
 banner_path = None , width = - 1 , height = - 1 ) :
  I1II1I1i = Gtk . Button . new_with_mnemonic ( button_label )
  I1II1I1i . set_halign ( Gtk . Align . CENTER )
  I1II1I1i . get_style_context ( ) . add_class ( 'suggested-action' )
  return self . _add_intro_or_finish ( title , text , I1II1I1i ,
 banner_path , width , height )
  if 59 - 59: i1iiIII111
 def add_finish ( self , title , text ,
 banner_path = None , width = - 1 , height = - 1 ) :
  if 33 - 33: ooo000 . Iii1i % ooo0O0oO00
  return self . _add_intro_or_finish ( title , text ,
 banner_path = banner_path ,
 width = width , height = height )
  if 60 - 60: I1I . IiIIii11Ii % IIiIIiIi11I1 % iI1iII1I1I1i
 def add_page ( self , title ) :
  i1iII1 = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL )
  if 63 - 63: Iii1i
  iIOooO0O = ooO000oOo0o0 ( self , title , margin = 0 )
  iIOooO0O . connect ( "notify::page-backable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-forwardable" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-intro" , self . _on_page_notify )
  iIOooO0O . connect ( "notify::page-busy" , self . _on_page_notify )
  i1iII1 . pack_end ( iIOooO0O , expand = True , fill = True , padding = 0 )
  if 81 - 81: I1Ii1I1 / ooo0O0oO00 + ooo0O0oO00 . i1i1i1111I - i1
  i1iII1 . show_all ( )
  if 15 - 15: OooOoo . oOo0O00 - ooOOO % Ooo0Ooo
  i1iII1 . page = iIOooO0O
  self . notebook . append_page ( i1iII1 )
  if 62 - 62: iI1iII1I1I1i / OooOoo % I1I - i11
  return iIOooO0O
  if 66 - 66: i1i1i1111I / Ooo0Ooo + iIiii1i + Iii1i + oOo0O00 + o00o0OO00O
 def show_notification ( self , message , timeout = 5 ) :
  if self . _notification_timer and self . _notification_timer . is_alive ( ) :
   self . _notification_timer . cancel ( )
   if 75 - 75: OooOoo - ooo0O0oO00 - IiIIii11Ii - ooo0O0oO00 + ooo000 % iI1iII1I1I1i
  self . _notify_label . set_text ( message )
  self . _revealer . set_reveal_child ( True )
  if 42 - 42: i1 * o00o0OO00O
  if 50 - 50: Ii - i1iiIII111
  self . _notification_timer = threading . Timer ( timeout ,
 self . hide_notification )
  self . _notification_timer . start ( )
  if 96 - 96: ooo000 * OooOoo - Ii - OooOoo
  if 65 - 65: Oo + Oo - iI1iII1I1I1i % OooOoo . Ooo0Ooo
  iII11I1iI = self . get_window ( )
  iII11I1iI . set_cursor ( Gdk . Cursor . new_for_display (
 iII11I1iI . get_display ( ) ,
 cursor_type = Gdk . CursorType . ARROW
 ) )
  if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
 def hide_notification ( self , * args ) :
  if self . _notification_timer and self . _notification_timer . is_alive ( ) :
   self . _notification_timer . cancel ( )
   if 81 - 81: i1 + i1i1i1111I * Oo - Oo * I1Ii1I1 - oOo0O00
  self . _revealer . set_reveal_child ( False )
  if 4 - 4: i1iiIII111
 def _build_ui ( self ) :
  IIIii1I = self . _build_notification_overlay ( )
  self . add ( IIIii1I )
  if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % o00o0OO00O - OooOoo
  IIII1iII11ii = Gtk . Box ( orientation = Gtk . Orientation . VERTICAL )
  IIIii1I . add ( IIII1iII11ii )
  if 57 - 57: oOo0O00 % Ooo0Ooo * ooOOO
  self . notebook = Gtk . Notebook ( )
  self . notebook . set_show_tabs ( False )
  self . notebook . set_show_border ( False )
  self . notebook . connect ( "page-added" , self . _page_change )
  self . notebook . connect ( "page-removed" , self . _page_change )
  self . notebook . connect ( "switch-page" , self . _switch_page )
  IIII1iII11ii . pack_start ( self . notebook , expand = True , fill = True , padding = 0 )
  if 59 - 59: ooo000 / Oo - i1
  OO0Oo0OOo00 = Gtk . HeaderBar ( )
  OO0Oo0OOo00 . show ( )
  if 100 - 100: i11 . IIiIIiIi11I1 * i1 + IiIIii11Ii % I1I / i11
  self . window_title = tlgtk . Label ( label = "" )
  self . window_title . get_style_context ( ) . add_class ( "title" )
  self . window_title . show ( )
  OO0Oo0OOo00 . set_custom_title ( self . window_title )
  if 33 - 33: OooOoo * Oo * Ii * iI1iII1I1I1i + o00o0OO00O . IiIIii11Ii
  self . cancel_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Cancel" ) )
  self . cancel_button . connect ( "clicked" , self . _on_cancel )
  OO0Oo0OOo00 . pack_start ( self . cancel_button )
  if 94 - 94: oOo0O00 . i1iiIII111
  self . back_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Back" ) )
  self . back_button . connect ( "clicked" , self . _on_back )
  OO0Oo0OOo00 . pack_start ( self . back_button )
  if 96 - 96: I1I / ooo0O0oO00 / iIiii1i + iIiii1i
  self . forward_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Forward" ) )
  self . forward_button . connect ( "clicked" , self . _on_forward )
  self . forward_button . get_style_context ( ) . add_class ( 'suggested-action' )
  self . forward_button . set_property ( "can-default" , True )
  OO0Oo0OOo00 . pack_end ( self . forward_button )
  if 35 - 35: IIiIIiIi11I1 + oOo0O00
  self . close_button = Gtk . Button . new_with_mnemonic ( iI111iiIi11i ( "_Close" ) )
  self . close_button . connect ( "clicked" , self . _on_close )
  self . close_button . get_style_context ( ) . add_class ( 'suggested-action' )
  self . close_button . set_property ( "can-default" , True )
  OO0Oo0OOo00 . pack_end ( self . close_button )
  if 96 - 96: iI1iII1I1I1i . OooOoo . i1
  self . set_titlebar ( OO0Oo0OOo00 )
  if 87 - 87: ooo000 * IiIIii11Ii % ooo000 . ooOOO . Oo % iI1iII1I1I1i
  IIIii1I . show_all ( )
  if 48 - 48: ooOOO * ooo000 % IiIIii11Ii * i1 . Iii1i - i11
 def _build_notification_overlay ( self ) :
  IIIii1I = Gtk . Overlay ( )
  if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
  self . _revealer = Gtk . Revealer ( valign = Gtk . Align . START ,
 halign = Gtk . Align . CENTER )
  Oo0O0o0oO000 = Gtk . Box ( orientation = "horizontal" , spacing = 18 )
  Oo0O0o0oO000 . get_style_context ( ) . add_class ( "app-notification" )
  if 90 - 90: Ooo0Ooo * OooOoo . Ii
  self . _notify_label = Gtk . Label ( wrap = True )
  Oo0O0o0oO000 . pack_start ( self . _notify_label , expand = False , fill = True , padding = 18 )
  if 5 - 5: Oo - i1 . ooo0O0oO00
  II1111I11 = Gtk . Button . new_from_icon_name ( "window-close-symbolic" ,
 Gtk . IconSize . BUTTON )
  II1111I11 . set_relief ( Gtk . ReliefStyle . NONE )
  II1111I11 . set_receives_default ( True )
  II1111I11 . connect ( "clicked" , self . hide_notification )
  if 94 - 94: Oo - IIiIIiIi11I1
  Oo0O0o0oO000 . pack_start ( II1111I11 , expand = False , fill = True , padding = 18 )
  self . _revealer . add ( Oo0O0o0oO000 )
  if 79 - 79: Ii + IiIIii11Ii * iI1iII1I1I1i / iI1iII1I1I1i
  IIIii1I . add_overlay ( self . _revealer )
  return IIIii1I
  if 31 - 31: IiIIii11Ii . IiIIii11Ii % Ii
 def _get_next_willing ( self , index = None ) :
  if index is None :
   index = self . notebook . get_current_page ( )
   if 51 - 51: Oo / i1i1i1111I - I1I
  while True :
   index += 1
   if 83 - 83: Iii1i % i1iiIII111 . OooOoo / I1I % ooo0O0oO00 . I1I
   IIiiI11ii = self . notebook . get_nth_page ( index )
   if IIiiI11ii is None :
    return None
    if 76 - 76: i1iiIII111 / OooOoo
   iIOooO0O = IIiiI11ii . page
   if iIOooO0O is None :
    return index
    if 77 - 77: ooOOO
   iIii1iiiIi = iIOooO0O . emit ( "page-unwilling" , self )
   if not iIii1iiiIi :
    return index
    if 76 - 76: I1Ii1I1 . Ii + OooOoo
 def do_close ( self ) :
  self . _on_delete ( self , None )
  if 95 - 95: Oo % i1i1i1111I * iI1iII1I1I1i - IiIIii11Ii
 def _on_delete ( self , window , event ) :
  Ii1i111II1 = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( Ii1i111II1 )
  if 4 - 4: IIiIIiIi11I1
  if iIOooO0O is None or not iIOooO0O . get_page_busy ( ) :
   if 52 - 52: Oo * iI1iII1I1I1i - i1i1i1111I . i1iiIII111
   if 78 - 78: OooOoo . ooOOO
   self . _on_cancel ( None )
   if 80 - 80: ooo0O0oO00 % i1iiIII111 * i11 - oOo0O00 % iIiii1i - i11
   if 56 - 56: Oo
  return True
  if 84 - 84: I1I % iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + Ooo0Ooo - Oo
 def _on_key_press ( self , window , event ) :
  if event . keyval == Gdk . KEY_Escape :
   self . emit ( "close" )
   if 41 - 41: ooOOO + OooOoo + IIiIIiIi11I1 * i1i1i1111I
 def _on_cancel ( self , button ) :
  iIi = "Abort and exit"
  oo000O0oOO = "Are you sure you wish to abort " + "%s and exit?" % self . get_title ( )
  if 86 - 86: Ii * i11 + IiIIii11Ii + Oo
  iIiiI1IiI1iI = tlgtk . SimpleMessageDialog (
 title = self . get_title ( ) ,
 text = iIi ,
 secondary_text = oo000O0oOO ,
 cancel_button = True ,
 cancel_button_label = iI111iiIi11i ( "_Return" ) ,
 ok_button_label = iI111iiIi11i ( "_Abort" ) ,
 default_response = Gtk . ResponseType . CANCEL ,
 transient_for = self ,
 modal = True ,
 message_type = Gtk . MessageType . QUESTION )
  IiOOooo00 = iIiiI1IiI1iI . run ( )
  iIiiI1IiI1iI . destroy ( )
  if 52 - 52: OooOoo
  if IiOOooo00 != Gtk . ResponseType . OK :
   return
   if 95 - 95: i1i1i1111I . iIiii1i * ooo000 / iI1iII1I1I1i - I1Ii1I1 + IiIIii11Ii
  Ii1i111II1 = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( Ii1i111II1 )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-abort" , self )
   if 40 - 40: o00o0OO00O + i1i1i1111I % OooOoo . i11 / i1i1i1111I . ooOOO
  self . destroy ( )
  if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - iIiii1i / IiIIii11Ii . Ooo0Ooo
 def _on_back ( self , button ) :
  assert len ( self . _history ) > 0
  Ii1i111II1 = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( Ii1i111II1 )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-abort" , self )
   if 15 - 15: o00o0OO00O * iIiii1i - oOo0O00
  self . notebook . set_current_page ( self . _history [ - 1 ] )
  if 6 - 6: i11 - Ii
 def _on_forward ( self , button ) :
  Ii1i111II1 = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( Ii1i111II1 )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-done" , self )
   if 1 - 1: I1I + OooOoo
  Ii1i111II1 = self . _get_next_willing ( )
  assert Ii1i111II1 is not None
  if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
  self . notebook . set_current_page ( Ii1i111II1 )
  if 96 - 96: OooOoo / ooo0O0oO00 - i1 * iIiii1i
 def _on_close ( self , button ) :
  Ii1i111II1 = self . notebook . get_current_page ( )
  iIOooO0O = self . _get_page_widget ( Ii1i111II1 )
  if iIOooO0O is not None :
   iIOooO0O . emit ( "page-done" , self )
   if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - o00o0OO00O + Ooo0Ooo
  self . _finished = True
  if 74 - 74: Ooo0Ooo * Oo + Iii1i - i1iiIII111
  self . destroy ( )
  if 22 - 22: IiIIii11Ii - Ooo0Ooo . i1 . o00o0OO00O - ooo000
 def _page_change ( self , notebook , child , page_num ) :
  self . _update_buttons ( self . notebook . get_current_page ( ) )
  if 68 - 68: ooo000
 def _switch_page ( self , notebook , page , page_num ) :
  OOoo0 = self . _get_page_widget ( page_num )
  if 82 - 82: iIiii1i
  if OOoo0 . title :
   self . window_title . set_label ( OOoo0 . title )
  else :
   self . window_title . set_label ( self . get_title ( ) )
   if 66 - 66: IiIIii11Ii + OooOoo
  if page_num in self . _history :
   Ii1i111II1 = self . _history . index ( page_num )
   self . _history = self . _history [ : Ii1i111II1 ]
  else :
   Ii1i111II1 = self . notebook . get_current_page ( )
   if Ii1i111II1 != - 1 :
    self . _history . append ( Ii1i111II1 )
    if 31 - 31: OooOoo
  self . _update_buttons ( page_num )
  if 33 - 33: i11 / OooOoo
 def _on_page_notify ( self , page , property ) :
  self . _update_buttons ( self . notebook . get_current_page ( ) )
  if 98 - 98: I1Ii1I1 . IIiIIiIi11I1 * o00o0OO00O - iI1iII1I1I1i % o00o0OO00O * i11
 def _update_buttons ( self , page_num ) :
  iIOooO0O = self . _get_page_widget ( page_num )
  if iIOooO0O is not None :
   OOoO = iIOooO0O . get_page_backable ( )
   O0oO0o = iIOooO0O . get_page_forwardable ( )
   OooOOo0o0 = iIOooO0O . get_page_intro ( )
   O00oO00oO0O = iIOooO0O . get_page_busy ( )
  else :
   OOoO = True
   O0oO0o = True
   OooOOo0o0 = False
   O00oO00oO0O = False
   if 65 - 65: iI1iII1I1I1i . Oo
  if len ( self . _history ) > 0 :
   self . back_button . show ( )
   self . back_button . set_sensitive ( OOoO and not O00oO00oO0O )
  else :
   self . back_button . hide ( )
   if 44 - 44: iIiii1i . I1Ii1I1 * i1 . iI1iII1I1I1i * iIiii1i - iIiii1i
  if OooOOo0o0 :
   self . forward_button . hide ( )
   self . forward_button . set_sensitive ( False )
   self . cancel_button . show ( )
   self . cancel_button . set_sensitive ( True )
   self . close_button . hide ( )
  elif self . _get_next_willing ( page_num ) is not None :
   self . forward_button . show ( )
   self . forward_button . set_sensitive ( O0oO0o and not O00oO00oO0O )
   self . set_default ( self . forward_button )
   self . cancel_button . show ( )
   self . cancel_button . set_sensitive ( not O00oO00oO0O )
   self . close_button . hide ( )
  else :
   self . forward_button . hide ( )
   self . cancel_button . hide ( )
   self . close_button . show ( )
   self . close_button . set_sensitive ( not O00oO00oO0O )
   self . set_default ( self . close_button )
   if 79 - 79: IiIIii11Ii + oOo0O00
   if 50 - 50: i11 + i1iiIII111 . i1iiIII111 . Oo
  iII11I1iI = self . get_window ( )
  if iII11I1iI is not None :
   if O00oO00oO0O :
    O000oO = Gdk . Cursor . new_for_display (
 iII11I1iI . get_display ( ) ,
 cursor_type = Gdk . CursorType . WATCH
 )
    iII11I1iI . set_cursor ( O000oO )
   else :
    iII11I1iI . set_cursor ( None )
    if 11 - 11: OooOoo * oOo0O00 + ooo000 * i11 / i1i1i1111I
 def _get_page_widget ( self , page_num ) :
  IIiiI11ii = self . notebook . get_nth_page ( page_num )
  if IIiiI11ii is None :
   return None
   if 40 - 40: i1iiIII111 - iIiii1i / Ooo0Ooo . IiIIii11Ii % Iii1i
  return IIiiI11ii . page
  if 47 - 47: I1I / IIiIIiIi11I1 + I1I
class ooO000oOo0o0 ( Gtk . Bin ) :
 __gproperties__ = {

 # OooOoo / i1i1i1111I
 'page-backable' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 True ,
 GObject . ParamFlags . READWRITE ) ,

 # iIiii1i . iIiii1i % Ii
 'page-forwardable' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 True ,
 GObject . ParamFlags . READWRITE ) ,

 # i11 + i11 / OooOoo - I1Ii1I1 / i11 * I1Ii1I1
 'page-intro' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 False ,
 GObject . ParamFlags . READWRITE ) ,

 # Ii - IiIIii11Ii - i1 * i11 - iI1iII1I1I1i + i1
 # oOo0O00 / I1I - o00o0OO00O + iI1iII1I1I1i - oOo0O00
 'page-busy' : ( GObject . TYPE_BOOLEAN ,
 '' , '' ,
 False ,
 GObject . ParamFlags . READWRITE )
 }
 if 100 - 100: iIiii1i % I1Ii1I1 - i11 / OooOoo
 __gsignals__ = {

 # IIiIIiIi11I1 . ooo0O0oO00 + Oo
 'page-unwilling' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_BOOLEAN ,
 ( Wizard , ) ) ,

 # Oo % i1i1i1111I + ooOOO / iIiii1i - Ooo0Ooo / i1i1i1111I
 'page-show' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_NONE ,
 ( Wizard , GObject . TYPE_BOOLEAN ) ) ,

 # IiIIii11Ii - Iii1i
 'page-done' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_NONE ,
 ( Wizard , ) ) ,

 # ooo000 . IiIIii11Ii % ooo000 / i1i1i1111I
 'page-abort' : ( GObject . SignalFlags . RUN_LAST ,
 GObject . TYPE_NONE ,
 ( Wizard , ) ) ,
 }
 if 48 - 48: i1iiIII111 . Oo
 def __init__ ( self , wizard , title = None , ** kwargs ) :
  GObject . GObject . __init__ ( self , ** kwargs )
  if 92 - 92: OooOoo + Ii / IIiIIiIi11I1 + OooOoo * IIiIIiIi11I1 * iI1iII1I1I1i
  self . title = title
  if 79 - 79: i1i1i1111I
  self . page_backable = True
  self . page_forwardable = True
  self . page_intro = False
  self . page_busy = False
  if 3 - 3: OooOoo / i11 % iIiii1i
  self . _first_map = True
  self . _wizard = wizard
  if 55 - 55: oOo0O00
  self . connect ( "map" , ooO000oOo0o0 . on_map )
  if 31 - 31: Ii . Ooo0Ooo / i11
 def get_page_backable ( self ) :
  return self . get_property ( 'page-backable' )
  if 59 - 59: Oo
 def set_page_backable ( self , value ) :
  return self . set_property ( 'page-backable' , value )
  if 64 - 64: Iii1i % iIiii1i * i1 % OooOoo * oOo0O00
 def get_page_forwardable ( self ) :
  return self . get_property ( 'page-forwardable' )
  if 55 - 55: i11
 def set_page_forwardable ( self , value ) :
  return self . set_property ( 'page-forwardable' , value )
  if 46 - 46: Ooo0Ooo % I1Ii1I1
 def get_page_intro ( self ) :
  return self . get_property ( 'page-intro' )
  if 86 - 86: iIiii1i . i1i1i1111I + ooo0O0oO00 % iIiii1i % Iii1i % ooo000
 def set_page_intro ( self , value ) :
  return self . set_property ( 'page-intro' , value )
  if 61 - 61: ooo000
 def get_page_busy ( self ) :
  return self . get_property ( 'page-busy' )
  if 48 - 48: Iii1i * i1i1i1111I + IiIIii11Ii
 def set_page_busy ( self , value ) :
  return self . set_property ( 'page-busy' , value )
  if 31 - 31: Oo * i1iiIII111 % Ii / ooo0O0oO00 + I1Ii1I1 + iI1iII1I1I1i
 def on_map ( self ) :
  if 90 - 90: I1Ii1I1 * i1i1i1111I / iI1iII1I1I1i * Ii
  if 38 - 38: I1I . Ii
  self . emit ( "page-show" , self . _wizard , self . _first_map )
  self . _first_map = False
  if 41 - 41: ooo000 % IIiIIiIi11I1 % ooOOO
 def do_size_request ( self , req ) :
  req . width = 0
  req . height = 0
  iIi1II = self . get_child ( )
  if iIi1II and iIi1II . get_property ( "visible" ) :
   ( req . width , req . height ) = iIi1II . size_request ( )
   if 16 - 16: ooo000 - iI1iII1I1I1i * ooo000
 def do_size_allocate ( self , alloc ) :
  self . set_allocation ( alloc )
  iIi1II = self . get_child ( )
  if iIi1II and iIi1II . get_property ( "visible" ) :
   iIi1II . size_allocate ( alloc )
   if 44 - 44: IIiIIiIi11I1 - IiIIii11Ii
 def do_get_property ( self , property ) :
  if property . name == "page-backable" :
   return self . page_backable
  if property . name == "page-forwardable" :
   return self . page_forwardable
  if property . name == "page-intro" :
   return self . page_intro
  if property . name == "page-busy" :
   return self . page_busy
   if 67 - 67: Ooo0Ooo . Ooo0Ooo . i11
  raise AttributeError
  if 24 - 24: i1iiIII111 + i1i1i1111I . oOo0O00 + iI1iII1I1I1i + i11
 def do_set_property ( self , property , value ) :
  if property . name == "page-backable" :
   self . page_backable = value
  elif property . name == "page-forwardable" :
   self . page_forwardable = value
  elif property . name == "page-intro" :
   self . page_intro = value
  elif property . name == "page-busy" :
   self . page_busy = value
  else :
   raise AttributeError
   if 92 - 92: iI1iII1I1I1i / iI1iII1I1I1i + IiIIii11Ii . i11
GObject . type_register ( Wizard )
GObject . type_register ( ooO000oOo0o0 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
