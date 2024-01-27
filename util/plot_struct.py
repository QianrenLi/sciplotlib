class DataStruct():
    def __init__(self, **kwargs):
        self.xdata = []
        self.ydata = []
        self.val = []

        # heatmap, line, bar            
        self.xlabel = []
        self.ylabel = []
        self.title = ''

        # conf_matrix
        self.labels = []
        self.pre = []
        self.classes = []
        self.normalize = False
        self.conf_matrix = []

        # tsne
        self.features = []
        self.tsne_result = []

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