#!/bin/sh
# -*- mode: shell-script; coding: utf-8 -*-
#
# Copyright 2016 Cendio AB.
# For more information, see http://www.cendio.com
#

_find_pkgtool() {
    # Some systems may have multiple tools. Try to sort this so that
    # the most recent/relevant tool "wins".
    if type dnf >/dev/null 2>&1 ; then
        echo "dnf"
    elif type yum >/dev/null 2>&1 ; then
        echo "yum"
    elif type zypper >/dev/null 2>&1 ; then
        echo "zypper"
    elif type apt >/dev/null 2>&1 ; then
        echo "apt"
    fi
}

_can_use_x11_tool() {
    if ! _has_x11_display; then
        return 1
    fi

    # On modern distributions, running X applications when logged in
    # through SSH might not work, especially if a desktop environment
    # is running on the console. For example, executing gnome-terminal
    # will just create another terminal window on the existing
    # desktop.
    if [ -n "${SSH_CONNECTION}" ]; then
        return 1
    fi

    if ! type "$1" >/dev/null 2>&1; then
        return 1
    fi

    return 0
}

_has_x11_display() {
    test -n "${DISPLAY}"
    return $?
}

_has_terminal() {
    test -t 1
    return $?
}

_message() {
    local msg

    msg="$1"

    echo "${msg}"

    if _can_use_x11_tool zenity ; then
        env -u WINDOWID zenity --error --ellipsize --text "${msg}"
    elif _can_use_x11_tool kdialog ; then
        kdialog --error "${msg}"
    fi
}

_yesno() {
    local msg

    msg="$1"

    echo "${msg}"

    if _can_use_x11_tool zenity ; then
        env -u WINDOWID zenity --question --ellipsize --text "${msg}"
        return $?
    elif _can_use_x11_tool kdialog ; then
        kdialog --yesno "${msg}"
        return $?
    elif _has_terminal ; then
        local answer
        echo
        read -p "(Y/n)? " answer
        local ret=$?
        echo

        # Catch errors from read, such as EOF.
        if [ $ret -ne 0 ]; then
            return 1
        fi

        if [ -z "$answer" -o "$answer" = "y" -o "$answer" = "Y" ]; then
            return 0
        else
            return 1
        fi
    else
        return 1
    fi
}

_doinstall() {
    local cmd

    cmd="$1"

    local term _t

    for _t in gnome-terminal konsole xfce4-terminal \
              mate-terminal xterm; do
        if _can_use_x11_tool $_t; then
            term=$_t
            break
        fi
    done

    if [ -n "${term}" ]; then
        echo Starting $term to run \"$cmd\"...

        case "${term}" in
            "gnome-terminal")
            term="${term} --"
                ;;
            "xfce4-terminal"|"mate-terminal")
            term="${term} -x"
                ;;
            "xterm"|"konsole")
            term="${term} -e"
                ;;
        esac

        exec $term bash -c "
        echo \"\$ ${cmd}\"
        $cmd
        ret=\$?
        echo
        if [ \$ret -ne 0 ]; then
            echo \"Installation failed. Please report this issue to ThinLinc support.\"
            echo \"Visit https://www.cendio.com/thinlinc/support for information on how to contact us.\"
        else
            echo \"Installation completed successfully.\"
            echo \"Please restart $0 to continue.\"
        fi
        echo
        read -p \"Press Enter to close this terminal...\"
        "
    elif _has_terminal; then
        echo "\$ ${cmd}"
        ${cmd}
        local ret=$?
        echo
        if [ $ret -ne 0 ]; then
            echo "Installation failed. Please report this issue to ThinLinc support."
            echo "Visit https://www.cendio.com/thinlinc/support for information on how to contact us."
            exit 1
        else
            echo "Installation completed successfully."
            echo "Restarting $0..."
            echo
            exec "$0" "$@"
        fi
    else
        echo "Could not find a terminal program."
        _text=`
        echo
        echo "I could not find a graphical terminal program to run the"
        echo "command in. Please run the command manually:"
        echo
        echo "    ${cmd}"
        echo
        echo "Please try again once the command has completed."
        `
        _message "$_text"
        exit 1
    fi
}

# sudo is only needed if not root
if [ `id -u` -eq 0 ]; then
    _sudo=""
else
    _sudo="sudo "
fi

# If we need to use sudo with X11, then we need to make sure we have
# a cookie or things will most likely be denied once we switch user
if [ -n "${_sudo}" -a -n "${DISPLAY}" ]; then
    if ! type xauth >/dev/null 2>&1 ; then
        # No xauth, assume the worst
        _xauth_entries=""
    else
        _xauth_entries=`xauth list $DISPLAY`
    fi

    # Any entries for the current display?
    if [ -z "${_xauth_entries}" ]; then
        # Nope, so make sure nothing tries to use X11
        unset DISPLAY
    fi
fi

# Make sure we have a Python interpreter
PYTHON=/usr/bin/python3
if [ ! -x ${PYTHON} ]; then
    _pkgtool=`_find_pkgtool`

    # We have assumed that we don't have to do further platform
    # tests to determine which package to install
    case "${_pkgtool}" in
        "dnf")
            _pkgcmd="${_sudo}dnf install python3"
            ;;
        "yum")
            _pkgcmd="${_sudo}yum install python3"
            ;;
        "zypper")
            _pkgcmd="${_sudo}zypper install python3"
            ;;
        "apt")
            _pkgcmd="${_sudo}apt install python3"
            ;;
    esac

    _text=`
    echo 
    echo "Error: No Python 3.x interpreter found."
    echo
    echo "A Python 3.x interpreter is required for ThinLinc."
    echo "I was trying to use the Python interpreter '${PYTHON}'."
    echo 

    if [ -z "${_pkgtool}" ]; then
        echo "I could not detect the correct command to install Python."
        echo "Please install Python manually and try again."
    else
        echo "To install Python, please run this command:"
        echo
        echo "    ${_pkgcmd}"
        echo
        echo "Would you like to run this command now?"
    fi
    `

    if [ -z "${_pkgtool}" ]; then
        _message "$_text"
    else
        if _yesno "$_text"; then
            _doinstall "${_pkgcmd}"
        else
            _message "Please try again once Python is installed."
        fi
    fi

    exit 1
fi

# Make sure we have valid Python
if ${PYTHON} -c "import sys; sys.exit(sys.hexversion < 0x3040400)"; then
    :
else
    _text=`
    echo 
    echo "Error: A Python interpreter of version 3.4.4 or newer is required."
    echo
    echo "I was trying to use the Python interpreter named '${PYTHON}'."
    `

    _message "$_text"

    exit 1
fi
