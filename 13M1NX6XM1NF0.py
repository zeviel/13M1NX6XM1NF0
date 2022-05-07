import amino
print("""\u001b[31m
Script by deluvsushi
Github : https://github.com/deluvsushi
╱╭╮╭━━━┳━╮╭━╮╭╮╭━╮╱╭┳━╮╭━┳━━━┳━╮╭━┳━╮╭━╮╭╮╭━╮╱╭┳━━━┳━━━╮
╭╯┃┃╭━╮┃┃╰╯┃┣╯┃┃┃╰╮┃┣╮╰╯╭┫╭━━┻╮╰╯╭┫┃╰╯┃┣╯┃┃┃╰╮┃┃╭━━┫╭━╮┃
╰╮┃╰╯╭╯┃╭╮╭╮┣╮┃┃╭╮╰╯┃╰╮╭╯┃╰━━╮╰╮╭╯┃╭╮╭╮┣╮┃┃╭╮╰╯┃╰━━┫┃┃┃┃
╱┃┃╭╮╰╮┃┃┃┃┃┃┃┃┃┃╰╮┃┃╭╯╰╮┃╭━╮┃╭╯╰╮┃┃┃┃┃┃┃┃┃┃╰╮┃┃╭━━┫┃┃┃┃
╭╯╰┫╰━╯┃┃┃┃┃┣╯╰┫┃╱┃┃┣╯╭╮╰┫╰━╯┣╯╭╮╰┫┃┃┃┃┣╯╰┫┃╱┃┃┃┃╱╱┃╰━╯┃
╰━━┻━━━┻╯╰╯╰┻━━┻╯╱╰━┻━╯╰━┻━━━┻━╯╰━┻╯╰╯╰┻━━┻╯╱╰━┻╯╱╱╰━━━╯
""")
client = amino.Client()
com_id = client.get_from_code(
    input("-- Community Link::: ")).json["extensions"]["community"]["ndcId"]
community_info = client.get_community_info(comId=com_id).json
icon = community_info["icon"]
tagline = community_info["tagline"]
endpoint = community_info["endpoint"]
description = community_info["content"]
created_time = community_info["createdTime"]
community_cover = str(community_info["promotionalMediaList"]).split("'")[1]
print(f"""
-- Community icon link::: {icon}
-- Community cover link::: {community_cover}
-- Community tagline::: {tagline}
-- Community endpoint::: {endpoint}
-- Community created time::: {created_time}
""")
