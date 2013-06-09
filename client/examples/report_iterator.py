class ReportIterator:

    def __init__(self, start=0,end=0,child_iterator=None):
        self._start = start-1
        self.start = start-1
        self.end = end
        self.child_iterator = child_iterator
    def __iter__(self):
        return self

    def __next__(self):
        self.start=self.start+1;
        if self.start > self.end:
            self.start=self._start
            raise StopIteration
        return self.start

    def next_child(self):
        self.child_iterator.__next__()