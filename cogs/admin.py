import discord
from discord.ext import commands
import logging
import helper_files.settings as settings

logger = logging.getLogger('HonestBear')


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('GOD')
    async def load(self, ctx, extension):
        """load [extension]"""
    
        self.bot.load_extension(f'cogs.{extension}')
        msg = f'[LOAD] cogs.{extension}\n'
        logger.info(msg)
        await ctx.send(msg)
    
    
    @commands.command()
    @commands.has_role('GOD')
    async def unload(self, ctx, extension):
        """unload [extension]"""
    
        self.bot.unload_extension(f'cogs.{extension}')
        msg = f'[UNLOAD] cogs.{extension}\n'
        logger.info(msg)
        await ctx.send(msg)
    
    
    @commands.command()
    @commands.has_role('GOD')
    async def reload(self, ctx, extension):
        """reload [extension]"""
    
        self.bot.unload_extension(f'cogs.{extension}')
        self.bot.load_extension(f'cogs.{extension}')
        msg = f'[RELOAD] cogs.{extension}\n'
        logger.info(msg)
        await ctx.send(msg)


    @commands.command()
    @commands.has_role('GOD')
    async def shutdown(self, ctx):
        """bot goes offline"""
    
        settings.conn.close()
        await ctx.send("Shutting down!")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(Admin(bot))