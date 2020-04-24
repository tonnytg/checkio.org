def replace(phrase):
    words = ""
    phrases = list(phrases)
    for i in phrases:
        if words == "":
            words = i.replace('right','left')
        else:
            words = words +","+i.replace('right','left')
    return(words)
if __name__ == '__main__':
    replace("Hello,baby,aright,wright")
    # replace("left","right","left","stop")
    # replace("bright aright","ok")# == "bleft aleft,ok"
    # replace("brightness wright",)# == "bleftness wleft"
    # replace("enough","jokes")# == "enough,jokes"