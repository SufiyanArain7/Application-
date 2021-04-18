import discord
import os
import json
import random
import asyncio
from discord.ext import commands


client = commands.Bot(command_prefix = '%', intents=discord.Intents.all())

@client.event
async def on_ready():
	print("Bot Got Online!")

@client.command()
async def apply(ctx):
	if ctx.channel.id == 829694089388621864:
		await ctx.send(f"{ctx.author.mention} Application has been started in DM!")

		questions = ["How much Experience do you have on discord?",
		"For how much time can you be active in the server and chat?",
		"You must use our tag on your name. [ YOUR NAME ᴸᴬ ]",
		"You can only use 2 other clan tags with our tag.",
  		"You will kicked from Last4rmy Officials if you are inactive.",]

		answers = []

		channel = await ctx.author.create_dm()

		def check(m):
			return m.author == ctx.author and m.channel == channel

		for i in questions:
			await channel.send(i)

			try:
				msg = await client.wait_for("message", timeout=300.0, check=check)
			except asyncio.TimeoutError:
				await channel.send("You didnt Answer in time.")
				return
			else:
				answers.append(msg.content)

		discord_experience = answers[0]
		activeness = answers[1]
		tag = answers[2]
		confirmation = answers[3]
		inactive = answers[4]
        
		application_channel = client.get_channel(833468297843703888)
		embed=discord.Embed(title="NEW APPLICATION!", description=f"Application by {ctx.author.name}\nUser ID: {ctx.author.id}", color=discord.Color.blue())
		embed.add_field(name="How much Experience do you have on discord?", value=answers[0], inline=False)
		embed.add_field(name="For how much time can you be active in the server and chat?", value=answers[1], inline=False)
		embed.add_field(name="You must use our tag on your name. [ YOUR NAME ᴸᴬ ]", value=answers[2], inline=False)
		embed.add_field(name="You can only use 2 other clan tags with our tag.", value=answers[3], inline=False)
		embed.add_field(name="You will kicked from Last4rmy Officials if you are inactive.", value=answers[4], inline=False)
		embed.set_footer(text="Last4rmy.")
		await application_channel.send(embed=embed)

		await channel.send("Your Application has been sent successfully!")

def application_logs_channel(ctx):
	return ctx.channel.id == 833467934964711474

@client.command()
async def accept(ctx, member: discord.Member):
	channel = await member.create_dm()
	await channel.send("Congratulations! You have been accepted! Contact CEO for Interview.")
	results_channel = client.get_channel(833467934964711474)
	await results_channel.send(f"{member.mention} You have been accepted! Contact CEO for Interview.")

@accept.error
async def accept_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Please Enter the ID of the member you want to accept!")

@client.command()
async def decline(ctx, member: discord.Member):
	channel = await member.create_dm()
	await channel.send("Sorry, your application is declined!")
	results_channel = client.get_channel(833467934964711474)
	await results_channel.send(f"{member.mention} Your Application has been declined!")

@decline.error
async def decline_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("Please Enter the ID of the member you want to decline!")

client.run("Nzk5NjU5ODczMzAyMDg1NjMy.YAGzSg.GNOpNmM5IdaDgBxU3wCMD_qu5hQ")