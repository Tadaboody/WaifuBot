import asyncio
import json


# loads json file
def load_file(fp):
    with open(fp, 'r') as file:
        return json.load(file)

# returns perfect fizzbuzz response 
def fizzbuzz(number, divisors):
    output = ''
    for divisor in divisors:
        output = output+divisors[divisor] if number%divisor==0 else output
    return output if output != '' else number

# gets count messages from ctx.channel
async def get_messages(bot, ctx, count):
    messages = bot.logs_from(ctx.message.channel, limit=count+1)
    messages = [message async for message in messages]
    return messages

# splits word into groups of size step
def split_word_by_step(word, step):
    return [word[i:i+step] for i in range(0, len(word), step)]

# not sure yet
def turn_into_emoji(message):
    pass
