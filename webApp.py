import streamlit as st
import aiohttp
import asyncio
import fpl as fp
import pandas as pd
import random

playerIds = random.sample(range(1,101), 30)
df = pd.DataFrame()
df2 = pd.DataFrame()
async def main():
    async with aiohttp.ClientSession() as session:
        fpl = fp.FPL(session)
        players = await fpl.get_players(playerIds)        
        values = []
        points = []
        names = []
        for player in players:            
            if float(player.value_season) > 0:
                values.append(player.value_season)
                points.append(player.pp90)
                names.append(player.second_name)
                #for debug purposes
                #print(player, player.value_season, player.pp90)
        df['Average Points'] = points
        df2['Values'] = values
        df.index = names
        df2.index = names     
asyncio.run(main())

st.line_chart(df)
st.line_chart(df2)


    

