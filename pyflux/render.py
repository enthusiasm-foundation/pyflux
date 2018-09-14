from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

from pyflux import Result

import pandas as pd
class Render(object):

    def timeplot(self, results):
        plots = []
        for res in results:
            xy = []
            for columns in res.lines:
                time = datetime.strptime(columns[res.headers.index("_time")], "%Y-%m-%dT%H:%M:%SZ")
                val = float(columns[res.headers.index("_value")])
                xy.append([time,val])
            xy.sort(key=lambda y: y[0])
            plots.append(plt.plot([x[0] for x in xy], [y[1] for y in xy]))
        return plots

    def table(self, result):
        return pd.DataFrame(result.lines, columns=result.headers)
