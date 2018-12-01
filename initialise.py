from Decorators.task import task

UPDATEBOT_DESCRIPTION = 'informs a server about changes happening on the server'
UPDATEBOT_CREDITS = 'Created by @MII#0255'

@task(run_time='init')
async def update_bot_startup(self):
    self.module_info.update({'UpdateInformer':(UPDATEBOT_DESCRIPTION, UPDATEBOT_CREDITS)})
    
