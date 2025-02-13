# -*-mode: python; coding: utf-8 -*-
#
# Based on rpmvercmp.c from librpm version 4.16.1.3.
#
# Copyright by the various authors of librm.
# Copyright 2012-2014 Pierre Ossman for Cendio AB.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free
# Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

__all__ = ["rpmVersionCompare"]

# Designed to be a direct copy of the C code, to avoid differences
# in behaviour

def strcmp(a, b):
    return (a > b) - (a < b)

def _rislower(c):
    return c >= 'a' and c <= 'z'

def _risupper(c):
    return c >= 'A' and c <= 'Z'

def _risalpha(c):
    return _rislower(c) or _risupper(c)

def _risdigit(c):
    return c >= '0' and c <= '9'

def _risalnum(c):
    return _risalpha(c) or _risdigit(c)

def _rpmvercmp(a, b):
    # easy comparison to see if versions are identical
    if a == b:
        return 0

    str1 = a
    str2 = b

    one = str1
    two = str2

    # loop through each version segment of str1 and str2 and compare them
    while one or two:
        while one and not _risalnum(one[0]) and one[0] not in ['^', '~']:
            one = one[1:]
        while two and not _risalnum(two[0]) and two[0] not in ['^', '~']:
            two = two[1:]

        # handle the tilde separator, it sorts before everything else
        if (one and one[0] == '~') or (two and two[0] == '~'):
            if not one or one[0] != '~': return 1
            if not two or two[0] != '~': return -1
            one = one[1:]
            two = two[1:]
            continue

        # Handle caret separator. Concept is the same as tilde,
        # except that if one of the strings ends (base version),
        # the other is considered as higher version.
        if (one and one[0] == '^') or (two and two[0] == '^'):
            if not one: return -1
            if not two: return 1
            if one[0] != '^': return 1
            if two[0] != '^': return -1
            one = one[1:]
            two = two[1:]
            continue

        # If we ran to the end of either, we are finished with the loop
        if not (one and two): break

        str1 = one
        str2 = two

        # grab first completely alpha or completely numeric segment
        # leave one and two pointing to the start of the alpha or numeric
        # segment and walk str1 and str2 to end of segment
        if str1 and _risdigit(str1[0]):
            while str1 and _risdigit(str1[0]):
                str1 = str1[1:]
            while str2 and _risdigit(str2[0]):
                str2 = str2[1:]
            isnum = True
        else:
            while str1 and _risalpha(str1[0]):
                str1 = str1[1:]
            while str2 and _risalpha(str2[0]):
                str2 = str2[1:]
            isnum = False

        # save character at the end of the alpha or numeric segment
        # so that they can be restored after the comparison
        oldch1 = str1;
        if str1: # XXX Python conversion
            one = one[:-len(str1)]
        str1 = '';
        oldch2 = str2;
        if str2: # XXX Python conversion
            two = two[:-len(str2)]
        str2 = '';

        # take care of the case where the two version segments are
        # different types: one numeric, the other alpha (i.e. empty)
        if one == str1:    # arbitrary
            return -1
        # XXX See patch #60884 (and details) from bugzilla #50977.
        if two == str2:
            if isnum:
                return 1
            else:
                return -1

        if isnum:
            # this used to be done by converting the digit segments
            # to ints using atoi() - it's changed because long
            # digit segments can overflow an int - this should fix that.

            # throw away any leading zeros - it's a number, right?
            while one and one[0] == '0':
                one = one[1:]
            while two and two[0] == '0':
                two = two[1:]

            # whichever number has more digits wins
            if len(one) > len(two):
                return 1
            if len(two) > len(one):
                return -1

        # strcmp will return which one is greater - even if the two
        # segments are alpha or if they are numeric.  don't return
        # if they are equal because there might be more segments to
        # compare
        rc = strcmp(one, two)
        if rc:
            if rc < 1:
                return -1
            else:
                return 1

        # restore character that was replaced by null above
        str1 = oldch1
        one = str1
        str2 = oldch2
        two = str2

    # this catches the case where all numeric and alpha segments have
    # compared identically but the segment sepparating characters were
    # different
    if not one and not two:
        return 0

    # whichever version still has characters left over wins
    if not one:
        return -1
    else:
        return 1

def rpmVersionCompare(first, second):
    # Missing epoch becomes zero here, which is what we want
    try:
        epochOne = int(first[0])
    except ValueError:
        epochOne = 0
    try:
        epochTwo = int(second[0])
    except ValueError:
        epochTwo = 0

    if epochOne < epochTwo:
        return -1
    elif epochOne > epochTwo:
        return 1

    rc = _rpmvercmp(first[1], second[1])
    if rc:
        return rc

    return _rpmvercmp(first[2], second[2])
