from subprocess import Popen, PIPE

def write_to_clipboard(output):
    process = Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=PIPE)
    process.communicate(output.encode('utf-8'))



