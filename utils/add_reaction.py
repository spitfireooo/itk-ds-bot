async def add_reaction_on_message(message, *reactions):
    if reactions:
        message_res = await message.original_response()
        for reaction in reactions:
            await message_res.add_reaction(reaction)