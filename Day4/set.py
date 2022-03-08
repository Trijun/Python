websites = {"youtube","gmail","insta","meta","cod","gmail"}
games={"pubg","cod","insta"}

temp=websites.intersection(games)
print(temp)
##websites.intersection_update()
print(websites)

"""when you use _update, there is no need for temporary varaible to store as it will make all the changes in the original set"""

websites.symmetric_difference_update(games)
print(websites)

"""it will combine both the sets and will remove the things that are common in both"""
