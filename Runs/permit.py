import pandas as pd

Trailer ='BC111'
Truck ='stone'

d= {'0': ['Bev', 'stone', 'evy'], 'BC123': ['Y', 'N', 'Y'],'BC111': ['N', 'Y', 'N']}

df = pd.DataFrame(d).set_index('0')


def permit(df,Trailer,Truck):
    permitted = (df[Trailer][Truck])
    return permitted

trailer_1 = [("H180J","H180J"),
("FC505","FC505"),("FC503","FC503"),("FC504","FC504"),("M441R","M441R"),("Q738U","Q738U"),
("BC606","BC606"),("BC604","BC604"),("BC605","BC605"),("BC607","BC607"),("BC608","BC608"),("BC602","BC602"),("BC619","BC619"),("BC603","BC603"),("BC615","BC615"),("BC620","BC620"),("BC609","BC609"),("FC502","FC502"),
("BC614","BC614"), ("BC621","BC621"),("BC610","BC610"),("BC622","BC622"),("Ole Yella","Ole Yella"),("BC623","BC623"),]


trailer_2 =[
("BC606B","BC606B"),("BC604B","BC604B"),("BC605B","BC605B"),("BC607B","BC607B"),("BC608B","BC608B"),("BC602B","BC602B"),("BC619B","BC619B"),("BC603B","BC603B"),
("BC615B","BC615B"),("BC620B","BC620B"),("BC609B","BC609B"),("FC501","FC501"),("BC614B","BC614B"),("BC621B","BC621B"),("BC610B","BC610B"),("5Y411","5Y411"),("Ole Yellab","Ole Yellab"),("BC622B","BC622B"),
("BC623B","BC623B")]








 