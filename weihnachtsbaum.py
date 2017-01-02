import steckdose

light1 = steckdose.Steckdose('01011', 1) # rgb
light2 = steckdose.Steckdose('01011', 4) # white

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print 'usage: python %1 <rgb|white|both> <on|off>' % (sys.argv[0])
    else:
        onOff = 1 if sys.argv[2] == 'on' else 0
        if onOff:
            if sys.argv[1] == 'rgb':
                light1.switchOn()
            elif sys.argv[1] == 'white':
                light2.switchOn()
            elif sys.argv[1] == 'both':
                light1.switchOn()
                light2.switchOn()
        else:
            if sys.argv[1] == 'rgb':
                light1.switchOff()
            elif sys.argv[1] == 'white':
                light2.switchOff()
            elif sys.argv[1] == 'both':
                light1.switchOff()
                light2.switchOff()
