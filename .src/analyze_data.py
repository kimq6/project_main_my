from select_analyze_data import select_analyze_data
from iv_graph import parsing_iv_data, plot_iv, save_png_iv
from handle_subplot import handle_subplot
from ts_graph import ts_graph, ts_fitting_graph, flat_ts_graph
from save_csv import save_csv
from ts_fitting import flat_peak, plot_fitting_graph
import os


def function1(ax1, xml):
    plot_iv(ax1, parsing_iv_data(xml))


def function2(ax2, xml):
    ts_graph(ax2, xml)


def function3(ax3, xml):
    ts_fitting_graph(ax3, xml)


def function4(ax4, xml):
    flat_ts_graph(ax4, xml)


def function5(xml):
    save_csv(xml)


def function6(ax5, xml):
    flat_peak(ax5, xml)


def function7(ax6, xml):
    plot_fitting_graph(ax6, xml)


def analyze_data(self, option_list):
    # './res/csv_files/' 폴더 내 모든 csv 파일 삭제
    [os.remove(os.path.join('./res/csv_files/', file)) for file in os.listdir('./res/csv_files/') if file.endswith('.csv')]
    # './res/png_files/' 폴더 내 모든 png 파일 삭제
    [os.remove(os.path.join('./res/png_files/', file)) for file in os.listdir('./res/png_files/') if file.endswith('.png')]
    print(option_list)

    for i, xml in enumerate(self.xml_files):
        ax1, ax2, ax3, ax4, ax5, ax6 = select_analyze_data(option_list)

        # data 분석할 것들을 모음
        if 'ax1' in option_list:
            ax1.set_yscale('log', base=10)
            function1(ax1, xml)
        if 'ax2' in option_list:
            function2(ax2, xml)
        if 'ax3' in option_list:
            function3(ax3, xml)
        if 'ax4' in option_list:
            function4(ax4, xml)
        if 'save_csv' in option_list:
            function5(xml)
        if 'ax5' in option_list:
            function6(ax5, xml)
            function7(ax6, xml)

        handle_subplot(ax1, ax2, ax3, ax4, ax5, ax6)
        save_png_iv(xml)
        self.update()
        self.progress_bar.step(100/len(self.xml_files))
        self.progress_ratio_label.config(text=f"Progress ratio: {round((i+1)*100/len(self.xml_files))}%")
    self.update()
