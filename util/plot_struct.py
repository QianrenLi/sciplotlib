class DataStruct():
    def __init__(self, **kwargs):
        self.xdata = []
        self.ydata = []
        self.val = []

        # heatmap, line           
        self.xlabel = []
        self.ylabel = []
        self.title = ''

        # bar
        self.xlabel = []
        self.ylabel = []
        self.classes = []
        self.bar_width = 0.35
        self.inter_width = 0.35
        self.print_ydata = False

        # conf_matrix, bar
        self.labels = []
        self.pre = []
        self.classes = []
        self.normalize = False
        self.conf_matrix = []

        # cdf
        self.line_style = []

        # tsne
        self.features = []
        self.tsne_result = []

        self.color = []
        self.filePath = 'untitled.png'
        self.dpi = 300
        self.show = False

    """
    @description  :
    ---------
    @param  :
    -------
    @Returns  :
    -------
    """

    def __str__(self) -> str:
        return f'xdata: {self.xdata}\nydata: {self.ydata}\nval: {self.val}\nfilePath: {self.filePath}'