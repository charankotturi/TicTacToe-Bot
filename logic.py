import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import PlayGame

load_dotenv()

TOKEN = os.getenv('TOKEN')
GUILD_NAME = os.getenv('GUILD_NAME')

bot = commands.Bot(command_prefix='&', status=discord.Status.idle)

play1 = True
board = ['_']*9
dualPlayers = PlayGame.players('one', 'two')
MainBoard = PlayGame.board(dualPlayers, board)

@bot.event
async def on_ready():
    print('X and O bot is online!')

@bot.command(name='start', help='Enter two member names!')
async def start(ctx,opponent: str):
    
    global board
    global play1

    playerOne = ctx.author.display_name
    MainBoard.printMatrix()
    print(playerOne)
    embed = printBoard()

    await ctx.send(embed=embed)

@bot.command(name='my_turn')
async def my_turn(ctx,option: str):
    
    embed = updatePlayer(option)

    print(MainBoard.printMatrix())
    print(f'{option}')

    await ctx.send(embed=embed)

def updatePlayer(option: str):

    global val
    global play1
    global MainBoard

    if play1:
        val = option
    else:
        val = option

    if validateInput(int(val)):
        MainBoard.updateBoard(play1, option)
        play1 = not play1
    else:
        return discord.Embed(
            title='Enter a valid input!',
            description='Index is between 1 - 9 and check if the index is occupied!',
            color=discord.Color.red()
        )

    if MainBoard.checkForDraw():
        return discord.Embed(
                title='Its a Draw!',
                description='Another game? use the command "&start"',
                color=discord.Color.greyple()
        )
    
    if MainBoard.checkForWin():
        print()
        if not play1:
            return discord.Embed(
                title='Congratulations!!',
                description='Player one won!!',
                color=discord.Color.green()
            )
        else:
            return discord.Embed(
                title='Congratulations!!',
                description='Player two won!!',
                color=discord.Color.green()
            )
    
    return printBoard()

def validateInput(x: int):
    global board
    if x <= 9 and x > 0 :
        if board[x - 1] != '_':
            print('Invalid Input!\nTry again!')
            return False 
        return True
    
    return False

def printBoard():

    global board
    global play1

    if play1:
        x = 'Its player ones turn playing with X'
    else:
        x = 'Its player twos turn playing with O'

    embed = discord.Embed(
        title=x,
        description='Players use the command &my_turn <index> to play your turn!',
        color=discord.Color.teal()
    )

    embed.set_author(
        name='X and O game!',
        icon_url='https://image.shutterstock.com/image-vector/illustration-hand-drawn-tictactoe-game-260nw-277642736.jpg'
    )

    embed.set_thumbnail(url='https://image.shutterstock.com/image-vector/illustration-hand-drawn-tictactoe-game-260nw-277642736.jpg')

    row1 = ''
    row2 = ''
    row3 = ''

    row1 ='**' + board[0] + '**' + '\n' + str(1)+ '\n\n' +'**' + board[3] +'**' + '\n' + str(4)+ '\n\n' +'**' + board[6] +'**' + '\n' + str(7)
    
    row2 = '**' +board[1] + '**' +'\n' + str(2)+ '\n\n'+ '**' +board[4] + '**' +'\n' + str(5) + '\n\n' +'**' + board[7] +'**' + '\n' + str(8)
    
    row3 = '**' +board[2] + '**' +'\n' + str(3)+ '\n\n'+'**' + board[5] + '**' +'\n' + str(6)+ '\n\n' + '**' + board[8] + '**' + '\n' + str(9)

    embed.add_field(
        name='Row - 1',
        value=row1,
        inline=True
    )

    embed.add_field(
        name='Row - 2',
        value=row2,
        inline=True
    )

    embed.add_field(
        name='Row - 3',
        value=row3,
        inline=True
    )

    return embed

bot.run(TOKEN)
