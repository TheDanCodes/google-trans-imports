@client.command(aliases=["translate", "t"])
async def translator(ctx, lang, *, args):
  t = Translator()
  a = t.translate(args, dest=lang)

  embed = discord.Embed(
    description = f"{a.text}"
  )
  embed.set_author(icon_url=ctx.author.avatar_url, name=f"{ctx.author.name}")
  embed.set_footer(icon_url="https://media.discordapp.net/attachments/952675978428186637/953438943674765312/icon_1.0.1303.1871.png", text=f"{args} → {lang}")
    
  await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.CommandInvokeError):
    embed = discord.Embed(
      title = f":shield: Language does not exist!",
      description = "Please use a valid argument when using this command!"
    )
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"{ctx.author}")
    await ctx.send(embed=embed)

client.run(os.environ["TOKEN"])
