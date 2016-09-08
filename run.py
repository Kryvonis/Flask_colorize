# from app import app
# app.run()

from app import colorize as c
c.image_overlay('app/static/res.png')
c.merge('app/static/res.png','app/static/res.png',(50,50)).save('merge_res.png')