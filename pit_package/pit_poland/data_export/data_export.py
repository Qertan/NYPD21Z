# Funkcja zapisuje podany plik o podanej nazwie w podanym katalogu (format xlsx)

def save_to_excel(data_frame, path, name):
    data_frame.to_excel(excel_writer=path + "/" + name + ".xlsx", engine="openpyxl")
    return 0
