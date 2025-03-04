###3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names = ['Tom', 'Jerry', 'Mike', 'John']
###3-2 问候语：继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
for name in names:
    print("Hello, " + name + "!")
###3-3 自己的列表：想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。
transports = ['motorcycle', 'car', 'bicycle']
for transport in transports:
    print("I would like to own a Honda " + transport + ".")
###3-4 嘉宾名单：如果你可以邀请任何人一起共进晚餐，你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
guests = ['Tom', 'Jerry', 'Mike']
for guest in guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")
###3-5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此你需要另外邀请一位嘉宾。请以新闻方式将此消息通知给嘉宾，然后使用一种方法将新嘉宾加入到名单中。再次打印一系列消息，向名单中的每位嘉宾发出邀请。
print(guests[0] + " can't make it to the dinner.")
guests[0] = 'John'
for guest in guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")
###3-6 添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请的人，然后使用insert()将一位新嘉宾添加到名单开头或中间。
print("I found a bigger table.")
guests.insert(0, 'Jack')
guests.insert(2, 'Rose')
guests.append('Lucy')
for guest in guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")
###3-7 缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。请以新闻方式通知剩余嘉宾，然后使用pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾后，都打印一条消息，指出你很抱歉无法邀请他来共进晚餐。
print("I'm sorry, the new table won't arrive in time.")
while len(guests) > 2:
    print("Sorry, " + guests.pop() + ", I can't invite you to dinner.")
for guest in guests:
    print("Dear " + guest + ", I would like to invite you to dinner.")
###3-8 放眼世界：想出至少5个你渴望去旅游的地方。将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
places = ['Beijing', 'New York', 'Paris', 'Tokyo', 'London']
###3-9 按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只打印原始Python列表。
print(places)
###3-10 使用sorted()按字母顺序打印这个列表，同时不要修改它。
print(sorted(places))
###3-11 再次打印该列表，核实排列顺序未变。
print(places)
###3-12 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(sorted(places, reverse=True))
###3-13 再次打印该列表，核实排列顺序未变。
print(places)
###3-14 使用reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
places.reverse()
print(places)
###3-15 使用reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
places.reverse()
print(places)
###3-16 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
places.sort()


