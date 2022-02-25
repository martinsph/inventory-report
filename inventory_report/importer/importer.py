from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def import_data(self, path, report_type):
        raise NotImplementedError
