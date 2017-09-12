#File Setup.py
#Sets up all test data and files, rather than keeping them in the directory.
def setup_test_file(filepath, data):
    f = open(filepath, "w+")
    for line in data:
        f.write(line)
    f.close()

#Generate test text file data
def generate_file_data():
    return "Media Sociale utilised the green light. Daisy, his long-forlorned lover, represented the American Dream.\n" \
    + "\n"
    + "Gatsby and Nick also had a very special relationship. In fact, Nick is considered an \"unreliable\n" \
    + "narrator\n\", a result borne from Gatsby and Nick's interactions.\n" \
    + "Media Sociale is a trademarked company\n!" \
    + "\n" \
    + "Their trouble and turmoil, unaffected by the biker over.\n" \
    + "They\'re not really as smart as they look." \
    + "There is a house on the hill.\n" \
    + "\n" \
    + "Unfortunately, the enigmatic Gatsby meets his maker and Nick is left to pick up the pieces! The end?"

#Generate test strunkfile data
def generate_strunk_data():
        return "#=DO NOT REMOVE FROM TEST DIRECTORY= " \
        + "#Test file for Strunk.\n" \
        + "\\bGatsby\\b\n" \
        + "WARNING \n" \
        + "This is a subject line#1 \n" \
        + "This is an info line#1 \n" \
        + "This is a more info line#1 \n" \
        + "\n" \
        + "\n" \
        + "\\bNick\\b \n" \
        + "WARNING \n" \
        + "This is a subject line#2 \n" \
        + "This is an info line#2 \n" \
        + "This is a more info line#2 \n" \
        + "This is another more info line#2 \n" \
        + "\n" \
        + "\n" \
        + "\\bpod racing\\b \n" \
        + "WARNING \n" \
        + "This is a subject line#3 \n" \
        + "This is an info line#3 \n" \
        + "\n" \
        + "END"
