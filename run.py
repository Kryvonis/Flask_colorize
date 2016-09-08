# from app import app
# app.run()

from app import colorize as c
c.merge(c.image_overlay('app/static/res.png','255,0,0'),'app/static/res.png',(50,50)).save('app/static/color_merge_res.png')