# Task 5 — Abstract Classes + Duck Typing
# Instructions
# 1. Create an abstract base class DataExporter with an abstract method
# export(data).
# 2. Create two subclasses:
# ○ JSONExporter (return JSON string)
# ○ CSVExporter (return a CSV string with one row)
# 3. Create a third class NOT inheriting from DataExporter called XMLExporter, but
# give it a method export(data).
# 4. Create a function run_export(exporter, data) that:
# ○ Accepts any object
# ○ Calls its export(data) method without checking its type
# 5. Demonstrate that all three exporter types work with run_export.

from abc import ABC, abstractmethod
import json
import csv
import io
class DataExporter(ABC):
    @abstractmethod
    def export(self, data) -> str:
        pass
class JSONExporter(DataExporter):
    def jsonexport(self, data):
        return json.dumps(data)

    def export(self, data):
        return json.dumps(data)


class CSVExporter(DataExporter):
    def csvexport(self, data):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(data)
        return output.getvalue().strip()

    def export(self, data):
        return self.csvexport(data)


class XMLExporter:
    def export(self, data):
        xml_data = "<data>\n"
        for item in data:
            xml_data += f"  <item>{item}</item>\n"
        xml_data += "</data>"
        return xml_data
def run_export(exporter, data):
    return exporter.export(data)
# Example usage
if __name__ == "__main__":
    data = ["apple", "banana", "cherry"]
    json_exporter = JSONExporter()
    csv_exporter = CSVExporter()
    xml_exporter = XMLExporter()
    print("JSON Export:")
    print(run_export(json_exporter, data))
    print("\nCSV Export:")
    print(run_export(csv_exporter, data))
    print("\nXML Export:")
    print(run_export(xml_exporter, data))

    
# Expected Output:
# JSON Export:
# ["apple", "banana", "cherry"]
# CSV Export:
# apple,banana,cherry
# XML Export:
# <data>
#   <item>apple</item>
#   <item>banana</item>
#   <item>cherry</item>
# </data>
