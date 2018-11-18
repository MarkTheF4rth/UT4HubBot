from Decorators.command import command
import os
import datetime

@command(aliases=['cc'], description='Lists the content currently on the server')
def contentquery(self, message, ctx):
    """Checks the content dir for what paks are present and prints them"""
    header = "**Paks installed on the hub:**\n```"
    formatstr = "{} - {} : {}"
    output = []

    for pak in open(self.data_path+'cache.txt').readlines():
        pak = pak.split()
        pak[1] = datetime.datetime.fromtimestamp(float(pak[1])).strftime('%Y-%m-%d %H:%M:%S')
        output.append(formatstr.format(pak[1], pak[0], pak[2]))

    self.message_printer('\n'.join(output)+'```', message.channel, header=header, footer='```', msg_break='```')
