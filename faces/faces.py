def emoji():
    var = input('message? ')
    var = var.replace(':)', '🙂')
    var = var.replace(':(', '🙁')
    var = var.replace('(:', '🙂')
    var = var.replace('):', '🙁')
    print(var)

emoji()