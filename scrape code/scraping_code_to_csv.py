import csv
# Open the output text file for reading
with open("output.txt", "r", encoding="utf-8") as file:
    # Initialize variables to store data
    chunks = []
    current_chunk = {}

    # Iterate through each line in the file
    for line in file:
        # Check if the line starts with "Heading"
        if line.startswith("Heading"):
            # If current chunk is not empty, append it to chunks list
            if current_chunk:
                chunks.append(current_chunk)
            # Initialize a new chunk
            current_chunk = {}
            # Extract id and speciality from the line
            parts = line.split(":")
            current_chunk["id"] = parts[0].split()[1]
            current_chunk["Speciality"] = parts[1].strip()
        elif line.startswith("Paragraph"):
            # Extract description
            current_chunk["Description"] = line.split(":", 1)[1].strip()
        elif line.startswith("List Item"):
            # Extract subspecialities
            current_chunk.setdefault("Subspeciality", []).append(line.split(":", 1)[1].strip())

    # Append the last chunk to chunks list
    if current_chunk:
        chunks.append(current_chunk)

# Write data to CSV file
with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id", "Speciality", "Description", "Subspeciality"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for chunk in chunks:
        writer.writerow(chunk)
