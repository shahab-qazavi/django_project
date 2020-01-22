from pymongo import MongoClient
import os

con = MongoClient()
db = con['djangodb_test']
col_users = db['auth_user']

# col_users.update_one({'id':2},{'$set':{'first_name':'kiiiir'}})



path ='/home/oem/django_projects/site_with_foldmenu/media/'

print(os.listdir(path))

# files = []
# # r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.txt' in file:
#             files.append(os.path.join(r, file))
#
# for f in files:
#     print(f)

