import os

# Open the text file for reading
with open("sectionnums", "r") as f:
    # Loop over each line in the file
    for line in f:
        # Remove any trailing whitespace or newline characters
        line = line.strip()

        # Construct the URL using the line text and any necessary formatting
        url = f"'https://app.leg.wa.gov/RCW/default.aspx?cite={line}&full=true&pdf=true'"

        # Use wget to download the file
        os.system(f"wget --content-disposition {url}")
