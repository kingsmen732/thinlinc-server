# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# For more information, see http://www.cendio.com
if 82 - 82: Iii1i
import os
import sys
import _thread
import re
import warnings
import shutil
import textwrap
import subprocess
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from itertools import cycle
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
import thinlinc . prefix
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
__all__ = [ "init" ,
 "has_gtk" ,
 "Gtk" , "Gdk" , "GdkPixbuf" , "GLib" , "GObject" , "Pango" ,
 "factory" , "wizard" , "Label" , "SimpleMessageDialog" , "EntryDialog" ,
 "linkify_text" , "sanitise_wrap" , "message" , "avoid_center_on_seam"
 ]
if 98 - 98: I11iiIi11i1I % oOO
if 31 - 31: i1I
if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
has_gtk = False
if 16 - 16: i1i1i1111I / i1iiIII111
if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
if 9 - 9: i1iiIII111
i1Ii1i = _thread . get_ident ( )
if 93 - 93: IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo . Ooo0Ooo
def OO0o000o ( exc_type , exc_value , exc_traceback , old_hook ) :
 old_hook ( exc_type , exc_value , exc_traceback )
 if 8 - 8: i1iiIII111 * i1 . I1I / oOO
 if 58 - 58: I1Ii1I1 - ooOOO
 if 60 - 60: iI1iII1I1I1i . oOO
 if 13 - 13: oOO
 if _thread . get_ident ( ) != i1Ii1i :
  return
  if 2 - 2: i1
  if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
 if Gtk . main_level ( ) == 0 :
  return
  if 1 - 1: iI1iII1I1I1i + Ooo0Ooo + oOO * IIiIIiIi11I1
 sys . exit ( 1 )
 if 20 - 20: I1I + Ii
def init ( wmclass = None ) :
 global Gtk , Gdk , GdkPixbuf , GLib , GObject , Pango
 global has_gtk
 if 75 - 75: Ii % i1iiIII111 * Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
 if 8 - 8: I1Ii1I1 . IiI11Ii111 . i1 . Oo - i1I
 if 32 - 32: Ii % i1i1i1111I % i1I - I11iiIi11i1I % i1iiIII111
 if not os . environ . get ( "DISPLAY" , "" ) :
  return False
  if 34 - 34: i1iiIII111 * i1
 try :
  import gi
  if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
  if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
  if 32 - 32: I1Ii1I1 + oOO - oOo0O00
  if 79 - 79: Iii1i % oOO * Oo + ooOOO / Oo . oOO
  if not hasattr ( gi , 'require_version' ) :
   raise ImportError
   if 20 - 20: IiI11Ii111 + i1iiIII111 / I1I
   if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
   if 43 - 43: ooOOO * I1Ii1I1
   if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  gi . require_version ( "Gtk" , "3.0" )
  gi . require_version ( "Gdk" , "3.0" )
  gi . require_version ( "GdkPixbuf" , "2.0" )
  gi . require_version ( "GLib" , "2.0" )
  gi . require_version ( "GObject" , "2.0" )
  gi . require_version ( "Pango" , "1.0" )
  if 70 - 70: IiIIii11Ii
  if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
  if 88 - 88: Oo * IiIIii11Ii
  if 100 - 100: IiI11Ii111 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
  if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
  if 29 - 29: IiIIii11Ii - oOo0O00
  gi . require_foreign ( 'cairo' )
  if 30 - 30: I1I . ooo000
  if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
  if 87 - 87: Iii1i + ooOOO . i1I / Ii + Oo
  with warnings . catch_warnings ( ) :
   warnings . filterwarnings ( "ignore" , ".*falling back to load_module.*" , ImportWarning )
   if 77 - 77: i1iiIII111 + IiI11Ii111 - Oo % ooo000
   from gi . repository import Gtk
   from gi . repository import Gdk
   from gi . repository import GdkPixbuf
   from gi . repository import GLib
   from gi . repository import GObject
   from gi . repository import Pango
   if 74 - 74: Ii + Ooo0Ooo
   if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if Gtk . check_version ( 3 , 20 , 0 ) is not None :
   raise RuntimeError
   if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
   if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * i1I % oOo0O00
  if not hasattr ( Gtk , 'PyGTKDeprecationWarning' ) :
   raise ImportError
   if 52 - 52: oOo0O00 . I1I + i1I - i1iiIII111 % iI1iII1I1I1i
  try :
   Oo0O0o0oO000 = GdkPixbuf . PixbufLoader . new_with_mime_type ( 'image/svg+xml' )
   if 80 - 80: i1 . oOo0O00 * i1
   try :
    Oo0O0o0oO000 . close ( )
   except GLib . GError :
    if 26 - 26: Ii . i1
    pass
  except GLib . GError :
   raise RuntimeError
   if 61 - 61: iI1iII1I1I1i . i1I - ooo000 / ooo000 - i1
  iIi = Gtk . init_check ( [ ] ) [ 0 ]
  if not iIi :
   raise RuntimeError
   if 23 - 23: iI1iII1I1I1i % oOO . Oo / OooOoo - I11iiIi11i1I - oOO
  if wmclass is not None :
   Gdk . set_program_class ( wmclass )
   if 77 - 77: IiI11Ii111 - I11iiIi11i1I * Ooo0Ooo
  has_gtk = True
  if 71 - 71: IIiIIiIi11I1 / ooOOO - ooOOO / I11iiIi11i1I
  if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + oOO
  if 11 - 11: i1 / ooo000
  if 89 - 89: I1I * i1i1i1111I
  if 54 - 54: oOO + Ooo0Ooo - I1I . Ooo0Ooo
  oOOoOOOO000 = sys . excepthook
  sys . excepthook = lambda IIIIi , O0O0oOo00oO0 , iIiIiiIIIiII : OO0o000o ( IIIIi , O0O0oOo00oO0 , iIiIiiIIIiII , oOOoOOOO000 )
 except ImportError :
  if 44 - 44: Ooo0Ooo + i1i1i1111I + Iii1i - oOO
  return False
 except RuntimeError :
  if 7 - 7: i1i1i1111I / Ii * Iii1i
  return False
 except ValueError :
  if 32 - 32: IiI11Ii111 . OooOoo
  return False
  if 31 - 31: Oo - i1I
  if 28 - 28: ooOOO * I1Ii1I1 + IiI11Ii111 % Oo
  if 100 - 100: Oo + i1I
 I1II1ii111i = Gtk . CssProvider ( )
 I1II1ii111i . load_from_data ( b"""
    .title-1 {
       font-weight: 800;
       font-size: 20pt;
    }
    """ )
 if 14 - 14: IiI11Ii111 + i1I . IiIIii11Ii . Ooo0Ooo % IiIIii11Ii * i1i1i1111I
 if 65 - 65: Iii1i + IIiIIiIi11I1 - Ooo0Ooo . iI1iII1I1I1i + OooOoo * Ooo0Ooo
 if 23 - 23: ooOOO % oOO % iI1iII1I1I1i - i1I - i1iiIII111 + i1
 if 12 - 12: i1 - i1I - IiI11Ii111
 if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
 if 46 - 46: ooOOO + ooOOO % oOO
 if Gtk . MAJOR_VERSION == 3 and Gtk . MINOR_VERSION < 22 :
  I1II1ii111i . load_from_data ( b"""
        .title-1 {
           font-weight: 800;
           font-size: 20px;
        }
        """ )
  if 2 - 2: i1i1i1111I / Ooo0Ooo / oOO - IIiIIiIi11I1 / IIiIIiIi11I1
 Gtk . StyleContext . add_provider_for_screen (
 Gdk . Screen . get_default ( ) ,
 I1II1ii111i ,
 Gtk . STYLE_PROVIDER_PRIORITY_FALLBACK )
 if 58 - 58: i1i1i1111I
 o0oO00OO = thinlinc . prefix . get_tl_prefix ( ) + "/share/icons"
 if 71 - 71: Ooo0Ooo + oOO * IiIIii11Ii + iI1iII1I1I1i * ooOOO
 Oo0oO = [ ]
 for ii1II in [ 16 , 22 , 24 , 32 , 48 , 64 , 128 ] :
  try :
   oOoOo = "%s/thinlinc_%d.png" % ( o0oO00OO , ii1II )
   o0oOoo0O0o0Oo = GdkPixbuf . Pixbuf . new_from_file ( oOoOo )
  except :
   o0oOoo0O0o0Oo = None
   if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
  if o0oOoo0O0o0Oo is None :
   try :
    oOoOo = "%s/thinlinc.svg" % o0oO00OO
    o0oOoo0O0o0Oo = GdkPixbuf . Pixbuf . new_from_file_at_size ( oOoOo , ii1II , ii1II )
   except :
    o0oOoo0O0o0Oo = None
    if 15 - 15: ooo000
  if o0oOoo0O0o0Oo is not None :
   Oo0oO . append ( o0oOoo0O0o0Oo )
   if 63 - 63: i1I
 if Oo0oO :
  Gtk . Window . set_default_icon_list ( Oo0oO )
  if 81 - 81: OooOoo . i1I / i1i1i1111I + Oo / Ooo0Ooo % IiI11Ii111
  if 77 - 77: I11iiIi11i1I / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  if 73 - 73: IiI11Ii111 . Oo * I1I / i1i1i1111I + I1Ii1I1
 global factory
 from . import factory
 if 31 - 31: i1i1i1111I % I1Ii1I1
 global wizard
 from . import wizard
 if 1 - 1: IiI11Ii111 - oOo0O00 - i1 . oOo0O00
 global Label
 from . label import Label
 if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
 global EntryDialog
 from . dialog import EntryDialog
 if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
 global SimpleMessageDialog
 from . dialog import SimpleMessageDialog
 if 19 - 19: Ii
 if 22 - 22: i1I % iI1iII1I1I1i + Oo
 if 60 - 60: ooo000 + I11iiIi11i1I + IIiIIiIi11I1 % i1i1i1111I - Ii % Ooo0Ooo
 return True
 if 95 - 95: ooOOO % i1i1i1111I . i1
 if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
 if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
def linkify_text ( text , link_texts = [ ] ) :
 if not has_gtk :
  return text
  if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
 OOO0O0oOoOOOo = "(https?|ftp)://[0-9a-zA-Z;/?:@&=+$\\.\\-_!~*'()%]+(#[0-9a-zA-Z;/?:@&=+$\\.\\-_!~*'()%]+)?"
 if 99 - 99: Iii1i % oOO * Ooo0Ooo - Ii
 if len ( link_texts ) > 0 :
  if 25 - 25: IiI11Ii111 + iI1iII1I1I1i - I1I . oOO + OooOoo
  class OOoo00o0oO0o0 ( cycle ) :
   def __call__ ( self , match_obj ) :
    return "<a href=\"%s\">%s</a>" % ( match_obj . group ( 0 ) , next ( self ) )
  ooOo0 = OOoo00o0oO0o0 ( link_texts )
 else :
  ooOo0 = "<a href=\"\\1\">\\1</a>"
  if 20 - 20: oOo0O00 * ooOOO % IIiIIiIi11I1 - IIiIIiIi11I1
 return sanitise_wrap ( re . sub ( "(%s)" % OOO0O0oOoOOOo , ooOo0 , text ) )
 if 32 - 32: OooOoo % I1I - I11iiIi11i1I % OooOoo
def sanitise_wrap ( text ) :
 if not has_gtk :
  return text
  if 9 - 9: i1iiIII111 - ooOOO % Iii1i
  if 37 - 37: i1I + IIiIIiIi11I1 % iI1iII1I1I1i / IIiIIiIi11I1 % i1iiIII111 + oOO
  if 98 - 98: iI1iII1I1I1i - I1I + i1 * ooo000 % i1
  if 100 - 100: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
  if 85 - 85: IIiIIiIi11I1 / OooOoo . i1I % Oo + Oo - I11iiIi11i1I
  if 59 - 59: OooOoo
  if 53 - 53: i1i1i1111I / ooOOO - IiI11Ii111 + ooo000 * i1i1i1111I * i1iiIII111
  if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
  if 81 - 81: i1 + i1i1i1111I * Oo - Oo * I1Ii1I1 - oOo0O00
  if 4 - 4: i1iiIII111
 IIIii1I = ""
 ii1I = False
 for IiiI1III1iI in text :
  if IiiI1III1iI == "<" :
   ii1I = True
   if 37 - 37: I1Ii1I1 % iI1iII1I1I1i . i1I + Ooo0Ooo + ooOOO * iI1iII1I1I1i
  if ii1I or IiiI1III1iI . isalnum ( ) or IiiI1III1iI . isspace ( ) :
   IIIii1I += IiiI1III1iI
  else :
   IIIii1I += "\u200d%s\u200d" % IiiI1III1iI
   if 39 - 39: IIiIIiIi11I1 - Oo
  if IiiI1III1iI == ">" :
   ii1I = False
   if 31 - 31: IiIIii11Ii % oOo0O00 % oOo0O00 * Iii1i
 return IIIii1I
 if 85 - 85: Iii1i + Ii % IIiIIiIi11I1 % oOo0O00
def I1i1I ( mainwin ) :
 i1iIIi1I1iiI = Gtk . check_version ( 3 , 22 , 0 ) is None
 if 42 - 42: I1Ii1I1 - OooOoo / IiIIii11Ii % I11iiIi11i1I % I1Ii1I1 + ooOOO
 if i1iIIi1I1iiI :
  return mainwin . get_display ( ) . get_n_monitors ( )
 else :
  return mainwin . get_screen ( ) . get_n_monitors ( )
  if 62 - 62: i1iiIII111 * iI1iII1I1I1i . i1i1i1111I
  if 19 - 19: ooo000 * oOO
  if 47 - 47: ooo000
  if 2 - 2: Oo % IiIIii11Ii - ooOOO
  if 75 - 75: IiIIii11Ii * i1 . Iii1i - IiI11Ii111
  if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
  if 90 - 90: Ooo0Ooo * OooOoo . Ii
  if 5 - 5: Oo - i1 . oOO
def avoid_center_on_seam ( mainwin ) :
 if I1i1I ( mainwin ) == 1 :
  i1iIIi1I1iiI = Gtk . check_version ( 3 , 22 , 0 ) is None
  if i1iIIi1I1iiI :
   II1111I11 = mainwin . get_display ( ) . get_monitor ( 0 )
   IiI1IIi1IiII = II1111I11 . get_geometry ( )
   I1IoOooOo0o , iii1ii1 = IiI1IIi1IiII . width , IiI1IIi1IiII . height
  else :
   iIi1i = mainwin . get_screen ( )
   I1IoOooOo0o , iii1ii1 = iIi1i . get_width ( ) , iIi1i . get_height ( )
   if 36 - 36: oOO / ooOOO
  iiiiIi1IiiIi , Ii1iIII11i = I1IoOooOo0o , iii1ii1
  if 58 - 58: IiI11Ii111 / I11iiIi11i1I . iI1iII1I1I1i + Iii1i * Ii
  if 62 - 62: Oo - iI1iII1I1I1i - i1i1i1111I . i1iiIII111
  if 78 - 78: OooOoo . ooOOO
  if 80 - 80: oOO % i1iiIII111 * IiI11Ii111 - oOo0O00 % I11iiIi11i1I - IiI11Ii111
  if 56 - 56: Oo
  for IiIIIII1i in range ( 1 , I1IoOooOo0o ) :
   iiiiIi1IiiIi = I1IoOooOo0o / IiIIIII1i
   if float ( iiiiIi1IiiIi ) / iii1ii1 < 2.4 :
    break
  for IiIIIII1i in range ( 1 , iii1ii1 ) :
   Ii1iIII11i = iii1ii1 / IiIIIII1i
   if float ( iiiiIi1IiiIi ) / Ii1iIII11i > 1.2 :
    break
  O0OOo0O , iiI = mainwin . get_size ( )
  I1i1 = ( iiiiIi1IiiIi - O0OOo0O ) / 2
  oO0O0oO0 = ( Ii1iIII11i - iiI ) / 2
  if I1i1 > 0 and oO0O0oO0 > 0 :
   mainwin . move ( I1i1 , oO0O0oO0 )
   if 40 - 40: i1I . I1I % OooOoo
def oO0 ( title , msg ) :
 o0oO00 = shutil . which ( "zenity" )
 if o0oO00 is None :
  return False
  if 79 - 79: oOO * IiI11Ii111 . ooOOO * I1Ii1I1 . oOo0O00 + i1iiIII111
 try :
  oo00 = subprocess . call ( [ o0oO00 , "--error" , "--title" , title , "--text" , msg ] )
  if oo00 < 0 or oo00 == 255 :
   return False
 except OSError :
  return False
  if 52 - 52: OooOoo
 return True
 if 95 - 95: i1i1i1111I . I11iiIi11i1I * ooo000 / iI1iII1I1I1i - I1Ii1I1 + IiIIii11Ii
def O0oooo0o0oO ( title , msg ) :
 o0oO00 = shutil . which ( "Xdialog" )
 if o0oO00 is None :
  return False
  if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
 try :
  oo00 = subprocess . call ( [ o0oO00 , "--title" , title ,
 "--msgbox" , msg , "0" , "0" ] )
  if oo00 < 0 :
   return False
 except OSError :
  return False
  if 15 - 15: i1I * I11iiIi11i1I - oOo0O00
 return True
 if 6 - 6: IiI11Ii111 - Ii
def iiiIII ( title , msg ) :
 o0oO00 = shutil . which ( "kdialog" )
 if o0oO00 is None :
  return False
  if 16 - 16: IIiIIiIi11I1
 try :
  oo00 = subprocess . call ( [ o0oO00 , "--title" , title , "--error" , msg ] )
  if oo00 != 0 :
   return False
 except OSError :
  return False
  if 96 - 96: OooOoo / oOO - i1 * I11iiIi11i1I
 return True
 if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - i1I + Ooo0Ooo
def message ( title , msg ) :
 if 74 - 74: Ooo0Ooo * Oo + Iii1i - i1iiIII111
 if 22 - 22: IiIIii11Ii - Ooo0Ooo . i1 . i1I - ooo000
 if 68 - 68: ooo000
 if not os . environ . get ( "DISPLAY" , "" ) :
  return False
  if 40 - 40: i1 + I1Ii1I1 + I11iiIi11i1I . Oo * I11iiIi11i1I % I1I
  if 100 - 100: OooOoo + Oo / OooOoo
 msg = "\n" . join ( textwrap . wrap ( msg ) )
 if 33 - 33: IiI11Ii111 / OooOoo
 if oO0 ( title , msg ) :
  return True
  if 98 - 98: I1Ii1I1 . IIiIIiIi11I1 * i1I - iI1iII1I1I1i % i1I * IiI11Ii111
 if O0oooo0o0oO ( title , msg ) :
  return True
  if 42 - 42: OooOoo + i1i1i1111I - iI1iII1I1I1i - oOo0O00 * i1I + Ii
 if iiiIII ( title , msg ) :
  return True
  if 46 - 46: oOo0O00 . iI1iII1I1I1i - Ii . oOo0O00 + i1i1i1111I
 return False
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
