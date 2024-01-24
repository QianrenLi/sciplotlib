class DataStruct():
    def __init__(self, **kwargs):
        self.xdata = []
        self.ydata = []
        self.val = []

        self.xlabel = []
        self.ylabel = []

        self.filePath = ''
        self.dpi = 300

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