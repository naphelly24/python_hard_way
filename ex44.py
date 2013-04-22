# 类的风格
# 你的 class 应该使用 “camel case（驼峰式大小写）”，例如你应该使用 SuperGoldFactory 而不是 super_gold_factory。
# 你的 __init__ 不应该做太多的事情，这会让 class 变得难以使用。
# 你的其它函数应该使用 “underscore format（下划线隔词）”，所以你可以写 my_awesome_hair， 而不是 myawesomehair 或者 MyAwesomeHair 。
# 用一致的方式组织函数的参数。如果你的 class 需要处理 users、dogs、和 cats，就保持这个次序（特别情况除外）。如果一个函数的参数是 (dog, cat, user) ，另一个的是 (user, cat, dog) ，这会让函数使用起来很困难。
# 不要对全局变量或者来自模组的变量进行重定义或者赋值，让这些东西自顾自就行了。
# 不要一根筋式地维持风格一致性，这是思维力底下的妖怪喽啰做的事情。一致性是好事情，不过愚蠢地跟着别人遵从一些白痴口号是错误的行为——这本身就是一种坏的风格。好好为自己照想把。
# 永远永远都使用 class Name(object) 的方式定义 class，否则你会碰到大麻烦。
