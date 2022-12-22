from datetime import date
from dateutil.relativedelta import relativedelta

today = date.today()
current = today + relativedelta(months=1)

about_str = f"""---
title: About
---

Hi! 

Test text

I'm Eric and currently work at Caterpillar, Inc. as a Sr. Data Scientist building digital 
products using IIoT data. Previously, I was a graduate teaching assistant at 
Western Michigan University while completing my Master's in Statistics. 

In my free time I enjoy travelling, playing golf and trying new foods/restaurants!

{{{{<mermaid>}}}}
gantt
    title :round_pushpin::hand: Hastings, MI :arrow_right: :round_pushpin::house_with_garden: Peoria, Il
    dateFormat  YYYY-MM
    axisFormat  %b %Y
    section School
    B.A. Mathematics    :done , 2013-09 , 2017-05
    M.S. Statistics     :done , 2017-09 , 2019-05
    section Work
    Baseball Umpire     :done , 2014-05 , 2019-05
    WMU GA              :done , 2017-09 , 2019-05
    Data Scientist      :done , 2019-05 , 2021-05
    Sr. Data Scientist  :active , 2021-06 , {current.strftime('%Y-%m')}
{{{{</mermaid>}}}}
"""

with open('content/about.md', 'w') as f:
    f.write(about_str)
