import streamlit as st
import aiohttp
import asyncio
import fpl as fp
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

playerIds = random.sample(range(1,201), 200)

df = pd.DataFrame()
async def main():
    async with aiohttp.ClientSession() as session:
        fpl = fp.FPL(session)
        players = await fpl.get_players(playerIds)        
        values = []
        points = []
        names = []
        for player in players:            
            if float(player.value_season)  > 0 and player.minutes > 450:
                value = float(player.now_cost)/10
                values.append(value)
                points.append(player.pp90)
                names.append(player.second_name)
                #for debug purposes
                #print(player, player.now_cost, player.pp90)
        df['Average Points'] = points
        df['Values'] = values 
        df['Names'] = names   
asyncio.run(main())

dfSorted = df.sort_values(by = 'Values')
fig, ax = plt.subplots(ncols = 1, figsize = (22,7))

sns.pointplot(x = "Names", y ="Average Points", hue = 'Values',data = dfSorted)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
 
plt.xticks(rotation = 90)

st.pyplot(fig)


    

