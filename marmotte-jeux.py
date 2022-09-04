import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "/", intents = discord.Intents.all(), description = "Bot de joam")


@bot.event
async def on_ready():
	print("Ready !")

"""
@bot.command()
async def amixem(ctx):
	messages = await ctx.channel.history(limit =  1).flatten()
	for message in messages:
		await message.delete()
	await ctx.send ("https://www.youtube.com/channel/UCgvqvBoSHB1ctlyyhoHrGwQ")

@bot.command()
async def nozman(ctx):
	messages = await ctx.channel.history(limit=1).flatten()
	for message in messages:
			await message.delete()
	await ctx.send ("https://www.youtube.com/channel/UCWnfDPdZw6A23UtuBpYBbAg")




@bot.command()
async def video(ctx):
	messages = await ctx.channel.purge(limit=1)
	for message in messages:
			await message.delete()
	await ctx.send("dr.nozman:    /nozman")
	await ctx.send("amixem:      /amixem")
	await ctx.send("fuze:       /fuze")


@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.purge(limit=nombre+1)
    for message in messages:
        await message.delete()




@bot.command()
async def ninjaxx(ctx):
	messages = await ctx.channel.history(limit = + 1).flatten()
	for message in messages:
		await message.delete()
	await ctx.send("https://www.youtube.com/channel/UCDB1PaqiausfXbVI2Jjk0iQ")


@bot.command()
async def fuze(ctx):
	messages = await ctx.channel.history(limit = + 1).flatten()
	for message in messages:
		await message.delete()
	await ctx.send("https://www.youtube.com/c/FuzeIII")


@bot.command()
async def message(ctx):
	messages = await ctx.channel.history(limit = 1).flatten()
	for message in messages:
		await message.delete()
		await ctx.send("@membre")
"""


@bot.command()
async def amixem(ctx):
	await ctx.send ("https://www.youtube.com/channel/UCgvqvBoSHB1ctlyyhoHrGwQ")

@bot.command()
async def nozman(ctx):
	await ctx.send ("https://www.youtube.com/channel/UCWnfDPdZw6A23UtuBpYBbAg")




@bot.command()
async def video(ctx):
	await ctx.send("```dr.nozman:    /nozman```")
	await ctx.send("```amixem:      /amixem```")
	await ctx.send("```fuze:       /fuze```")
	await ctx.send("```ninjaxx:   /ninjaxx ```")


@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.purge(limit=nombre+1)
    for message in messages:
        await message.delete()




@bot.command()
async def ninjaxx(ctx):
	await ctx.send("https://www.youtube.com/channel/UCDB1PaqiausfXbVI2Jjk0iQ")


@bot.command()
async def fuze(ctx):
	await ctx.send("https://c.tenor.com/yey7ZY_HBRAAAAAM/fuze-iii-paladium.gif")
	await ctx.send("https://www.youtube.com/c/FuzeIII")

@bot.command()
async def aiwen(ctx):
	await ctx.send("https://c.tenor.com/HrvL_DHGlycAAAAM/clap-nationsglory.gif")

@bot.command()
async def coucou(ctx):
	await ctx.send( " ```bonjour je suis en bot en cours de test``` " )


@bot.command()
async def mco(ctx):
	await ctx.send("https://www.youtube.com/channel/UCC6IeG99-g96JtFruvomPuA")





bot.run("MTAxNTkyMzU5ODA4NDU0MjQ2NQ.G87Dex.XV0GFSPAhHpS9cWQJo2d926dCiLnLYMbJEfGnU")