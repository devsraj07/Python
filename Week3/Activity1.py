'''
Week 3- Activity 1: File data processing
============================================
Open the Iris dataset (https://archive.ics.uci.edu/dataset/53/iris) and perform the initial data processing to identify:
Open the file and find the total number of records in the file.
The total number of different flower available.
The names of all different flowers in the dataset.
'''
from ucimlrepo import fetch_ucirepo 
  
class IrisDataProcessor:
    def __init__(self):
        self.data = []
        self.load_data()

    def load_data(self):
        iris = fetch_ucirepo(id=53)
        X = iris.data.features 
        y = iris.data.targets
        self.data = iris.data.features.values.tolist()
        self.targets = y

    def total_records(self):
        return len(self.data)

    def unique_flowers(self):
        species_column = self.targets.columns[0]
        unique_species = self.targets[species_column].unique()
        return unique_species

def main(): 
    processor = IrisDataProcessor()
    total_records = processor.total_records()
    unique_flowers = processor.unique_flowers()

    print(f"Total number of records: {total_records}")
    print(f"Total number of different flowers: {len(unique_flowers)}")
    print(f"Names of all different flowers: {unique_flowers}")

if __name__ == "__main__":
    main()
