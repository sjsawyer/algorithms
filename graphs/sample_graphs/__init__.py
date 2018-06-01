import load
import os


_sample_graphs_dir = os.path.dirname(os.path.abspath(__file__))
g1 = load.from_txt(os.path.join(_sample_graphs_dir,
                                "g1.txt"))
