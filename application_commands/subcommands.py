from dis_snek import (
    Snake,
    slash_command,
    InteractionContext,
)

bot = Snake(
    sync_interactions=True,  # sync application commands with discord
    delete_unused_application_cmds=True,  # Delete commands that arent listed here
    debug_scope=701347683591389185,  # Override the commands scope, and only create them in this guild
)
# during testing, we recommend setting `debug_scope`, this forces your commands to only be registered in the listed guild


@slash_command(
    "hello",
    description="hello...",
    sub_cmd_name="there",
    sub_cmd_description="General Kenobi",
)
async def hello_there(ctx: InteractionContext):
    await ctx.send(f"General {ctx.author.mention}")


# one way to add a subcommand to an existing command
@hello_there.subcommand("mention", sub_cmd_description="mention me!")
async def hello_mention(ctx: InteractionContext):
    await ctx.send(ctx.author.mention)


# another way
@slash_command(
    "hello",
    description="hello...",
    sub_cmd_name="world",
    sub_cmd_description="The first line",
)
async def hello_world(ctx: InteractionContext):
    await ctx.send("Hello World!")


bot.start("token")
