import csv
import io

def get_csv(data):
    # Verwende newline='' um zu verhindern, dass zusätzliche \r hinzugefügt werden
    output = io.StringIO(newline='')
    writer = csv.writer(output)

    # Kopfzeile schreiben
    writer.writerow(["title", "category", "description"])

    # Datenzeilen schreiben
    for item in data:
        writer.writerow([item["title"], item["category"], item["description"]])

    return output.getvalue()
