import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping.py is ready!")

    # @commands.command()
    # async def ping(self, ctx):
    #     bot_latency = round(self.client.latency * 1000)
    #
    #     await ctx.send(f"Pong! {bot_latency} ms.")

    @commands.command()
    async def embed(self, ctx):
        embed_mesage = discord.Embed(title="Title of embed", description="Description of embed",
                                     color=discord.Color.green())
        embed_mesage.set_author(name=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
        embed_mesage.set_thumbnail(url=ctx.guild.icon)
        embed_mesage.set_image(url=ctx.guild.icon)
        embed_mesage.add_field(name="Field name", value="Field value", inline=False)
        embed_mesage.set_footer(text="This is the footer", icon_url=ctx.author.avatar)

        await ctx.send(embed=embed_mesage)


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is online.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        await ctx.channel.purge(limit=count)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.kick(member)

        conf_embed = discord.Embed(title="Sucess!", color=discord.Color.green())
        conf_embed.add_field(name="Kicked",
                             value=f"{member.mention} has been kicked from the server by {ctx.author.mention}.")
        conf_embed.add_field(name="Reason", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, modreason):
        await ctx.guild.ban(member)

        conf_embed = discord.Embed(title="Sucess!", color=discord.Color.green())
        conf_embed.add_field(name="Banned",
                             value=f"{member.name} has been banned from the server by {ctx.author.name}.")
        conf_embed.add_field(name="Reason", value=modreason, inline=False)

        await ctx.send(embed=conf_embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user_id):
        user = discord.Object(id=user_id)
        await ctx.guild.unban(user)

        conf_embed = discord.Embed(title="Sucess!", color=discord.Color.green())
        conf_embed.add_field(name="Unbanned",
                             value=f"<@{user_id}> has been unbanned from the server by {ctx.author.name}.")

        await ctx.send(embed=conf_embed)


async def setup(client):
    await client.add_cog(Ping(client))
    await client.add_cog(Moderation(client))
