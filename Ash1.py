import asana
from datetime import date
from datetime import timedelta
import datetime

# def n dates
def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

today = str(date.today())

week = str(date.today() - timedelta(days = 7))


# replace with your personal access token.
personal_access_token = '0/421b0b5b3df46a8330ca1edf42565df5'

# Construct an Asana client
client = asana.Client.access_token(personal_access_token)


# Get your user info
me = client.users.me()

# Print out your information
# print ( "Hello world! " + "My name is " + me['name'] + " and I my primary Asana workspace is " + me['workspaces'][0]['name'] + "." )
# print (me['workspaces'])


workspace = me['workspaces'][0] #set main workspace
# print('Initialising Asana session for ' + me['name'] + ' in workspace: ' + workspace['name'])
projects = client.projects.find_by_workspace(workspace['gid'], iterator_type=None) #find projects within workspace



# display tasks due this week

# for a in projects:
#
#     if a['name'] == "IMMED":
#         tasks = client.tasks.find_by_project(a['gid'], {"opt_expand":"name, \
#         projects, workspace, gid, due_on, created_at, modified_at, completed, \
#         completed_at, assignee, parent, notes, tags"}, iterator_type=None)
#         for b in tasks:
#             D = str(b['due_on'])
#             if D >= today and D < week and D != 'None':
#                 print (b['name'])
#                 print (b['created_at'], b['due_on'])

# display duration of each completed task
# def n dates
def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return (d1 - d2).days

# to pull duration of completed tasks
# D = str(b['completed_at'])
# if D >= today and D < week and D != 'None':
for a in projects:

    if a['name'] == "IMMED":
        tasks = client.tasks.find_by_project(a['gid'], {"opt_expand":"name, \
        projects, workspace, gid, due_on, created_at, modified_at, completed, \
        completed_at, assignee, parent, notes, tags"}, iterator_type=None)
        for b in tasks:
            # print (b['name'], b['completed'])
            D = str(b['modified_at'])
            if b['completed'] == 1 and D != 'None':
                t1 = b['completed_at']
                t1 = t1[0:10]
                t2 = str(b['due_on'])
                if t2 != 'None':
                    da = days_between(t1, t2)
                    print (b['name'], da )

            # D = str(b['due_on'])
            # if D >= today and D < week and D != 'None':
            #     print (b['name'])
            ##     print (b['created_at'], b['due_on'])