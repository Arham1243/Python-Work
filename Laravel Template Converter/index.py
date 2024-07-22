import os
import re


def fileCoverter(old_ext, new_ext):
    files = os.listdir()
    files.remove('index.py')
    for file in files:
        file_check = os.path.isfile(file)
        if file_check == True:
            ext_1 = f".{file.split('.')[-1]}"
            file_name = file.split(".")[0]
            if old_ext == ext_1:
                os.rename(file, f"{file_name}{new_ext}")


def change_image_sources():
    files = os.listdir()
    files.remove('index.py')
    for file in files:
        file_check = os.path.isfile(file)
        if file_check:
            with open(file, 'r', encoding="utf-8") as f:
                content = f.read()

            updated_content = re.sub(
                r'<img(.*?)src=[\'"]([^\'"\s>]+)[\'"](.*?)>',
                r'<img\1src="{{ asset("\2") }}"\3>',
                content
            )

            with open(file, 'w', encoding="utf-8") as f:
                f.write(updated_content)


def change_links():
    files = os.listdir()
    files.remove('index.py')
    for file in files:
        file_check = os.path.isfile(file)
        if file_check:
            with open(file, 'r', encoding="utf-8") as f:
                content = f.read()

            updated_content = re.sub(
                r'<a(.*?)href=[\'"]((?!(?:tel:|mailto:|#)).+?)[\'"](.*?)>',
                lambda match: '<a{}href="{{{{ route("{}") }}}}"{}>'.format(
                    match.group(1),
                    match.group(2).rsplit('.html', 1)[0].rsplit('.php', 1)[0],
                    match.group(3)
                ),
                content
            )

            with open(file, 'w', encoding="utf-8") as f:
                f.write(updated_content)


def routeCreating():
    files = os.listdir()
    files.remove('index.py')
    for file in files:
        file_check = os.path.isfile(file)
        if file_check:
            page_name = file.split(".")[0]

            func_name = page_name
            func_name = func_name.replace("-", "_")
            code = f"Route::get('/{page_name}', [IndexController::class, '{func_name}'])->name('{page_name}');\n"
            with open('routes.blade.php', 'a', encoding="utf-8") as f:
                f.write(code)


def funcCreating():
    files = os.listdir()
    files.remove('index.py')

    for file in files:
        file_check = os.path.isfile(file)
        if file_check:
            page_name = file.split(".")[0]

            title = page_name.title()
            title = title.replace("-", " ")
            func_name = page_name
            func_name = func_name.replace("-", "_")
            code = f"""
            public function {func_name}()
                [
                    return view('{page_name}')->with('title', '{title}');
                ]
            """
            code = code.replace("[", "{")
            code = code.replace("]", "}")
            with open('functions.blade.php', 'a', encoding="utf-8") as f:
                f.write(code)


fileCoverter('.php', '.blade.php')
change_image_sources()
change_links()
funcCreating()
routeCreating()
