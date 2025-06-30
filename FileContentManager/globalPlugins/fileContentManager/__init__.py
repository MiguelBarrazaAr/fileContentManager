# -*- coding: utf-8 -*-
# Copyright (C) 2025 
# Miguel Barraza <miguelbarraza2015@gmail.com>

import os
import wx
import gui
import globalPluginHandler
from comtypes.client import CreateObject as COMCreate
import api
import controlTypes
from scriptHandler import script
from ui import message, browseableMessage

def getFilePath():
    """
    Obtiene la ruta del archivo enfocado en el explorador de Windows.
    """
    fg = api.getForegroundObject()
    if fg.role != controlTypes.Role.PANE and fg.appModule.appName != "explorer":
        return None
    shell = COMCreate("shell.application")
    for window in shell.Windows():
        try:
            if window.hwnd and window.hwnd == fg.windowHandle:
                focusedItem = window.Document.FocusedItem
                break
        except:
            pass
    else:
        return None
    return focusedItem.path

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    
    @script(
        gesture='kb:NVDA+control+shift+c',
        category='fileContentManager',
        description='Copiar al portapapeles el contenido del archivo enfocado'
    )
    def script_fileRead(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            api.copyToClip(content)
            message('Contenido copiado al portapapeles')
        except PermissionError:
            message('Error: permiso denegado al leer el archivo')
        except UnicodeDecodeError:
            message('Error: no se pudo decodificar el archivo')

    @script(
        gesture='kb:NVDA+control+alt+c',
        category='fileContentManager',
        description='Agregar al portapapeles el contenido del archivo enfocado sin sobrescribir'
    )
    def script_clipboardAppend(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_text = f.read()
        except PermissionError:
            message('Error: permiso denegado al leer el archivo')
            return
        except UnicodeDecodeError:
            message('Error: no se pudo decodificar el archivo')
            return
        existing = api.getClipData() or ""
        new_clip = existing + ("\n" if existing else "") + file_text
        api.copyToClip(new_clip)
        message('Contenido del archivo agregado al portapapeles')

    @script(
        gesture='kb:NVDA+control+shift+v',
        category='fileContentManager',
        description='Sobrescribir el archivo enfocado con el texto del portapapeles'
    )
    def script_fileOverwrite(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        text = api.getClipData()
        if text is None:
            message('Error: no hay texto en el portapapeles')
            return
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            message('Archivo sobrescrito con el portapapeles')
        except PermissionError:
            message('Error: permiso denegado al escribir en el archivo')
        except Exception as e:
            message(f'Error al escribir: {e}')

    @script(
        gesture='kb:NVDA+control+alt+v',
        category='fileContentManager',
        description='Agregar al final del archivo enfocado el texto del portapapeles'
    )
    def script_fileAppend(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        text = api.getClipData()
        if text is None:
            message('Error: no hay texto en el portapapeles')
            return
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(( "\n" if os.path.getsize(file_path) > 0 else "" ) + text)
            message('Portapapeles agregado al final del archivo')
        except PermissionError:
            message('Error: permiso denegado al escribir en el archivo')
        except Exception as e:
            message(f'Error al escribir: {e}')

    @script(
        gesture='kb:NVDA+shift+space',
        category='fileContentManager',
        description='Mostrar en el visor el contenido del archivo enfocado'
    )
    def script_showInViewer(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            message(f'Error al leer el archivo: {e}')
            return
        browseableMessage(content, isHtml=False)

    @script(
        gesture='kb:NVDA+alt+a',
        category='fileContentManager',
        description='Abrir cuadro para escribir texto y copiarlo al portapapeles'
    )
    def script_inputDialog(self, gesture):
        dlg = wx.TextEntryDialog(
            gui.mainFrame,
            "Escribe el texto a copiar:",
            "Entrada de texto",
            "",
            style=wx.OK | wx.CANCEL
        )
        def onClose(result):
            if result == wx.ID_OK:
                text = dlg.GetValue()
                api.copyToClip(text)
                message('Texto copiado al portapapeles')
        gui.runScriptModalDialog(dlg, onClose)

    @script(
        gesture='kb:NVDA+control+shift+a',
        category='fileContentManager',
        description='Abrir cuadro para añadir texto al portapapeles con salto de línea'
    )
    def script_inputDialogAppend(self, gesture):
        dlg = wx.TextEntryDialog(
            gui.mainFrame,
            "Escribe el texto a añadir:",
            "Entrada de texto (append)",
            "",
            style=wx.OK | wx.CANCEL
        )
        def onClose(result):
            if result == wx.ID_OK:
                new_text = dlg.GetValue()
                existing = api.getClipData() or ""
                combined = existing + ("\n" if existing else "") + new_text
                api.copyToClip(combined)
                message('Texto añadido al portapapeles')
        gui.runScriptModalDialog(dlg, onClose)

    @script(
        gesture='kb:NVDA+control+shift+r',
        category='fileContentManager',
        description='Copiar al portapapeles la ruta del archivo enfocado'
    )
    def script_copyFilePath(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        api.copyToClip(file_path)
        message('Ruta copiada al portapapeles')

    @script(
        gesture='kb:NVDA+control+shift+z',
        category='fileContentManager',
        description='Mostrar en el visor el texto del portapapeles'
    )
    def script_showClipboardInViewer(self, gesture):
        content = api.getClipData() or ''
        if not content:
            message('Error: no hay texto en el portapapeles')
            return
        browseableMessage(content, isHtml=False)

    @script(
        gesture='kb:NVDA+control+shift+f',
        category='fileContentManager',
        description='Crear archivo con nombre y pegar contenido del portapapeles'
    )
    def script_createFileFromClipboard(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo o carpeta enfocada')
            return
        default_name = "a.txt"
        dlg = wx.TextEntryDialog(
            gui.mainFrame,
            "Nombre del nuevo archivo:",
            "Crear archivo",
            default_name,
            style=wx.OK | wx.CANCEL
        )
        def onClose(result):
            if result == wx.ID_OK:
                name = dlg.GetValue().strip() or default_name
                folder = os.path.dirname(file_path)
                new_path = os.path.join(folder, name)
                try:
                    text = api.getClipData() or ""
                    with open(new_path, 'w', encoding='utf-8') as f:
                        f.write(text)
                    message(f'Archivo creado: {name}')
                except Exception as e:
                    message(f'Error al crear el archivo: {e}')
        gui.runScriptModalDialog(dlg, onClose)

    @script(
        gesture='kb:NVDA+alt+control+r',
        category='fileContentManager',
        description='Copiar ruta del archivo con barras como en linux al portapapeles'
    )
    def script_copyFilePathLinux(self, gesture):
        file_path = getFilePath()
        if not file_path:
            message('No hay archivo enfocado')
            return
        linux_path = file_path.replace("\\", "/")
        api.copyToClip(linux_path)
        message('Ruta (con bara) copiada al portapapeles')

    @script(
        gesture='kb:NVDA+control+shift+d',
        category='fileContentManager',
        description='Abrir en el Explorador la ruta del portapapeles'
    )
    def script_openPathFromClipboard(self, gesture):
        path = api.getClipData()
        if not path:
            message('Error: no hay ruta en el portapapeles')
            return
        try:
            # Asegura formato Windows
            path = path.replace("/", "\\")
            os.startfile(path)
        except Exception as e:
            message(f'Error al abrir la ruta: {e}')
