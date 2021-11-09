from dis_snek.client import Snake
from dis_snek.models import (
    listen,
    slash_command,
    slash_option,
    OptionTypes,
    InteractionContext,
    context_menu,
    CommandTypes,
)

bot = Snake(
    sync_interactions=True,  # sync application commands with discord
    delete_unused_application_cmds=True,  # Delete commands that arent listed here
    debug_scope=701347683591389185,  # Override the commands scope, and only create them in this guild
)
# during testing, we recommend setting `debug_scope`, this forces your commands to only be registered in the listed guild


@slash_command("hello", description="Hello there!")
async def hello(ctx: InteractionContext):
    await ctx.send(f"Hi there {ctx.author.mention}")


@slash_command("echo", description="echo your options")
@slash_option("text", "the text to echo", OptionTypes.STRING, required=True)
async def echo(ctx: InteractionContext, text: str):
    await ctx.send(text)


@context_menu("user menu", CommandTypes.USER)
async def user_menu(ctx: InteractionContext):
    # this command can be triggered by right clicking a user, and pressing `apps`
    target_user = await bot.get_user(ctx.target_id)
    await ctx.send(f"You clicked on {target_user.mention}")


@listen()
async def on_ready():
    print(f"Logged in as {bot.user.username}")


bot.start("token")
