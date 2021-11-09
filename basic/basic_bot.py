from dis_snek.client import Snake
from dis_snek.models import message_command, MessageContext, listen

bot = Snake()
# by default the prefix will be mentioning your bot


@message_command()
async def hello(ctx: MessageContext):
    # to invoke: @bot hello
    await ctx.send(f"Hi there {ctx.author.mention}")


@listen()
async def on_ready():
    print(f"Logged in as {bot.user.username}")


bot.start("token")
