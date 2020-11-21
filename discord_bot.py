import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("과제")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반갑습니다")
    if message.content.startswith("누구"):
        await message.channel.send("감귤과 한라봉입니다")
    if message.content.startswith("뭐하고있니?"):
        await message.channel.send("과제중입니다")


client.run("Nzc5Njk3MzgzMTAwNjQ1Mzg2.X7kTxg.j5MyJOUcAJd6WHBuoImQ_XTcCuw")
