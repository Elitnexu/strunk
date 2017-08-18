def setup_text_file():
    pass

def setup_strunk_file(filepath, data):
    f = open(filepath, "w+")
    for line in data:
        f.write(line)
    f.close()

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
