import hikari
import lightbulb

plugin = lightbulb.Plugin('react')


def load(bot):
    bot.add_plugin(plugin)


# Command that changes the boolean from true to false and vice versa
@plugin.command
@lightbulb.command('shutthefuckup', 'I will shut the fuck up')
@lightbulb.implements(lightbulb.SlashCommand)
async def shutup(ctx: lightbulb.Context) -> None:
    if ctx.bot.d.spam:
        print(f'{ctx.author.username} made me shut up')
        await ctx.respond('I will shut my trap')
    else:
        print(f'{ctx.author.username} let me reply again')
        await ctx.respond('Prepare yourself, mortal')
    ctx.bot.d.spam = not ctx.bot.d.spam

