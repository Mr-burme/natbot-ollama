import ollama
import pexpect
import re
message = 'ask Kārlis and Estere if the website is ready to deploy'


def ollamaCLI(message, model="phi3"):
    child = pexpect.spawn('ollama run ' + model, dimensions=(200,200))
    #child.expect(">>>")
    child.sendline(message)
    #child.expect("Send a message (/? for help)")
    child.expect(">>>", timeout=100000000)
    #print(child.before.decode())
    child.sendcontrol('d')

    # print(child.read())
    # print("AAAAAAAAAAAAAAA")
    # print(child.read().decode("utf-8"))
    #child.interact()
    output = child.read().decode("utf-8")

    ansi_escape = re.compile(r'\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    output = ansi_escape.sub('', output)



    result = re.search('>>>(.*)>>>', output)
    result = output.split(">>>")[-2]
    result = re.sub(r'>>>.*\n?', '', result, flags=re.MULTILINE)
    result = re.sub(r' Send a message .*\n?', '', result, flags=re.MULTILINE)
    l = "⠙ ⠙ ⠸ ⠼ ⠼ ⠦ ⠧ ⠇ ⠏ ⠋ ⠙ ⠙ ⠸ ⠼ ⠦ ⠧ ⠧ ⠏ ⠋ ⠋ ⠙ ⠹ ⠼ ⠦ ⠦ ⠇ ⠏ ⠋ ⠴".split()

    for char in l:

        result = re.sub(char+" ", '', result)


    return result










