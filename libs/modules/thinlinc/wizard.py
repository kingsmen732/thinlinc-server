# -*-mode: python; coding: utf-8 -*-
#
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
# Copyright 2024 Samuel Mannehed for Cendio AB.
# For more information, see http://www.cendio.com
import textwrap
import math
if 82 - 82: Iii1i
from . import tlgtk
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
__all__ = [ "Wizard" ,
 "text_print_wrapped" , "text_print_columns" , "text_print_title" ,
 "text_wait_prompt" , "text_prompt" , "interactive" ]
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
if 31 - 31: i1I
if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
if 16 - 16: i1i1i1111I / i1iiIII111
interactive = True
if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
def text_print_wrapped ( text , width = 72 ) :
 for ii1iI1I in text . splitlines ( ) :
  print ( textwrap . fill ( ii1iI1I , width , break_long_words = False ,
 break_on_hyphens = False ) )
  if 28 - 28: i1I / IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo
def IIII1i1 ( orig_list , number_of_splits ) :
 i1Iiiii1 = orig_list . copy ( )
 ooOOooO0 = [ ]
 if 13 - 13: oOO
 if 2 - 2: i1
 if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
 IIII11 = len ( i1Iiiii1 ) / number_of_splits
 oOoo0 = round ( ( IIII11 % 1 ) * number_of_splits )
 IIII11 = math . ceil ( IIII11 )
 if 95 - 95: i1iiIII111 . Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
 while len ( i1Iiiii1 ) > 0 :
  ooOOooO0 . append ( i1Iiiii1 [ : IIII11 ] )
  if 8 - 8: I1Ii1I1 . IiI11Ii111 . i1 . Oo - i1I
  del i1Iiiii1 [ : IIII11 ]
  if 32 - 32: Ii % i1i1i1111I % i1I - I11iiIi11i1I % i1iiIII111
  if 34 - 34: i1iiIII111 * i1
  if oOoo0 > 0 :
   oOoo0 -= 1
   if oOoo0 == 0 :
    IIII11 -= 1
    if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
 return ooOOooO0
 if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
def text_print_columns ( string_list , max_cols = 3 , total_width = 72 ) :
 IiI11I = "  "
 IiiIii11iII1 = max_cols
 if 27 - 27: I1I + ooOOO * IIiIIiIi11I1 % Ii + Ooo0Ooo . ooOOO
 if 6 - 6: i1iiIII111
 if 99 - 99: ooOOO * I1Ii1I1
 if len ( string_list ) <= max_cols :
  IiiIii11iII1 = 1
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
 I1iIiiIIiIi = total_width - ( IiiIii11iII1 * len ( IiI11I ) )
 i1I11ii = IIII1i1 ( string_list , IiiIii11iII1 )
 if 21 - 21: Iii1i - I1Ii1I1
 def O0oOo0oOoOoo ( col ) :
  return len ( max ( col , key = len ) )
  if 59 - 59: i1 + Iii1i / I1I
  if 52 - 52: i1i1i1111I + IiIIii11Ii + I11iiIi11i1I
  if 52 - 52: i1iiIII111 % Oo . I1Ii1I1 + ooOOO % Oo . IiI11Ii111
 while sum ( O0oOo0oOoOoo ( OOO00oO0oOo0O ) for OOO00oO0oOo0O in i1I11ii ) > I1iIiiIIiIi :
  IiiIii11iII1 -= 1
  I1iIiiIIiIi = total_width - ( IiiIii11iII1 * len ( IiI11I ) )
  if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
  if IiiIii11iII1 <= 1 :
   IiiIii11iII1 = 1
   break
   if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * i1I % oOo0O00
  i1I11ii = IIII1i1 ( string_list , IiiIii11iII1 )
  if 52 - 52: oOo0O00 . I1I + i1I - i1iiIII111 % iI1iII1I1I1i
 Oo0O0o0oO000 = math . ceil ( len ( string_list ) / IiiIii11iII1 )
 if 80 - 80: i1 . oOo0O00 * i1
 if 26 - 26: Ii . i1
 oO00o00OO = IiI11I
 for OOO00oO0oOo0O in i1I11ii :
  oO00o00OO += "{:<" + str ( O0oOo0oOoOoo ( OOO00oO0oOo0O ) ) + "}" + IiI11I
  if 52 - 52: Iii1i / Oo
  if 100 - 100: I1Ii1I1 / I11iiIi11i1I * Ii - oOO
 oO00o00OO = oO00o00OO [ : - len ( IiI11I ) ]
 if 32 - 32: iI1iII1I1I1i
 for I111II111I1I in range ( Oo0O0o0oO000 ) :
  IIi1I1I1i = [ ]
  for OOO00oO0oOo0O in i1I11ii :
   if 36 - 36: oOo0O00 . ooOOO / i1iiIII111 + oOO
   if I111II111I1I < len ( OOO00oO0oOo0O ) :
    IIi1I1I1i . append ( OOO00oO0oOo0O [ I111II111I1I ] )
   else :
    IIi1I1I1i . append ( "" )
    if 11 - 11: i1 / ooo000
  print ( oO00o00OO . format ( * IIi1I1I1i ) )
  if 89 - 89: I1I * i1i1i1111I
def text_print_title ( title ) :
 print ( title )
 print ( len ( title ) * "=" )
 if 54 - 54: oOO + Ooo0Ooo - I1I . Ooo0Ooo
 if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
def text_wait_prompt ( ) :
 if interactive :
  input ( "Press Enter to continue..." )
  if 54 - 54: oOO * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
  if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - IiI11Ii111
def text_prompt ( text , accepts ) :
 I11ii1IiIii = None
 if 34 - 34: I1I + i1iiIII111 - ooo000 + ooOOO
 if 97 - 97: i1i1i1111I + Iii1i - oOO * Ii
 if 45 - 45: i1i1i1111I * Ii
 if 97 - 97: i1
 if 26 - 26: IiI11Ii111
 for iI1i in accepts :
  if not iI1i . islower ( ) and I11ii1IiIii is None :
   I11ii1IiIii = iI1i . lower ( )
   if 73 - 73: ooOOO - IiIIii11Ii
   if 22 - 22: Oo % oOo0O00 / i1I . oOo0O00 . i1I
 Ooo000oo0O00o = [ iI1i . lower ( ) for iI1i in accepts ]
 if 73 - 73: IiIIii11Ii
 while ( True ) :
  O00 = input ( text + " [" + "/" . join ( accepts ) + "]? " )
  if len ( O00 ) == 0 and I11ii1IiIii is not None :
   return I11ii1IiIii
   if 44 - 44: Ooo0Ooo
  O00 = O00 . lower ( )
  if 63 - 63: Ooo0Ooo
  if O00 is None :
   continue
   if 47 - 47: OooOoo - I1Ii1I1 - I11iiIi11i1I * ooOOO * oOO % IIiIIiIi11I1
   if 60 - 60: i1I * i1iiIII111 + i1i1i1111I / ooOOO
  o000OOoOO = 0
  IIIII = ""
  for iI1i in Ooo000oo0O00o :
   if iI1i . startswith ( O00 ) :
    o000OOoOO = o000OOoOO + 1
    if o000OOoOO == 1 :
     IIIII = iI1i
     if 77 - 77: oOO + I11iiIi11i1I . i1i1i1111I / Ooo0Ooo / oOO - i1
  if o000OOoOO == 1 :
   return IIIII
   if 89 - 89: IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
   if 52 - 52: oOo0O00 / i1I * IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO
class Wizard :
 def __init__ ( self ) :
  self . _title = None
  if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
  self . _intro = None
  self . _intro_title = None
  self . _intro_text = None
  self . _intro_button_text = None
  if 30 - 30: I1I
  self . _banner_path = None
  self . _width = - 1
  self . _height = - 1
  if 41 - 41: oOO
  self . _text_handlers = [ ]
  self . _gui_handlers = [ ]
  if 98 - 98: I1I / IIiIIiIi11I1 / i1I + IiI11Ii111 % Oo + I1I
 def set_title ( self , title ) :
  self . _title = title
  if 38 - 38: I1Ii1I1 + oOo0O00
 def set_intro ( self , title , text , button_text ,
 banner_path = None , width = - 1 , height = - 1 ) :
  self . _intro_title = title
  self . _intro_text = text
  self . _intro_button_text = button_text
  if 2 - 2: OooOoo % Ii + oOO . OooOoo + IIiIIiIi11I1 * Oo
  self . _banner_path = banner_path
  self . _width = width
  self . _height = height
  if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
 def add_text_handler ( self , handler ) :
  self . _text_handlers . append ( handler )
  if 15 - 15: ooo000
 def add_gui_handler ( self , handler ) :
  self . _gui_handlers . append ( handler )
  if 63 - 63: i1I
 def run ( self ) :
  try :
   if not tlgtk . has_gtk :
    return self . _run_text ( )
   else :
    return self . _run_gui ( )
  except KeyboardInterrupt :
   return False
   if 81 - 81: OooOoo . i1I / i1i1i1111I + Oo / Ooo0Ooo % IiI11Ii111
 def _run_text ( self ) :
  if self . _intro_title is not None :
   text_print_title ( self . _intro_title )
   print ( )
   if 77 - 77: I11iiIi11i1I / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  if self . _intro_text is not None :
   text_print_wrapped ( self . _intro_text )
   print ( )
   text_wait_prompt ( )
   print ( )
   if 73 - 73: IiI11Ii111 . Oo * I1I / i1i1i1111I + I1Ii1I1
  for iiiiII11II in self . _text_handlers :
   iiiiII11II ( )
   if 5 - 5: oOo0O00 + iI1iII1I1I1i
  return True
  if 10 - 10: ooOOO / i1I * I1I * Oo - i1 % OooOoo
 def _run_gui ( self ) :
  ooo = tlgtk . wizard . Wizard ( )
  ooo . set_default_size ( 880 , 530 )
  if 40 - 40: i1I * iI1iII1I1I1i + iI1iII1I1I1i . oOo0O00 * ooo000
  if self . _title is not None :
   ooo . set_title ( self . _title )
   if 35 - 35: IIiIIiIi11I1 % i1i1i1111I - Ii % i1iiIII111 - IiI11Ii111
  if self . _intro_title is not None :
   oo0 = self . _intro_text
   ooo . add_intro ( self . _intro_title , oo0 ,
 self . _intro_button_text ,
 self . _banner_path , self . _width , self . _height )
   if 74 - 74: ooOOO . Ii % IIiIIiIi11I1 / iI1iII1I1I1i % ooOOO
  for iiiiII11II in self . _gui_handlers :
   iiiiII11II ( ooo )
   if 24 - 24: IIiIIiIi11I1 - IIiIIiIi11I1 . Ooo0Ooo + i1iiIII111 + Oo
  return ooo . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
