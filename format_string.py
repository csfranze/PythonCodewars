#Given: an array containing hashes of names

#Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

#Example:

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

#namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

#namelist([ {'name': 'Bart'} ])
# returns 'Bart'

#namelist([])
# returns ''
#Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

def namelist(names):
    names_lst = []
    for i in names:
        names_lst.append(i['name'])
    joined_lst = ', '.join(names_lst[0:len(names_lst)-1])
    if len(names_lst) == 0:
        return('')
    elif len(names_lst) == 1:
        return(names_lst[0])
    else:
        return('{} & {}'.format(joined_lst,names_lst[-1]))
