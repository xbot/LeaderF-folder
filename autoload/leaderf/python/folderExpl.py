#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from leaderf.utils import *
from leaderf.explorer import *
from leaderf.manager import *


# *****************************************************
# FolderExplorer
# *****************************************************
class FolderExplorer(Explorer):
    def __init__(self):
        self._content = []

    def getContent(self, *args, **kwargs):
        if self._content:
            return self._content
        else:
            return self.getFreshContent()

    def getFreshContent(self, *args, **kwargs):
        self._content = lfEval("system('fd -t directory -I')").split()

        return self._content

    def getStlCategory(self):
        return "Folder"

    def getStlCurDir(self):
        return escQuote(lfEncode(os.getcwd()))

    def supportsNameOnly(self):
        return True


# *****************************************************
# FolderExplManager
# *****************************************************
class FolderExplManager(Manager):
    def _getExplClass(self):
        return FolderExplorer

    def _defineMaps(self):
        lfCmd("call leaderf#Folder#Maps()")

    def _acceptSelection(self, *args, **kwargs):
        if len(args) == 0:
            return

        cmd = lfEval("g:Lf_FolderAcceptSelectionCmd")
        if cmd == "":
            cmd = "lcd"

        if kwargs.get("mode", '') == 't':
            lfCmd("tabnew")

        lfCmd(cmd + " " + args[0])

    def _getDigest(self, line, mode):
        """
        specify what part in the line to be processed and highlighted
        Args:
            mode: 0, return the full path
                  1, return the name only
                  2, return the directory name
        """
        if not line:
            return ""
        if mode == 0:
            return line
        elif mode == 1:
            return line.rstrip('/').split('/')[-1]
        else:
            start_pos = line.rstrip('/').rfind('/')
            return line[:start_pos]

    def _getDigestStartPos(self, line, mode):
        """
        specify what part in the line to be processed and highlighted
        Args:
            mode: 0, return the full path
                  1, return the name only
                  2, return the directory name
        """
        if not line:
            return 0

        if mode == 1:
            start_pos = line.rstrip('/').rfind('/')
            if start_pos < 0:
                start_pos = 0
            return lfBytesLen(line[:start_pos+1])
        else:
            return 0

    def _createHelp(self):
        help = []
        help.append('" <CR>/<double-click>/o : open the folder under cursor')
        help.append('" t : open the folder under cursor in a new tab')
        help.append('" i : switch to the input mode')
        help.append('" q : quit')
        help.append('" <F1> : toggle this help')
        help.append('" <F5> : refresh the cache')
        help.append('" ---------------------------------------------------------')
        return help


# *****************************************************
# folderExplManager is a singleton
# *****************************************************
folderExplManager = FolderExplManager()

__all__ = ["folderExplManager"]
