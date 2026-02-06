import os

def rename_files(dirname, oldextension, newextension):
    for file in os.listdir(dirname):
        if file.endswith(oldextension):
            oldextension = os.path.join(dirname, file)
            newextension = os.path.join(
                dirname, file.replace(oldextension, newextension)
            )
            os.rename(oldextension, newextension)

    print("Files renamed successfully")

def main():
    dirname = input("Enter directory name: ")
    oldextension= input("Enter old extension (example .txt): ")
    newextension = input("Enter new extension (example .doc): ")

    rename_files(dirname, oldextension, newextension)

main()