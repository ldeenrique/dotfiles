# Ivaylo Kuzev <ivkuzev@gmail.com>, 2014
# Zenburn like colorscheme for https://github.com/hut/ranger .

# default colorscheme.
# Copyright (C) 2009-2013  Roman Zimbelmann <hut@lepus.uberspace.de>
# This software is distributed under the terms of the GNU GPL version 3.

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import default_colors, reverse, bold, normal, default


# pylint: disable=too-many-branches,too-many-statements
class kiwi(ColorScheme):
    progress_bar_color = 232

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                #FOLDER VACIO
                fg = 210
            if context.border:
                #SEPARADOR
                fg = 248
            if context.image:
                #IMAGENES
                fg = 194
            if context.video:
                #VIDEOS
                fg = 153
            if context.audio:
                #AUDIOS
                fg = 109
            if context.document:
                #CUALQUIER ARCHIVO
                fg = 189
            if context.container:
                #ARCHIVOS COMPRIMIDOS
                #attr |= bold
                fg = 146
            if context.directory:
                #CARPETAS
                attr |= bold
                #fg = 194 verde color culo
                fg = 251
            elif context.executable and not \
                    any((context.media, context.container,
                         context.fifo, context.socket)):
                #EJECUTABLES COMO EXE,BAT,ETC
                #attr |= bold
                fg = 230



            if context.socket:
                fg = 180
                attr |= bold
            if context.fifo or context.device:
                fg = 144
                if context.device:
                    attr |= bold
            if context.link:
                #ARCHIVOS ENLAZADOS A CARPETAS U OTRA COSA
                fg = 194 if context.good else 183
            # MARCAR CON T
            if context.tag_marker and not context.selected:
                attr |= normal
                if fg in (174, 95):
                    fg = 193
                else:
                    #este es por cierto
                    fg = 189

            #CONTEXTO SEELECCIONADO
            if not context.selected and (context.cut or context.copied):
                fg = 194
                #bg = 234

            #CARPETAS SELECCIONADAS
            if context.main_column:
                if context.selected:
                    attr |= normal
                if context.marked:
                    attr |= normal
                    fg = 194
            if context.badinfo:
                if attr & reverse:
                    bg = 95
                else:
                    fg = 95
        
        #BARRAS DE TITULO
        elif context.in_titlebar:
            #attr |= bold
            #Usuario+maquina
            if context.hostname:
                attr |= bold
                fg = 194 if context.bad else 194
            #mostrar directorio actual
            elif context.directory:
                fg = 189
            elif context.tab:
                if context.good:
                    bg = 108
            #folders linkeados
            elif context.link:
                fg = 183

        #BARRA DE ESTATUS
        elif context.in_statusbar:
            #permisos
            if context.permissions:
                if context.good:
                    fg = 147
                elif context.bad:
                    fg = 147
            if context.marked:
                attr |= bold | reverse
                fg = 223
            if context.message:
                if context.bad:
                    attr |= bold
                    fg = 174
            if context.loaded:
                bg = self.progress_bar_color
            if context.vcsinfo:
                fg = 116
                attr &= ~bold
            if context.vcscommit:
                fg = 144
                attr &= ~bold

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = 116

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        if context.vcsfile and not context.selected:
            attr &= ~bold
            if context.vcsconflict:
                fg = 95
            elif context.vcschanged:
                fg = 174
            elif context.vcsunknown:
                fg = 174
            elif context.vcsstaged:
                fg = 108
            elif context.vcssync:
                fg = 108
            elif context.vcsignored:
                fg = default

        elif context.vcsremote and not context.selected:
            attr &= ~bold
            if context.vcssync:
                fg = 108
            elif context.vcsbehind:
                fg = 174
            elif context.vcsahead:
                fg = 116
            elif context.vcsdiverged:
                fg = 95
            elif context.vcsunknown:
                fg = 174

        return fg, bg, attr
