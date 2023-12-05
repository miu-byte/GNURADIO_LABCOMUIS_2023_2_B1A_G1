#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: labcom
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from ModulacionPAM import ModulacionPAM  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import sip



class LAB5A_2_2grc(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "LAB5A_2_2grc")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100e3
        self.fs = fs = 1e3
        self.fm = fm = 100
        self.D4 = D4 = 0
        self.D3 = D3 = 0
        self.D2 = D2 = 0
        self.D1 = D1 = 0
        self.D = D = 10
        self.Am = Am = 1

        ##################################################
        # Blocks
        ##################################################

        self._fs_range = Range(0, 10e3, 1, 1e3, 200)
        self._fs_win = RangeWidget(self._fs_range, self.set_fs, "Frecuencia Pulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fs_win)
        self._fm_range = Range(0, 10e3, 10, 100, 200)
        self._fm_win = RangeWidget(self._fm_range, self.set_fm, "Frecuencia Mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._D4_range = Range(0, 100, 1, 0, 200)
        self._D4_win = RangeWidget(self._D4_range, self.set_D4, "Retardo Audio", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D4_win)
        self._D3_range = Range(0, 100, 1, 0, 200)
        self._D3_win = RangeWidget(self._D3_range, self.set_D3, "Retardo 3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D3_win)
        self._D2_range = Range(0, 100, 1, 0, 200)
        self._D2_win = RangeWidget(self._D2_range, self.set_D2, "Retardo 2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D2_win)
        self._D1_range = Range(0, 100, 1, 0, 200)
        self._D1_win = RangeWidget(self._D1_range, self.set_D1, "Retardo 1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D1_win)
        self._D_range = Range(0, 50, 1, 10, 200)
        self._D_win = RangeWidget(self._D_range, self.set_D, "Ancho Pulso", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_win)
        self._Am_range = Range(0, 10e3, 100e-3, 1, 200)
        self._Am_win = RangeWidget(self._Am_range, self.set_Am, "Amplitud Mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=1,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            6, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(6):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/labcom/Descargas/despecha_rosalia.wav', True)
        self.blocks_delay_1_0 = blocks.delay(gr.sizeof_float*1, D4)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_float*1, D3)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, D2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, D1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, Am, 0, 0)
        self.ModulacionPAM_0_2_0 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0_2 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0_1 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0_0 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModulacionPAM_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.ModulacionPAM_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModulacionPAM_0_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModulacionPAM_0_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.ModulacionPAM_0_2, 0), (self.blocks_delay_0_1, 0))
        self.connect((self.ModulacionPAM_0_2_0, 0), (self.blocks_delay_1_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModulacionPAM_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.ModulacionPAM_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.ModulacionPAM_0_1, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.ModulacionPAM_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_0_1, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_delay_1_0, 0), (self.qtgui_time_sink_x_0, 5))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.ModulacionPAM_0_2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "LAB5A_2_2grc")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ModulacionPAM_0.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_0.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_1.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_2.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_0_2_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModulacionPAM_0.set_fs(self.fs)
        self.ModulacionPAM_0_0.set_fs(self.fs)
        self.ModulacionPAM_0_1.set_fs(self.fs)
        self.ModulacionPAM_0_2.set_fs(self.fs)
        self.ModulacionPAM_0_2_0.set_fs(self.fs)

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_1.set_frequency(self.fm)
        self.analog_sig_source_x_0_2.set_frequency(self.fm)

    def get_D4(self):
        return self.D4

    def set_D4(self, D4):
        self.D4 = D4
        self.blocks_delay_1_0.set_dly(int(self.D4))

    def get_D3(self):
        return self.D3

    def set_D3(self, D3):
        self.D3 = D3
        self.blocks_delay_0_1.set_dly(int(self.D3))

    def get_D2(self):
        return self.D2

    def set_D2(self, D2):
        self.D2 = D2
        self.blocks_delay_0_0.set_dly(int(self.D2))

    def get_D1(self):
        return self.D1

    def set_D1(self, D1):
        self.D1 = D1
        self.blocks_delay_0.set_dly(int(self.D1))

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.ModulacionPAM_0.set_D(self.D)
        self.ModulacionPAM_0_0.set_D(self.D)
        self.ModulacionPAM_0_1.set_D(self.D)
        self.ModulacionPAM_0_2.set_D(self.D)
        self.ModulacionPAM_0_2_0.set_D(self.D)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.analog_sig_source_x_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_1.set_amplitude(self.Am)
        self.analog_sig_source_x_0_2.set_amplitude(self.Am)




def main(top_block_cls=LAB5A_2_2grc, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
