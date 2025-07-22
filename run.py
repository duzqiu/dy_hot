from settings import *
from bark_send import SendBark
from dy_hot import BarkText  
import asyncio

bark = SendBark()

async def hot_run():
    bark_text_hot = BarkText(HOT_PARAMS)
    title_rise, content_rise = bark_text_hot.get_rise_bark()
    title_hot, content_hot = bark_text_hot.get_hot_bark()
    bark.send_t_c(title_rise, content_rise)
    await asyncio.sleep(1)
    bark.send_t_c(title_hot, content_hot)

async def plant_run():
    bark_text_plant = BarkText(PLANT_PARAMS)
    title_plant, content_plant = bark_text_plant.get_hot_bark()
    bark.send_t_c(title_plant, content_plant)

async def entertain_run():
    bark_text_entertain = BarkText(ENTERTAIN_PARAMS)
    title_entertain, content_entertain = bark_text_entertain.get_hot_bark()
    bark.send_t_c(title_entertain, content_entertain)

async def society_run():
    bark_text_society = BarkText(SOCIETY_PARAMS)
    title_society, content_society = bark_text_society.get_hot_bark()
    bark.send_t_c(title_society, content_society)

async def sh_run():
    bark_text_sh = BarkText(SH_PARAMS)
    title_sh, content_sh = bark_text_sh.get_hot_bark()
    bark.send_t_c(title_sh, content_sh)

async def main():
    await asyncio.gather(
        hot_run(),
        plant_run(),
        entertain_run(),
        society_run(),
        sh_run()
    )

if __name__ == "__main__":
    asyncio.run(main())