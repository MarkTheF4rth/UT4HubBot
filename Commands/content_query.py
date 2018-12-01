from Decorators.command import command
import os
import datetime

@command(aliases=['cc'], description='Lists the content currently on the server')
def contentquery(self, message, ctx):
    """Checks the content dir for what paks are present and prints them"""
    data_path = self.config['Update_Config']['data_path']

    header = "**Paks installed on the hub:**\n```"
    formatstr = "{} - {} : {}"
    output = []

    for pak in open(data_path+'cache.txt').readlines():
        pak = pak.split()
        pak[1] = datetime.datetime.fromtimestamp(float(pak[1])).strftime('%Y-%m-%d %H:%M:%S')
        #output.append(formatstr.format(pak[1], pak[0], pak[2]))
        output.append(pak)

    final_output = {}
    mutators = []
    for pak in output: # sort paks into gamemodes
        if '-' in pak[0][:5]:
            mode = pak[0].split('-')[0]
            if mode not in final_output:
                final_output[mode] = []

            final_output[mode].append(pak)
        else:
            mutators.append(pak)


    format_output = '\n'.join(['\n'.join([" ```**Paks for"+mode+"**``` "]+
        sorted([formatstr.format(pak[1], pak[0], pak[2]) for pak in paks], key=lambda x : x.split()[3])) 
        for mode, paks in final_output.items()] +
        ['```**Mutators:**```'] +
        [formatstr.format(pak[1],pak[0],pak[2]) for pak in mutators])

    self.message_printer(format_output+'```', message.channel, header=header, footer='```', msg_break='```')
