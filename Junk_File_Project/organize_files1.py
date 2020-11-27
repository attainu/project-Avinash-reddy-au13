import os
from pathlib import Path
def organize_files1(paath,FILE_FORMATS):
    direct = paath
    os.chdir(direct)
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry.name)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok = True)
            file_path.rename(directory_path.joinpath(file_path))
        #If there is no specified extension create a new file "OTHER"
    try:
        os.mkdir("OTHER")
    except:
        pass
    for path in os.scandir():
        try:
            if path.is_dir():
                os.rmdir(path)
            else:
                os.rename(os.getcwd() + '/' + str(Path(path)), os.getcwd() + '/OTHER/' + str(Path(path)))
        except:
            pass

