#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
#
#Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:
#
#likes [] // must be "no one likes this"
#likes ["Peter"] // must be "Peter likes this"
#likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
#likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
#likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
#For 4 or more names, the number in and 2 others simply increases.

def likes(names):
    if len(names) == 0:
        message = "no one likes this"
    if len(names) == 1:
        message = "{} likes this".format(names[0])
    if len(names) == 2:
        message = "{} and {} like this".format(names[0],names[1])
    if len(names) == 3:
        message = "{}, {} and {} like this".format(names[0],names[1],names[2])
    if len(names) > 3:
        number_remaining = len(names)-2
        message = "{}, {} and {} others like this".format(names[0],names[1],str(number_remaining))
    return(message)