management = 'users-management' 
func_name = management.replace('-','_')
model = 'User'
title = 'Users Management'
singular_var = 'user'
plural_var = 'users'
folder_name = 'users-management'

with open("input/controller.txt", 'r', encoding='utf-8') as f:
    code = f.read()
    controllers = code.replace('{management}', management).replace('{model}', model).replace('{singular_var}', singular_var).replace('{plural_var}', plural_var).replace('{folder_name}', folder_name).replace('{title}', title).replace('{func_name}', func_name)

with open("input/routes.txt", 'r', encoding='utf-8') as f:
    code = f.read()
    routes = code.replace('{management}', management).replace('{model}', model).replace('{func_name}', func_name)


with open('output/routes.php','w') as f:
    f.write(routes)

with open('output/controller.php','w') as f:
    f.write(controllers)


