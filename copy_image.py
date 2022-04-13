import shutil

def copy(file):
    shutil.copy(f'uploads/{file}', f'static/{file}')