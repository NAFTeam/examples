from dis_snek import Snake, message_command, MessageContext, listen, Task
from dis_snek.tasks.triggers import IntervalTrigger

bot = Snake()
# by default the prefix will be mentioning your bot


@message_command()
async def hello(ctx: MessageContext):
    # to invoke: @bot hello
    await ctx.send(f"Hi there {ctx.author.mention}")


# A task runs every time its trigger is satisfied, in this case we're using an intervalTrigger
# So every 10 seconds, the trigger runs the task
@Task.create(IntervalTrigger(10))
async def ten_seconds():
    print(f"10 seconds have passed")


@listen()
async def on_startup():
    ten_seconds.start()


bot.start("token")
